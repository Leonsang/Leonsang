# 04.4 · Usar el MongoDB Shell

Tareas prácticas en mongosh: insertar y buscar documentos, usar funciones JavaScript, cargar scripts, cambiar de base dentro de un script y editar código con un editor externo.

## Insertar y buscar documentos

```javascript
use sample_mflix
db.movies.find({ title: "Christmas Vacation" })   // sin resultados

db.movies.insertOne({
  title: "Christmas Vacation",
  cast: ["Chevy Chase", "Beverly D'Angelo", "Juliette Lewis"],
  runtime: 97,
  rated: "PG-13",
  directors: ["John Hughes"]
})
// { acknowledged: true, insertedId: ObjectId('66be...') }

db.movies.find({ title: "Christmas Vacation" })   // ahora devuelve el documento
```

- `find()` recibe un documento filtro con pares campo-valor.
- `insertOne()` inserta un documento y devuelve el estado (`acknowledged`) y el `_id` generado.
- Gracias al esquema flexible se puede insertar con información parcial y completar el documento después.

![insertOne en mongosh](evidencias/04-insertone.png)

*Figura: `insertOne()` devuelve `acknowledged: true` y el ObjectId del nuevo documento.*

## Funciones JavaScript

mongosh está construido sobre **Node.js**, así que acepta JavaScript:

```javascript
function cube(number) {
  if (typeof number !== 'number') {
    throw new Error("Input must be a number");
  }
  return number ** 3;
}
cube(16)   // 4096
```

Al pegar la función, queda en el **ámbito global** de la sesión.

![Función cube](evidencias/04-funcion-cube.png)

*Figura: una función auxiliar escrita en JavaScript dentro de mongosh.*

## Cargar scripts con `load()` y cambiar de base con `getSiblingDB()`

```javascript
// randomPost.js
db = db.getSiblingDB("sample_training");
let result = db.posts.aggregate({ $sample: { size: 1 } });
print(result.next().body);
```

```javascript
load("randomPost.js")   // imprime un post al azar y deja la sesión en sample_training
```

- **`load()`** ejecuta un archivo JavaScript en la sesión actual.
- **`db.getSiblingDB()`** cambia de base dentro de un script **sin datos de conexión**, lo que hace los scripts portables.
- `$sample` es una etapa de agregación que elige documentos al azar.

![Script con getSiblingDB y $sample](evidencias/04-script-getsiblingdb.png)

*Figura: el script `randomPost.js` cambia a `sample_training` y muestra un post aleatorio.*

## Editar con un editor externo

```javascript
config.get('editor')          // null si no hay editor configurado
config.set('editor', 'vim')   // primero se define el editor
edit cube                     // abre la función en el editor
```

Al guardar y salir, la nueva versión de la función queda cargada en la sesión. Sirve para comandos de varias líneas o largos.

!!! tip "Para recordar"
    - `insertOne()` inserta un documento y `find()` consulta. Se profundiza en las unidades de CRUD.
    - Funciones JS: se escriben directamente en mongosh o se cargan desde un archivo con **`load()`**.
    - **`db.getSiblingDB("base")`** cambia de base dentro de un script.
    - Editor externo: **primero `config.set('editor', '...')`** y después `edit <función>`.

## Cuestionario y laboratorio

- Cuestionario: **2/2 correctas (100 %)**. Las preguntas cubrieron las formas de usar funciones JavaScript en mongosh y el primer paso para configurar un editor externo.
- Laboratorio práctico: **Completado**.

### Laboratorio

El laboratorio tuvo cuatro retos en mongosh:

```javascript
// 1. Insertar y recuperar un documento en sample_mflix.movies
db.movies.insertOne({ title: "Free Guy", genres: ["Comedy", "Action", "Adventure"],
  runtime: 115, rated: "PG-13", year: 2021, type: "movie" })
db.movies.findOne({ title: "Free Guy" })

// 2. Función JavaScript en el ámbito global del shell
const randomMovie = () => db.movies.aggregate([{ $sample: { size: 1 } }]).toArray();
randomMovie()

// 3. Script externo /lab/connectAndInsert.js
//    línea 2:  db = db.getSiblingDB("sample_analytics")
//    línea 38: print(result)   // resultado de insertMany() en customers
load("/lab/connectAndInsert.js")

// 4. Editor externo para comandos largos
config.get("editor")            // null
config.set("editor", "nano")
edit                            // se escribe el comando en nano, Ctrl+X, Y, Enter
db.transactions.updateOne({ account_id: 443178 },
  { $push: { transactions: { date: new Date(), amount: Math.floor(Math.random() * 1000),
    transaction_code: Math.random() < 0.5 ? "buy" : "sell", symbol: "test",
    price: "100.00", total: "1337.10" } } })
// { acknowledged: true, matchedCount: 1, modifiedCount: 1 }
```

![insertOne y findOne en mongosh](evidencias/04-lab-insertar-y-buscar.png)

![Comando editado con nano y ejecutado](evidencias/04-lab-editar-comando.png)

![Resultado del cuestionario de la lección 4](evidencias/04-resultado-quiz.png)

*Figura: cuestionario de la lección 4 aprobado.*

## Fuentes y aviso legal

- **Fuente:** cursos de MongoDB University. Sitios oficiales: [learn.mongodb.com](https://learn.mongodb.com) · [mongodb.com/docs](https://www.mongodb.com/docs).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por MongoDB. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../../aviso-legal.md).
