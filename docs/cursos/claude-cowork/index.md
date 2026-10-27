# Claude Academy · Introduction to Claude Cowork

Curso de Anthropic (14 lecciones, ~2,5 h y un quiz) sobre Cowork: **delegar trabajo completo** a Claude (planear, ejecutar y entregar) sobre carpetas, conectores, navegador y Microsoft 365, con instrucciones globales, proyectos, skills y plugins, trabajando de forma segura y compartiendo con el equipo.

**Estado:** Completado · **Quiz final:** 10/10 (100 %) · **Insignia:** emitida el 27 oct 2026

[Ver insignia verificable](https://academy.claude.com/badges/a950f135-7649-41c4-91c3-2543d898e512){ .md-button }

![Insignia Introduction to Claude Cowork](evidencias/01-insignia-claude-cowork.jpg)

## Módulo 1 · Conocer Cowork

- **Delegar, no solo conversar.** Chat es para pensar turno a turno; Cowork recibe un resultado descrito, planea, ejecuta los pasos con archivos y herramientas y entrega el entregable. Code es para construir software en un repositorio.
- **Anatomía de una tarea Cowork:** archivos locales + varias herramientas + varios pasos + un entregable real. Ejemplo: "¿qué decidimos sobre precios el trimestre pasado? Revisa notas, correos, Slack y decks y escríbeme un resumen de una página para el comité".
- **Tres patrones** que encajan: tareas de **varios pasos**, tareas sobre **archivos reales** (lee, edita y guarda en el formato que necesito) y tareas que **cruzan herramientas** (correo, calendario, chat, CRM).
- Funciona en escritorio, web y móvil; el **escritorio** es el que abre y guarda archivos del equipo. Desde web o móvil llega a los conectores, no a las carpetas locales, y la tarea se queda donde empezó.

### Configuración

- **Carpeta de trabajo:** elegir la **más pequeña** que contenga lo necesario; ahí Claude lee **y escribe**. Una carpeta no es lo mismo que adjuntar archivos: los resultados vuelven a la misma carpeta.
- **Conectores:** correo y calendario, mensajería, almacenamiento en la nube y CRM/gestión de proyectos; se activan o desactivan por tarea. Muchos conectores de nube (Drive, M365 por defecto) son solo de lectura y búsqueda.
- **Permisos:** *Ask before acting* (por defecto: pide confirmación antes de enviar, publicar o compartir) y *Act without asking* (solo con herramientas y tareas de confianza). En ambos modos **siempre pide permiso antes de borrar** archivos de forma permanente.

### Delegar la primera tarea

Un buen prompt de Cowork nombra:

1. **El entregable** (formato y extensión: "un memo de cuatro páginas", "una lista ordenada con notas").
2. **Los insumos** (qué carpeta, canales, fechas, aplicaciones).
3. **Los matices** que Claude no puede adivinar (audiencia, objetivo, "empieza por la recomendación", "marca lo que no se pueda verificar").

Después: responder sus **preguntas aclaratorias** (cierran huecos antes de empezar), **corregir el rumbo a mitad de tarea** sin esperar a que termine y **revisar el entregable** como el borrador de un colega: ¿cumple el objetivo?, ¿los datos son correctos?, ¿algo parece inventado? Si está casi bien, pedir cambios en vez de regenerar.

### Tareas programadas y trabajo remoto

- `/schedule` convierte una tarea (mejor si ya la hice una vez y salió bien) en una recurrente: cada hora, diaria, días hábiles o manual.
- Si solo usa conectores, corre en remoto aunque el equipo esté apagado; si necesita archivos locales, la app debe estar abierta (si no, la retoma al volver y avisa del retraso).
- Ideas: revisión del viernes, consolidado mensual de métricas, briefing matinal de reuniones.

## Módulo 2 · Hacer Cowork propio

| Bloque | Qué aprende Claude | Qué se desbloquea |
|--------|--------------------|-------------------|
| **Instrucciones globales** | Quién soy y cómo trabajo | Cada sesión arranca calibrada a mi rol, formatos y preferencias |
| **Proyectos** | El contexto de un frente de trabajo | Trabaja como alguien del equipo: archivos, historial y decisiones |
| **Skills** | Cómo se hace un proceso específico | Ejecuta la tarea como la haría el equipo (plantillas, estándares, pasos) |
| **Plugins** | La experiencia de un rol o área | Pasa de generalista a especialista |

- **Instrucciones globales:** rol, siglas y jerga, formato de entrega. Las correcciones que repito ("conclusión primero", "sin coma de Oxford") son candidatas.
- **Proyectos:** instrucciones propias, **tareas programadas**, **contexto** (carpetas y enlaces) y **memoria** que Claude construye solo con las conversaciones del proyecto. Buenos candidatos: una cuenta de cliente, un entregable recurrente, un lanzamiento.
- **Skills:** carpeta con `SKILL.md` (instrucciones), *assets* (logos, plantillas), *references* (ejemplos de buen resultado, guías de estilo) y *scripts* (cálculos que deben salir siempre igual). Se activan solas cuando la tarea coincide. Se crean conversando con Claude y se ajustan pidiéndole correcciones.
- **Plugins:** paquetes de skills + conectores + subagentes alrededor de un trabajo. Dos formas: **proceso de punta a punta** (p. ej. cierre mensual) o **caja de herramientas del equipo** (p. ej. legal: revisión de NDA, resumen de contratos, biblioteca de cláusulas). Se instalan en *Customize → Plugins*, se personalizan con ejemplos propios y `/setup-claude` recomienda uno según mi trabajo.

## Módulo 3 · Claude donde trabajo

- **Claude in Chrome** es el puente para herramientas **sin conector**: dashboards internos, portales de proveedores, apps detrás de un login, investigación de varias pestañas. Claude no inicia sesión por mí: trabaja en la sesión que ya tengo abierta. Pide permiso antes de acciones sensibles.
- **Claude para Microsoft 365:** complemento dentro de Excel (fórmulas, `#REF!`, escenarios), PowerPoint (respeta el patrón de diapositivas, gráficos nativos), Word (comentarios y control de cambios) y Outlook (triage y respuestas con contexto). Una conversación lleva el contexto de una app a otra (Outlook → Word → Excel → PowerPoint).
- **Regla:** Cowork cuando el trabajo junta muchas fuentes y termina en un entregable; M365 cuando estoy dentro del archivo editando en sitio.

## Módulo 4 · Seguridad y equipo

**Trabajar seguro:**

- Carpeta **dedicada**, nunca Documentos o Descargas completas; **copia de respaldo** de lo irremplazable; probar flujos nuevos sobre **copias**.
- Verbos destructivos **explícitos** ("quita la sección del borrador, pero conserva el archivo"), **límites** en el prompt ("solo los 3 archivos más recientes", "no le escribas a nadie, solo borrador") y tareas programadas en modo **borrador** al principio.
- Leer el plan, vigilar desvíos de alcance y **leer cada confirmación** antes de aprobarla.
- No usarlo para flujos regulados que exigen auditoría (la actividad de Cowork no queda en los logs de auditoría; la Compliance API solo en Enterprise), ni para lo que no dejaría sin supervisión a un colega nuevo, ni con datos personales sensibles fuera de lo aprobado por TI.

**Validar skills con evals:** skill-creator genera prompts realistas y compara la salida **con skill vs. sin skill**. Revisar cada par, dar feedback concreto ("el tono es muy formal", "falta el resumen ejecutivo"), cambiar **una cosa a la vez** y repetir. El listón: los casos importantes salen claramente mejor que la línea base.

**Compartir con el equipo:** el plugin se publica en el **marketplace privado** de la organización con un nivel de instalación: *Available*, *Installed by default*, *Required* u *Hidden*. Buenas prácticas: **un dueño** por plugin, **evals antes de cada publicación**, **nombres específicos** (`sales-customer-renewal-prep`, no `meeting-prep`) y revisión trimestral.

!!! tip "Para recordar"
    - **Chat para pensar, Cowork para delegar, Code para construir software.**
    - Prompt de delegación = **entregable + insumos + matices**. Si falta algo, Claude pregunta.
    - Corregir el rumbo **a mitad de tarea** es barato; no esperar a que termine para regenerar.
    - Carpeta mínima, respaldo de lo irremplazable y modo *Ask before acting* para todo lo que envía o comparte. **Borrar siempre pide permiso.**
    - Instrucciones globales → proyectos → skills → plugins: cada capa hace que el siguiente entregable salga mejor y más rápido.
