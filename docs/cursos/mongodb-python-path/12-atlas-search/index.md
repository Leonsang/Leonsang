# Unidad 12 · Introduction to Atlas Search (optativa)

Unidad optativa de la ruta *MongoDB Python Developer Path*. Cubre el funcionamiento de Atlas Search (`mongot` y Lucene), los mapeos dinámicos y estáticos, los tipos de datos, los operadores `text`, `equals`, `near` y `range`, y los facets con `$searchMeta`.

| # | Lección | Estado | Resultado | Apuntes |
|---|---|---|---|---|
| 1 | Atlas Search Fundamentals | Completado | Cuestionario 2/2 (100 %) | [Ver](01-indices-y-mapeos.md) |
| 2 | Dynamic vs. Static Mappings | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](01-indices-y-mapeos.md) |
| 3 | Data Types | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](01-indices-y-mapeos.md) |
| 4 | $search operators: text and equals | Completado | Cuestionario 2/2 (100 %) | [Ver](02-operadores-y-facets.md) |
| 5 | $search operators: near and range | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](02-operadores-y-facets.md) |
| 6 | Creating Search Facets | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](02-operadores-y-facets.md) |
| — | Conclusion | Completado | Unidad al 100 % | — |

**Resultado de la unidad:** 100 % de avance. 6 cuestionarios aprobados con **12/12** respuestas correctas.

!!! tip "Para recordar"
    - `mongot` + Lucene. Sin índice de búsqueda no hay consulta. `$search` / `$searchMeta` van primero.
    - Dinámico = todo. Estático = campos elegidos, más eficiente.
    - text (texto completo), equals (exacto), near (cercanía con pivote), range (rango sin `$`).
    - Facets: stringFacet, dateFacet o numberFacet con `$searchMeta`.

## Fuentes y aviso legal

- **Fuente:** cursos de MongoDB University. Sitios oficiales: [learn.mongodb.com](https://learn.mongodb.com) · [mongodb.com/docs](https://www.mongodb.com/docs).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por MongoDB. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../../aviso-legal.md).
