# Claude Academy · Introduction to Model Context Protocol

Curso de Anthropic (10 lecciones, ~1 h y un quiz) para construir un servidor y un cliente MCP con el SDK de Python: herramientas, el inspector, recursos y prompts, sobre un chatbot de línea de comandos que gestiona documentos.

**Estado:** En curso · Lecciones leídas · Quiz final pendiente

## Qué resuelve MCP

- Una **capa de comunicación** que mueve la definición y ejecución de herramientas desde mi servidor a **servidores MCP especializados**. Ejemplo: en vez de escribir decenas de esquemas para la API de GitHub, me conecto al servidor MCP de GitHub.
- Cualquiera puede publicar un servidor; a menudo lo hace el propio proveedor (p. ej. AWS).
- **MCP no es lo mismo que tool use:** MCP entrega herramientas ya implementadas; tool use es cómo Claude las llama.

## Cliente y transporte

- El **cliente MCP** es el puente entre mi servidor y los servidores MCP. Es agnóstico del transporte: stdio (mismo equipo, lo más común), HTTP, WebSockets.
- Mensajes clave: `ListToolsRequest/Result` y `CallToolRequest/Result`.
- Flujo completo: el usuario pregunta → listo las herramientas vía el cliente → envío pregunta + herramientas a Claude → Claude pide una herramienta → el cliente la ejecuta en el servidor MCP (que llama a la API externa) → el resultado vuelve a Claude → respuesta final.

## Servidor con el SDK de Python

```python
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")

@mcp.tool(name="read_doc_contents",
          description="Read the contents of a document and return it as a string.")
def read_document(doc_id: str = Field(description="Id of the document to read")):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

- Decoradores en lugar de JSON Schema a mano; las anotaciones de tipo validan y `Field` describe cada argumento.
- **Inspector:** `mcp dev mcp_server.py` abre una UI local (Connect → Tools → List Tools → Run Tool) que conserva el estado entre llamadas.

## Cliente

- Una clase propia que envuelve la `ClientSession` del SDK y libera los recursos al cerrar.
- `list_tools()` → `session.list_tools()`; `call_tool(nombre, input)` → `session.call_tool(...)`.
- En la práctica se implementa **o** un cliente **o** un servidor; el curso hace ambos para ver cómo encajan.

## Recursos y prompts

- **Recursos** = datos de solo lectura, como un GET. **Directos** (`docs://documents`) o **con plantilla** (`docs://documents/{doc_id}`, el SDK pasa los parámetros como argumentos). `mime_type` indica cómo interpretar la respuesta. Útiles para menciones `@documento`: el contenido entra al prompt sin llamar herramientas.
- **Prompts** = instrucciones probadas y reutilizables que el servidor ofrece (p. ej. `/format doc_id` para pasar un documento a Markdown). Se definen con `@mcp.prompt` y devuelven una lista de mensajes; el cliente los obtiene con `get_prompt(nombre, args)`.

| Primitivo | Lo controla | Para qué |
|-----------|-------------|----------|
| **Tools** | El **modelo** | Darle a Claude nuevas capacidades que usa por su cuenta |
| **Resources** | La **app** | Llevar datos a la UI o al contexto (autocompletar, adjuntar de Drive) |
| **Prompts** | El **usuario** | Flujos predefinidos que el usuario dispara (botones, slash commands) |

!!! tip "Para recordar"
    - MCP traslada el trabajo de integración a quien mejor conoce el servicio.
    - **Tools sirven al modelo, resources a la app, prompts al usuario.**
    - Probar el servidor con el **Inspector** antes de conectarlo a una app.
    - Descripciones claras en herramientas y argumentos: es lo que Claude lee para decidir.
