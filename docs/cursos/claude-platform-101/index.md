# Claude Academy · Claude Platform 101

Curso de Anthropic (13 lecciones, ~1,5 h y un quiz) para construir con Claude por API: la plataforma, la primera llamada, elegir modelo, el bucle agéntico, tool use, thinking, herramientas integradas, skills, MCP, gestión de contexto y Managed Agents.

**Estado:** En curso · Lecciones leídas · Quiz final pendiente

## La plataforma

- API REST, SDKs, CLIs y la **Console** (llaves, uso, managed agents, pruebas de prompts).
- **Tres capas:** *primitivas* (Messages API, tool use, archivos, web search, code execution, MCP, skills) → *infraestructura* (managed agents, reintentos, colas, observabilidad) → *controles* (dashboards, evals). **Construir con primitivas, escalar sobre infraestructura, operar con control.**
- La idea: pasar de "preguntarle a Claude" a "Claude es parte de mi producto".

## Primera llamada

- La llave va en `.env.local`, **nunca en el código** (así se filtran en GitHub).
- `messages.create` con `model`, `max_tokens` y `messages` (roles `user`/`assistant`); `system` define el rol o persona.
- La respuesta `content` es una **lista de bloques** (texto, llamadas a herramientas, thinking): recorrerla y revisar el `type`.

## Elegir modelo

| Familia | Para qué |
|---------|----------|
| **Fable** (`claude-fable-5-1`) | Lo más difícil; por encima de Opus y más caro |
| **Opus** (`claude-opus-5-5`) | Razonamiento profundo, análisis complejo, código de varios pasos |
| **Sonnet** (`claude-sonnet-5`) | Equilibrio de inteligencia, velocidad y costo; la mayoría del trabajo en producción |
| **Haiku** (`claude-haiku-4-5`) | Volumen y baja complejidad: clasificar, extraer, enrutar |

- Hacer un **eval simple** con 20–30 ejemplos reales y subir desde Haiku: **el modelo correcto es el más barato cuya salida publicaría.**
- `response.usage` trae los tokens de entrada y salida (la base de la factura). En producción, **enrutar** cada tipo de tarea a un modelo distinto en el mismo endpoint.

## Bucle agéntico y tool use

1. Enviar el mensaje con `tools` disponibles.
2. Claude responde con texto final o con una petición de herramienta (`stop_reason: "tool_use"`).
3. **Mi código ejecuta la herramienta** (Claude no la ejecuta).
4. Devolver un bloque `tool_result` con el `tool_use_id` en un mensaje `user`.
5. Repetir hasta `stop_reason: "end_turn"`.

- Una herramienta = `name` + `description` + `input_schema` (JSON Schema). **La descripción es lo que Claude lee para decidir**: una vaga es la causa número uno de agentes que fallan.
- Con varias herramientas, Claude elige cuál y en qué orden (a veces en el mismo turno).
- El **tool runner** (beta en los SDKs) define cada herramienta una vez y maneja el bucle completo.

## Thinking

- Razonamiento paso a paso antes de responder. En Opus 5 es **adaptativo y activo por defecto**; el resumen del razonamiento solo vuelve si se pide `"display": "summarized"`.
- La profundidad se controla con `effort` **dentro de `output_config`**: `low`, `medium`, `high` (defecto), `xhigh`, `max`.
- Útil en matemáticas, lógica de varios pasos, depuración, análisis regulatorio y comparaciones con trade-offs; innecesario para clasificar o extraer.

## Herramientas integradas, skills y MCP

- **Server tools** (las ejecuta Anthropic, sin bucle): web search, code execution, web fetch. Aparecen bloques `server_tool_use` y de resultado en la misma respuesta.
- **Client tools** con esquema ya entrenado (memory, bash): las ejecuta mi código.
- **Skills:** se suben una vez (`client.skills.create`) y se adjuntan en `container.skills` junto con code execution. Se cargan de forma progresiva (primero nombre y descripción).
- **MCP:** integraciones que **mantiene el proveedor** del servicio. Se declaran en `mcp_servers` (URL, nombre, token) y se habilitan con un `mcp_toolset`; para limitar, `default_config: {"enabled": false}` y activar solo las herramientas necesarias (p. ej. Slack solo lectura).

| Pieza | Para qué |
|-------|----------|
| Tools | Mis sistemas internos (yo mantengo el código) |
| Skills | Mis procesos (el *cómo*) |
| MCP | Servicios de terceros (los mantiene el proveedor) |

## Gestión de contexto

1. **Just-in-time:** cargar solo lo necesario y dejar que las herramientas traigan el resto (patrón de diseño).
2. **Compactación del lado del servidor:** `context_management` con `compact_20260112` resume turnos viejos al pasar un umbral.
3. **Prompt caching:** reutilizar las partes estables (system prompt, herramientas, documentos largos) a una fracción del costo.
4. **Memory tool:** Claude lee y escribe un directorio de memoria; yo implemento el almacenamiento y la memoria sobrevive entre sesiones.

## Managed Agents

- El bucle agéntico **alojado por Anthropic**, en un contenedor aislado con sistema de archivos, bash y búsqueda web.
- Cuatro primitivas: **Agent** (modelo, system prompt, herramientas; reutilizable) → **Environment** (nube o self-hosted, red, paquetes) → **Session** (una ejecución) → **Events** (lo que entra y sale). Ya no escribo un `while`: envío y leo eventos.
- Piezas adicionales: herramientas personalizadas en mi backend, MCP, **memoria**, **outcomes** (rúbricas y un evaluador en contexto separado que hace iterar al agente) y **coordinación multiagente** (un coordinador delega en especialistas).
- Ejemplos: tablero Kanban que lanza una sesión al mover un ticket (rúbrica de Lighthouse > 90), agente de investigación semanal con memoria y respuesta a incidentes con coordinador y aprobación humana antes de publicar.

!!! tip "Para recordar"
    - Las llaves de API van en archivos de entorno, nunca en el código.
    - **Eval primero, desde Haiku hacia arriba**; quedarse con el modelo más barato que sirve.
    - Claude **pide** la herramienta; **mi código la ejecuta**. La descripción de la herramienta decide si se usa bien.
    - `effort` va dentro de `output_config`.
    - Tools para lo mío, skills para mis procesos, MCP para lo de otros.
    - Cuando el bucle dura minutos u horas, delegarlo a Managed Agents.
