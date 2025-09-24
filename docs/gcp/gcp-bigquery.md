# BigQuery: Data Warehouse Serverless de Google Cloud

> "BigQuery es el data warehouse completamente administrado y serverless de Google que permite análisis de petabytes de datos."

---

## 🌟 ¿Qué es BigQuery?

BigQuery es una plataforma de análisis de datos completamente administrada que permite ejecutar consultas SQL súper rápidas en conjuntos de datos masivos utilizando la infraestructura de procesamiento de Google.

---

## 🏗️ Arquitectura de BigQuery

### Componentes Principales

- **Dremel Engine**: Motor de consultas columnares distribuido
- **Colossus**: Sistema de archivos distribuido de Google
- **Jupiter Network**: Red petabit interna de Google
- **Borg**: Sistema de orquestación de contenedores

### Almacenamiento Columnar

```sql
-- Consulta optimizada por columnas
SELECT
    customer_id,
    SUM(revenue) as total_revenue
FROM `project.dataset.sales`
WHERE date >= '2024-01-01'
GROUP BY customer_id
HAVING total_revenue > 10000;
```

---

## ⚡ Características Clave

### **Serverless y Escalable**
- Sin infraestructura que gestionar
- Escalamiento automático a petabytes
- Pago por consulta o capacidad reservada

### **SQL Estándar**
- Compatible con SQL ANSI estándar
- Funciones avanzadas de análisis
- Soporte para UDFs en JavaScript y SQL

### **Integración Nativa**
- Conecta con Dataflow, Dataproc, AI Platform
- Streaming inserts en tiempo real
- Exportación automática a Cloud Storage

---

## 🚀 Casos de Uso Comunes

### 1. Data Warehousing Empresarial

```sql
-- ETL con BigQuery SQL
CREATE OR REPLACE TABLE `analytics.customer_summary` AS
SELECT
    c.customer_id,
    c.customer_name,
    c.segment,
    COUNT(DISTINCT o.order_id) as total_orders,
    SUM(o.amount) as lifetime_value,
    DATE_DIFF(CURRENT_DATE(), MAX(o.order_date), DAY) as days_since_last_order
FROM `raw.customers` c
LEFT JOIN `raw.orders` o ON c.customer_id = o.customer_id
WHERE c.status = 'ACTIVE'
GROUP BY 1, 2, 3;
```

### 2. Análisis de Logs en Tiempo Real

```sql
-- Streaming analytics con BigQuery
SELECT
    EXTRACT(HOUR FROM timestamp) as hour,
    status_code,
    COUNT(*) as request_count,
    AVG(response_time) as avg_response_time
FROM `logs.web_requests`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)
GROUP BY 1, 2
ORDER BY 1, 2;
```

### 3. Machine Learning Integrado

```sql
-- BigQuery ML para predicción
CREATE OR REPLACE MODEL `ml.customer_churn_model`
OPTIONS(
    model_type='LOGISTIC_REG',
    input_label_cols=['churned']
) AS
SELECT
    days_since_last_order,
    total_orders,
    lifetime_value,
    segment,
    churned
FROM `analytics.customer_features`
WHERE partition_date >= '2023-01-01';

-- Hacer predicciones
SELECT
    customer_id,
    predicted_churned,
    predicted_churned_probs[OFFSET(0)] as churn_probability
FROM ML.PREDICT(MODEL `ml.customer_churn_model`,
    TABLE `analytics.current_customers`);
```

---

## 🔧 Optimización de Performance

### Particionado Inteligente

```sql
-- Crear tabla particionada
CREATE OR REPLACE TABLE `dataset.sales_partitioned`
PARTITION BY DATE(sale_date)
CLUSTER BY customer_id, product_category
AS SELECT * FROM `dataset.sales_raw`;
```

### Consultas Optimizadas

```sql
-- Usar particiones para mejor performance
SELECT
    product_category,
    SUM(revenue) as total_revenue
FROM `dataset.sales_partitioned`
WHERE DATE(sale_date) BETWEEN '2024-01-01' AND '2024-01-31'  -- Partition pruning
GROUP BY product_category;
```

---

## 💰 Estrategias de Costos

### Control de Costos por Query

```sql
-- Configurar límites de bytes procesados
SELECT
    customer_id,
    revenue
FROM `large_dataset.sales`
WHERE date = '2024-01-01'  -- Usa particiones
LIMIT 1000;  -- Limita resultados
```

### Slots Reservados vs On-Demand

- **On-Demand**: Pago por TB procesados
- **Flat-Rate**: Capacidad reservada mensual
- **Flex Slots**: Capacidad por minuto

---

## 📊 Integración con Ecosystem GCP

### Con Dataflow

```python
# Apache Beam pipeline a BigQuery
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run_pipeline():
    pipeline_options = PipelineOptions([
        '--project=my-gcp-project',
        '--runner=DataflowRunner',
        '--temp_location=gs://my-bucket/temp'
    ])

    with beam.Pipeline(options=pipeline_options) as pipeline:
        (pipeline
         | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/my-project/topics/events')
         | 'Parse JSON' >> beam.Map(parse_json)
         | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
             table='my-project:dataset.streaming_data',
             schema=table_schema,
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))
```

### Con Cloud Functions

```python
# Cloud Function para cargar datos
from google.cloud import bigquery

def load_data_to_bq(event, context):
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True
    )

    uri = f"gs://{event['bucket']}/{event['name']}"
    table_id = "my-project.dataset.uploaded_data"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )

    load_job.result()  # Waits for job completion
    print(f"Loaded {load_job.output_rows} rows to {table_id}")
```

---

## 🛡️ Seguridad y Governance

### Row-Level Security

```sql
-- Crear política de acceso por filas
CREATE ROW ACCESS POLICY region_filter
ON `dataset.sales`
GRANT TO ('data-analyst@company.com')
FILTER USING (region = SESSION_USER_REGION());
```

### Column-Level Security

```sql
-- Crear vista con masking
CREATE OR REPLACE VIEW `dataset.customer_masked` AS
SELECT
    customer_id,
    CASE
        WHEN SESSION_USER() IN ('admin@company.com')
        THEN email
        ELSE REGEXP_REPLACE(email, r'(.{3}).*(@.*)', r'\1***\2')
    END as email_masked,
    purchase_amount
FROM `dataset.customers`;
```

---

## 📚 Mejores Prácticas

!!! tip "Optimización de Consultas"
    - Usa SELECT específico, evita SELECT *
    - Aprovecha particionado y clustering
    - Usa APPROX functions para estimaciones rápidas
    - Implementa WHERE clauses en particiones

!!! info "Gestión de Costos"
    - Monitorea uso con Cloud Monitoring
    - Implementa alertas de presupuesto
    - Usa vistas materializadas para queries frecuentes
    - Considera slots reservados para cargas predecibles

!!! success "Seguridad"
    - Implementa principio de menor privilegio
    - Usa datasets separados por ambiente
    - Configura data loss prevention (DLP)
    - Audita acceso con Cloud Audit Logs

---

¿Listo para procesar petabytes con BigQuery? ¡Explora más casos avanzados en las otras secciones de GCP!