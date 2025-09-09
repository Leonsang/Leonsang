# Airflow: Orquestación de Workflows

> "Airflow es el estándar para automatizar y monitorear pipelines de datos."

---

## 🛫 ¿Qué es Apache Airflow?

Airflow es una plataforma open source para programar, orquestar y monitorear flujos de trabajo (DAGs) en data engineering. Permite definir dependencias, programar tareas y visualizar la ejecución de pipelines complejos.

---

## 🛠️ Componentes Clave

- **DAGs:** Flujos de trabajo dirigidos y acíclicos.
- **Operadores:** Tareas individuales (PythonOperator, BashOperator, etc).
- **Sensors:** Espera por eventos o condiciones externas.
- **Hooks:** Conexión con bases de datos, APIs y servicios cloud.
- **XComs:** Comunicación entre tareas.

---

## 💡 Buenas Prácticas

!!! tip "Divide y vencerás"
    Crea DAGs modulares y reutilizables para facilitar el mantenimiento.

!!! info "Monitorea y alerta"
    Configura notificaciones y alertas para detectar fallos rápidamente.

!!! success "Versiona y documenta"
    Usa control de versiones y docstrings en tus DAGs.

---

## 📝 Ejemplo de DAG en Airflow

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'ericksang',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG('ejemplo_dag', default_args=default_args, schedule_interval='@daily')

tarea1 = BashOperator(
    task_id='inicio',
    bash_command='echo "Inicio del pipeline"',
    dag=dag
)

tarea2 = BashOperator(
    task_id='fin',
    bash_command='echo "Fin del pipeline"',
    dag=dag
)

tarea1 >> tarea2
```

---

## 📚 Recursos

- [Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
- [Airflow Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
- [Awesome Airflow](https://github.com/apache/airflow/blob/main/README.md)

---

¿Quieres ver ejemplos avanzados o notebooks embebidos? ¡Explora la sección Notebooks!
