-- =====================================================================
-- Esquema en estrella a partir de ventas_integradas.parquet (DuckDB 1.x)
-- =====================================================================

-- 0) Carga de la tabla plana en una tabla temporal
CREATE OR REPLACE TEMP TABLE ventas AS
SELECT * FROM read_parquet('ventas_integradas.parquet');

-- 1) dim_fecha: calendario completo de 2025 (un registro por día)
COPY (
    WITH calendario AS (
        SELECT CAST(d AS DATE) AS fecha
        FROM generate_series(DATE '2025-01-01', DATE '2025-12-31', INTERVAL 1 DAY) AS t(d)
    )
    SELECT
        fecha,
        CAST(year(fecha) AS INTEGER)                    AS anio,
        concat('T', quarter(fecha))                     AS trimestre,
        CAST(month(fecha) AS INTEGER)                   AS mes_num,
        -- Nombres en español por lista (índice base 1), sin depender del locale
        ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
         'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'][month(fecha)] AS mes_nombre,
        strftime(fecha, '%Y-%m')                        AS anio_mes,
        CAST(isodow(fecha) AS INTEGER)                  AS dia_semana_num,   -- 1 = lunes ... 7 = domingo
        ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado',
         'Domingo'][isodow(fecha)]                      AS dia_semana_nombre,
        isodow(fecha) >= 6                              AS es_fin_de_semana
    FROM calendario
    ORDER BY fecha
) TO 'dim_fecha.parquet' (FORMAT PARQUET);

-- 2) dim_cliente: un registro por cod_cliente; nulos -> 'Sin información'
COPY (
    SELECT
        cod_cliente,
        -- MAX ignora nulos: toma el valor informado si existe en alguna venta
        COALESCE(MAX(razon_social), 'Sin información') AS razon_social,
        COALESCE(MAX(segmento),     'Sin información') AS segmento,
        COALESCE(MAX(ciudad),       'Sin información') AS ciudad,
        COALESCE(MAX(departamento), 'Sin información') AS departamento
    FROM ventas
    GROUP BY cod_cliente
    ORDER BY cod_cliente
) TO 'dim_cliente.parquet' (FORMAT PARQUET);

-- 3) dim_producto: un registro por sku (atributos de la venta más reciente)
COPY (
    SELECT sku, nombre_producto, categoria, costo_unitario
    FROM (
        SELECT
            sku, nombre_producto, categoria, costo_unitario,
            ROW_NUMBER() OVER (PARTITION BY sku ORDER BY fecha DESC, id_venta DESC) AS rn
        FROM ventas
    )
    WHERE rn = 1
    ORDER BY sku
) TO 'dim_producto.parquet' (FORMAT PARQUET);

-- 4) fact_ventas: una fila por venta, solo llaves, medidas e indicadores
COPY (
    SELECT
        id_venta,
        CAST(fecha AS DATE) AS fecha,
        cod_cliente,
        sku,
        canal,
        cantidad,
        precio_unitario,
        total_venta,
        margen,
        es_devolucion,
        cliente_sin_crm
    FROM ventas
    ORDER BY fecha, id_venta
) TO 'fact_ventas.parquet' (FORMAT PARQUET);

-- =====================================================================
-- VALIDACIONES (se leen los Parquet generados; una fila por validación)
-- =====================================================================

-- (a) Llaves únicas en cada dimensión
SELECT 'a1. Llave única en dim_fecha' AS validacion,
       CASE WHEN count(*) = count(DISTINCT fecha) THEN 'OK' ELSE 'ERROR' END AS resultado,
       concat('filas=', count(*), ' | llaves distintas=', count(DISTINCT fecha)) AS detalle
FROM read_parquet('dim_fecha.parquet')

UNION ALL
SELECT 'a2. Llave única en dim_cliente',
       CASE WHEN count(*) = count(DISTINCT cod_cliente) THEN 'OK' ELSE 'ERROR' END,
       concat('filas=', count(*), ' | llaves distintas=', count(DISTINCT cod_cliente))
FROM read_parquet('dim_cliente.parquet')

UNION ALL
SELECT 'a3. Llave única en dim_producto',
       CASE WHEN count(*) = count(DISTINCT sku) THEN 'OK' ELSE 'ERROR' END,
       concat('filas=', count(*), ' | llaves distintas=', count(DISTINCT sku))
FROM read_parquet('dim_producto.parquet')

-- (b) Sin llaves huérfanas de la tabla de hechos
UNION ALL
SELECT 'b1. Huérfanas fact -> dim_fecha',
       CASE WHEN count(*) = 0 THEN 'OK' ELSE 'ERROR' END,
       concat('filas huérfanas=', count(*))
FROM read_parquet('fact_ventas.parquet') f
LEFT JOIN read_parquet('dim_fecha.parquet') d ON f.fecha = d.fecha
WHERE d.fecha IS NULL

UNION ALL
SELECT 'b2. Huérfanas fact -> dim_cliente',
       CASE WHEN count(*) = 0 THEN 'OK' ELSE 'ERROR' END,
       concat('filas huérfanas=', count(*))
FROM read_parquet('fact_ventas.parquet') f
LEFT JOIN read_parquet('dim_cliente.parquet') d ON f.cod_cliente = d.cod_cliente
WHERE d.cod_cliente IS NULL

UNION ALL
SELECT 'b3. Huérfanas fact -> dim_producto',
       CASE WHEN count(*) = 0 THEN 'OK' ELSE 'ERROR' END,
       concat('filas huérfanas=', count(*))
FROM read_parquet('fact_ventas.parquet') f
LEFT JOIN read_parquet('dim_producto.parquet') d ON f.sku = d.sku
WHERE d.sku IS NULL

-- (c) Conciliación de filas y de total_venta contra la tabla plana
UNION ALL
SELECT 'c1. Número de filas fact vs tabla plana',
       CASE WHEN f.n = p.n THEN 'OK' ELSE 'ERROR' END,
       concat('fact=', f.n, ' | plana=', p.n)
FROM (SELECT count(*) AS n FROM read_parquet('fact_ventas.parquet')) f
CROSS JOIN (SELECT count(*) AS n FROM read_parquet('ventas_integradas.parquet')) p

UNION ALL
SELECT 'c2. Suma total_venta fact vs tabla plana',
       -- Tolerancia de 1 centavo por redondeo de punto flotante (DOUBLE)
       CASE WHEN abs(f.s - p.s) < 0.01 THEN 'OK' ELSE 'ERROR' END,
       concat('fact=', round(f.s, 2), ' | plana=', round(p.s, 2))
FROM (SELECT COALESCE(sum(total_venta), 0) AS s FROM read_parquet('fact_ventas.parquet')) f
CROSS JOIN (SELECT COALESCE(sum(total_venta), 0) AS s FROM read_parquet('ventas_integradas.parquet')) p

-- (d) dim_fecha con 365 filas
UNION ALL
SELECT 'd1. dim_fecha tiene 365 filas',
       CASE WHEN count(*) = 365 THEN 'OK' ELSE 'ERROR' END,
       concat('filas=', count(*))
FROM read_parquet('dim_fecha.parquet')

ORDER BY validacion;
