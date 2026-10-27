# Claude Academy · Claude Code 101

Curso de Anthropic (12 lecciones, ~1,5 h y un quiz) sobre Claude Code, la herramienta agéntica de programación: cómo funciona, cómo instalarla y los flujos de trabajo diarios (explorar → planear → codificar → commit, contexto, revisión de código, CLAUDE.md, subagentes, skills, MCP y hooks).

**Estado:** Completado · **Quiz final:** 4/4 (100 %) · **Insignia:** emitida el 27 oct 2026

[Ver insignia verificable](https://academy.claude.com/badges/ba748ca0-5d7d-41ec-b2d9-b2b900484eb5){ .md-button }

![Insignia Claude Code 101](evidencias/01-insignia-claude-code-101.jpg)

## Qué es y cómo funciona

- **Agente de IA:** software que interactúa con su entorno y ejecuta acciones para cumplir una meta; un LLM operando **en bucle** con herramientas. A diferencia de Claude.ai, Claude Code tiene acceso directo a archivos, terminal y repositorio: lee el código, edita varios archivos, ejecuta comandos (build, tests, paquetes) y busca en la web.
- **Bucle agéntico:** prompt → reunir contexto → actuar (editar, ejecutar) → **verificar** → terminar o volver a intentar. En cualquier momento puedo interrumpir, agregar contexto o reorientar.
- **Herramientas:** permiten pasar de "texto entra, texto sale" a ejecutar acciones; Claude decide cuándo llamarlas por comprensión semántica.
- **Puede equivocarse:** malinterpretar, introducir bugs o sobrediseñar. Estar en el circuito ayuda a detectarlo temprano.

## Modos de permiso (Shift + Tab)

| Modo | Comportamiento |
|------|----------------|
| **Manual** | Pide permiso antes de cada edición o comando |
| **Auto-accept** | Edita archivos y corre comandos comunes (`mkdir`, `mv`, `rm`) sin preguntar; el resto pide aprobación |
| **Plan** | Lee y explora sin editar el código fuente, hace preguntas y entrega un plan detallado |
| **Auto** | Sin avisos de rutina; un clasificador en segundo plano bloquea lo irreversible, destructivo o fuera del entorno |

Todo se configura en `settings.json`. Saltarse permisos hace más difícil atrapar un error antes de que ocurra.

## Instalación y superficies

- **Terminal:** `curl` en macOS/Linux/WSL; `Invoke-RestMethod` en PowerShell o `curl` en CMD (Homebrew y winget no se actualizan solos). Luego `claude` en la carpeta del proyecto: tendrá acceso a ese directorio y subcarpetas.
- **VS Code / JetBrains:** extensión o plugin oficial de Anthropic.
- **Escritorio:** pestaña *Code*, con carpeta local o entorno en la nube.
- **Web:** claude.ai/code, solo con repositorios de GitHub.
- Las funciones nuevas llegan **primero a la terminal**; el escritorio sirve para dejar a Claude trabajando en segundo plano.

## El flujo clave: Explorar → Planear → Codificar → Commit

1. **Explorar y planear** en *Plan mode*: Claude lee archivos, busca en la web y propone un plan. Es el mejor momento para corregir el rumbo, **antes** de escribir código.
2. **Codificar:** aprobar el plan; definir **criterios de éxito** explícitos, darle herramientas (p. ej. Claude in Chrome para probar UIs) y una **suite de pruebas** confiable.
3. **Commit:** probar yo mismo, pedir una revisión con un **subagente** (ojos frescos, sin el sesgo de la sesión) y generar el mensaje de commit en mi estilo.

## Gestión del contexto

- El contexto es la **memoria de trabajo**: prompts, archivos leídos y resultados de herramientas ocupan espacio. Al acercarse al límite se **compacta** automáticamente (puede perder detalles).
- `/compact` para resumir y seguir en la misma funcionalidad; `/clear` para empezar algo nuevo sin sesgo; `/context` para ver qué ocupa espacio.
- **Ahorrar contexto:** prompts específicos (uno vago obliga a explorar más), desactivar servidores MCP que no se usan y delegar búsquedas a **subagentes** que solo devuelven el resumen.

## Revisión de código

- No confiar solo en el resumen: `/diff` muestra los cambios archivo por archivo. Buscar **cambios no pedidos**, **pruebas debilitadas** (saltadas o aserciones relajadas) y **paquetes nuevos o valores fijos** en el código (URLs, llaves).
- `/rewind` (o Esc dos veces) restaura código y conversación a un prompt anterior; no revierte lo hecho por comandos de shell.
- `/code-review` revisa en un **contexto limpio** y solo reporta. Cada hallazgo va a una de tres pilas: **arreglar ya**, **preguntar por qué** (el revisor también se equivoca) o **dejarlo**. Pedir siempre **evidencia** con cada arreglo ("corre las pruebas y muéstrame la salida").

## CLAUDE.md

- Markdown en la raíz que Claude lee **al inicio de cada sesión**: un guion de onboarding (stack, comandos, estilo de código).
- Nivel **proyecto** (en el repo, compartido) y nivel **usuario** (preferencias personales para todos los proyectos).
- Guardar ahí las correcciones repetidas; referenciar docs con `@README.md`; empezar sin él para ver qué corrige uno siempre y luego generarlo con `/init`.

## Subagentes, skills, MCP y hooks

| Mecanismo | Qué es | Cuándo |
|-----------|--------|--------|
| **Subagente** | Agente con su propio contexto, definido en Markdown + YAML en `.claude/agents/` (proyecto) o `~/.claude/agents/` (usuario) | Exploración o revisión cuyo recorrido no debe ensuciar el contexto principal |
| **Skill** | `SKILL.md` en `.claude/skills/`; solo carga nombre y descripción hasta que coincide con la tarea | Conocimiento por tarea (estándares de PR, formato de commits, marca) |
| **MCP** | Servidores HTTP (remotos) o stdio (locales) añadidos con `claude mcp add`; alcance local, usuario o proyecto (`.mcp.json`) | Datos y herramientas externas (Linear, documentación con Context7) |
| **Hook** | Comando en `settings.json` ligado a un evento (`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `Notification`) | Lo que **debe** pasar siempre: formatear tras editar, registrar comandos, bloquear operaciones peligrosas |

- CLAUDE.md se carga **siempre**; una skill se carga **bajo demanda**; un slash command hay que escribirlo.
- Si existe un CLI equivalente (`gh`, `aws`), gasta menos contexto que un servidor MCP. *Tool search* mantiene fuera del contexto la definición completa de cada herramienta hasta que se necesita.
- En `PreToolUse`, el código de salida **0** deja pasar, **2** bloquea (y stderr vuelve a Claude como feedback), otro código es un error no bloqueante. `CLAUDE_PROJECT_DIR` permite referenciar scripts del repo.

!!! tip "Para recordar"
    - **Explorar → Planear → Codificar → Commit.** Corregir en el plan es más barato que corregir código.
    - `/compact` para seguir, `/clear` para empezar algo nuevo; lo que debe sobrevivir entre sesiones va en **CLAUDE.md**.
    - Revisar el **diff**, no solo el resumen; segunda opinión con `/code-review` en contexto limpio.
    - Si algo debe pasar **siempre, sin excepción**, no va en un prompt: va en un **hook**.
    - Si le explico lo mismo a Claude una y otra vez, eso es **una skill** esperando ser escrita.
