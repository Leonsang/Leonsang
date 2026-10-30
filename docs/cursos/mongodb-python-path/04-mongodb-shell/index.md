# Unidad 4 · Connecting to a MongoDB Database Using the MongoDB Shell

Unidad de la ruta *MongoDB Python Developer Path*. Cubre los connection strings, la instalación de **mongosh**, la conexión a Atlas y a instancias locales, la resolución de errores de conexión y el uso del shell con JavaScript.

| # | Lección | Estado | Resultado | Apuntes |
|---|---|---|---|---|
| 1 | Using MongoDB Connection Strings | Completado | Cuestionario 2/2 (100 %) | [Ver](01-connection-strings.md) |
| 2 | Installing and Connecting to the MongoDB Shell | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](02-instalar-y-conectar-mongosh.md) |
| 3 | Troubleshooting Connection Errors | Completado | Cuestionario 2/2 (100 %). Lab en Atlas: Pendiente | [Ver](03-resolver-errores-de-conexion.md) |
| 4 | Using the MongoDB Shell | Completado | Cuestionario 2/2 (100 %). Lab: Completado | [Ver](04-usar-mongosh.md) |
| — | Conclusion | Completado | Unidad al 100 % | — |

**Resultado de la unidad:** 100 % de avance. 4 cuestionarios aprobados con **8/8** respuestas correctas.

## Objetivos cubiertos

- Definir el connection string, ubicarlo en Atlas e identificar sus componentes.
- Instalar mongosh y conectarse a una instancia local y a un cluster de Atlas.
- Resolver errores de conexión con Atlas.
- Insertar y recuperar documentos con mongosh.
- Escribir y usar funciones JavaScript, `db.getSiblingDB()`, `load()` y un editor externo.

!!! tip "Para recordar"
    - `mongodb+srv://` = TLS y descubrimiento de hosts por DNS. Atlas lo usa por defecto.
    - Puerto por defecto: 27017. Otro puerto: `mongosh --port N`.
    - Error de red → IP en Network Access. `bad auth` → credenciales o usuario en Database Access. Demasiadas conexiones → escalar, reiniciar o `maxPoolSize`.
    - `load()` para scripts, `getSiblingDB()` para cambiar de base, `config.set('editor', ...)` antes de `edit`.

## Fuentes y aviso legal

- **Fuente:** cursos de MongoDB University. Sitios oficiales: [learn.mongodb.com](https://learn.mongodb.com) · [mongodb.com/docs](https://www.mongodb.com/docs).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por MongoDB. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../../aviso-legal.md).
