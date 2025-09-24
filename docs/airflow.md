# Airflow: Orquestación de Workflows

> "Airflow es el estándar para automatizar y monitorear pipelines de datos."

---

## 🛫 ¿Qué es Apache Airflow?

Airflow es una plataforma open source para programar, orquestar y monitorear flujos de trabajo (DAGs) en data engineering. Permite definir dependencias, programar tareas y visualizar la ejecución de pipelines complejos.

---

## 🏗️ Arquitectura de Airflow

### Componentes Principales

![Arquitectura Airflow](https://github.com/vedanthv/data-engg/assets/44313631/898d4868-0e23-4111-aae6-976e4c35ba01)

- **Web Server:** Interfaz de usuario para monitorear y gestionar DAGs
- **Scheduler:** Programa y ejecuta tareas según las dependencias
- **Executor:** Ejecuta las tareas (LocalExecutor, CeleryExecutor, KubernetesExecutor)
- **Metadata Database:** Almacena estado de DAGs, tareas y configuraciones
- **Worker Nodes:** Ejecutan las tareas distribuidas

### Flujo de Ejecución

![Flujo Airflow](https://github.com/vedanthv/data-engg/assets/44313631/7cd5614e-cb73-4d13-8ec0-0d33d48915d6)

1. **DAG Parsing:** El scheduler lee y parsea los archivos DAG
2. **DAG Run Creation:** Se crea un objeto DAGRun para cada ejecución programada
3. **Task Scheduling:** Las tareas se programan según dependencias
4. **Task Execution:** Los workers ejecutan las tareas
5. **State Updates:** El estado se actualiza en la base de datos

---

## 🛠️ Componentes Clave

- **DAGs:** Flujos de trabajo dirigidos y acíclicos.
- **Operadores:** Tareas individuales (PythonOperator, BashOperator, etc).
- **Sensors:** Espera por eventos o condiciones externas.
- **Hooks:** Conexión con bases de datos, APIs y servicios cloud.
- **XComs:** Comunicación entre tareas.
- **Variables:** Configuración global accesible desde cualquier DAG.
- **Connections:** Credenciales encriptadas para sistemas externos.

---

## 🚀 Instalación y Setup

### Método 1: Instalación con pip

```bash
# Crear ambiente virtual
python3 -m venv airflow_env
source airflow_env/bin/activate

# Instalar Airflow
pip install apache-airflow

# Configurar directorio
export AIRFLOW_HOME=.

# Inicializar base de datos
airflow db init

# Crear usuario admin
airflow users create --username admin --firstname Erick --lastname Sang --role Admin --email ericksang@gmail.com

# Iniciar servicios
airflow webserver -p 8080
airflow scheduler
```

### Método 2: Docker con Astronomer CLI

```bash
# Instalar Astronomer CLI
winget install -e --id Astronomer.AstroCLI

# Crear proyecto
mkdir airflow-project && cd airflow-project
astro dev init

# Iniciar Airflow
astro dev start
```

!!! info "Astronomer CLI"
    Astronomer CLI simplifica el desarrollo local con Docker y facilita el despliegue en producción.

---

## 📝 Creando DAGs

### Método Tradicional

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ericksang',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'mi_pipeline_datos',
    default_args=default_args,
    description='Pipeline de procesamiento de datos',
    schedule_interval='@daily',
    catchup=False,
    tags=['data-engineering', 'etl']
)

def extraer_datos():
    print("Extrayendo datos de la fuente...")
    return {'registros': 1000, 'estado': 'exitoso'}

def transformar_datos():
    print("Transformando datos...")
    return {'registros_transformados': 950}

def cargar_datos():
    print("Cargando datos al destino...")

# Definir tareas
extraccion = PythonOperator(
    task_id='extraer_datos',
    python_callable=extraer_datos,
    dag=dag
)

transformacion = PythonOperator(
    task_id='transformar_datos',
    python_callable=transformar_datos,
    dag=dag
)

validacion = BashOperator(
    task_id='validar_datos',
    bash_command='echo "Validando calidad de datos..."',
    dag=dag
)

carga = PythonOperator(
    task_id='cargar_datos',
    python_callable=cargar_datos,
    dag=dag
)

# Definir dependencias
extraccion >> transformacion >> validacion >> carga
```

### Método Moderno: TaskFlow API

```python
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['taskflow', 'modern']
)
def pipeline_moderno():

    @task
    def extraer_datos():
        return {'registros': 1000, 'timestamp': datetime.now().isoformat()}

    @task
    def transformar_datos(datos_extraidos):
        registros = datos_extraidos['registros']
        return {'registros_transformados': registros * 0.95}

    @task
    def cargar_datos(datos_transformados):
        print(f"Cargando {datos_transformados['registros_transformados']} registros")
        return "Carga completada exitosamente"

    # Flujo de datos automático
    datos = extraer_datos()
    datos_transformados = transformar_datos(datos)
    resultado = cargar_datos(datos_transformados)

# Instanciar el DAG
pipeline_moderno()
```

---

## 🔄 XComs: Intercambio de Datos

### ¿Qué son los XComs?

XCom (Cross-Communication) permite compartir datos pequeños entre tareas del mismo DAG.

![XComs](https://github.com/vedanthv/data-engg/assets/44313631/912756d0-d44b-4eec-96bc-633f81fee0a0)

### Características Importantes

- **Tamaño limitado:** SQLite (1GB), PostgreSQL (1GB), MySQL (64KB)
- **JSON serializable:** Los datos deben ser serializables
- **Por DAG Run:** Los datos son específicos para cada ejecución

### Ejemplo Práctico

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extraer_metricas(ti):
    """Extrae métricas y las almacena en XCom"""
    metricas = {
        'registros_procesados': 1500,
        'errores': 3,
        'tiempo_procesamiento': 45.2
    }
    # Push automático con return
    return metricas

def validar_calidad(ti):
    """Valida calidad usando datos de XCom"""
    metricas = ti.xcom_pull(task_ids='extraer_metricas')

    if metricas['errores'] > 5:
        raise ValueError("Demasiados errores en el procesamiento")

    # Push con clave específica
    ti.xcom_push(key='calidad_ok', value=True)
    return "Validación exitosa"

def generar_reporte(ti):
    """Genera reporte final"""
    metricas = ti.xcom_pull(task_ids='extraer_metricas')
    calidad = ti.xcom_pull(task_ids='validar_calidad', key='calidad_ok')

    reporte = {
        'metricas': metricas,
        'calidad_aprobada': calidad,
        'timestamp': datetime.now().isoformat()
    }
    print(f"Reporte generado: {reporte}")

dag = DAG('ejemplo_xcoms', start_date=datetime(2024, 1, 1), schedule='@daily')

tarea1 = PythonOperator(task_id='extraer_metricas', python_callable=extraer_metricas, dag=dag)
tarea2 = PythonOperator(task_id='validar_calidad', python_callable=validar_calidad, dag=dag)
tarea3 = PythonOperator(task_id='generar_reporte', python_callable=generar_reporte, dag=dag)

tarea1 >> tarea2 >> tarea3
```

---

## ⚙️ Variables y Configuración

### Variables en Airflow

Las Variables permiten almacenar configuraciones globales accesibles desde cualquier DAG.

```python
from airflow.models import Variable
from airflow.operators.python import PythonOperator

# Método 1: Python
def procesar_con_config():
    # Obtener variable simple
    ambiente = Variable.get("AMBIENTE", default_var="dev")

    # Obtener variable JSON
    config_db = Variable.get("CONFIG_DATABASE", deserialize_json=True)

    print(f"Procesando en ambiente: {ambiente}")
    print(f"Conectando a: {config_db['host']}")

# Método 2: Templating Jinja
tarea_templated = BashOperator(
    task_id='reporte',
    bash_command='echo "Generando reporte para {{ var.value.AMBIENTE }}"'
)
```

### Variables de Entorno

```bash
# En archivo .env
AIRFLOW_VAR_AMBIENTE=production
AIRFLOW_VAR_CONFIG_DATABASE={"host":"prod-db","port":5432}
```

---

## 🔗 Connections: Integraciones Externas

### Crear Connections

```python
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python import PythonOperator

def consultar_base_datos():
    # Usar connection definida en UI
    hook = PostgresHook(postgres_conn_id='postgres_prod')

    sql = "SELECT COUNT(*) FROM usuarios WHERE activo = true"
    resultado = hook.get_first(sql)

    print(f"Usuarios activos: {resultado[0]}")

tarea_db = PythonOperator(
    task_id='consultar_db',
    python_callable=consultar_base_datos
)
```

---

## 📅 Programación Avanzada

### Conceptos de Scheduling

![Scheduling](https://github.com/vedanthv/data-engg/assets/44313631/f83699c2-18cf-458e-8358-c05c9eabd0f9)

- **start_date:** Fecha de inicio del DAG
- **schedule_interval:** Frecuencia de ejecución
- **catchup:** Ejecutar DAGs perdidos automáticamente
- **max_active_runs:** Máximo de ejecuciones concurrentes

### Ejemplos de Schedule

```python
# Diferentes tipos de programación
dags_ejemplos = {
    'diario': '@daily',
    'cada_hora': '@hourly',
    'semanal': '@weekly',
    'mensual': '@monthly',
    'cada_15_min': '*/15 * * * *',
    'lunes_a_viernes': '0 9 * * 1-5',
    'primer_dia_mes': '0 0 1 * *',
    'manual_solo': None
}
```

### Backfilling

```bash
# Ejecutar DAGs históricos
airflow dags backfill \
    --start-date 2024-01-01 \
    --end-date 2024-01-31 \
    mi_dag_id
```

---

## 🐛 Debugging y Troubleshooting

### Comandos Útiles

```bash
# Listar DAGs
airflow dags list

# Verificar errores de importación
airflow dags list-import-errors

# Verificar sintaxis de DAG específico
airflow dags show mi_dag_id

# Ver logs del scheduler
astro dev logs -s

# Acceder al contenedor
astro dev bash
```

### Errores Comunes

!!! warning "DAG no aparece en UI"
    - Verificar que el archivo esté en la carpeta `dags/`
    - Comprobar que no hay errores de sintaxis
    - Confirmar que el DAG tiene `dag_id` único
    - Revisar que el archivo contiene "airflow" o "dag"

!!! error "Tasks no se ejecutan"
    - Verificar que el DAG esté "unpaused"
    - Confirmar que `start_date` está en el pasado
    - Revisar configuración de `max_active_runs`
    - Comprobar conexiones y credenciales

### Mejores Prácticas de Debug

```python
import logging
from airflow.decorators import task

@task
def tarea_con_logs():
    logger = logging.getLogger(__name__)

    try:
        # Código de la tarea
        resultado = procesar_datos()
        logger.info(f"Procesamiento exitoso: {resultado}")
        return resultado

    except Exception as e:
        logger.error(f"Error en procesamiento: {str(e)}")
        raise
```

---

## 🎯 Casos de Uso Avanzados

### 1. Pipeline ETL Completo

```python
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import pandas as pd

@dag(schedule='@daily', start_date=datetime(2024, 1, 1))
def pipeline_etl_completo():

    @task
    def extraer_datos_fuente():
        """Extrae datos de base de datos fuente"""
        hook = PostgresHook(postgres_conn_id='fuente_datos')
        sql = """
        SELECT usuario_id, fecha, transaccion, monto
        FROM transacciones
        WHERE fecha = '{{ ds }}'
        """
        df = hook.get_pandas_df(sql)
        return df.to_json(orient='records')

    @task
    def transformar_datos(datos_json):
        """Aplica transformaciones de negocio"""
        df = pd.read_json(datos_json, orient='records')

        # Transformaciones
        df['monto_usd'] = df['monto'] * 0.85  # Conversión
        df['categoria'] = df['monto'].apply(lambda x: 'alto' if x > 1000 else 'bajo')

        return df.to_json(orient='records')

    @task
    def validar_calidad(datos_transformados):
        """Valida calidad de datos"""
        df = pd.read_json(datos_transformados, orient='records')

        assert len(df) > 0, "No hay datos para procesar"
        assert df['monto'].min() >= 0, "Montos negativos encontrados"

        return {"registros": len(df), "validacion": "exitosa"}

    @task
    def cargar_a_dw(datos_transformados):
        """Carga datos al data warehouse"""
        df = pd.read_json(datos_transformados, orient='records')

        hook = PostgresHook(postgres_conn_id='data_warehouse')
        hook.insert_rows(
            table='hechos_transacciones',
            rows=df.values.tolist(),
            target_fields=list(df.columns)
        )

        return f"Cargados {len(df)} registros al DW"

    # Flujo del pipeline
    datos_crudos = extraer_datos_fuente()
    datos_transformados = transformar_datos(datos_crudos)
    validacion = validar_calidad(datos_transformados)
    resultado_carga = cargar_a_dw(datos_transformados)

pipeline_etl_completo()
```

### 2. Monitoreo con Sensores

```python
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.http_sensor import HttpSensor

@dag(schedule='@hourly', start_date=datetime(2024, 1, 1))
def pipeline_con_sensores():

    # Esperar archivo
    sensor_archivo = FileSensor(
        task_id='esperar_archivo_datos',
        filepath='/datos/archivo_{{ ds }}.csv',
        timeout=300,
        poke_interval=30
    )

    # Verificar API disponible
    sensor_api = HttpSensor(
        task_id='verificar_api_activa',
        http_conn_id='api_externa',
        endpoint='health',
        timeout=120,
        poke_interval=20
    )

    @task
    def procesar_cuando_listo():
        print("Archivo y API listos, procesando...")

    [sensor_archivo, sensor_api] >> procesar_cuando_listo()

pipeline_con_sensores()
```

---

## 💡 Buenas Prácticas

!!! tip "Diseño de DAGs"
    - Mantén DAGs pequeños y enfocados
    - Usa nombres descriptivos para tareas
    - Implementa idempotencia en todas las tareas
    - Evita dependencias circulares

!!! info "Monitoreo y Alertas"
    - Configura alertas por email/Slack para fallos
    - Usa métricas personalizadas para monitoreo
    - Implementa health checks regulares
    - Documenta tiempos esperados de ejecución

!!! success "Gestión de Código"
    - Usa control de versiones (Git)
    - Implementa tests unitarios para funciones
    - Separa configuración de lógica de negocio
    - Usa ambientes separados (dev/staging/prod)

!!! warning "Rendimiento"
    - Evita transferir grandes volúmenes por XCom
    - Usa pooling para limitar concurrencia
    - Optimiza consultas SQL en hooks
    - Monitorea uso de recursos de workers

---

## 📚 Recursos Avanzados

### Documentación Oficial
- [Apache Airflow Docs](https://airflow.apache.org/docs/)
- [Astronomer Registry](https://registry.astronomer.io/)
- [Airflow Providers](https://airflow.apache.org/docs/apache-airflow-providers/)

### Herramientas Complementarias
- [Airflow dbt Integration](https://github.com/dbt-labs/dbt-airflow)
- [Great Expectations + Airflow](https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_great_expectations_with_airflow)
- [Airflow Kubernetes Executor](https://airflow.apache.org/docs/apache-airflow/stable/executor/kubernetes.html)

### Monitoreo y Observabilidad
- [Airflow StatsD](https://airflow.apache.org/docs/apache-airflow/stable/logging-monitoring/metrics.html)
- [Datadog Airflow Integration](https://docs.datadoghq.com/integrations/airflow/)
- [Prometheus Airflow Exporter](https://github.com/robinhood/airflow_prometheus_exporter)

---

¿Quieres profundizar en algún tema específico? ¡Explora las otras secciones de arquitectura y casos de uso!
