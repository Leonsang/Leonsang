"""ETL de ventas: ERP (CSV) + CRM (Parquet) + catálogo (CSV) -> ventas_integradas.parquet"""

import shutil
import tempfile
from pathlib import Path

import polars as pl

RUTA_VENTAS = Path("ventas_erp.csv")
RUTA_CLIENTES = Path("clientes_planos.parquet")
RUTA_PRODUCTOS = Path("productos.csv")
RUTA_SALIDA = Path("ventas_integradas.parquet")

# Columnas de salida, en orden, con su tipo final
ESQUEMA_SALIDA = {
    "id_venta": pl.String,
    "fecha": pl.Date,
    "cod_cliente": pl.String,
    "razon_social": pl.String,
    "segmento": pl.String,
    "ciudad": pl.String,
    "departamento": pl.String,
    "sku": pl.String,
    "nombre_producto": pl.String,
    "categoria": pl.String,
    "canal": pl.String,
    "cantidad": pl.Int64,
    "precio_unitario": pl.Float64,
    "costo_unitario": pl.Float64,
    "total_venta": pl.Float64,
    "margen": pl.Float64,
    "es_devolucion": pl.Boolean,
    "cliente_sin_crm": pl.Boolean,
}


def _llave(columna: str) -> pl.Expr:
    """Normaliza una llave: sin espacios (tampoco internos) y en mayúsculas."""
    return pl.col(columna).str.replace_all(r"\s+", "").str.to_uppercase()


def extraer(dir_tmp: Path) -> tuple[pl.LazyFrame, pl.LazyFrame, pl.LazyFrame]:
    """Abre las tres fuentes en modo lazy, todo como texto en los CSV."""
    # scan_csv solo acepta UTF-8: se transcodifica el latin-1 a una copia temporal
    ruta_utf8 = dir_tmp / "ventas_erp_utf8.csv"
    with (
        open(RUTA_VENTAS, encoding="latin-1", newline="") as origen,
        open(ruta_utf8, "w", encoding="utf-8", newline="") as destino,
    ):
        shutil.copyfileobj(origen, destino)

    ventas = pl.scan_csv(ruta_utf8, separator=";", infer_schema=False)
    clientes = pl.scan_parquet(RUTA_CLIENTES)
    productos = pl.scan_csv(RUTA_PRODUCTOS, separator=",", infer_schema=False)
    return ventas, clientes, productos


def limpiar_ventas(ventas: pl.LazyFrame) -> tuple[pl.LazyFrame, dict[str, int]]:
    """Aplica las reglas 1 a 5 y devuelve las ventas limpias junto con los conteos."""
    fecha_txt = pl.col("fecha").str.strip_chars()

    marcadas = (
        ventas
        # Regla 1: se marca el duplicado exacto sobre la fila cruda, antes de transformar
        .with_columns(_duplicada=~pl.struct(pl.all()).is_first_distinct())
        .with_columns(
            pl.col("id_venta").str.strip_chars(),
            # Regla 3: se prueban ambos formatos; si ninguno aplica queda nulo
            pl.coalesce(
                fecha_txt.str.to_date("%d/%m/%Y", strict=False),
                fecha_txt.str.to_date("%Y-%m-%d", strict=False),
            ).alias("fecha"),
            # Regla 2: llaves normalizadas
            _llave("cod_cliente"),
            _llave("sku"),
            pl.col("cantidad").str.strip_chars().cast(pl.Int64, strict=False),
            # Coma decimal -> punto decimal
            pl.col("precio_unitario")
            .str.strip_chars()
            .str.replace(",", ".", literal=True)
            .cast(pl.Float64, strict=False),
            pl.col("canal").str.strip_chars(),
        )
        # Regla 6: la ciudad del ERP no se usa
        .drop("ciudad")
        # collect necesario: los conteos de calidad requieren materializar las ventas
        .collect()
    )

    unica = ~pl.col("_duplicada")
    fecha_mala = pl.col("fecha").is_null()
    cantidad_nula = pl.col("cantidad").is_null()
    precio_nulo = pl.col("precio_unitario").is_null()

    # Los descartes se atribuyen en cascada para que el reporte cuadre
    conteos = marcadas.select(
        filas_leidas=pl.len(),
        duplicados=pl.col("_duplicada").sum(),
        desc_fecha=(unica & fecha_mala).sum(),
        desc_cantidad=(unica & ~fecha_mala & cantidad_nula).sum(),
        desc_precio=(unica & ~fecha_mala & ~cantidad_nula & precio_nulo).sum(),
    ).row(0, named=True)

    limpias = (
        marcadas
        # Reglas 1, 3 y 4: se descartan duplicados, fechas inválidas y nulos
        .filter(unica & ~fecha_mala & ~cantidad_nula & ~precio_nulo)
        .drop("_duplicada")
        # Regla 5: la cantidad negativa se conserva y se marca
        .with_columns(es_devolucion=pl.col("cantidad") < 0)
    )
    conteos["filas_limpias"] = limpias.height
    return limpias.lazy(), conteos


def integrar(
    ventas: pl.LazyFrame, clientes: pl.LazyFrame, productos: pl.LazyFrame
) -> pl.LazyFrame:
    """Aplica las reglas 6 a 8: joins con CRM y catálogo, y cálculo de importes."""
    dim_clientes = clientes.select(
        _llave("cod_cliente"),
        "razon_social",
        "segmento",
        "ciudad",
        "departamento",
        pl.lit(True).alias("_en_crm"),  # testigo para detectar clientes sin CRM
    )
    dim_productos = productos.select(
        _llave("sku"),
        "nombre_producto",
        "categoria",
        pl.col("costo_unitario").str.strip_chars().cast(pl.Float64, strict=False),
    )

    return (
        ventas
        # Regla 7: LEFT JOIN desde ventas
        .join(dim_clientes, on="cod_cliente", how="left")
        .join(dim_productos, on="sku", how="left")
        .with_columns(
            cliente_sin_crm=pl.col("_en_crm").is_null(),
            # Regla 8: importes
            total_venta=pl.col("cantidad") * pl.col("precio_unitario"),
            margen=(pl.col("precio_unitario") - pl.col("costo_unitario"))
            * pl.col("cantidad"),
        )
        .select(pl.col(nombre).cast(tipo) for nombre, tipo in ESQUEMA_SALIDA.items())
        .sort("fecha", "id_venta")
    )


def main() -> None:
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        ventas, clientes, productos = extraer(Path(tmp))
        ventas_limpias, conteos = limpiar_ventas(ventas)

    resultado = integrar(ventas_limpias, clientes, productos).collect()

    # Validaciones antes de escribir
    assert resultado.height <= conteos["filas_limpias"], (
        "Los joins aumentaron las filas: hay llaves repetidas en clientes o productos"
    )
    assert resultado["id_venta"].is_unique().all(), "id_venta no es único en la salida"

    resultado.write_parquet(RUTA_SALIDA)

    # Reporte de calidad
    print("REPORTE DE CALIDAD")
    print(f"Filas leídas:                        {conteos['filas_leidas']}")
    print(f"Duplicados eliminados:               {conteos['duplicados']}")
    print(f"Descartadas por fecha inválida:      {conteos['desc_fecha']}")
    print(f"Descartadas por cantidad nula:       {conteos['desc_cantidad']}")
    print(f"Descartadas por precio nulo:         {conteos['desc_precio']}")
    print(f"Devoluciones marcadas:               {resultado['es_devolucion'].sum()}")
    print(f"Ventas sin cliente en CRM:           {resultado['cliente_sin_crm'].sum()}")
    print(f"Ventas sin costo (SKU sin catálogo): {resultado['costo_unitario'].null_count()}")
    print(f"Filas finales:                       {resultado.height}")
    print(f"Archivo generado:                    {RUTA_SALIDA}")


if __name__ == "__main__":
    main()
