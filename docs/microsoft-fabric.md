# Microsoft Fabric: Plataforma Analytics Unificada

> "Microsoft Fabric revoluciona la analítica empresarial con una plataforma SaaS todo-en-uno."

---

## 🔥 ¿Qué es Microsoft Fabric?

Microsoft Fabric es una plataforma de análisis empresarial unificada que integra herramientas de ingeniería de datos, ciencia de datos, análisis en tiempo real, inteligencia empresarial y almacenamiento de datos en una sola experiencia SaaS.

---

## 🏗️ Arquitectura y Componentes

### Vista General de la Plataforma

![Fabric Architecture](https://github.com/user-attachments/assets/7c34baaa-fe51-4d01-b47e-34a19eb573e0)

### Componentes Clave

![Fabric Components](https://github.com/user-attachments/assets/0bf7b0ad-55f1-4744-a6d9-98bdfb9ac455)

#### **Data Factory**
- Integración y orquestación de datos
- Pipelines ETL/ELT visuales
- Conectores a 200+ fuentes de datos
- Dataflows para transformaciones self-service

#### **Synapse Data Engineering**
- Apache Spark notebooks nativos
- Spark job definitions y pipelines
- Bibliotecas y gestión de ambientes
- Integración con Git y CI/CD

#### **Synapse Data Warehouse**
- SQL engine de alto rendimiento
- Escalamiento automático
- Compatibilidad T-SQL completa
- Seguridad a nivel de fila y columna

#### **Synapse Data Science**
- Notebooks Jupyter integrados
- MLflow tracking y deployment
- AutoML y herramientas visuales
- Integración con Azure ML

#### **Real-Time Analytics**
- KQL databases para streaming
- Event streams y event houses
- Dashboards en tiempo real
- Integración con Power BI

#### **Power BI Premium**
- Modelado semántico avanzado
- Reportes y dashboards
- Paginated reports
- Embedding capabilities

---

## 🚀 Arquitectura del Proyecto

### Prerrequisitos

![Prerequisites](https://github.com/user-attachments/assets/7eb5d4bc-accd-44f9a276-11acfb8a3f5b)

- **Microsoft Fabric Capacity:** F2 mínimo recomendado
- **Power BI Pro/Premium:** Para desarrollo y compartir
- **Azure Subscription:** Para recursos complementarios
- **OneLake Storage:** Incluido automáticamente

### Arquitectura de Implementación

![Project Architecture](https://github.com/user-attachments/assets/10271b70-df84-4690-a1ac-1d0b823aca45)

```
Data Sources → Data Factory → Lakehouse → Data Warehouse → Power BI
     ↓              ↓            ↓            ↓           ↓
External APIs → Dataflows → Delta Tables → Semantic Layer → Reports
```

#### Flujo Detallado

![Detailed Flow](https://github.com/user-attachments/assets/73e21ba7-23e7-4d80-ba87-617384b8de4f)

1. **Ingestion:** Data Factory extrae de múltiples fuentes
2. **Raw Storage:** OneLake almacena datos crudos
3. **Processing:** Spark transforma y limpia datos
4. **Curated:** Delta Lake con datos estructurados
5. **Serving:** Data Warehouse para analytics
6. **Visualization:** Power BI para insights

---

## 📊 OneLake: El Corazón de Fabric

### Arquitectura Delta Lake

![Delta Lake Structure](https://github.com/user-attachments/assets/5103715a-10a1-483c-a784-b02d0932867d)

OneLake utiliza Delta Lake como formato de almacenamiento estándar, proporcionando:

#### Características Principales
- **ACID Transactions:** Garantías de consistencia
- **Schema Evolution:** Cambios seguros de estructura
- **Time Travel:** Versioning automático de datos
- **Unified Storage:** Un solo lake para toda la organización
- **Security:** Governance centralizada

### Estructura Interna

![Delta Internal](https://github.com/user-attachments/assets/c9d5b8eb-e2b9-4d2d-a202-3406834797c4)

```
OneLake/
├── Workspaces/
│   ├── Sales-Analytics/
│   │   ├── Lakehouses/
│   │   │   └── sales-data/
│   │   │       ├── Tables/          # Managed tables
│   │   │       └── Files/           # Unstructured data
│   │   └── Warehouses/
│   │       └── sales-dw/
└── System/
    ├── _delta_log/                  # Transaction logs
    └── _metadata/                   # System metadata
```

### Ejemplo: Trabajando con Delta Tables

```python
# Fabric Notebook - PySpark
from pyspark.sql import SparkSession
from delta.tables import DeltaTable
import pyspark.sql.functions as F

# Spark session automáticamente configurado en Fabric
spark = spark  # Pre-configured in Fabric

# Leer datos desde OneLake
df_sales = spark.read.format("delta").table("sales_lakehouse.sales_transactions")

print(f"📊 Total registros: {df_sales.count()}")
df_sales.printSchema()

# Transformaciones
df_processed = df_sales \
    .withColumn("revenue", F.col("quantity") * F.col("price")) \
    .withColumn("month", F.month("transaction_date")) \
    .filter(F.col("status") == "completed")

# Escribir a nueva tabla Delta
df_processed.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("sales_lakehouse.processed_sales")

print("✅ Datos procesados y guardados en OneLake")
```

### Schema Evolution en Fabric

```python
# Evolución automática de esquemas
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Datos con nueva columna
new_data = [
    (1, "Product A", 100, "Electronics", "Online"),  # Nueva columna: channel
    (2, "Product B", 150, "Clothing", "Retail")
]

schema_expanded = StructType([
    StructField("id", IntegerType()),
    StructField("product_name", StringType()),
    StructField("price", IntegerType()),
    StructField("category", StringType()),
    StructField("channel", StringType())  # Nueva columna
])

df_new = spark.createDataFrame(new_data, schema_expanded)

# Delta Lake automáticamente evoluciona el schema
df_new.write \
    .format("delta") \
    .mode("append") \
    .option("mergeSchema", "true") \
    .saveAsTable("sales_lakehouse.products")

print("✅ Schema evolucionado automáticamente")

# Verificar history de cambios
delta_table = DeltaTable.forName(spark, "sales_lakehouse.products")
delta_table.history().show()
```

---

## 🔧 Data Factory: Orquestación de Datos

### Pipeline Visual

![Data Factory Pipeline](https://github.com/user-attachments/assets/39a6f9d6-7842-4401-8f02-486ea80b82ce)

### Ejemplo: Pipeline ETL Completo

```python
# Fabric Data Factory - Copy Activity
{
  "name": "Copy_Sales_Data",
  "type": "Copy",
  "source": {
    "type": "SqlServerSource",
    "sqlReaderQuery": "SELECT * FROM sales WHERE modified_date >= @{formatDateTime(addDays(utcNow(), -1), 'yyyy-MM-dd')}"
  },
  "sink": {
    "type": "DeltaLakeSink",
    "tableName": "sales_lakehouse.raw_sales",
    "mergeSchema": true
  },
  "enableStaging": false,
  "translator": {
    "type": "TabularTranslator",
    "mappings": [
      {"source": {"name": "sale_id"}, "sink": {"name": "transaction_id"}},
      {"source": {"name": "customer_id"}, "sink": {"name": "customer_id"}},
      {"source": {"name": "amount"}, "sink": {"name": "revenue"}}
    ]
  }
}
```

### Dataflow para Transformaciones

```python
# Fabric Dataflow (Power Query M)
let
    Source = Sql.Database("server.database.windows.net", "SalesDB"),
    SalesTable = Source{[Schema="dbo",Item="Sales"]}[Data],

    // Filtrar datos recientes
    FilteredRows = Table.SelectRows(SalesTable, each [ModifiedDate] >= Date.AddDays(Date.From(DateTime.LocalNow()), -7)),

    // Transformaciones
    AddedRevenue = Table.AddColumn(FilteredRows, "Revenue", each [Quantity] * [UnitPrice]),
    AddedCategory = Table.AddColumn(AddedRevenue, "Category",
        each if [Revenue] > 1000 then "High Value"
             else if [Revenue] > 100 then "Medium Value"
             else "Low Value"),

    // Limpiar datos
    RemovedNulls = Table.SelectRows(AddedCategory, each [CustomerID] <> null),
    ChangedTypes = Table.TransformColumnTypes(RemovedNulls, {
        {"Revenue", type number},
        {"TransactionDate", type datetime}
    })
in
    ChangedTypes
```

---

## ⚡ Synapse Data Engineering

### Spark Pools Configuration

```python
# Configuración de Spark Pool en Fabric
spark_config = {
    "spark.sql.adaptive.enabled": "true",
    "spark.sql.adaptive.coalescePartitions.enabled": "true",
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
    "spark.sql.adaptive.skewJoin.enabled": "true",
    "spark.sql.legacy.timeParserPolicy": "LEGACY"
}

# Aplicar configuraciones
for key, value in spark_config.items():
    spark.conf.set(key, value)

print("✅ Spark configurado para optimización")
```

### Ejemplo de Notebook Spark

```python
# Fabric Notebook
# %%markdown
# # Análisis de Ventas - Microsoft Fabric
#
# Este notebook procesa datos de ventas y genera métricas clave para el negocio.

# %%pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import matplotlib.pyplot as plt
import seaborn as sns

# Leer datos desde Lakehouse
df_ventas = spark.table("ventas_lakehouse.transacciones_ventas")
df_productos = spark.table("ventas_lakehouse.productos")
df_clientes = spark.table("ventas_lakehouse.clientes")

print(f"📊 Registros de ventas: {df_ventas.count():,}")
print(f"📦 Productos únicos: {df_productos.count():,}")
print(f"👥 Clientes únicos: {df_clientes.count():,}")

# %%pyspark
# Análisis de tendencias mensuales
tendencias_mensuales = df_ventas \
    .withColumn("anio_mes", date_format("fecha_venta", "yyyy-MM")) \
    .groupBy("anio_mes") \
    .agg(
        sum("monto").alias("ingresos_totales"),
        count("id_venta").alias("transacciones"),
        avg("monto").alias("ticket_promedio"),
        countDistinct("id_cliente").alias("clientes_unicos")
    ) \
    .orderBy("anio_mes")

# Guardar resultados en tabla curada
tendencias_mensuales.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("ventas_lakehouse.tendencias_mensuales")

tendencias_mensuales.show(12)

# %%pyspark
# Análisis por categoría de producto
categoria_performance = df_ventas \
    .join(df_productos, "id_producto") \
    .groupBy("categoria") \
    .agg(
        sum("monto").alias("ingresos"),
        count("id_venta").alias("ventas"),
        avg("monto").alias("precio_promedio")
    ) \
    .orderBy(desc("ingresos"))

categoria_performance.show()

# Visualización
categoria_pd = categoria_performance.toPandas()

plt.figure(figsize=(12, 6))
sns.barplot(data=categoria_pd, x="categoria", y="ingresos")
plt.title("Ingresos por Categoría de Producto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%sql
-- SQL nativo en Fabric Notebook
SELECT
    c.region,
    COUNT(DISTINCT v.id_cliente) as clientes_activos,
    SUM(v.monto) as ingresos_totales,
    AVG(v.monto) as ticket_promedio
FROM ventas_lakehouse.transacciones_ventas v
JOIN ventas_lakehouse.clientes c ON v.id_cliente = c.id_cliente
WHERE v.fecha_venta >= CURRENT_DATE - INTERVAL 90 DAYS
GROUP BY c.region
ORDER BY ingresos_totales DESC

# %%pyspark
# Detección de anomalías en ventas
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

# Preparar features para clustering
feature_cols = ["monto", "cantidad", "descuento_aplicado"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")

df_features = df_ventas.select(
    "id_venta",
    "monto",
    col("cantidad").cast("double"),
    col("descuento_aplicado").cast("double")
).na.fill(0)

df_vector = assembler.transform(df_features)

# K-means clustering para identificar outliers
kmeans = KMeans(k=5, seed=42)
model = kmeans.fit(df_vector)

df_clusters = model.transform(df_vector)

# Identificar transacciones anómalas (cluster con menor población)
cluster_counts = df_clusters.groupBy("prediction").count().collect()
anomaly_cluster = min(cluster_counts, key=lambda x: x['count'])['prediction']

anomalias = df_clusters.filter(col("prediction") == anomaly_cluster)
print(f"🚨 Detectadas {anomalias.count()} transacciones anómalas")

# Guardar anomalías para investigación
anomalias.select("id_venta", "monto", "cantidad", "prediction") \
        .write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable("ventas_lakehouse.transacciones_anomalas")
```

---

## 🏪 Data Warehouse: SQL Analytics

### Creación de Warehouse

```sql
-- Fabric SQL - Crear tablas dimensionales
CREATE TABLE dim_fecha (
    fecha_key INT PRIMARY KEY,
    fecha DATE NOT NULL,
    año INT,
    mes INT,
    trimestre INT,
    nombre_mes VARCHAR(20),
    dia_semana INT,
    nombre_dia VARCHAR(20),
    es_fin_semana BIT
);

CREATE TABLE dim_producto (
    producto_key INT PRIMARY KEY,
    producto_id VARCHAR(50) NOT NULL,
    nombre_producto VARCHAR(200),
    categoria VARCHAR(100),
    subcategoria VARCHAR(100),
    marca VARCHAR(100),
    precio_lista DECIMAL(10,2)
);

CREATE TABLE dim_cliente (
    cliente_key INT PRIMARY KEY,
    cliente_id VARCHAR(50) NOT NULL,
    nombre VARCHAR(200),
    email VARCHAR(200),
    telefono VARCHAR(50),
    ciudad VARCHAR(100),
    estado VARCHAR(100),
    pais VARCHAR(100),
    segmento VARCHAR(50)
);

-- Tabla de hechos
CREATE TABLE fact_ventas (
    venta_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    fecha_key INT,
    producto_key INT,
    cliente_key INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    descuento DECIMAL(10,2),
    impuestos DECIMAL(10,2),
    ingresos DECIMAL(12,2),
    costo DECIMAL(12,2),
    utilidad DECIMAL(12,2),

    FOREIGN KEY (fecha_key) REFERENCES dim_fecha(fecha_key),
    FOREIGN KEY (producto_key) REFERENCES dim_producto(producto_key),
    FOREIGN KEY (cliente_key) REFERENCES dim_cliente(cliente_key)
);
```

### Stored Procedures para ETL

```sql
-- Procedimiento para cargar dimensión fecha
CREATE PROCEDURE sp_load_dim_fecha
AS
BEGIN
    TRUNCATE TABLE dim_fecha;

    WITH date_series AS (
        SELECT CAST('2020-01-01' AS DATE) as fecha
        UNION ALL
        SELECT DATEADD(day, 1, fecha)
        FROM date_series
        WHERE fecha < '2030-12-31'
    )
    INSERT INTO dim_fecha (
        fecha_key, fecha, año, mes, trimestre,
        nombre_mes, dia_semana, nombre_dia, es_fin_semana
    )
    SELECT
        CAST(FORMAT(fecha, 'yyyyMMdd') AS INT) as fecha_key,
        fecha,
        YEAR(fecha) as año,
        MONTH(fecha) as mes,
        DATEPART(quarter, fecha) as trimestre,
        DATENAME(month, fecha) as nombre_mes,
        DATEPART(weekday, fecha) as dia_semana,
        DATENAME(weekday, fecha) as nombre_dia,
        CASE WHEN DATEPART(weekday, fecha) IN (1, 7) THEN 1 ELSE 0 END as es_fin_semana
    FROM date_series
    OPTION (MAXRECURSION 0);

    PRINT 'Dimensión fecha cargada exitosamente';
END;

-- Procedimiento para cargar hechos de ventas
CREATE PROCEDURE sp_load_fact_ventas
    @fecha_proceso DATE = NULL
AS
BEGIN
    IF @fecha_proceso IS NULL
        SET @fecha_proceso = CAST(GETDATE() AS DATE);

    -- Upsert de hechos de ventas
    MERGE fact_ventas AS target
    USING (
        SELECT
            df.fecha_key,
            dp.producto_key,
            dc.cliente_key,
            v.cantidad,
            v.precio_unitario,
            v.descuento,
            v.impuestos,
            v.cantidad * v.precio_unitario - v.descuento as ingresos,
            v.costo_unitario * v.cantidad as costo,
            (v.cantidad * v.precio_unitario - v.descuento) - (v.costo_unitario * v.cantidad) as utilidad
        FROM ventas_lakehouse.transacciones_ventas v
        JOIN dim_fecha df ON CAST(v.fecha_venta AS DATE) = df.fecha
        JOIN dim_producto dp ON v.id_producto = dp.producto_id
        JOIN dim_cliente dc ON v.id_cliente = dc.cliente_id
        WHERE CAST(v.fecha_venta AS DATE) = @fecha_proceso
    ) AS source ON 1=0  -- Always insert for fact table

    WHEN NOT MATCHED THEN
        INSERT (fecha_key, producto_key, cliente_key, cantidad,
                precio_unitario, descuento, impuestos, ingresos, costo, utilidad)
        VALUES (source.fecha_key, source.producto_key, source.cliente_key,
                source.cantidad, source.precio_unitario, source.descuento,
                source.impuestos, source.ingresos, source.costo, source.utilidad);

    PRINT CONCAT('Cargados hechos de ventas para fecha: ', @fecha_proceso);
END;
```

---

## 📊 Power BI Integration

### Semantic Layer

```dax
-- Medidas DAX para el modelo semántico

-- Ingresos Totales
Total Ingresos = SUM(fact_ventas[ingresos])

-- Ingresos Mes Anterior
Ingresos Mes Anterior =
CALCULATE(
    [Total Ingresos],
    DATEADD(dim_fecha[fecha], -1, MONTH)
)

-- Crecimiento MoM
Crecimiento MoM =
VAR IngresosMesActual = [Total Ingresos]
VAR IngresosMesAnterior = [Ingresos Mes Anterior]
RETURN
IF(
    IngresosMesAnterior <> 0,
    DIVIDE(IngresosMesActual - IngresosMesAnterior, IngresosMesAnterior),
    BLANK()
)

-- Top N Productos
Top N Productos Ingresos =
VAR TopNValue = 10
VAR CurrentProductRank =
    RANKX(
        ALL(dim_producto[nombre_producto]),
        [Total Ingresos],
        ,
        DESC
    )
RETURN
IF(CurrentProductRank <= TopNValue, [Total Ingresos], BLANK())

-- Margen de Utilidad %
Margen Utilidad % =
DIVIDE(
    SUM(fact_ventas[utilidad]),
    SUM(fact_ventas[ingresos])
)

-- Clientes Nuevos
Clientes Nuevos =
VAR FechaMinCliente =
    CALCULATE(
        MIN(fact_ventas[fecha_key]),
        ALLEXCEPT(fact_ventas, dim_cliente[cliente_id])
    )
VAR FechaActual = MAX(fact_ventas[fecha_key])
RETURN
COUNTROWS(
    FILTER(
        VALUES(dim_cliente[cliente_id]),
        FechaMinCliente = FechaActual
    )
)

-- Customer Lifetime Value
Customer LTV =
AVERAGEX(
    VALUES(dim_cliente[cliente_id]),
    CALCULATE(SUM(fact_ventas[ingresos]))
)
```

### Report Examples

```json
{
  "reportConfig": {
    "pages": [
      {
        "name": "Executive Dashboard",
        "visuals": [
          {
            "type": "card",
            "title": "Ingresos Totales",
            "measure": "[Total Ingresos]",
            "format": "$#,##0"
          },
          {
            "type": "card",
            "title": "Crecimiento MoM",
            "measure": "[Crecimiento MoM]",
            "format": "0.0%"
          },
          {
            "type": "lineChart",
            "title": "Tendencia de Ingresos",
            "xAxis": "dim_fecha[nombre_mes]",
            "yAxis": "[Total Ingresos]"
          },
          {
            "type": "barChart",
            "title": "Top 10 Productos",
            "xAxis": "dim_producto[nombre_producto]",
            "yAxis": "[Top N Productos Ingresos]"
          }
        ]
      },
      {
        "name": "Customer Analytics",
        "visuals": [
          {
            "type": "table",
            "title": "Customer Analysis",
            "columns": [
              "dim_cliente[nombre]",
              "[Total Ingresos]",
              "[Customer LTV]",
              "[Margen Utilidad %]"
            ]
          },
          {
            "type": "map",
            "title": "Ventas por Región",
            "location": "dim_cliente[ciudad]",
            "size": "[Total Ingresos]"
          }
        ]
      }
    ]
  }
}
```

---

## 🔄 Real-Time Analytics

### Event Streams

```sql
-- KQL para Real-Time Analytics en Fabric
.create table sales_events (
    timestamp: datetime,
    customer_id: string,
    product_id: string,
    event_type: string,
    amount: decimal,
    channel: string,
    session_id: string
)

-- Ingest data from Event Hub
.create-or-alter function ProcessSalesEvents() {
    sales_events
    | where timestamp > ago(1h)
    | where event_type in ("purchase", "add_to_cart", "view_product")
    | extend hour_bucket = bin(timestamp, 1h)
    | summarize
        total_events = count(),
        unique_customers = dcount(customer_id),
        total_amount = sum(amount)
        by hour_bucket, event_type
}

-- Real-time dashboard query
.show table sales_events
| where timestamp > ago(15m)
| summarize
    live_revenue = sum(case(event_type == "purchase", amount, 0)),
    active_sessions = dcount(session_id),
    conversion_rate = todouble(countif(event_type == "purchase")) / todouble(countif(event_type == "view_product")) * 100
    by bin(timestamp, 1m)
| order by timestamp desc
```

### Streaming Integration

```python
# Fabric Real-Time Analytics - Python SDK
from azure.eventhub import EventHubProducerClient, EventData
import json
from datetime import datetime

# Configurar Event Hub producer
producer = EventHubProducerClient.from_connection_string(
    conn_str="Endpoint=sb://...",
    eventhub_name="sales-events"
)

def send_sales_event(customer_id, product_id, event_type, amount=0, channel="web"):
    """Envía eventos de ventas en tiempo real a Fabric"""

    event_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "customer_id": customer_id,
        "product_id": product_id,
        "event_type": event_type,
        "amount": float(amount),
        "channel": channel,
        "session_id": f"session_{customer_id}_{datetime.now().strftime('%Y%m%d_%H')}"
    }

    # Crear evento para Event Hub
    event = EventData(json.dumps(event_data))

    with producer:
        producer.send_batch([event])

    print(f"📡 Evento enviado: {event_type} - Customer: {customer_id}")

# Ejemplos de uso
send_sales_event("cust_123", "prod_456", "view_product", channel="mobile")
send_sales_event("cust_123", "prod_456", "add_to_cart", channel="mobile")
send_sales_event("cust_123", "prod_456", "purchase", amount=299.99, channel="mobile")
```

---

## 💡 Buenas Prácticas

!!! tip "Organización de Workspace"
    - **Separar por dominio:** Ventas, Marketing, Finanzas en workspaces diferentes
    - **Naming conventions:** Usar prefijos consistentes (dim_, fact_, raw_)
    - **Access control:** Implementar security groups por función
    - **Environment separation:** Dev, Test, Prod workspaces

!!! info "Optimización de Performance"
    - **Partitioning:** Particionar tablas grandes por fecha
    - **Indexing:** Crear índices en columnas de join frecuentes
    - **Caching:** Usar Power BI Premium caching para reports frecuentes
    - **Query optimization:** Optimizar consultas DAX y SQL

!!! success "Governance y Calidad"
    - **Data lineage:** Documentar origen y transformaciones
    - **Quality monitoring:** Implementar checks automáticos
    - **Schema evolution:** Gestionar cambios de esquema controladamente
    - **Backup strategy:** Configurar retention policies apropiadas

!!! warning "Gestión de Costos"
    - **Capacity monitoring:** Monitorear consumo de CU (Capacity Units)
    - **Auto-pause:** Configurar pausa automática en desarrollo
    - **Resource optimization:** Dimensionar clusters apropiadamente
    - **Usage tracking:** Implementar alertas de consumo

---

## 🛠️ Comandos y Utilidades

### Fabric REST API

```python
# Microsoft Fabric REST API
import requests
import json

class FabricAPI:
    def __init__(self, access_token):
        self.base_url = "https://api.fabric.microsoft.com/v1"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def list_workspaces(self):
        """Lista todos los workspaces"""
        response = requests.get(f"{self.base_url}/workspaces", headers=self.headers)
        return response.json()

    def create_lakehouse(self, workspace_id, lakehouse_name):
        """Crea nuevo lakehouse"""
        data = {
            "displayName": lakehouse_name,
            "type": "Lakehouse"
        }
        response = requests.post(
            f"{self.base_url}/workspaces/{workspace_id}/items",
            headers=self.headers,
            data=json.dumps(data)
        )
        return response.json()

    def run_notebook(self, workspace_id, notebook_id, parameters=None):
        """Ejecuta notebook con parámetros"""
        data = {"parameters": parameters or {}}
        response = requests.post(
            f"{self.base_url}/workspaces/{workspace_id}/items/{notebook_id}/jobs/instances",
            headers=self.headers,
            data=json.dumps(data)
        )
        return response.json()

# Uso del API
fabric = FabricAPI(access_token="your_token")
workspaces = fabric.list_workspaces()
print(f"📂 Workspaces disponibles: {len(workspaces['value'])}")
```

### PowerShell Cmdlets

```powershell
# Microsoft Fabric PowerShell
Install-Module -Name MicrosoftPowerBIMgmt -Force

# Conectar a Power BI Service
Connect-PowerBIServiceAccount

# Listar workspaces Fabric
Get-PowerBIWorkspace | Where-Object {$_.Type -eq "PersonalGroup"}

# Crear nuevo workspace
New-PowerBIWorkspace -Name "Sales-Analytics-Prod" -Description "Production workspace for sales analytics"

# Asignar usuarios a workspace
Add-PowerBIWorkspaceUser -Scope Organization -Id $workspaceId -AccessRight Admin -EmailAddress "admin@company.com"

# Backup de workspace
$workspace = Get-PowerBIWorkspace -Name "Sales-Analytics"
$datasets = Get-PowerBIDataset -WorkspaceId $workspace.Id
$reports = Get-PowerBIReport -WorkspaceId $workspace.Id

# Export reports
foreach ($report in $reports) {
    Export-PowerBIReport -Id $report.Id -OutFile "backup_$($report.Name).pbix" -WorkspaceId $workspace.Id
}
```

---

## 📚 Recursos y Referencias

### Documentación Oficial
- [Microsoft Fabric Documentation](https://learn.microsoft.com/en-us/fabric/)
- [OneLake Documentation](https://learn.microsoft.com/en-us/fabric/onelake/)
- [Fabric Data Engineering](https://learn.microsoft.com/en-us/fabric/data-engineering/)
- [Power BI in Fabric](https://learn.microsoft.com/en-us/fabric/power-bi/)

### Aprendizaje y Certificación
- [Microsoft Fabric Learning Path](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/)
- [DP-600: Implementing Analytics Solutions Using Microsoft Fabric](https://learn.microsoft.com/en-us/certifications/exams/dp-600)
- [Fabric Community](https://community.fabric.microsoft.com/)

### Herramientas Complementarias
- [Fabric Git Integration](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/)
- [Fabric Monitoring Hub](https://learn.microsoft.com/en-us/fabric/admin/monitoring-hub)
- [Power BI REST APIs](https://learn.microsoft.com/en-us/rest/api/power-bi/)

### Casos de Uso Empresariales
- [Retail Analytics with Fabric](https://learn.microsoft.com/en-us/fabric/industry-solutions/)
- [Financial Services on Fabric](https://learn.microsoft.com/en-us/fabric/industry-solutions/)
- [Manufacturing Analytics](https://learn.microsoft.com/en-us/fabric/industry-solutions/)

---

¿Listo para implementar tu primera solución analytics end-to-end en Microsoft Fabric? ¡Explora los casos de uso específicos y arquitecturas complementarias!