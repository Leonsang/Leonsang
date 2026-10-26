# 06 · Conclusión y repaso

Cierre de la unidad *Getting Started with MongoDB Atlas*: un repaso de todo el recorrido.

## Resumen de la unidad

1. **Bases relacionales frente a no relacionales** y las ventajas del modelo de documentos.
2. **Sistema distribuido:** los datos se reparten entre nodos para tener failover automático y escalabilidad horizontal.
3. **Arquitectura:** documentos → colecciones → bases de datos → nodos → clusters.
4. **Replicación** (copias sincronizadas, alta disponibilidad), **read y write concerns** (equilibrio entre consistencia y disponibilidad) y **sharding** (cada shard guarda un subconjunto de los datos y juntos forman un sharded cluster).
5. **Atlas como DBaaS:** quita la carga operativa, ofrece tiers compartidos y dedicados, y permite elegir proveedor y región, incluso varios a la vez.
6. **Seguridad:** autenticación, autorización, certificaciones y capas avanzadas.
7. **Práctica en Atlas:** cluster gratuito M0, usuario de base de datos, carga de datos de ejemplo, consultas con Find y herramientas de operación (command line tools, métricas, Online Archive y Performance Advisor).

## Objetivos de aprendizaje cubiertos

- Definir qué es una base documental y un sistema distribuido.
- Explicar para qué sirve el esquema flexible.
- Definir documentos, colecciones y bases de datos.
- Describir cómo MongoDB mantiene la consistencia siendo distribuido.
- Explicar Atlas como base de datos como servicio, su operación en la nube y el failover automático.
- Desplegar un cluster, navegar la interfaz, cargar datos de ejemplo y consultar documentos.

## Para seguir

Documentación recomendada por el curso: *Get Started with Atlas*, *Introduction to MongoDB*, *FAQ: MongoDB Fundamentals*, *Atlas Vector Search Quickstart*, *Replication*, *Sharding* y *Security*.

!!! tip "Para recordar"
    - Tres pilares del sistema distribuido: **replicación = disponibilidad**, **read y write concerns = consistencia**, **sharding = escala**.
    - Atlas = MongoDB gestionado en AWS, GCP o Azure, con seguridad activada por defecto.
    - Ruta práctica mínima: cuenta → cluster M0 → IP en la Access List → usuario de base de datos → datos de ejemplo → Data Explorer.

![Unidad completada al 100 %](evidencias/curso-completado-100.png)

*Figura: la unidad aparece en «Completed» del panel de MongoDB University con 100 % y 1,25 horas.*
