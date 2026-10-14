!!! info "Curso SENA"
    Aplicación de la inteligencia artificial en la integración de datos · ficha 3635322 · octubre de 2026

# AA2-EV02 · Foro de modelado de datos

> **Pregunta del debate:** ¿Qué criterios se deben tener en cuenta al seleccionar una metodología de
> modelamiento de datos y una herramienta de analítica, y cómo influyen los algoritmos y las técnicas
> estadísticas en la precisión y utilidad de los resultados obtenidos?

## Aporte al foro

**Asunto:** El modelo se elige por las preguntas del negocio, no por la herramienta

Buen día, instructor y compañeros.

Desde mi experiencia en ingeniería de datos, el criterio que ordena todos los demás es **para qué se van a usar los datos**. Una metodología de modelamiento no es mejor que otra en abstracto; es mejor para un tipo de carga:

- **Entidad-relación con normalización (3FN):** la elijo cuando el sistema registra operaciones (un ERP, un CRM). El objetivo es la integridad: cada dato vive en un solo lugar y las reglas de negocio se vuelven restricciones (por ejemplo, "no puede existir una factura sin cliente").
- **Modelo dimensional (esquema en estrella):** lo elijo cuando el objetivo es analizar. Se desnormaliza a propósito: una tabla de hechos con las medidas y dimensiones descriptivas alrededor. Se pierde algo de pureza, pero se gana velocidad de consulta y, sobre todo, que una persona de negocio entienda el modelo.

Los criterios que reviso antes de decidir son: (1) tipo de uso, transaccional o analítico; (2) granularidad, es decir, qué representa exactamente una fila; (3) volumen y frecuencia de actualización; (4) reglas de negocio que el modelo debe hacer cumplir; (5) quién lo va a consumir y con qué conocimiento técnico; y (6) trazabilidad, que se pueda auditar de dónde salió cada dato.

Para la **herramienta de analítica** aplico la misma lógica: compatibilidad con las fuentes, escalabilidad, curva de aprendizaje del equipo, costo, y si necesito tableros interactivos (Power BI, Tableau) o análisis reproducible en código (Python, R). No son excluyentes. En el caso práctico que desarrollé para este curso integré tres fuentes heterogéneas (ventas en CSV, clientes en JSON anidado y un catálogo de productos) con Python y Polars, construí el esquema en estrella con SQL en DuckDB y lo consumí en Power BI: cada herramienta donde es más fuerte.

Sobre los **algoritmos y las técnicas estadísticas**, mi conclusión es que no corrigen un mal modelo; lo amplifican. Dos ejemplos concretos de ese ejercicio:

- El archivo de ventas traía 25 filas duplicadas y 12 devoluciones cargadas como cantidades negativas. Un promedio o una regresión calculados sin tratar eso habrían dado un resultado "preciso" numéricamente, pero falso para el negocio. La estadística descriptiva (conteos, nulos, mínimos y máximos) fue justamente lo que permitió detectarlo antes de modelar.
- La elección de la medida importa: con valores extremos, la mediana describe mejor un ticket típico que la media. Usar la técnica equivocada no produce un error visible, produce una decisión equivocada.

En resumen: primero la pregunta de negocio y la granularidad, luego la metodología, después la herramienta; y la estadística como control de calidad antes que como adorno al final.

Me gustaría saber si alguno ha tenido que migrar un modelo normalizado a uno dimensional y qué fue lo más difícil del proceso.

Saludos,
Erick Manuel Sang Cifuentes

---
