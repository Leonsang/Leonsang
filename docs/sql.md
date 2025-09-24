# SQL en Data Engineering

> "SQL es el lenguaje universal para consultar, transformar y modelar datos."

---

## 🗄️ ¿Por qué SQL?

SQL (Structured Query Language) es esencial en data engineering para interactuar con bases de datos relacionales y cloud, modelar datos, optimizar consultas y construir reportes.

---

## 🛠️ Motores y Herramientas

- **PostgreSQL:** Base de datos relacional open source, robusta y escalable.
- **BigQuery:** Data warehouse serverless de Google Cloud.
- **Snowflake:** Plataforma cloud para almacenamiento y análisis de datos.
- **Redshift:** Data warehouse de AWS.
- **SQL Server:** Solución empresarial de Microsoft.
- **SQLite:** Base de datos ligera y embebida.
- **dbt:** Modelado y transformación de datos con SQL.

---

## 🧩 Modelado y Transformación

- **Normalización y desnormalización**
- **Joins, subconsultas y CTEs**
- **Funciones de ventana y agregación**
- **Optimización de índices y particiones**
- **Testing y documentación con dbt**

---

## 💡 Buenas Prácticas

!!! tip "Escribe consultas legibles y eficientes"
    Usa CTEs, comentarios y evita subconsultas innecesarias.

!!! info "Versiona y documenta tus modelos"
    dbt permite mantener control y trazabilidad sobre los modelos SQL.

!!! success "Optimiza el performance"
    Analiza planes de ejecución, usa índices y particiones.

---

## 📝 Ejemplo de Consulta Avanzada

```sql
WITH ventas_diarias AS (
  SELECT fecha, SUM(monto) AS total
  FROM ventas
  WHERE fecha >= '2024-01-01'
  GROUP BY fecha
)
SELECT fecha, total
FROM ventas_diarias
WHERE total > 1000
ORDER BY fecha DESC;
```

---

## 📚 Recursos

- [SQL for Data Engineers](https://www.dataengineeringpodcast.com/sql-data-engineers-episode-100/)
- [Awesome SQL](https://github.com/numetriclabz/awesome-sql)
- [dbt Documentation](https://docs.getdbt.com/docs/introduction)
- [BigQuery SQL Reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

---

¿Quieres ver ejemplos de modelado avanzado o notebooks embebidos? ¡Explora la sección Notebooks!
