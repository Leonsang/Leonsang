# Unidad 5 · Connecting to MongoDB in Python

Unidad de la ruta *MongoDB Python Developer Path*. Cubre los drivers oficiales de MongoDB para Python, la instalación de **PyMongo**, la conexión de una aplicación a Atlas con `MongoClient` y la resolución de errores de conexión.

| # | Lección | Estado | Resultado | Apuntes |
|---|---|---|---|---|
| 1 | Using MongoDB Python Client Libraries | Completado | Cuestionario 2/2 (100 %) | [Ver](01-drivers-python.md) |
| 2 | Connecting to an Atlas Cluster in Python Applications | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Completado | [Ver](02-conectar-atlas-desde-python.md) |
| 3 | Troubleshooting a MongoDB Connection in Python Applications | Completado | Cuestionario 2/2 (100 %) | [Ver](03-resolver-conexion-en-python.md) |
| — | Conclusion | Completado | Unidad al 100 % | — |

**Resultado de la unidad:** 100 % de avance. 3 cuestionarios aprobados con **6/6** respuestas correctas.

## Objetivos cubiertos

- Instalar PyMongo con pip.
- Conectar una aplicación Python a un cluster de Atlas.
- Usar una sola instancia de MongoClient para todas las peticiones.
- Resolver problemas comunes de conexión y autenticación.

!!! tip "Para recordar"
    - PyMongo = síncrono. Motor = asíncrono.
    - `pip install pymongo dnspython`, y `MongoClient(uri)`.
    - Un MongoClient por aplicación.
    - `ServerSelectionTimeoutError` → IP en Network Access. `OperationFailure: Authentication failed` → usuario o contraseña.
