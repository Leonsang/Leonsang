"""Aplana el export de clientes del CRM (JSON anidado) a una tabla de Polars."""

import json
from pathlib import Path

import polars as pl

# Esquema explícito: las claves ausentes en el JSON quedan como nulos
# y las claves no declaradas se descartan.
ESQUEMA_CRM = {
    "id": pl.String,
    "razon_social": pl.String,
    "segmento": pl.String,
    "contacto": pl.Struct({"email": pl.String, "telefono": pl.String}),
    "direccion": pl.Struct({"ciudad": pl.String, "departamento": pl.String}),
    "fecha_registro": pl.String,
    "etiquetas": pl.List(pl.String),
}

COLUMNAS_SALIDA = [
    "cod_cliente",
    "razon_social",
    "segmento",
    "email",
    "telefono",
    "ciudad",
    "departamento",
    "fecha_registro",
    "etiquetas",
]


def aplanar_clientes(ruta_json) -> pl.DataFrame:
    """Devuelve una fila por cliente a partir del export anidado del CRM.

    Parámetros
    ----------
    ruta_json : str | pathlib.Path
        Ruta del archivo JSON (UTF-8) con la clave raíz ``clientes``.

    Retorna
    -------
    polars.DataFrame
        Columnas, en este orden: cod_cliente, razon_social, segmento, email,
        telefono, ciudad, departamento, fecha_registro (pl.Date), etiquetas.

    Lanza
    -----
    ValueError
        Si la clave ``clientes`` no es una lista o si hay ``cod_cliente``
        repetidos (el mensaje indica cuáles).
    """
    with Path(ruta_json).open(encoding="utf-8") as archivo:
        contenido = json.load(archivo)

    clientes = contenido.get("clientes")
    if not isinstance(clientes, list):
        raise ValueError("El JSON no contiene una lista en la clave 'clientes'.")

    # Carga con esquema fijo: tolera claves ausentes y valores null.
    crudo = pl.DataFrame(clientes, schema=ESQUEMA_CRM)

    segmento = pl.col("segmento").str.strip_chars()

    df = crudo.select(
        # Regla 1: mayúsculas y sin espacios (internos ni externos).
        pl.col("id").str.replace_all(r"\s+", "").str.to_uppercase().alias("cod_cliente"),
        pl.col("razon_social"),
        # Regla 2: primera letra en mayúscula y el resto en minúscula.
        pl.concat_str(
            segmento.str.slice(0, 1).str.to_uppercase(),
            segmento.str.slice(1).str.to_lowercase(),
        ).alias("segmento"),
        # Regla 3: un struct nulo o un campo ausente produce nulo, sin error.
        pl.col("contacto").struct.field("email").alias("email"),
        # Regla 6: el teléfono se conserva como texto.
        pl.col("contacto").struct.field("telefono").alias("telefono"),
        pl.col("direccion").struct.field("ciudad").alias("ciudad"),
        pl.col("direccion").struct.field("departamento").alias("departamento"),
        # Regla 4: texto ISO a pl.Date.
        pl.col("fecha_registro").str.to_date("%Y-%m-%d").alias("fecha_registro"),
        # Regla 5: lista a texto separado por "|"; lista vacía -> "".
        pl.col("etiquetas").list.join("|", ignore_nulls=True).alias("etiquetas"),
    ).select(COLUMNAS_SALIDA)

    # Regla 7: códigos repetidos (se evalúa después de normalizar).
    repetidos = (
        df.filter(
            pl.col("cod_cliente").is_not_null() & pl.col("cod_cliente").is_duplicated()
        )
        .get_column("cod_cliente")
        .unique()
        .sort()
        .to_list()
    )
    if repetidos:
        raise ValueError(f"cod_cliente repetidos: {', '.join(repetidos)}")

    return df


if __name__ == "__main__":
    clientes = aplanar_clientes("clientes_crm.json")

    print(f"Filas: {clientes.height}")
    print("Nulos por columna:")
    print(clientes.null_count())

    clientes.write_parquet("clientes_planos.parquet")
