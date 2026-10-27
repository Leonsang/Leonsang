# Unidad 11 · MongoDB Transactions (optativa)

Unidad optativa de la ruta *MongoDB Python Developer Path*. Cubre las propiedades ACID, la diferencia entre operaciones de un documento y de varios documentos, y cómo usar transacciones multidocumento en mongosh.

| # | Lección | Estado | Resultado | Apuntes |
|---|---|---|---|---|
| 1 | Introduction to ACID Transactions | Completado | Match pairs y cuestionario 2/2 (100 %) | [Ver](01-transacciones-acid.md) |
| 2 | ACID Transactions in MongoDB | Completado | Cuestionario 2/2 (100 %) | [Ver](01-transacciones-acid.md) |
| 3 | Using Transactions in MongoDB | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](01-transacciones-acid.md) |
| — | Conclusion | Completado | Unidad al 100 % | — |

**Resultado de la unidad:** 100 % de avance. 3 cuestionarios aprobados con **6/6** respuestas correctas.

!!! tip "Para recordar"
    - ACID: atomicidad, consistencia, aislamiento, durabilidad.
    - Un solo documento = atómico. Varios documentos = transacción multidocumento.
    - `startSession` → `startTransaction` → `commitTransaction` / `abortTransaction`. Límite de 60 s.
