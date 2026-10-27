# Unidad 9 · MongoDB Aggregation

Unidad de la ruta *MongoDB Python Developer Path*. Cubre el *aggregation framework*: pipelines, etapas, expresiones y las etapas `$match`, `$group`, `$sort`, `$limit`, `$project`, `$set`, `$count` y `$out`.

| # | Lección | Estado | Resultado | Apuntes |
|---|---|---|---|---|
| 1 | Introduction to MongoDB Aggregation | Completado | Cuestionario 2/2 (100 %) | [Ver](01-introduccion-agregacion.md) |
| 2 | Using $match and $group Stages | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](02-etapas-del-pipeline.md) |
| 3 | Using $sort and $limit Stages | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](02-etapas-del-pipeline.md) |
| 4 | Using $project, $count, and $set Stages | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](02-etapas-del-pipeline.md) |
| 5 | Using the $out Stage | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](02-etapas-del-pipeline.md) |
| — | Conclusion | Completado | Unidad al 100 % | — |

**Resultado de la unidad:** 100 % de avance. 5 cuestionarios aprobados con **10/10** respuestas correctas.

!!! tip "Para recordar"
    - `db.coleccion.aggregate([...etapas])`: la salida de una etapa es la entrada de la siguiente y los datos de origen no cambian.
    - `$match` lo más temprano posible, `$group` con `_id` y acumuladores, `$sort` + `$limit` para el top N.
    - `$project` da forma a la salida, `$set` agrega o modifica campos, `$count` cuenta, `$out` guarda en una colección (al final, y sobrescribe).
