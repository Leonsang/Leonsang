# 08.3 · Crear, gestionar y probar índices con `explain()`

## Crear índices

Atlas Data Explorer, Atlas CLI, Compass, mongosh y los drivers usan **`createIndex`** por debajo. Para crear **varios índices en una sola operación** se usa el comando `createIndexes`, que es más eficiente:

```javascript
db.runCommand({
  createIndexes: "messages",
  indexes: [
    { key: { userId: 1, timestamp: 1, category: 1 }, name: "userId_timestamp_category_index" },
    { key: { isRead: 1, userId: 1 },
      partialFilterExpression: { isRead: false },
      name: "isRead_userId_partial_index" }
  ]
})
```

- Con el comando de base de datos hay que dar un **nombre** (`name`) a cada índice.
- La colección pasa a tener 3 índices: `_id` más los dos nuevos.

![createIndexes con dos índices](evidencias/05-createindexes.png)

*Figura: `createIndexes` crea el índice compuesto y el parcial en una sola operación.*

## Gestionar los índices

| Método de mongosh | Para qué |
|---|---|
| `db.coleccion.getIndexes()` | Listar los índices |
| `db.coleccion.hideIndex()` | Ocultar un índice al planificador para **evaluar el impacto de borrarlo** antes de hacerlo |
| `dropIndex()` / `dropIndexes()` | Eliminar índices |
| `explain()` | Ver el plan de ejecución |

Herramientas para monitorear: Atlas (con el **Performance Advisor**, que recomienda índices), Compass y herramientas de terceros.

![Métodos de mongosh para índices](evidencias/05-metodos-mongosh.png)

*Figura: `getIndexes()` y `hideIndex()` para revisar los índices antes de borrar alguno.*

## Probar con `explain()`

```javascript
db.messages.explain("executionStats").find({ userId: "user505", timestamp: { $gte: ..., $lte: ... } }).sort({ timestamp: -1 })
```

- Niveles de detalle: **`queryPlanner`** (por defecto), **`executionStats`** y **`allPlansExecution`**, que incluye también los planes rechazados.
- **`winningPlan`**: dice si se usó **`COLLSCAN`** (sin índice) o **`IXSCAN`** (con índice) y cuál índice.
- **`executionStats`**: compara `nReturned` con `totalDocsExamined` y `totalKeysExamined`, y muestra `executionTimeMillis`. En el ejemplo se pasó de **105 915 documentos examinados para 23 devueltos (65 ms)** a **23 para 23 (0 ms)**.

![winningPlan sin y con índice](evidencias/06-explain-winningplan.png)

*Figura: sin índice el plan es COLLSCAN más SORT. Con índice es IXSCAN sobre `userId_timestamp_category_index`.*

![executionStats sin y con índice](evidencias/06-explain-executionstats.png)

*Figura: los documentos examinados bajan de 105 915 a 23 y el tiempo de 65 ms a 0 ms.*

## Consultas cubiertas (*covered queries*)

Una consulta está **cubierta** cuando **todos los campos que filtra y devuelve están en el mismo índice**. MongoDB responde solo con el índice, **sin leer documentos** (`totalDocsExamined: 0`). Para lograrlo, la proyección solo incluye campos del índice y excluye `_id`:

```javascript
db.messages.find({ userId: "user505", timestamp: {...} }, { _id: 0, userId: 1, timestamp: 1, category: 1 })
```

![Consulta cubierta](evidencias/06-consulta-cubierta.png)

*Figura: con una proyección que solo pide campos del índice (y `_id: 0`), la consulta queda cubierta.*

!!! tip "Para recordar"
    - `createIndexes` crea varios índices en una operación. Cada uno necesita `name`.
    - Antes de borrar un índice, **`hideIndex()`** para medir el impacto.
    - `explain("executionStats")`: busca **IXSCAN** frente a COLLSCAN y una relación **docsExamined ≈ nReturned**.
    - **Consulta cubierta** = filtro y proyección dentro del índice, con `_id: 0`. Examina 0 documentos.
