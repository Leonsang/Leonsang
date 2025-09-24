# Streaming Architecture: Procesamiento de Datos en Tiempo Real

> "Los datos en movimiento son más valiosos que los datos en reposo."

---

## 🌊 ¿Qué es Streaming de Datos?

El streaming de datos es el procesamiento continuo de flujos de datos en tiempo real, permitiendo análisis y respuestas inmediatas a eventos conforme ocurren, sin necesidad de almacenar primero los datos.

---

## 🏗️ Evolución del Procesamiento de Datos

### Batch Processing (Tradicional)
![Batch vs Stream](https://github.com/vedanthv/data-engg/assets/44313631/image-161.png)

**Características:**
- ❌ **Alta latencia:** Procesa datos en intervalos fijos
- ❌ **Limitado tiempo real:** Decisiones basadas en datos históricos
- ❌ **Complejidad:** Múltiples viajes al storage
- ✅ **Consistencia:** Garantías ACID fuertes

### Stream Processing (Moderno)
**Características:**
- ✅ **Baja latencia:** Procesamiento inmediato
- ✅ **Tiempo real:** Decisiones instantáneas
- ✅ **Escalabilidad:** Manejo de volúmenes masivos
- ✅ **Flexibilidad:** Adaptación dinámica a cambios

---

## 📊 Casos de Uso de Streaming

### Ejemplos Comunes

![Use Cases](https://github.com/vedanthv/data-engg/assets/44313631/image-167.png)

- **IoT Sensor Data:** Monitoreo ambiental, industrial
- **Financial Transactions:** Detección de fraude en tiempo real
- **Social Media Feeds:** Análisis de sentimientos, trending topics
- **Website Activity:** Personalización, recomendaciones
- **Infrastructure Events:** Monitoreo, alertas automáticas
- **Gaming Analytics:** Métricas de jugadores en vivo
- **Supply Chain:** Tracking de inventario y logística

### Arquitectura de Ejemplo: Sistema de Fraude

![Fraud Detection](https://github.com/vedanthv/data-engg/assets/44313631/image-168.png)

```
1. Transaction → 2. Kafka → 3. Stream Processor → 4. ML Model → 5. Alert/Action
```

---

## 🔧 Componentes de Arquitectura Streaming

### 1. **Message Brokers**
- **Apache Kafka:** Líder del mercado, alta performance
- **Redpanda:** Compatible con Kafka, más simple
- **Apache Pulsar:** Multi-tenancy nativo
- **Amazon Kinesis:** Managed service AWS

### 2. **Stream Processing Engines**
- **Apache Spark Streaming:** Micro-batching approach
- **Apache Flink:** True streaming, baja latencia
- **Apache Storm:** Tiempo real guaranteed processing
- **Kafka Streams:** Integrado con Kafka ecosystem

### 3. **Storage Systems**
- **Delta Lake:** ACID transactions para streaming
- **Apache Iceberg:** Open table format
- **Elasticsearch:** Search y analytics
- **InfluxDB:** Time series data

---

## 🚀 Apache Kafka: Plataforma de Streaming

### Arquitectura Core

![Kafka Architecture](https://github.com/vedanthv/data-engg/assets/44313631/image-164.png)

#### Componentes Principales
- **Broker:** Servidor que almacena y sirve mensajes
- **Topic:** Canal lógico de mensajes
- **Partition:** División física de un topic
- **Producer:** Publica mensajes a topics
- **Consumer:** Suscribe y procesa mensajes
- **Zookeeper/KRaft:** Coordinación del cluster

### Conceptos Fundamentales

#### Topics y Particiones
```bash
# Crear topic con particiones
kafka-topics --create \
  --topic user-events \
  --partitions 6 \
  --replication-factor 3 \
  --bootstrap-server localhost:9092
```

#### Producers
```python
from kafka import KafkaProducer
import json
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    key_serializer=lambda x: x.encode('utf-8') if x else None
)

# Enviar evento
evento = {
    'user_id': 'user_123',
    'action': 'login',
    'timestamp': datetime.now().isoformat(),
    'ip_address': '192.168.1.1',
    'device': 'mobile'
}

producer.send('user-events', key='user_123', value=evento)
producer.flush()
print("✅ Evento enviado a Kafka")
```

#### Consumers
```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    key_deserializer=lambda x: x.decode('utf-8') if x else None,
    group_id='analytics-group',
    auto_offset_reset='latest'
)

print("🔍 Escuchando eventos...")
for mensaje in consumer:
    evento = mensaje.value
    user_id = mensaje.key

    print(f"Usuario {user_id} realizó: {evento['action']}")

    # Procesar evento
    if evento['action'] == 'purchase':
        procesar_compra(evento)
    elif evento['action'] == 'login':
        actualizar_sesion(evento)
```

### Schema Registry

```python
from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

# Definir schema Avro
schema_str = """
{
  "type": "record",
  "name": "UserEvent",
  "fields": [
    {"name": "user_id", "type": "string"},
    {"name": "action", "type": "string"},
    {"name": "timestamp", "type": "long"},
    {"name": "properties", "type": {"type": "map", "values": "string"}}
  ]
}
"""

# Configurar Schema Registry
schema_registry_client = SchemaRegistryClient({
    'url': 'http://localhost:8081'
})

avro_serializer = AvroSerializer(
    schema_registry_client,
    schema_str
)

producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})

# Enviar con schema
evento = {
    'user_id': 'user_456',
    'action': 'view_product',
    'timestamp': int(datetime.now().timestamp() * 1000),
    'properties': {
        'product_id': 'prod_789',
        'category': 'electronics',
        'price': '299.99'
    }
}

producer.produce(
    topic='user-events-avro',
    value=avro_serializer(evento, None)
)
```

---

## 🟢 Redpanda: Kafka Simplificado

### ¿Por qué Redpanda?

![Redpanda Benefits](https://github.com/vedanthv/data-engg/assets/44313631/image-162.png)

#### Ventajas sobre Kafka
- **10x más rápido** en throughput
- **Sin Zookeeper:** Arquitectura más simple
- **C++ nativo:** Mayor eficiencia de memoria
- **API compatible:** Drop-in replacement para Kafka
- **Auto-tuning:** Configuración automática

### Setup con Docker

```yaml
# docker-compose.yml
version: '3.7'
services:
  redpanda:
    image: redpandadata/redpanda:latest
    container_name: redpanda
    command:
      - redpanda
      - start
      - --kafka-addr internal://0.0.0.0:9092,external://0.0.0.0:19092
      - --advertise-kafka-addr internal://redpanda:9092,external://localhost:19092
      - --pandaproxy-addr internal://0.0.0.0:8082,external://0.0.0.0:18082
      - --advertise-pandaproxy-addr internal://redpanda:8082,external://localhost:18082
      - --schema-registry-addr internal://0.0.0.0:8081,external://0.0.0.0:18081
      - --rpc-addr redpanda:33145
      - --advertise-rpc-addr redpanda:33145
      - --smp 1
      - --memory 1G
      - --mode dev-container
      - --default-log-level=info
    ports:
      - 18081:18081
      - 18082:18082
      - 19092:19092
      - 19644:9644
```

```bash
# Levantar Redpanda
docker-compose up -d

# Verificar cluster
rpk cluster info
```

### Ejemplo Streaming con Redpanda

```python
# Producer para Redpanda
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:19092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Simular stream de IoT sensors
def generar_datos_iot():
    while True:
        sensor_data = {
            'sensor_id': f'sensor_{random.randint(1, 100)}',
            'temperature': random.uniform(18.0, 35.0),
            'humidity': random.uniform(30.0, 80.0),
            'pressure': random.uniform(980.0, 1020.0),
            'timestamp': int(time.time() * 1000),
            'location': random.choice(['warehouse_a', 'warehouse_b', 'office'])
        }

        producer.send('iot-sensors', value=sensor_data)
        print(f"📊 Enviado: {sensor_data}")
        time.sleep(1)

# Consumer con alertas
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'iot-sensors',
    bootstrap_servers=['localhost:19092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    group_id='monitoring-group'
)

def procesar_alertas():
    print("🚨 Sistema de alertas iniciado...")
    for mensaje in consumer:
        data = mensaje.value

        # Detectar anomalías
        if data['temperature'] > 30:
            print(f"🔥 ALERTA: Temperatura alta en {data['sensor_id']}: {data['temperature']:.1f}°C")

        if data['humidity'] > 70:
            print(f"💧 ALERTA: Humedad alta en {data['sensor_id']}: {data['humidity']:.1f}%")

        # Enviar a sistema de almacenamiento
        almacenar_metricas(data)
```

---

## ⚡ Stream Processing Patterns

### 1. Windowing Operations

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("StreamWindowing") \
    .config("spark.sql.streaming.checkpointLocation", "/tmp/checkpoint") \
    .getOrCreate()

# Schema para eventos
evento_schema = StructType([
    StructField("user_id", StringType()),
    StructField("action", StringType()),
    StructField("amount", DoubleType()),
    StructField("timestamp", TimestampType())
])

# Leer stream desde Kafka
eventos_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .load() \
    .select(from_json(col("value").cast("string"), evento_schema).alias("data")) \
    .select("data.*")

# Ventana deslizante de 5 minutos
ventana_5min = eventos_stream \
    .filter(col("action") == "purchase") \
    .groupBy(
        window(col("timestamp"), "5 minutes", "1 minute"),
        col("user_id")
    ) \
    .agg(
        sum("amount").alias("total_spent"),
        count("*").alias("transaction_count")
    )

# Detección de gastos anómalos
alertas = ventana_5min \
    .filter(col("total_spent") > 1000) \
    .select(
        col("window.start").alias("window_start"),
        col("user_id"),
        col("total_spent"),
        col("transaction_count")
    )

# Output a consola
query = alertas.writeStream \
    .outputMode("append") \
    .format("console") \
    .trigger(processingTime='30 seconds') \
    .start()

query.awaitTermination()
```

### 2. Complex Event Processing

```python
# Detección de patrones complejos
from pyspark.sql.functions import lag
from pyspark.sql.window import Window

# Detectar secuencia sospechosa: login fallido → login exitoso → compra alta
eventos_ordenados = eventos_stream \
    .withWatermark("timestamp", "10 minutes") \
    .orderBy("user_id", "timestamp")

window_spec = Window.partitionBy("user_id").orderBy("timestamp")

patrones_sospechosos = eventos_ordenados \
    .withColumn("accion_anterior", lag("action").over(window_spec)) \
    .withColumn("accion_anterior_2", lag("action", 2).over(window_spec)) \
    .filter(
        (col("accion_anterior_2") == "login_failed") &
        (col("accion_anterior") == "login_success") &
        (col("action") == "purchase") &
        (col("amount") > 500)
    )

# Enviar alertas
def procesar_patron_sospechoso(batch_df, batch_id):
    if not batch_df.isEmpty():
        print(f"🚨 Batch {batch_id}: Detectados {batch_df.count()} patrones sospechosos")

        # Enviar a sistema de alertas
        batch_df.select("user_id", "timestamp", "amount") \
                .write \
                .format("jdbc") \
                .option("url", "jdbc:postgresql://localhost/alerts") \
                .option("dbtable", "fraud_alerts") \
                .mode("append") \
                .save()

query_patrones = patrones_sospechosos.writeStream \
    .foreachBatch(procesar_patron_sospechoso) \
    .start()
```

---

## 🏪 Arquitecturas de Streaming Comunes

### 1. Lambda Architecture

```
Raw Data → Batch Layer   → Batch Views  →
       ↘ Speed Layer   → Real-time Views → Serving Layer
```

**Ventajas:**
- ✅ Tolerante a fallos
- ✅ Datos completos (batch) + baja latencia (speed)

**Desventajas:**
- ❌ Complejidad dual
- ❌ Mantenimiento de dos codebases

### 2. Kappa Architecture

```
Raw Data → Stream Processing → Unified Views → Applications
```

**Ventajas:**
- ✅ Arquitectura unificada
- ✅ Menor complejidad
- ✅ Reprocessing simplificado

### Implementación Kappa con Kafka + Delta Lake

```python
# Unified streaming architecture
class KappaProcessor:
    def __init__(self, spark_session):
        self.spark = spark_session

    def process_unified_stream(self, kafka_topic, checkpoint_location):
        # Single stream processing pipeline
        raw_stream = self.spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("subscribe", kafka_topic) \
            .load()

        # Transform una sola vez
        processed_stream = self.transform_data(raw_stream)

        # Múltiples outputs del mismo stream
        self.write_to_delta_lake(processed_stream, "/delta/unified_table")
        self.write_to_analytics_store(processed_stream)
        self.trigger_real_time_alerts(processed_stream)

        return processed_stream

    def transform_data(self, raw_stream):
        return raw_stream \
            .select(from_json(col("value").cast("string"), event_schema).alias("data")) \
            .select("data.*") \
            .withColumn("processed_time", current_timestamp()) \
            .withColumn("event_date", to_date("timestamp"))

    def write_to_delta_lake(self, stream, delta_path):
        return stream.writeStream \
            .format("delta") \
            .option("checkpointLocation", f"{checkpoint_location}/delta") \
            .partitionBy("event_date") \
            .start(delta_path)
```

---

## 💡 Buenas Prácticas de Streaming

!!! tip "Diseño de Pipeline"
    - **Idempotencia:** Procesar el mismo evento múltiples veces debe dar el mismo resultado
    - **Exactly-once semantics:** Garantizar que cada evento se procesa exactamente una vez
    - **Backpressure handling:** Manejar scenarios donde producer > consumer speed
    - **Schema evolution:** Permitir cambios en estructura de datos sin downtime

!!! info "Monitoreo y Observabilidad"
    - **Lag monitoring:** Diferencia entre producer y consumer offsets
    - **Throughput metrics:** Mensajes por segundo, bytes por segundo
    - **Error rates:** Porcentaje de mensajes fallidos
    - **Processing latency:** Tiempo desde ingestion hasta processing

!!! success "Escalabilidad"
    - **Partitioning strategy:** Distribuir carga uniformemente
    - **Consumer groups:** Paralelizar processing
    - **Auto-scaling:** Ajustar recursos según demanda
    - **Resource isolation:** Separar workloads críticos

!!! warning "Gestión de Estado"
    - **Checkpointing:** Guardar estado regularmente para recovery
    - **State stores:** Usar almacenes eficientes (RocksDB)
    - **Cleanup policies:** Limpiar estado obsoleto
    - **Memory management:** Evitar memory leaks en long-running jobs

---

## 🛠️ Herramientas de Desarrollo

### Kafka Connect para Integraciones

```json
{
  "name": "postgres-source-connector",
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
    "connection.url": "jdbc:postgresql://localhost:5432/ecommerce",
    "connection.user": "kafka",
    "table.whitelist": "orders,customers,products",
    "mode": "incrementing",
    "incrementing.column.name": "id",
    "topic.prefix": "postgres-",
    "poll.interval.ms": 1000
  }
}
```

### ksqlDB para Stream Analytics

```sql
-- Crear stream desde topic
CREATE STREAM transactions (
    transaction_id VARCHAR,
    user_id VARCHAR,
    amount DOUBLE,
    merchant VARCHAR,
    timestamp BIGINT
) WITH (
    KAFKA_TOPIC='transactions',
    VALUE_FORMAT='JSON',
    TIMESTAMP='timestamp'
);

-- Detectar fraude en tiempo real
CREATE TABLE suspicious_activity AS
SELECT user_id,
       COUNT(*) as transaction_count,
       SUM(amount) as total_amount,
       WINDOWSTART as window_start
FROM transactions
WINDOW TUMBLING (SIZE 5 MINUTES)
GROUP BY user_id
HAVING COUNT(*) > 10 OR SUM(amount) > 5000;

-- Stream de alertas
CREATE STREAM fraud_alerts AS
SELECT user_id,
       'High velocity transactions detected' as alert_type,
       transaction_count,
       total_amount,
       window_start
FROM suspicious_activity;
```

### Testing de Streams

```python
import unittest
from kafka import KafkaProducer, KafkaConsumer
from testcontainers import DockerContainer

class StreamingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Levantar Kafka para testing
        cls.kafka = DockerContainer("confluentinc/cp-kafka:latest") \
            .with_env("KAFKA_ZOOKEEPER_CONNECT", "zookeeper:2181") \
            .with_env("KAFKA_ADVERTISED_LISTENERS", "PLAINTEXT://localhost:9092")

        cls.kafka.start()

    def test_event_processing(self):
        # Setup
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: json.dumps(x).encode()
        )

        consumer = KafkaConsumer(
            'test-output',
            bootstrap_servers=['localhost:9092'],
            value_deserializer=lambda x: json.loads(x.decode()),
            auto_offset_reset='earliest',
            consumer_timeout_ms=5000
        )

        # Test data
        test_event = {
            'user_id': 'test_user',
            'action': 'purchase',
            'amount': 100.0,
            'timestamp': int(time.time())
        }

        # Act
        producer.send('test-input', test_event)
        producer.flush()

        # Assert
        processed_events = []
        for message in consumer:
            processed_events.append(message.value)

        self.assertEqual(len(processed_events), 1)
        self.assertEqual(processed_events[0]['user_id'], 'test_user')

    @classmethod
    def tearDownClass(cls):
        cls.kafka.stop()
```

---

## 📚 Recursos y Referencias

### Documentación Oficial
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Redpanda Documentation](https://docs.redpanda.com/)
- [Apache Spark Streaming](https://spark.apache.org/streaming/)
- [Apache Flink Documentation](https://flink.apache.org/)

### Herramientas de Monitoreo
- [Kafka Manager (CMAK)](https://github.com/yahoo/CMAK)
- [Redpanda Console](https://redpanda.com/redpanda-console-kafka-ui)
- [Confluent Control Center](https://docs.confluent.io/platform/current/control-center/)

### Comunidad y Aprendizaje
- [Confluent Developer](https://developer.confluent.io/)
- [Kafka Tutorials](https://kafka-tutorials.confluent.io/)
- [Stream Processing with Apache Kafka](https://www.manning.com/books/kafka-streams-in-action)

---

¿Listo para implementar tu primera arquitectura streaming? ¡Explora los casos de uso específicos en las otras secciones!