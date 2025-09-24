# Google Cloud Dataflow: Streaming y Batch Processing

> "Dataflow es el servicio completamente administrado de Google para ejecutar pipelines de Apache Beam a escala."

---

## 🌊 ¿Qué es Cloud Dataflow?

Cloud Dataflow es una plataforma de procesamiento de datos unificada que permite crear pipelines tanto para procesamiento en lote (batch) como en tiempo real (streaming) utilizando Apache Beam.

---

## 🏗️ Arquitectura y Conceptos

### Unified Programming Model

```python
# Pipeline que funciona tanto para batch como streaming
import apache_beam as beam
from apache_beam.transforms import window

def create_pipeline(pipeline_options):
    with beam.Pipeline(options=pipeline_options) as pipeline:
        events = (pipeline
                 | 'Read Events' >> beam.io.ReadFromPubSub(topic=input_topic)
                 | 'Parse JSON' >> beam.Map(json.loads)
                 | 'Extract User Events' >> beam.Map(extract_user_data)
                 | 'Window into Fixed Windows' >> beam.WindowInto(
                     window.FixedWindows(60))  # 1-minute windows
                 | 'Count by User' >> beam.CombinePerKey(sum)
                 | 'Format Output' >> beam.Map(format_result)
                 | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                     table=output_table,
                     schema=output_schema))
```

### Componentes Clave

- **Apache Beam SDK**: Modelo de programación unificado
- **Dataflow Runner**: Motor de ejecución en Google Cloud
- **Auto-scaling**: Escalamiento automático de workers
- **Shuffle Service**: Servicio administrado para operaciones shuffle

---

## 🚀 Casos de Uso Streaming

### 1. Real-time Analytics Dashboard

```python
import apache_beam as beam
from apache_beam.transforms import window
from apache_beam.options.pipeline_options import PipelineOptions

class CalculateMetrics(beam.DoFn):
    def process(self, element, window=beam.DoFn.WindowParam):
        timestamp = window.end.to_utc_datetime()

        yield {
            'timestamp': timestamp.isoformat(),
            'metric_name': 'page_views',
            'value': element[1],
            'dimensions': {
                'page': element[0]['page'],
                'country': element[0]['country']
            }
        }

def run_streaming_pipeline():
    options = PipelineOptions([
        '--project=my-gcp-project',
        '--runner=DataflowRunner',
        '--streaming=true',
        '--region=us-central1'
    ])

    with beam.Pipeline(options=options) as pipeline:
        (pipeline
         | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(
             subscription='projects/my-project/subscriptions/web-events')
         | 'Parse JSON' >> beam.Map(json.loads)
         | 'Add Timestamp' >> beam.Map(
             lambda x: beam.window.TimestampedValue(x, x['timestamp']))
         | 'Window into 1min' >> beam.WindowInto(
             window.FixedWindows(60),
             allowed_lateness=30)
         | 'Group by Page+Country' >> beam.GroupBy(
             lambda x: (x['page'], x['country']))
         | 'Count Events' >> beam.CombineGlobally(
             beam.combiners.CountCombineFn()).without_defaults()
         | 'Calculate Metrics' >> beam.ParDo(CalculateMetrics())
         | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
             table='analytics.real_time_metrics',
             schema={
                 'fields': [
                     {'name': 'timestamp', 'type': 'TIMESTAMP'},
                     {'name': 'metric_name', 'type': 'STRING'},
                     {'name': 'value', 'type': 'INTEGER'},
                     {'name': 'dimensions', 'type': 'RECORD', 'mode': 'REPEATED'}
                 ]
             },
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))
```

### 2. Stream Processing con Side Inputs

```python
class EnrichWithUserData(beam.DoFn):
    def process(self, element, user_data):
        user_id = element['user_id']
        user_info = user_data.get(user_id, {})

        enriched = {
            **element,
            'user_segment': user_info.get('segment', 'unknown'),
            'user_country': user_info.get('country', 'unknown'),
            'user_registration_date': user_info.get('registration_date')
        }

        yield enriched

def create_streaming_pipeline_with_side_inputs():
    # Main pipeline
    main_stream = (pipeline
                  | 'Read Main Stream' >> beam.io.ReadFromPubSub(
                      topic='projects/my-project/topics/user-events'))

    # Side input - user data from BigQuery
    user_data = (pipeline
                | 'Read User Data' >> beam.io.ReadFromBigQuery(
                    query="SELECT user_id, segment, country, registration_date FROM users.profiles")
                | 'Create User Dict' >> beam.Map(
                    lambda row: (row['user_id'], row))
                | 'Convert to Dict' >> beam.combiners.ToDict())

    # Enrich stream with side input
    enriched_stream = (main_stream
                      | 'Parse Events' >> beam.Map(json.loads)
                      | 'Enrich with User Data' >> beam.ParDo(
                          EnrichWithUserData(),
                          user_data=beam.pvalue.AsDict(user_data)))
```

---

## 📊 Casos de Uso Batch Processing

### 1. ETL Masivo desde Cloud Storage

```python
class TransformRecord(beam.DoFn):
    def process(self, element):
        # Parse CSV row
        fields = element.split(',')

        if len(fields) < 5:
            return  # Skip invalid records

        try:
            yield {
                'transaction_id': fields[0],
                'customer_id': int(fields[1]),
                'product_id': fields[2],
                'amount': float(fields[3]),
                'transaction_date': fields[4],
                'processed_timestamp': datetime.utcnow().isoformat()
            }
        except (ValueError, IndexError):
            # Log error and continue
            logging.error(f"Failed to parse record: {element}")

def run_batch_etl():
    options = PipelineOptions([
        '--project=my-gcp-project',
        '--runner=DataflowRunner',
        '--region=us-central1',
        '--temp_location=gs://my-temp-bucket/temp'
    ])

    with beam.Pipeline(options=options) as pipeline:
        (pipeline
         | 'Read CSV Files' >> beam.io.ReadFromText(
             'gs://my-data-bucket/transactions/*.csv',
             skip_header_lines=1)
         | 'Transform Records' >> beam.ParDo(TransformRecord())
         | 'Validate Data' >> beam.Filter(validate_record)
         | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
             table='warehouse.transactions',
             schema=transaction_schema,
             write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE))
```

### 2. Procesamiento con Ventanas Complejas

```python
from apache_beam.transforms import window

def advanced_windowing_pipeline():
    with beam.Pipeline(options=pipeline_options) as pipeline:
        events = (pipeline
                 | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(
                     topic='projects/my-project/topics/sensor-data')
                 | 'Parse JSON' >> beam.Map(json.loads)
                 | 'Add Event Time' >> beam.Map(
                     lambda x: beam.window.TimestampedValue(
                         x, x['event_timestamp'])))

        # Ventana fija de 5 minutos
        fixed_window_metrics = (events
                               | 'Fixed Window 5min' >> beam.WindowInto(
                                   window.FixedWindows(5 * 60))
                               | 'Group by Sensor' >> beam.GroupBy('sensor_id')
                               | 'Calculate Avg' >> beam.CombinePerKey(
                                   beam.combiners.MeanCombineFn()))

        # Ventana deslizante de 10 minutos cada 2 minutos
        sliding_window_metrics = (events
                                 | 'Sliding Window' >> beam.WindowInto(
                                     window.SlidingWindows(10 * 60, 2 * 60))
                                 | 'Count per Window' >> beam.combiners.Count.PerElement())

        # Ventana por sesión (gap de 30 segundos)
        session_metrics = (events
                          | 'Session Window' >> beam.WindowInto(
                              window.Sessions(30))
                          | 'Session Analysis' >> beam.ParDo(AnalyzeSession()))
```

---

## ⚙️ Optimización y Tuning

### Worker Configuration

```python
# Opciones optimizadas para diferentes workloads
def get_pipeline_options(workload_type):
    base_options = [
        '--project=my-gcp-project',
        '--runner=DataflowRunner',
        '--region=us-central1'
    ]

    if workload_type == 'memory_intensive':
        return PipelineOptions(base_options + [
            '--machine_type=n1-highmem-4',
            '--max_num_workers=20',
            '--disk_size_gb=100'
        ])

    elif workload_type == 'cpu_intensive':
        return PipelineOptions(base_options + [
            '--machine_type=n1-highcpu-16',
            '--max_num_workers=50',
            '--num_workers=10'
        ])

    elif workload_type == 'streaming':
        return PipelineOptions(base_options + [
            '--streaming=true',
            '--enable_streaming_engine=true',
            '--max_num_workers=10',
            '--autoscaling_algorithm=THROUGHPUT_BASED'
        ])
```

### Custom Metrics y Monitoring

```python
class CustomMetricsDoFn(beam.DoFn):
    def __init__(self):
        self.error_counter = Metrics.counter('pipeline', 'processing_errors')
        self.success_counter = Metrics.counter('pipeline', 'successful_records')
        self.processing_time = Metrics.distribution('pipeline', 'processing_time_ms')

    def process(self, element):
        start_time = time.time()

        try:
            # Process element
            result = self.transform_element(element)
            self.success_counter.inc()

            processing_time_ms = (time.time() - start_time) * 1000
            self.processing_time.update(processing_time_ms)

            yield result

        except Exception as e:
            self.error_counter.inc()
            logging.error(f"Processing error: {e}")
```

---

## 💰 Optimización de Costos

### Estrategias de Ahorro

```python
# Usar preemptible workers para workloads tolerantes a fallos
cost_optimized_options = PipelineOptions([
    '--use_preemptible_workers=true',
    '--preemptible_worker_percentage=80',
    '--enable_streaming_engine=true',  # Reduce worker overhead
    '--max_num_workers=5',  # Limitar scaling
    '--autoscaling_algorithm=BASIC'
])

# Configurar shutdown automático
def create_pipeline_with_shutdown():
    options = PipelineOptions([
        '--save_main_session=true',
        '--setup_file=./setup.py',
        '--experiments=use_beam_bq_sink'
    ])
```

### Monitoring de Costos

```python
from google.cloud import monitoring_v3

def monitor_dataflow_costs():
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{PROJECT_ID}"

    # Query para obtener métricas de costo
    interval = monitoring_v3.TimeInterval({
        "end_time": {"seconds": int(time.time())},
        "start_time": {"seconds": int(time.time() - 3600)}  # Last hour
    })

    results = client.list_time_series(
        request={
            "name": project_name,
            "filter": 'resource.type="dataflow_job"',
            "interval": interval,
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
        }
    )

    for result in results:
        print(f"Job: {result.resource.labels['job_name']}")
        print(f"Cost: ${result.points[0].value.double_value}")
```

---

## 📚 Mejores Prácticas

!!! tip "Performance"
    - Usa Streaming Engine para cargas streaming
    - Implementa side inputs eficientemente
    - Optimiza ventanas según el caso de uso
    - Monitorea hotkeys en operaciones GroupBy

!!! info "Desarrollo"
    - Prueba pipelines localmente primero
    - Usa templates para reutilización
    - Implementa manejo de errores robusto
    - Versiona pipelines para rollbacks

!!! success "Operaciones"
    - Configura alertas de fallo
    - Usa dead letter queues para errores
    - Implementa checkpoints para recovery
    - Monitorea métricas de lag en streaming

---

¡Dataflow te permite procesar datos a escala Google! 🚀