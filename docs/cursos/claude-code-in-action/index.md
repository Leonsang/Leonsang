# Claude Academy · Claude Code in Action

Curso de Anthropic (9 lecciones, ~1 h y un quiz) sobre Claude Code en modo avanzado y sin supervisión: sesiones largas, un CLAUDE.md que se cumpla, skills de verificación, modos de permiso, hooks, rutinas y modo headless, GitHub Actions y Code Review, verificar ejecuciones desatendidas y plugins.

**Estado:** Completado · **Quiz final:** 8/8 (100 %) · **Insignia:** emitida el 29 oct 2026

[Ver insignia verificable](https://academy.claude.com/badges/f3bd2e65-d980-49f9-b6fe-e94e6cef89a5){ .md-button }

![Insignia Claude Code in Action](evidencias/01-insignia-claude-code-in-action.jpg)

## Sesiones largas

- **Acotar antes, guiar durante.** Plan mode primero y **leer el plan de verdad**: iterar un plan es mucho más rápido que limpiar después.
- `/compact <instrucciones>` dirige qué conserva el resumen ("enfócate en la implementación del flag --version").
- **Rewind** (Esc dos veces): restaurar código y conversación, solo conversación o solo código; *Summarize from here* y *Summarize up to here* para liberar contexto sin perder lo importante.
- `/goal <condición>`: Claude sigue trabajando hasta que un evaluador confirma la condición ("todas las pruebas de src/billing pasan y el type checker da cero errores"). El evaluador solo lee la transcripción, así que la condición debe verse en la salida. `/goal clear` la cancela.
- `/loop`: repite un prompt en un intervalo fijo o autoajustado para vigilar algo externo (CI, despliegue).
- **Worktrees** para trabajo en paralelo: cada sesión con su propio árbol de archivos; `.worktreeinclude` copia archivos ignorados por git (p. ej. `.env`) a cada worktree.

## Un CLAUDE.md que se cumpla

- Es **guía, no configuración forzada**: cada línea compite con las demás. Cuanto más corto, más se cumple.
- Las reglas duras ("nunca hagas push a main") van en un **hook PreToolUse**, que sí bloquea.
- Cuatro ubicaciones que se suman: **política gestionada** (organización), **usuario**, **proyecto** (en el repo) y **local** (ignorado por git, solo para mí en ese repo).
- Los imports `@.claude/conventions/testing.md` **organizan**, pero no reducen contexto: se expanden al inicio.
- Redactar reglas **específicas y verificables** ("rutas nuevas en `src/api/handlers`, una por archivo"), **nombrar el reemplazo** ("usa exports con nombre, no default") y tratar el énfasis (IMPORTANT, YOU MUST) como un **presupuesto** para 2 o 3 reglas.
- Cada error de Claude es un **bug report contra el CLAUDE.md**; si una línea no se justifica, se borra.

## Skills de verificación

- La primera skill que vale la pena: al terminar un cambio, **corre las pruebas, lee el diff, confirma que ninguna prueba se debilitó** y reporta pasa/falla con evidencia, sin que yo lo pida.
- Mantener `SKILL.md` corto; el detalle va en `reference.md` y las herramientas en scripts (p. ej. `check.sh`), que se ejecutan sin cargarse al contexto.
- Si escribí dos veces la misma instrucción de varios pasos, es una skill.

| Dónde va | Qué |
|----------|-----|
| CLAUDE.md | Convenciones que aplican siempre |
| Skill | Procedimientos y referencias de un tipo de tarea |
| Hook | Lo que Claude **no** puede saltarse |

## Modos de permiso

| Modo | Qué corre sin preguntar |
|------|-------------------------|
| Manual | Solo lecturas |
| Accept edits | Lecturas, ediciones y comandos comunes del sistema de archivos |
| Plan | Investiga y propone sin editar |
| **Auto** | Todo, con un clasificador que revisa la mayoría de acciones antes de ejecutarlas |
| Don't ask | Lecturas y herramientas preaprobadas; lo demás se niega solo (para CI y jobs nocturnos) |
| Bypass permissions | Nada se revisa; solo dentro de un contenedor o VM aislado |

- El clasificador de auto bloquea despliegues y migraciones a producción, *force push*, ejecutar código descargado, enviar datos sensibles afuera y borrar archivos previos. Revisa **intención, no corrección**: por eso se combina con un **Stop hook que corre las pruebas**.

## Hooks a fondo

- ~30 eventos; los clave: `PreToolUse` (el primitivo para hacer cumplir), `PostToolUse` (formatear, lint), `Stop`/`SubagentStop` (decir "aún no terminas"), `PreCompact`/`PostCompact`, `InstructionsLoaded` y `SessionStart`.
- `PreToolUse` puede responder JSON con `permissionDecision`: `allow`, `deny` o `ask`; y con `updatedInput` **reescribir** la llamada (p. ej. redactar un secreto `sk_live_` y dejar que el comando corra). `updatedInput` reemplaza todo el objeto: hay que devolver también los campos que no cambian.
- Códigos de salida: **0** éxito; **2** bloquea y stderr vuelve a Claude; cualquier otro (incluido **1**) **no bloquea**.
- Para reinyectar contexto tras compactar: `SessionStart` con el matcher `compact`, no `PostCompact`.

## Rutinas, headless y Agent SDK

| Opción | Cuándo |
|--------|--------|
| **Rutinas** (claude.ai/code/routines o `/schedule`) | Trabajo repetido en la nube de Anthropic: cron (máximo cada hora), POST HTTP o evento de GitHub; parten de un clon limpio y empujan a una rama `claude/` |
| **Headless** `claude -p` | El trabajo necesita mi entorno o lógica alrededor; se encadena con pipes |
| `--bare` | CI con la misma configuración en todas las máquinas (sin hooks, skills, plugins, MCP ni CLAUDE.md; requiere `ANTHROPIC_API_KEY`) |
| **Agent SDK** (TypeScript/Python) | Claude Code dentro de mi propio producto (`query`, `allowedTools`, system prompt, modo de permiso) |

- Salida estructurada: `--output-format json --json-schema '…'` y leer `.structured_output` con `jq`. Sesiones de varios pasos con `--resume` y el `session_id`.

## GitHub: Code Review y la Action

- **Code Review** (gestionado, Team/Enterprise): la app de GitHub revisa cada PR contra todo el código y publica comentarios en línea por severidad. **Nunca aprueba ni bloquea** y no empuja arreglos.
- **claude-code-action@v1** para lo que va más allá de revisar: implementar desde un comentario `@claude`, reportes programados. Se configura con `/install-github-app`; entradas clave: `anthropic_api_key`, `trigger_phrase`, `prompt` (ejecución automática), `claude_args` (`--max-turns`, modo de permiso, herramientas permitidas) y `use_bedrock`/`use_vertex`/`use_foundry`.

## Verificar ejecuciones sin supervisión

- **Cuanto menos lo vi, más verifico.** Desatendido: modo auto, no bypass.
- Empezar por el **diff**, no por el resumen (`/code-review` y `git diff`).
- Las pruebas como **compuerta**, no como promesa: Stop hook que corre pruebas y PostToolUse con lint y type check; con exit 2 Claude ve el fallo y lo arregla.
- **Segunda opinión en frío**: una sesión o subagente nuevo, sin memoria de cómo se construyó.

## Plugins

- Una unidad instalable con skills, subagentes, hooks, servidores MCP y más. `/plugin install nombre@marketplace`; para equipos, `/plugin marketplace add org/repo`.
- **Leer antes de instalar**: corre código con mis privilegios y sus hooks se **suman** a los míos. Que esté listado no significa que sea confiable.
- Empaquetar mi `.claude`: misma estructura de carpetas y un manifiesto opcional `.claude-plugin/plugin.json` (solo `name` es obligatorio; los skills quedan como `/plugin:skill`).

!!! tip "Para recordar"
    - CLAUDE.md corto y verificable; **lo que no se puede saltar va en un hook**.
    - Exit **2** bloquea; exit **1** no.
    - Auto mode cuida la **intención**; las pruebas en un Stop hook cuidan la **corrección**.
    - Empezar por rutinas; bajar a `-p`, `--bare` o el Agent SDK solo cuando el trabajo lo pida.
    - Verificar en proporción a cuánto se dejó correr solo: diff, pruebas como compuerta y segunda opinión en frío.

## Fuentes y aviso legal

- **Fuente:** cursos de Anthropic Academy (Claude Academy). Sitios oficiales: [anthropic.com/learn](https://www.anthropic.com/learn) · [docs.anthropic.com](https://docs.anthropic.com).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por Anthropic. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../aviso-legal.md).
