# Databricks: Plataforma Lakehouse Unificada

> "Databricks acelera el ciclo de vida de datos y machine learning con una arquitectura lakehouse moderna."

---

## 🔥 ¿Qué es Databricks?

Databricks es una plataforma cloud que integra Apache Spark, Delta Lake y MLflow para procesamiento de datos, análisis avanzado y machine learning colaborativo. Combina las ventajas de data warehouses y data lakes en una única arquitectura lakehouse.

---

## 🏗️ Arquitectura Lakehouse

### Evolución: Data Warehouse → Data Lake → Lakehouse

![Evolución Arquitectura](https://github.com/user-attachments/assets/155a9882-97a7-4cbd-a37b-720b8b04e2fb)

#### Problemas de Data Warehouses Tradicionales
- ❌ Solo datos estructurados
- ❌ Escalabilidad limitada
- ❌ Procesamiento lento para Big Data
- ❌ No soporta ML/AI eficientemente

#### Problemas de Data Lakes
- ❌ Sin soporte transaccional ACID
- ❌ Falta de governance y esquemas
- ❌ "Data swamps" - datos sin calidad
- ❌ Complejidad en mantenimiento

#### ✅ Solución Lakehouse
- **Mejor de ambos mundos:** Flexibilidad del data lake + Estructura del data warehouse
- **ACID transactions:** Garantías de consistencia
- **Schema enforcement:** Control de calidad de datos
- **Unified governance:** Seguridad centralizada
- **Performance:** Optimizado para analytics y ML

---

## 🛠️ Componentes Clave

### Core Technologies

- **Delta Lake:** Almacenamiento transaccional con versionado y time travel
- **Apache Spark:** Motor de procesamiento distribuido
- **Photon Engine:** Acelerador de consultas nativo C++
- **Unity Catalog:** Governance y seguridad centralizada
- **MLflow:** Gestión completa del ciclo de vida ML

### Workspace Components

- **Notebooks colaborativos:** Python, SQL, Scala, R
- **Clusters escalables:** Auto-scaling, multi-cloud
- **Jobs & Workflows:** Orquestación y automatización
- **Delta Live Tables:** Pipelines declarativos de datos
- **Dashboards:** Visualización interactiva
- **Repos:** Integración Git para DevOps

---

## 🚀 Delta Lake: El Corazón del Lakehouse

### ¿Qué es Delta Lake?

![Delta Lake Structure](https://github.com/user-attachments/assets/5103715a-10a1-483c-a784-b02d0932867d)

Delta Lake es un formato de almacenamiento open source que aporta:

#### Características Principales
- **ACID Transactions:** Operaciones atómicas, consistentes, aisladas y durables
- **Schema Evolution:** Cambios de esquema seguros y automáticos
- **Time Travel:** Consultar versiones históricas de datos
- **Unified Batch & Streaming:** API unificada para ambos patrones
- **Audit History:** Registro completo de cambios

#### Arquitectura de Archivos

![Delta Files](https://github.com/user-attachments/assets/c9d5b8eb-e2b9-4d2d-a202-3406834797c4)

```
delta-table/
├── _delta_log/           # Transaction log
│   ├── 00000000000000000000.json
│   ├── 00000000000000000001.json
│   └── ...
├── part-00000-xxx.parquet # Data files
├── part-00001-xxx.parquet
└── ...
```

### Ejemplo Práctico con Delta Lake

```python
# Databricks notebook source
from pyspark.sql import SparkSession
from delta.tables import DeltaTable
import pyspark.sql.functions as F

spark = SparkSession.builder \
    .appName("Delta Lake Demo") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Crear tabla Delta
data = [
    (1, "Juan", "Ventas", 50000),
    (2, "María", "Marketing", 60000),
    (3, "Pedro", "IT", 70000)
]

schema = ["id", "nombre", "departamento", "salario"]
df = spark.createDataFrame(data, schema)

# Escribir como tabla Delta
df.write \
  .format("delta") \
  .mode("overwrite") \
  .saveAsTable("empleados")

print("✅ Tabla Delta creada exitosamente")
```

### Operaciones CRUD con Delta Lake

```python
from delta.tables import DeltaTable

# Leer tabla Delta
empleados = spark.table("empleados")
empleados.show()

# Update con condiciones
delta_table = DeltaTable.forName(spark, "empleados")

delta_table.update(
    condition = "departamento = 'IT'",
    set = {"salario": "salario * 1.1"}  # Aumento 10%
)

# Merge (Upsert)
nuevos_datos = [
    (4, "Ana", "HR", 55000),
    (2, "María", "Marketing", 65000)  # Update existing
]

df_nuevos = spark.createDataFrame(nuevos_datos, schema)

delta_table.alias("target") \
    .merge(df_nuevos.alias("source"), "target.id = source.id") \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll() \
    .execute()

print("✅ Merge completado")

# Time Travel - Ver versiones históricas
empleados_v0 = spark.read.format("delta") \
    .option("versionAsOf", 0) \
    .table("empleados")

print("📅 Version 0:")
empleados_v0.show()

# Ver historia de cambios
delta_table.history().select("version", "timestamp", "operation").show()
```

### Schema Evolution Automática

```python
# Agregar nuevas columnas dinámicamente
nuevos_empleados = [
    (5, "Carlos", "Finanzas", 75000, "carlos@empresa.com", "2024-01-15")
]

nuevo_schema = ["id", "nombre", "departamento", "salario", "email", "fecha_ingreso"]
df_expandido = spark.createDataFrame(nuevos_empleados, nuevo_schema)

# Delta Lake automáticamente evoluciona el schema
df_expandido.write \
    .format("delta") \
    .mode("append") \
    .option("mergeSchema", "true") \
    .saveAsTable("empleados")

print("✅ Schema evolucionado automáticamente")
spark.table("empleados").printSchema()
```

---

## ⚡ Photon Engine: Aceleración Nativa

### ¿Qué es Photon?

![Photon Engine](https://github.com/user-attachments/assets/259e096d-ebe7-49ba-9547-9a9749b7ad6c)

Photon es un motor de ejecución nativo en C++ que acelera consultas SQL y operaciones Spark:

- **3-8x más rápido** que Spark tradicional
- **Reducción de costos** por mayor eficiencia
- **Compatibilidad total** con APIs Spark existentes
- **Optimizado para Delta Lake**

### Configuración de Cluster con Photon

```python
# En configuración de cluster
spark.conf.set("spark.databricks.photon.enabled", "true")
spark.conf.set("spark.databricks.photon.adaptive.enabled", "true")

# Verificar si Photon está activo
print(f"Photon enabled: {spark.conf.get('spark.databricks.photon.enabled', 'false')}")
```

---

## 🔐 Unity Catalog: Governance Unificada

### Arquitectura de Governance

![Unity Catalog](https://github.com/user-attachments/assets/73e21ba7-23e7-4d80-ba87-617384b8de4f)

Unity Catalog proporciona:

#### Características Principales
- **Metastore centralizado** para múltiples workspaces
- **Fine-grained access control** a nivel de fila y columna
- **Data lineage** automático
- **Audit logging** completo
- **Tag-based governance**

### Ejemplo de Configuración de Acceso

```sql
-- Crear esquema con permisos
CREATE SCHEMA IF NOT EXISTS main.sales_data;

-- Otorgar permisos granulares
GRANT SELECT, INSERT ON SCHEMA main.sales_data TO `data-analysts@empresa.com`;
GRANT ALL PRIVILEGES ON SCHEMA main.sales_data TO `data-engineers@empresa.com`;

-- Row-level security
CREATE OR REPLACE FUNCTION main.sales_data.filter_region(region STRING)
RETURNS BOOLEAN
RETURN current_user() LIKE '%admin%' OR region = current_user_region();

ALTER TABLE main.sales_data.transactions
SET ROW FILTER main.sales_data.filter_region(region);

-- Column masking para datos sensibles
ALTER TABLE main.sales_data.customers
ALTER COLUMN email
SET MASK CASE
  WHEN current_user() LIKE '%admin%' THEN email
  ELSE regexp_replace(email, '(.+)@(.+)', 'xxx@$2')
END;
```

---

## 🔄 Delta Live Tables: Pipelines Declarativos

### ¿Qué son Delta Live Tables?

DLT permite definir pipelines de datos usando SQL o Python declarativo con:

- **Dependency management** automático
- **Data quality monitoring**
- **Schema inference**
- **Auto-scaling** de recursos

### Ejemplo de Pipeline DLT

```python
import dlt
from pyspark.sql.functions import *

# Bronze layer - Raw data ingestion
@dlt.table(
    comment="Raw sales data from source system",
    table_properties={"quality": "bronze"}
)
def raw_sales():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.schemaLocation", "/path/to/schema")
        .load("/path/to/raw/sales/")
    )

# Silver layer - Cleaned and validated
@dlt.table(
    comment="Cleaned sales data with quality checks"
)
@dlt.expect_or_drop("valid_amount", "amount > 0")
@dlt.expect_or_drop("valid_date", "sale_date IS NOT NULL")
def cleaned_sales():
    return (
        dlt.read_stream("raw_sales")
        .select(
            col("transaction_id"),
            col("customer_id"),
            to_timestamp("sale_date").alias("sale_date"),
            col("amount").cast("decimal(10,2)"),
            col("product_id")
        )
        .dropDuplicates(["transaction_id"])
    )

# Gold layer - Business aggregations
@dlt.table(
    comment="Daily sales aggregations for reporting"
)
def daily_sales_summary():
    return (
        dlt.read_stream("cleaned_sales")
        .groupBy(
            window(col("sale_date"), "1 day").alias("date_window"),
            col("product_id")
        )
        .agg(
            sum("amount").alias("total_sales"),
            count("transaction_id").alias("transaction_count"),
            avg("amount").alias("avg_transaction_value")
        )
        .select(
            col("date_window.start").alias("sale_date"),
            col("product_id"),
            col("total_sales"),
            col("transaction_count"),
            col("avg_transaction_value")
        )
    )
```

---

## 🔧 Clusters y Configuración Avanzada

### Tipos de Clusters

#### All-Purpose Clusters
```python
# Configuración recomendada para desarrollo
cluster_config = {
    "spark_version": "13.3.x-scala2.12",
    "node_type_id": "i3.xlarge",
    "num_workers": 2,
    "autoscale": {
        "min_workers": 1,
        "max_workers": 8
    },
    "spark_conf": {
        "spark.databricks.photon.enabled": "true",
        "spark.serializer": "org.apache.spark.serializer.KryoSerializer"
    }
}
```

#### Job Clusters (Producción)
```python
# Optimizado para workloads específicos
production_config = {
    "new_cluster": {
        "spark_version": "13.3.x-scala2.12",
        "node_type_id": "i3.2xlarge",
        "num_workers": 10,
        "spark_conf": {
            "spark.databricks.photon.enabled": "true",
            "spark.sql.adaptive.enabled": "true",
            "spark.sql.adaptive.coalescePartitions.enabled": "true"
        }
    },
    "libraries": [
        {"pypi": {"package": "great-expectations"}},
        {"maven": {"coordinates": "io.delta:delta-core_2.12:2.4.0"}}
    ]
}
```

### Optimizaciones de Performance

```python
# Configuraciones avanzadas de Spark
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.databricks.delta.preview.enabled", "true")

# Optimización para Delta Lake
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.databricks.delta.autoCompact.enabled", "true")

# Cache inteligente
df_frecuente = spark.table("sales_data").cache()
df_frecuente.count()  # Materializar cache
```

---

## 🎯 Casos de Uso Avanzados

### 1. Pipeline ETL Completo en Databricks

```python
# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from delta.tables import DeltaTable

class DataPipeline:
    def __init__(self, spark):
        self.spark = spark

    def extract_from_source(self, source_path):
        """Extrae datos de múltiples fuentes"""
        # Bronze layer - Raw ingestion
        raw_df = (
            self.spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "json")
            .option("cloudFiles.schemaHints", "timestamp timestamp")
            .load(source_path)
            .withColumn("ingestion_time", current_timestamp())
            .withColumn("source_file", input_file_name())
        )

        return raw_df

    def transform_silver_layer(self, bronze_df):
        """Limpia y estructura los datos"""
        silver_df = (
            bronze_df
            .filter(col("customer_id").isNotNull())
            .withColumn("sale_date", to_date("timestamp"))
            .withColumn("amount", col("amount").cast("decimal(10,2)"))
            .dropDuplicates(["transaction_id"])
            .withColumn("processed_time", current_timestamp())
        )

        return silver_df

    def create_gold_aggregations(self, silver_df):
        """Crea agregaciones de negocio"""
        gold_df = (
            silver_df
            .groupBy(
                window("sale_date", "1 day"),
                "product_category"
            )
            .agg(
                sum("amount").alias("total_revenue"),
                count("transaction_id").alias("transaction_count"),
                countDistinct("customer_id").alias("unique_customers")
            )
            .select(
                col("window.start").alias("date"),
                col("product_category"),
                col("total_revenue"),
                col("transaction_count"),
                col("unique_customers")
            )
        )

        return gold_df

# Ejecutar pipeline
pipeline = DataPipeline(spark)

# Bronze
bronze_stream = pipeline.extract_from_source("/mnt/raw-data/sales/")

# Silver
silver_stream = pipeline.transform_silver_layer(bronze_stream)

# Escribir a Delta Lake con checkpointing
bronze_query = (
    bronze_stream.writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/checkpoints/bronze/")
    .table("bronze.raw_sales")
)

silver_query = (
    silver_stream.writeStream
    .format("delta")
    .option("checkpointLocation", "/mnt/checkpoints/silver/")
    .table("silver.clean_sales")
)

print("🚀 Pipeline iniciado exitosamente")
```

### 2. Machine Learning con MLflow

```python
import mlflow
import mlflow.spark
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Configurar MLflow
mlflow.set_experiment("/Shared/sales-prediction")

with mlflow.start_run():
    # Preparar datos
    df = spark.table("silver.clean_sales")

    # Feature engineering
    assembler = VectorAssembler(
        inputCols=["previous_purchases", "customer_score", "days_since_last"],
        outputCol="features"
    )

    scaler = StandardScaler(
        inputCol="features",
        outputCol="scaled_features"
    )

    # Model
    lr = LinearRegression(
        featuresCol="scaled_features",
        labelCol="amount",
        regParam=0.01
    )

    # Pipeline
    pipeline = Pipeline(stages=[assembler, scaler, lr])

    # Train/Test split
    train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

    # Entrenar modelo
    model = pipeline.fit(train_df)

    # Predicciones
    predictions = model.transform(test_df)

    # Evaluación
    evaluator = RegressionEvaluator(
        labelCol="amount",
        predictionCol="prediction",
        metricName="rmse"
    )

    rmse = evaluator.evaluate(predictions)

    # Log metricas y modelo
    mlflow.log_param("regParam", 0.01)
    mlflow.log_metric("rmse", rmse)
    mlflow.spark.log_model(model, "sales-prediction-model")

    print(f"✅ Modelo entrenado con RMSE: {rmse:.2f}")
```

---

## 💡 Buenas Prácticas

!!! tip "Diseño de Arquitectura"
    - Implementa arquitectura medallion (Bronze → Silver → Gold)
    - Usa Delta Lake para todas las capas
    - Aplica principios de data mesh para datasets grandes
    - Separa clusters por workload (batch vs streaming)

!!! info "Optimización de Performance"
    - Habilita Photon Engine para workloads SQL intensivos
    - Usa Z-Ordering para optimizar queries frecuentes
    - Implementa Auto Optimize para mantenimiento automático
    - Particiona tablas grandes por fechas

!!! success "Governance y Seguridad"
    - Implementa Unity Catalog desde el inicio
    - Usa tag-based governance para clasificación automática
    - Configura row/column level security según necesidades
    - Mantén audit logs habilitados

!!! warning "Gestión de Costos"
    - Usa Job Clusters para workloads de producción
    - Configura auto-termination en clusters interactivos
    - Monitorea DBU consumption regularmente
    - Implementa resource tagging para cost allocation

---

## 🔧 Comandos y Utilidades

### Mantenimiento de Delta Tables

```sql
-- Optimize y Z-Order
OPTIMIZE sales_data ZORDER BY (customer_id, sale_date);

-- Vacuum para limpiar archivos antiguos
VACUUM sales_data RETAIN 168 HOURS;

-- Analyze table statistics
ANALYZE TABLE sales_data COMPUTE STATISTICS FOR ALL COLUMNS;

-- Ver métricas de tabla
DESCRIBE DETAIL sales_data;

-- History y time travel
SELECT * FROM sales_data TIMESTAMP AS OF '2024-01-15T10:30:00';
SELECT * FROM sales_data VERSION AS OF 42;
```

### Comandos útiles de cluster

```python
# Información del cluster
spark.conf.get("spark.app.name")
spark.conf.get("spark.databricks.clusterUsageTags.clusterId")

# Métricas de memoria
spark.sparkContext.getExecutorMemoryStatus()

# Cache management
spark.catalog.clearCache()
spark.catalog.cacheTable("my_table")
spark.catalog.uncacheTable("my_table")
```

---

## 📚 Recursos Avanzados

### Documentación Oficial
- [Databricks Documentation](https://docs.databricks.com/)
- [Delta Lake Documentation](https://docs.delta.io/)
- [Unity Catalog Guide](https://docs.databricks.com/data-governance/unity-catalog/)
- [Delta Live Tables](https://docs.databricks.com/workflows/delta-live-tables/)

### Certificaciones
- [Databricks Certified Data Engineer Associate](https://academy.databricks.com/)
- [Databricks Certified Data Analyst Associate](https://academy.databricks.com/)
- [Delta Lake Accreditation](https://academy.databricks.com/)

### Comunidad y Recursos
- [Databricks Community](https://community.databricks.com/)
- [Delta Lake Community](https://github.com/delta-io/delta)
- [Databricks Academy](https://academy.databricks.com/)

---

¿Quieres profundizar en casos específicos? ¡Explora las otras secciones sobre Spark internals y arquitecturas avanzadas!
