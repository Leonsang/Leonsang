# Spark Internals: Arquitectura y Optimización Avanzada

> "Para optimizar Spark efectivamente, debes entender cómo funciona por dentro."

---

## ⚡ ¿Qué es Apache Spark?

Apache Spark es un motor de computación distribuida diseñado para procesamiento rápido de grandes volúmenes de datos. Su arquitectura in-memory y lazy evaluation lo hacen ideal para analytics, machine learning y stream processing.

---

## 🏗️ Arquitectura Interna de Spark

### Vista General del Sistema

![Spark Architecture](https://github.com/vedanthv/data-engg/assets/44313631/fc63ecce-41ce-477b-8964-86a4a4b86d20)

### Componentes Principales

#### 1. **Driver Program**
- **SparkContext:** Punto de entrada principal
- **DAG Scheduler:** Crea plan de ejecución
- **Task Scheduler:** Programa tareas en el cluster
- **Block Manager:** Gestiona almacenamiento y cache

#### 2. **Cluster Manager**
- **Standalone:** Manager nativo de Spark
- **YARN:** Hadoop resource manager
- **Kubernetes:** Orquestación cloud-native
- **Mesos:** Manager genérico de recursos

#### 3. **Worker Nodes**
- **Executors:** JVMs que ejecutan tareas
- **Tasks:** Unidades mínimas de trabajo
- **Cache:** Almacenamiento in-memory

---

## 🔄 Flujo de Ejecución Interno

### Proceso Completo

![Execution Flow](https://github.com/vedanthv/data-engg/assets/44313631/a0091ce1-edaf-4dce-9754-caf5238f8506)

#### Paso a Paso

1. **Application Submission**
   - Driver program inicia SparkContext
   - Solicita recursos al Cluster Manager
   - Lanza executors en worker nodes

2. **DAG Creation**
   - Transformations crean RDD graph
   - Lazy evaluation: no ejecución inmediata
   - Actions triggerer job execution

3. **Job Planning**
   - DAGScheduler divide jobs en stages
   - TaskScheduler asigna tasks a executors
   - Considera data locality

4. **Task Execution**
   - Executors reciben serialized tasks
   - Procesan particiones en paralelo
   - Devuelven resultados al driver

### Ejemplo de Flujo Interno

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# 1. Crear SparkSession (Driver)
spark = SparkSession.builder \
    .appName("Spark Internals Demo") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .getOrCreate()

# 2. Cargar datos (Lazy - no ejecuta todavía)
df_sales = spark.read.parquet("s3://data/sales/")
df_products = spark.read.parquet("s3://data/products/")

print(f"🔍 Particiones sales: {df_sales.rdd.getNumPartitions()}")
print(f"🔍 Particiones products: {df_products.rdd.getNumPartitions()}")

# 3. Transformaciones (Lazy evaluation)
df_enriched = df_sales \
    .join(df_products, "product_id") \
    .withColumn("revenue", col("quantity") * col("price")) \
    .filter(col("revenue") > 100) \
    .groupBy("category", "month") \
    .agg(
        sum("revenue").alias("total_revenue"),
        count("transaction_id").alias("transaction_count"),
        avg("revenue").alias("avg_revenue")
    )

# 4. Action - Aquí empieza la ejecución real
print("🚀 Iniciando ejecución...")
df_enriched.explain(True)  # Ver plan de ejecución

# 5. Recopilar resultados
results = df_enriched.collect()  # Action - triggers job execution
print(f"✅ Resultados: {len(results)} filas procesadas")
```

---

## 🧠 Arquitectura de Worker Node

### Configuración Interna

![Worker Architecture](https://github.com/vedanthv/data-engg/assets/44313631/ea6e5e52-7b70-4550-8fef-8858691bbbd2)

#### Distribución de Recursos

```python
# Configuración óptima para worker de 16 cores, 64GB RAM
spark_config = {
    # Executor configuration
    "spark.executor.instances": "4",           # 4 executors por nodo
    "spark.executor.cores": "4",               # 4 cores por executor
    "spark.executor.memory": "12g",            # 12GB por executor
    "spark.executor.memoryFraction": "0.8",    # 80% para processing

    # Driver configuration
    "spark.driver.memory": "8g",
    "spark.driver.cores": "2",

    # Performance tuning
    "spark.sql.adaptive.enabled": "true",
    "spark.sql.adaptive.coalescePartitions.enabled": "true",
    "spark.sql.adaptive.skewJoin.enabled": "true",

    # Serialization
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",

    # Network
    "spark.sql.broadcastTimeout": "36000",
    "spark.network.timeout": "800s"
}

# Aplicar configuración
for key, value in spark_config.items():
    spark.conf.set(key, value)

print("⚙️  Configuración Spark optimizada aplicada")

# Verificar configuración
print(f"Executors: {spark.conf.get('spark.executor.instances')}")
print(f"Cores por executor: {spark.conf.get('spark.executor.cores')}")
print(f"Memoria por executor: {spark.conf.get('spark.executor.memory')}")
```

#### Gestión de Memoria

```python
# Análisis de uso de memoria
def analizar_uso_memoria(spark_session):
    """Analiza el uso actual de memoria en Spark"""

    sc = spark_session.sparkContext

    # Status de executors
    executor_infos = sc.statusTracker().getExecutorInfos()

    print("📊 ANÁLISIS DE MEMORIA SPARK")
    print("=" * 50)

    total_cores = 0
    total_memory = 0

    for executor in executor_infos:
        print(f"Executor {executor.executorId}:")
        print(f"  - Host: {executor.host}")
        print(f"  - Cores activos: {executor.totalCores}")
        print(f"  - Memoria máxima: {executor.maxMemory / 1024**3:.1f} GB")
        print(f"  - Memoria usada: {executor.memoryUsed / 1024**3:.1f} GB")
        print(f"  - Almacenamiento: {executor.diskUsed / 1024**3:.1f} GB")
        print()

        total_cores += executor.totalCores
        total_memory += executor.maxMemory

    print(f"TOTAL CLUSTER:")
    print(f"  - Cores disponibles: {total_cores}")
    print(f"  - Memoria total: {total_memory / 1024**3:.1f} GB")

    return {
        'total_cores': total_cores,
        'total_memory_gb': total_memory / 1024**3,
        'executors': len(executor_infos)
    }

# Usar la función
stats = analizar_uso_memoria(spark)
```

---

## 📊 RDDs vs DataFrames vs Datasets

### Evolución de APIs

![API Evolution](https://github.com/vedanthv/data-engg/assets/44313631/93110364-1dc5-443c-b6ad-9d89edcf7b46)

### Comparación Práctica

```python
import time
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Datos de prueba
data = [(i, f"name_{i}", i * 100) for i in range(1000000)]
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("value", IntegerType(), True)
])

print("🔬 COMPARACIÓN DE RENDIMIENTO")
print("=" * 40)

# 1. RDD - Nivel más bajo
def test_rdd_performance():
    start_time = time.time()

    rdd = spark.sparkContext.parallelize(data)
    result = rdd.filter(lambda x: x[2] > 50000) \
               .map(lambda x: (x[1], x[2])) \
               .collect()

    end_time = time.time()
    return len(result), end_time - start_time

# 2. DataFrame - Catalyst optimizer
def test_dataframe_performance():
    start_time = time.time()

    df = spark.createDataFrame(data, schema)
    result = df.filter(col("value") > 50000) \
              .select("name", "value") \
              .collect()

    end_time = time.time()
    return len(result), end_time - start_time

# 3. SQL - Máxima optimización
def test_sql_performance():
    start_time = time.time()

    df = spark.createDataFrame(data, schema)
    df.createOrReplaceTempView("test_data")

    result = spark.sql("""
        SELECT name, value
        FROM test_data
        WHERE value > 50000
    """).collect()

    end_time = time.time()
    return len(result), end_time - start_time

# Ejecutar pruebas
rdd_count, rdd_time = test_rdd_performance()
df_count, df_time = test_dataframe_performance()
sql_count, sql_time = test_sql_performance()

print(f"RDD:       {rdd_count:,} filas en {rdd_time:.3f}s")
print(f"DataFrame: {df_count:,} filas en {df_time:.3f}s")
print(f"SQL:       {sql_count:,} filas en {sql_time:.3f}s")
print()
print(f"DataFrame vs RDD: {rdd_time/df_time:.1f}x más rápido")
print(f"SQL vs RDD:       {rdd_time/sql_time:.1f}x más rápido")
```

---

## 🚀 Catalyst Optimizer

### Motor de Optimización

![Catalyst Optimizer](https://github.com/vedanthv/data-engg/assets/44313631/de3e02ff-2580-433f-8183-935ac4b2feda)

### Fases de Optimización

1. **Análisis Lógico:** Resuelve referencias y tipos
2. **Optimización Lógica:** Aplica reglas de optimización
3. **Planificación Física:** Selecciona algoritmos de ejecución
4. **Generación de Código:** Compila a bytecode Java

### Ejemplo de Optimización

```python
from pyspark.sql.functions import *

# Crear datos de prueba
df_large = spark.range(10000000).withColumn("value", col("id") % 1000)
df_small = spark.range(1000).withColumn("lookup", col("id"))

print("🔍 ANÁLISIS DEL PLAN DE EJECUCIÓN")
print("=" * 50)

# Query compleja para optimizar
query = df_large.filter(col("value") < 100) \
                .join(df_small, df_large.value == df_small.lookup) \
                .groupBy("lookup") \
                .agg(count("id").alias("count"),
                     sum("id").alias("sum")) \
                .filter(col("count") > 1000)

# Ver diferentes niveles de plan
print("📋 PLAN LÓGICO:")
query.explain(False)
print()

print("🛠️  PLAN FÍSICO OPTIMIZADO:")
query.explain(True)
print()

# Análisis de query execution
print("📊 ESTADÍSTICAS DE EJECUCIÓN:")
query.cache()  # Cache para análisis
result = query.collect()

print(f"Resultados: {len(result)} filas")
```

### Optimizaciones Manuales

```python
# Técnicas avanzadas de optimización
class SparkOptimizer:
    def __init__(self, spark_session):
        self.spark = spark_session

    def optimize_join_order(self, large_df, small_df, join_key):
        """Optimiza orden de joins basado en tamaño"""

        # Broadcast join para tablas pequeñas
        if small_df.count() < 10000:
            print("🔄 Aplicando Broadcast Join")
            optimized = large_df.join(
                broadcast(small_df),
                join_key
            )
        else:
            print("🔄 Usando Sort-Merge Join")
            optimized = large_df.join(small_df, join_key)

        return optimized

    def optimize_partitioning(self, df, partition_col, target_partitions=200):
        """Optimiza particionado para mejor distribución"""

        current_partitions = df.rdd.getNumPartitions()

        if current_partitions != target_partitions:
            print(f"📦 Reparticionando: {current_partitions} → {target_partitions}")

            # Repartition by column para joins eficientes
            optimized = df.repartition(target_partitions, partition_col)
        else:
            optimized = df

        return optimized

    def optimize_caching_strategy(self, df, storage_level="MEMORY_AND_DISK"):
        """Aplica estrategia de caching inteligente"""

        # Determinar si vale la pena cachear
        row_count = df.count()

        if row_count > 1000000:  # Solo cachear datasets grandes
            print(f"💾 Cacheando {row_count:,} filas con {storage_level}")

            from pyspark import StorageLevel
            level_map = {
                "MEMORY_ONLY": StorageLevel.MEMORY_ONLY,
                "MEMORY_AND_DISK": StorageLevel.MEMORY_AND_DISK,
                "DISK_ONLY": StorageLevel.DISK_ONLY
            }

            df.persist(level_map[storage_level])
            df.count()  # Materializar cache

        return df

# Uso del optimizador
optimizer = SparkOptimizer(spark)

# Ejemplo práctico
df_sales = spark.table("sales_data")
df_products = spark.table("products")

# Optimizar pipeline completo
df_optimized = optimizer.optimize_partitioning(
    df_sales, "customer_id", 400
)

df_joined = optimizer.optimize_join_order(
    df_optimized, df_products, "product_id"
)

df_cached = optimizer.optimize_caching_strategy(
    df_joined, "MEMORY_AND_DISK"
)
```

---

## 📊 Stages y Tasks

### División del Trabajo

![Stages and Tasks](https://github.com/vedanthv/data-engg/assets/44313631/0c913da4-73d2-4bf2-b844-05a6a38b2797)

### Conceptos Clave

- **Job:** Acción que triggerea ejecución
- **Stage:** Grupo de tasks que pueden ejecutar en paralelo
- **Task:** Unidad mínima de trabajo en una partición
- **Shuffle:** Intercambio de datos entre stages

### Análisis de Performance

```python
def analizar_spark_jobs(spark_session):
    """Analiza jobs y stages ejecutados"""

    sc = spark_session.sparkContext
    status_tracker = sc.statusTracker()

    print("🎯 ANÁLISIS DE JOBS SPARK")
    print("=" * 40)

    # Jobs activos
    active_jobs = status_tracker.getActiveJobIds()
    print(f"Jobs activos: {len(active_jobs)}")

    # Información de stages
    active_stages = status_tracker.getActiveStageIds()

    for stage_id in active_stages:
        stage_info = status_tracker.getStageInfo(stage_id)
        if stage_info:
            print(f"\nStage {stage_id}:")
            print(f"  - Tasks totales: {stage_info.numTasks}")
            print(f"  - Tasks activas: {stage_info.numActiveTasks}")
            print(f"  - Tasks completadas: {stage_info.numCompletedTasks}")
            print(f"  - Tasks fallidas: {stage_info.numFailedTasks}")

    # Executor status
    print(f"\n📊 EXECUTORS:")
    for executor in status_tracker.getExecutorInfos():
        print(f"Executor {executor.executorId}: {executor.totalCores} cores")

# Simulación con análisis detallado
def demo_stages_analysis():
    """Demuestra cómo analizar stages en una operación compleja"""

    # Crear dataset grande para múltiples stages
    df = spark.range(5000000).withColumn("value", col("id") % 10000)

    print("🔍 Iniciando operación compleja...")

    # Operación que genera múltiples stages
    result = df.filter(col("value") < 5000) \
               .groupBy("value") \
               .count() \
               .filter(col("count") > 100) \
               .orderBy(col("count").desc()) \
               .limit(100)

    # Ver plan antes de ejecutar
    print("\n📋 PLAN DE EJECUCIÓN:")
    result.explain()

    # Ejecutar con timing
    start_time = time.time()
    final_result = result.collect()
    end_time = time.time()

    print(f"\n✅ Completado en {end_time - start_time:.2f} segundos")
    print(f"Registros resultado: {len(final_result)}")

    # Analizar jobs después
    analizar_spark_jobs(spark)

# Ejecutar demo
demo_stages_analysis()
```

---

## 🚀 Optimizaciones Avanzadas

### 1. Adaptive Query Execution (AQE)

```python
# Habilitar AQE para optimización dinámica
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.adaptive.localShuffleReader.enabled", "true")

# Configurar thresholds
spark.conf.set("spark.sql.adaptive.advisoryPartitionSizeInBytes", "128MB")
spark.conf.set("spark.sql.adaptive.coalescePartitions.minPartitionNum", "10")

print("🔧 Adaptive Query Execution habilitado")

# Demostrar beneficios de AQE
def demo_aqe_benefits():
    """Demuestra beneficios de Adaptive Query Execution"""

    # Dataset con particiones desbalanceadas
    df_skewed = spark.range(1000000) \
                    .withColumn("partition_key",
                              when(col("id") < 900000, lit(1))
                              .when(col("id") < 990000, lit(2))
                              .otherwise(col("id") % 100 + 3))

    # Join que genera skew
    df_small = spark.range(100).withColumn("lookup_key", col("id") + 1)

    joined = df_skewed.join(df_small,
                           df_skewed.partition_key == df_small.lookup_key)

    print("⚡ Ejecutando join con AQE...")
    start_time = time.time()
    result_count = joined.count()
    end_time = time.time()

    print(f"AQE Result: {result_count:,} filas en {end_time - start_time:.2f}s")

    # Mostrar plan adaptado
    print("\n📊 PLAN ADAPTADO:")
    joined.explain()

demo_aqe_benefits()
```

### 2. Dynamic Partition Pruning

```python
# Optimización para queries con filtros en joins
def demo_partition_pruning():
    """Demuestra Dynamic Partition Pruning"""

    # Crear tabla particionada por fecha
    from datetime import datetime, timedelta
    import random

    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d')
             for x in range(30)]

    # Dataset grande particionado
    large_data = []
    for date in dates:
        for i in range(100000):
            large_data.append((i, date, random.randint(1, 1000)))

    df_large = spark.createDataFrame(
        large_data,
        ["id", "date", "value"]
    ).repartition(col("date"))

    # Tabla de filtros pequeña
    filter_dates = [dates[0], dates[1], dates[2]]  # Solo 3 fechas
    df_filter = spark.createDataFrame(
        [(date,) for date in filter_dates],
        ["filter_date"]
    )

    # Join que activa partition pruning
    pruned_query = df_large.join(
        df_filter,
        df_large.date == df_filter.filter_date
    ).groupBy("date").count()

    print("🌟 Ejecutando con Dynamic Partition Pruning...")
    pruned_query.explain()

    result = pruned_query.collect()
    print(f"Particiones procesadas: {len(result)}")

demo_partition_pruning()
```

### 3. Bucketing para Joins Eficientes

```python
# Precomputar bucketing para joins frecuentes
def setup_bucketed_tables():
    """Configura tablas con bucketing para joins optimizados"""

    # Crear datos de ejemplo
    sales_data = [(i, i % 1000, f"product_{i % 100}", 100 + (i % 50))
                  for i in range(1000000)]

    customer_data = [(i, f"customer_{i}", f"city_{i % 100}")
                     for i in range(1000)]

    df_sales = spark.createDataFrame(
        sales_data,
        ["sale_id", "customer_id", "product", "amount"]
    )

    df_customers = spark.createDataFrame(
        customer_data,
        ["customer_id", "name", "city"]
    )

    print("📦 Creando tablas con bucketing...")

    # Escribir con bucketing en customer_id
    df_sales.write \
            .mode("overwrite") \
            .option("path", "/tmp/bucketed_sales") \
            .bucketBy(10, "customer_id") \
            .saveAsTable("bucketed_sales")

    df_customers.write \
               .mode("overwrite") \
               .option("path", "/tmp/bucketed_customers") \
               .bucketBy(10, "customer_id") \
               .saveAsTable("bucketed_customers")

    print("✅ Tablas bucketed creadas")

    # Join optimizado sin shuffle
    bucketed_join = spark.table("bucketed_sales") \
                         .join(spark.table("bucketed_customers"), "customer_id")

    print("\n🔍 PLAN DE JOIN BUCKETED:")
    bucketed_join.explain()

    return bucketed_join

# Comparar con join normal
def compare_join_strategies():
    """Compara diferentes estrategias de join"""

    print("⚔️  COMPARACIÓN DE ESTRATEGIAS DE JOIN")
    print("=" * 50)

    # Setup datos
    df_sales = spark.table("bucketed_sales")
    df_customers = spark.table("bucketed_customers")

    # 1. Broadcast join
    start_time = time.time()
    broadcast_result = df_sales.join(
        broadcast(df_customers),
        "customer_id"
    ).count()
    broadcast_time = time.time() - start_time

    # 2. Sort-merge join normal
    start_time = time.time()
    sortmerge_result = df_sales.join(df_customers, "customer_id").count()
    sortmerge_time = time.time() - start_time

    print(f"Broadcast Join:   {broadcast_result:,} filas en {broadcast_time:.2f}s")
    print(f"Sort-Merge Join:  {sortmerge_result:,} filas en {sortmerge_time:.2f}s")

    return {
        'broadcast': broadcast_time,
        'sortmerge': sortmerge_time
    }

# setup_bucketed_tables()
# times = compare_join_strategies()
```

---

## 🔧 Tuning y Monitoring

### Spark UI Analysis

```python
def generar_spark_ui_report():
    """Genera reporte basado en métricas de Spark UI"""

    sc = spark.sparkContext

    print("📊 REPORTE SPARK UI")
    print("=" * 30)

    # Application info
    app_id = sc.applicationId
    app_name = sc.appName

    print(f"Application: {app_name}")
    print(f"ID: {app_id}")
    print(f"UI: http://localhost:4040")
    print()

    # Executor metrics
    status_tracker = sc.statusTracker()
    executors = status_tracker.getExecutorInfos()

    total_cores = sum(e.totalCores for e in executors)
    total_memory = sum(e.maxMemory for e in executors)
    total_storage = sum(e.diskUsed for e in executors)

    print("🖥️  RECURSOS:")
    print(f"  Executors: {len(executors)}")
    print(f"  Total Cores: {total_cores}")
    print(f"  Total Memory: {total_memory / 1024**3:.1f} GB")
    print(f"  Storage Used: {total_storage / 1024**3:.1f} GB")
    print()

    # Stage metrics
    completed_stages = status_tracker.getStageIds()

    if completed_stages:
        print("📈 STAGES RECIENTES:")
        for stage_id in completed_stages[-5:]:  # Últimos 5 stages
            stage_info = status_tracker.getStageInfo(stage_id)
            if stage_info:
                print(f"  Stage {stage_id}: {stage_info.numCompletedTasks}/{stage_info.numTasks} tasks")

    return {
        'app_id': app_id,
        'total_cores': total_cores,
        'total_memory_gb': total_memory / 1024**3,
        'executors': len(executors)
    }

# Custom metrics tracking
class SparkMetricsTracker:
    def __init__(self, spark_session):
        self.spark = spark_session
        self.metrics_history = []

    def track_operation(self, operation_name, operation_func):
        """Trackea métricas de una operación específica"""

        print(f"📊 Tracking: {operation_name}")

        # Pre-execution metrics
        sc = self.spark.sparkContext
        pre_metrics = self._get_current_metrics()

        # Execute operation
        start_time = time.time()
        result = operation_func()
        end_time = time.time()

        # Post-execution metrics
        post_metrics = self._get_current_metrics()

        # Calculate deltas
        operation_metrics = {
            'name': operation_name,
            'duration': end_time - start_time,
            'memory_used': post_metrics['memory_used'] - pre_metrics['memory_used'],
            'disk_used': post_metrics['disk_used'] - pre_metrics['disk_used'],
            'result_size': len(result) if hasattr(result, '__len__') else 1
        }

        self.metrics_history.append(operation_metrics)

        print(f"✅ {operation_name}: {operation_metrics['duration']:.2f}s")
        print(f"   Memory delta: {operation_metrics['memory_used'] / 1024**2:.1f} MB")

        return result

    def _get_current_metrics(self):
        """Obtiene métricas actuales del cluster"""
        sc = self.spark.sparkContext
        executors = sc.statusTracker().getExecutorInfos()

        return {
            'memory_used': sum(e.memoryUsed for e in executors),
            'disk_used': sum(e.diskUsed for e in executors)
        }

    def generate_report(self):
        """Genera reporte de todas las operaciones trackeadas"""
        if not self.metrics_history:
            print("No hay métricas para reportar")
            return

        print("\n📈 REPORTE DE PERFORMANCE")
        print("=" * 50)

        for metric in self.metrics_history:
            print(f"{metric['name']}: {metric['duration']:.2f}s")

        # Top operations by duration
        sorted_ops = sorted(self.metrics_history,
                          key=lambda x: x['duration'], reverse=True)

        print("\n🏆 TOP OPERACIONES MÁS LENTAS:")
        for i, op in enumerate(sorted_ops[:3], 1):
            print(f"{i}. {op['name']}: {op['duration']:.2f}s")

# Uso del tracker
tracker = SparkMetricsTracker(spark)

# Ejemplo de tracking
def heavy_operation():
    df = spark.range(1000000)
    return df.groupBy(col("id") % 100).count().collect()

def light_operation():
    return spark.range(1000).collect()

# Trackear operaciones
# tracker.track_operation("Heavy Group By", heavy_operation)
# tracker.track_operation("Light Collection", light_operation)
# tracker.generate_report()
```

---

## 💡 Buenas Prácticas de Optimización

!!! tip "Configuración de Cluster"
    - **Sizing adecuado:** 2-5 cores por executor, evitar executors muy grandes
    - **Memoria balanceada:** 70% processing, 30% storage
    - **Serialización:** Usar KryoSerializer para mejor performance
    - **Network tuning:** Ajustar timeouts para clusters grandes

!!! info "Optimización de Queries"
    - **Predicate pushdown:** Filtros lo más temprano posible
    - **Column pruning:** Seleccionar solo columnas necesarias
    - **Partitioning strategy:** Particionar por columnas de filtro frecuente
    - **Join optimization:** Broadcast para tablas pequeñas (<1GB)

!!! success "Gestión de Datos"
    - **File formats:** Usar Parquet/Delta para mejor compresión y performance
    - **Compression:** SNAPPY para balance velocidad/tamaño
    - **Bucketing:** Para joins frecuentes en mismas columnas
    - **Caching strategy:** Cache datasets que se reusan múltiples veces

!!! warning "Evitar Anti-patterns"
    - **collect() en datasets grandes:** Puede causar OOM en driver
    - **count() repetido:** Es operación costosa, almacenar resultado
    - **UDFs innecesarios:** Usar funciones nativas cuando sea posible
    - **Skewed joins:** Identificar y mitigar data skewness

---

## 🛠️ Herramientas de Diagnóstico

### Spark History Server

```python
# Configurar History Server para análisis post-ejecución
history_config = {
    "spark.eventLog.enabled": "true",
    "spark.eventLog.dir": "hdfs://namenode/spark-logs",
    "spark.history.fs.logDirectory": "hdfs://namenode/spark-logs",
    "spark.history.ui.port": "18080"
}

# Aplicar configuración
for key, value in history_config.items():
    spark.conf.set(key, value)

print("📚 History Server configurado")
print("   Acceso: http://localhost:18080")
```

### Custom Listeners

```python
from pyspark import TaskContext

class CustomSparkListener:
    """Listener personalizado para métricas detalladas"""

    def __init__(self):
        self.task_metrics = []
        self.stage_metrics = []

    def track_task_metrics(self):
        """Trackea métricas a nivel de task"""
        tc = TaskContext.get()
        if tc:
            metrics = {
                'task_id': tc.taskAttemptId(),
                'partition_id': tc.partitionId(),
                'stage_id': tc.stageId(),
                'memory_usage': tc.taskMemoryManager().currentMemoryUsage() if tc.taskMemoryManager() else 0
            }
            self.task_metrics.append(metrics)
            return metrics
        return None

# Usar en UDF o transformaciones
listener = CustomSparkListener()

def monitored_udf(value):
    """UDF que trackea métricas"""
    metrics = listener.track_task_metrics()
    # Process value
    return value * 2

# Registrar UDF
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

monitored_udf_spark = udf(monitored_udf, IntegerType())
```

---

## 📚 Recursos de Profundización

### Documentación Técnica
- [Spark Architecture Overview](https://spark.apache.org/docs/latest/cluster-overview.html)
- [Spark SQL Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
- [Spark Configuration Guide](https://spark.apache.org/docs/latest/configuration.html)

### Herramientas de Análisis
- [Spark UI Guide](https://spark.apache.org/docs/latest/web-ui.html)
- [Dr. Elephant](https://github.com/linkedin/dr-elephant) - LinkedIn's performance analyzer
- [Sparklens](https://github.com/qubole/sparklens) - Spark performance analytics

### Libros y Cursos
- "Spark: The Definitive Guide" - Bill Chambers & Matei Zaharia
- "High Performance Spark" - Holden Karau & Rachel Warren
- [Databricks Academy](https://academy.databricks.com/) - Cursos oficiales

### Comunidad
- [Spark User Mailing List](https://spark.apache.org/community.html)
- [Stack Overflow Spark](https://stackoverflow.com/questions/tagged/apache-spark)
- [Spark Summits](https://databricks.com/sparkaisummit) - Conferencias anuales

---

¿Listo para optimizar tus workloads Spark como un experto? ¡Combina este conocimiento con las arquitecturas de Databricks y streaming para máximo impacto!