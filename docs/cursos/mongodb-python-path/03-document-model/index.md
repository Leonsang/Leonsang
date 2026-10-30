# Unidad 3 · MongoDB and the Document Model

Unidad de la ruta *MongoDB Python Developer Path* (1,25 h). Cubre la estructura de los documentos, JSON y BSON, los tipos de datos, la gestión de datos en Atlas y los fundamentos del modelado: relaciones, embeber y referenciar.

| # | Lección | Estado | Resultado | Apuntes |
|---|---|---|---|---|
| 1 | Overview of the Document Model | Completado | Cuestionario 2/2 (100 %) | [Ver](01-vision-general-modelo-documentos.md) |
| 2 | Data Types in MongoDB | Completado | Cuestionario 2/2 (100 %) | [Ver](02-tipos-de-datos.md) |
| 3 | Managing Databases, Collections, and Documents in Atlas | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Completado | [Ver](03-gestionar-datos-en-atlas.md) |
| 4 | Data Relationships | Completado | Cuestionario 2/2 (100 %) | [Ver](04-relaciones-de-datos.md) |
| 5 | Embedding and Referencing | Completado | Cuestionario 2/2 (100 %) | [Ver](05-embeber-y-referenciar.md) |
| — | Conclusion | Completado | Unidad al 100 % | — |

**Resultado de la unidad:** 100 % de avance. 5 cuestionarios aprobados con **10/10** respuestas correctas.

## Objetivos cubiertos

- Describir el modelo de documentos y la estructura de un documento.
- Explicar para qué sirve el esquema flexible.
- Listar los tipos de datos de MongoDB.
- Crear una base de datos y una colección, e insertar un documento en la interfaz de Atlas.
- Identificar relaciones uno a uno, uno a muchos y muchos a muchos.
- Distinguir cuándo embeber y cuándo referenciar.

!!! tip "Para recordar"
    - Lo que se consulta junto, se guarda junto.
    - BSON = JSON binario con más tipos (Date, ObjectId, Decimal128…).
    - `_id` es obligatorio y único. Si falta, MongoDB genera un ObjectId.
    - 1:1 → embeber. 1:N → embeber o referenciar según el tamaño y el acceso. N:M → depende del caso.
    - Límites: 16 MB por documento y 100 niveles de anidamiento.

## Fuentes y aviso legal

- **Fuente:** cursos de MongoDB University. Sitios oficiales: [learn.mongodb.com](https://learn.mongodb.com) · [mongodb.com/docs](https://www.mongodb.com/docs).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por MongoDB. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../../aviso-legal.md).
