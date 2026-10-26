# Unidad 7 · MongoDB CRUD Operations in Python

Unidad de la ruta *MongoDB Python Developer Path*. Cubre cómo se representan los documentos BSON en Python, las operaciones CRUD con PyMongo y las transacciones multidocumento con la *callback API*.

| # | Lección | Estado | Resultado | Apuntes |
|---|---|---|---|---|
| 1 | Working with MongoDB Documents in Python | Completado | Cuestionario 2/2 (100 %) | [Ver](01-documentos-bson-en-python.md) |
| 2 | Inserting a Document in Python Applications | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Pendiente | [Ver](02-crud-con-pymongo.md) |
| 3 | Querying a MongoDB Collection in Python Applications | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Pendiente | [Ver](02-crud-con-pymongo.md) |
| 4 | Updating Documents in Python Applications | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Pendiente | [Ver](02-crud-con-pymongo.md) |
| 5 | Deleting Documents in Python Applications | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Pendiente | [Ver](02-crud-con-pymongo.md) |
| 6 | Creating MongoDB Transactions in Python Applications | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Pendiente | [Ver](03-transacciones-en-python.md) |
| — | Conclusion | Completado | Unidad al 100 % | — |

**Resultado de la unidad:** 100 % de avance. 6 cuestionarios aprobados con **12/12** respuestas correctas.

!!! tip "Para recordar"
    - Documento = `dict`. PyMongo convierte a BSON solo. ObjectId, Int64, Decimal128 y Regex vienen del paquete `bson`.
    - `insert_one` / `insert_many`, `find_one` / `find` (cursor), `update_one` / `update_many`, `delete_one` / `delete_many`.
    - Transacciones: callback, después `start_session()` y `with_transaction(callback)`, con `session=session` en cada operación.
