# Claude Academy · Model Context Protocol: Advanced Topics

Curso de Anthropic (11 lecciones, ~1,5 h y un quiz) sobre MCP avanzado: sampling, logging y notificaciones de progreso, roots, tipos de mensajes JSON y transportes (stdio y Streamable HTTP), con estado y sin estado.

**Estado:** En curso · Lecciones leídas · Quiz final pendiente

!!! note "Versión de la especificación"
    El curso enseña MCP como funcionaba antes de la revisión **2026-07-28**, que deprecia sampling, logging y roots y elimina el handshake `initialize` y los IDs de sesión. Todo sigue funcionando en la versión 1 del SDK de Python.

## Sampling

- El **servidor le pide al cliente** que llame al modelo por él (`ctx.session.create_message(...)`); el cliente responde con un `sampling_callback` que usa su propia conexión a Claude.
- Ventajas: el servidor no necesita llave de API ni integración con el modelo y **el costo lo paga el cliente**. Ideal para **servidores públicos**.

## Logging y progreso

- Con el `Context` del tool: `await context.info("...")` y `await context.report_progress(70, 100)`.
- En el cliente: `logging_callback` al crear la sesión y `progress_callback` en cada `call_tool`. Cómo se muestran (terminal, WebSockets/SSE, barra de progreso) lo decide la app.

## Roots

- Indican al servidor **qué carpetas puede tocar**: Claude lista las roots, busca el archivo y llama la herramienta con la ruta completa, sin que el usuario la escriba.
- El SDK **no** las hace cumplir solo: hay que implementar algo como `is_path_allowed()` antes de cada operación con archivos.

## Mensajes y transportes

- Todo es JSON: pares **request → result** (`CallTool`, `ListPrompts`, `ReadResource`, `Initialize`) y **notificaciones** sin respuesta (progreso, logging, cambios en la lista de herramientas, recursos actualizados). El protocolo es **bidireccional**: el servidor también inicia mensajes.
- **stdio:** el cliente lanza el servidor como subproceso; stdin/stdout en ambos sentidos; solo en la misma máquina. Handshake: `Initialize Request` → `Initialize Result` → `Initialized Notification`.
- **Streamable HTTP:** para servidores remotos. Como HTTP no deja al servidor iniciar peticiones, usa **SSE**: una conexión GET de larga duración para mensajes del servidor y una conexión SSE por cada llamada a herramienta (logs y resultado). El `mcp-session-id` va en todas las peticiones tras inicializar.

| Bandera | Qué hace | Qué se pierde |
|---------|----------|---------------|
| `stateless_http=True` | Sin sesión; permite escalar horizontalmente detrás de un balanceador; no exige inicialización | Peticiones del servidor al cliente, sampling, progreso, suscripciones |
| `json_response=True` | Respuestas POST como JSON plano, sin streaming | Mensajes intermedios de progreso y logs |

!!! tip "Para recordar"
    - **Sampling** traslada el costo del modelo al cliente: clave para servidores públicos.
    - Las roots ayudan a encontrar archivos, pero **la restricción de acceso la implementa uno**.
    - Si funciona en stdio y falla al desplegar en HTTP, revisar `stateless_http` y `json_response`.
    - Probar con **el mismo transporte que se usará en producción**.
