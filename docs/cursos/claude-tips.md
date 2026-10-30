# Tips & Tricks de Claude

Chuleta práctica que reúne lo más útil de cada curso de Claude Academy, ordenada por herramienta. Crece con cada curso completado; cada sección enlaza a las notas de donde sale.

[Ver insignias y cursos](../claude-academy/){ .md-button }

## Claude Code

### Atajos y comandos

| Atajo / comando | Para qué |
|-----------------|----------|
| `Shift + Tab` | Cambiar de modo: manual → accept edits → plan → auto |
| `Esc Esc` (prompt vacío) | Abrir **rewind**: restaurar código, conversación o ambos a un checkpoint |
| `/compact <instrucciones>` | Compactar diciendo **qué conservar** ("enfócate en el flag --version") |
| `/clear` | Empezar de cero para una tarea nueva (sin sesgo de la anterior) |
| `/context` | Ver qué está ocupando el contexto |
| `/diff` | Revisar los cambios archivo por archivo antes de confiar en el resumen |
| `/code-review` | Segunda opinión en contexto limpio; solo reporta. `--fix` aplica los hallazgos |
| `/init` | Generar el CLAUDE.md cuando ya sé qué le corrijo siempre |
| `/goal <condición>` | Trabajar hasta que se cumpla algo verificable ("todas las pruebas pasan y cero errores de tipos") |
| `/loop` | Repetir un prompt en intervalo para vigilar CI o un despliegue |
| `/schedule` | Convertir una tarea en rutina en la nube |
| `/mcp`, `/hooks` | Ver servidores MCP conectados y hooks configurados |
| `/plugin install x@marketplace` | Instalar un plugin (leer antes qué trae) |

### Flujo

- **Explorar → Planear → Codificar → Commit.** Corregir en el plan es lo más barato.
- Leer el plan **de verdad**, no solo hojearlo.
- Definir **criterios de éxito** y darle una suite de pruebas confiable.
- Antes del commit: revisión con subagente o `/code-review`, y el mensaje de commit en mi estilo.
- Trabajo en paralelo: **worktrees** (uno por sesión); `.worktreeinclude` para copiar `.env` y configs locales.

### Contexto

- Un prompt **específico** gasta menos contexto que uno vago (el vago obliga a explorar).
- Delegar búsquedas a **subagentes**: solo vuelve el resumen.
- Apagar servidores MCP que no se usan; si existe CLI (`gh`, `aws`), gasta menos que un MCP.
- Para reinyectar contexto tras compactar: hook `SessionStart` con matcher `compact`.

### CLAUDE.md

- Corto gana: cada línea compite con las demás.
- Reglas **específicas y verificables** ("rutas nuevas en `src/api/handlers`, una por archivo").
- **Nombrar el reemplazo**: "usa exports con nombre", no solo "no uses default exports".
- El énfasis (IMPORTANT) es un **presupuesto** para 2 o 3 reglas.
- Cada error repetido = bug report contra el CLAUDE.md ("agrega eso al CLAUDE.md").
- Niveles: política gestionada, usuario, proyecto y local (ignorado por git).

### Dónde va cada regla

| Si la regla… | Va en |
|--------------|-------|
| Aplica siempre (convenciones) | CLAUDE.md |
| Es un procedimiento de un tipo de tarea | Skill |
| **No se puede saltar** | Hook |
| La explico una y otra vez | Skill nueva |

### Hooks

- `PreToolUse` bloquea o **reescribe** (`updatedInput`, p. ej. redactar un `sk_live_...`); `PostToolUse` formatea y hace lint; `Stop` hace correr las pruebas antes de terminar.
- Exit **2** bloquea y devuelve stderr a Claude; exit **1 no bloquea**.
- `updatedInput` reemplaza todo el input: devolver también los campos que no cambian.
- Hooks del proyecto en `.claude/settings.json` + `CLAUDE_PROJECT_DIR` para scripts del repo.

### Sin supervisión

- **Auto mode** cuida la intención (bloquea despliegues, force push, exfiltración); un **Stop hook con pruebas** cuida la corrección.
- *Don't ask* para CI; *bypass* solo en contenedor o VM aislado.
- Verificar en proporción a lo que no vi: diff → pruebas como compuerta → segunda opinión en frío.
- `claude -p` para scripts; `--output-format json --json-schema` + `jq '.structured_output'`; `--resume` con `session_id`; `--bare` para CI reproducible.

Fuentes: [Claude Code 101](../claude-code-101/) · [Claude Code in Action](../claude-code-in-action/)

## Prompting (Chat y en general)

- Prompt = **escenario** (rol, objetivo, contexto) + **tarea** + **reglas** (formato, tono, ejemplos).
- ¿Respuesta genérica? Falta contexto. ¿Formato mal? Mostrar un ejemplo.
- Feedback específico: "quita los dos primeros párrafos y cierra con acciones" > "hazlo más corto".
- Pedir **el entregable** ("un one-pager para el comité") y no solo el contenido.
- Antes de delegar algo recurrente, probarlo con un caso cuya respuesta ya conozco (**eval casero**).
- **Proyectos guardan conocimiento, skills ejecutan procesos.** Nombres de archivo descriptivos en el conocimiento del proyecto.

Fuente: [Claude 101](../claude-101/)

## Cowork

- Prompt de delegación = **entregable + insumos + matices**.
- Carpeta de trabajo **mínima** y dedicada; respaldo de lo irremplazable; probar flujos nuevos sobre **copias**.
- Verbos destructivos explícitos: "quita la sección del borrador, pero conserva el archivo".
- Límites en el prompt: "solo los 3 archivos más recientes", "no le escribas a nadie, solo borrador".
- Corregir **a mitad de tarea** en lugar de esperar y regenerar.
- `/schedule` después de haber hecho la tarea una vez y validado el resultado; `/setup-claude` para descubrir plugins.
- Instrucciones globales con las correcciones que repito ("conclusión primero").

Fuente: [Introduction to Claude Cowork](../claude-cowork/)

## Claude Tag (Slack)

- `@Claude what can you access from here?` antes de pedir algo grande.
- `@Claude remember for this channel: …` para probar una regla; cuando se asienta, pasarla a las instrucciones del canal.
- Rutinas que **no publican nada si no hay novedades**.
- `@Claude !scheduled` lista rutinas; `!mute` silencia un hilo.
- Si varios lugares sirven, **canal público**: otros corrigen y lo aprendido beneficia a todos.

Fuente: [Introduction to Claude Tag](../claude-tag/)

## API y Claude Platform

- Llaves en `.env.local`, nunca en el código.
- `response.content` es una **lista de bloques**: iterar y revisar `type`.
- Eval de 20–30 ejemplos y subir **desde Haiku**: el modelo correcto es el más barato que sirve. `response.usage` = la factura.
- Claude **pide** la herramienta, **mi código la ejecuta**; la **descripción** de la herramienta decide si se usa bien.
- `effort` va dentro de `output_config` (low → max); thinking solo donde hay trade-offs.
- Server tools (web search, code execution, web fetch) no necesitan bucle.
- Contexto: just-in-time + compactación del servidor + **prompt caching** + memory tool.
- Bucles de minutos u horas → **Managed Agents** (agent, environment, session, events).

Fuente: [Claude Platform 101](../claude-platform-101/)

## MCP

- **Tools sirven al modelo, resources a la app, prompts al usuario.**
- `mcp dev server.py` abre el Inspector para probar sin app.
- En la API: `mcp_servers` + `mcp_toolset`; para solo lectura, `default_config: {"enabled": false}` y activar herramientas puntuales.
- Si funciona en stdio y falla en HTTP: revisar `stateless_http` y `json_response`.
- Sampling traslada el costo del modelo al cliente (servidores públicos).

Fuentes: [Introduction to MCP](../mcp-intro/) · [MCP Advanced Topics](../mcp-advanced/)

!!! tip "Para recordar"
    - Si algo debe pasar **siempre**, es un hook; si lo explico **dos veces**, es una skill; si aplica **siempre como convención**, va en CLAUDE.md.
    - Revisar el **diff** y la **evidencia**, no el resumen.
    - Empezar simple: una tarea recurrente de esta semana, probarla, iterar.

## Fuentes y aviso legal

- **Fuente:** cursos de Anthropic Academy (Claude Academy). Sitios oficiales: [anthropic.com/learn](https://www.anthropic.com/learn) · [docs.anthropic.com](https://docs.anthropic.com).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por Anthropic. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../aviso-legal.md).
