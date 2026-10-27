# 01 · Conocer a Claude

**Lecciones:** Qué es Claude · Tu primera conversación · Obtener mejores resultados · Cómo trabajarás con Claude en el escritorio · **Estado:** Completado

## Qué es Claude

- Asistente de IA pensado como **compañero de pensamiento**, no como caja de búsqueda. Una pregunta de dato puntual (tasa de cambio de hoy) la resuelve un buscador; lo que necesita razonar contigo es trabajo para Claude.
- Entrenado con **IA Constitucional**: principios para evitar contenido dañino o discriminatorio y comportarse de forma segura y transparente.
- Es **dirigible**: acepta instrucciones de personalidad, tono y comportamiento.
- Fortalezas: redacción, investigación y análisis (ventana de contexto de 200K+ tokens, hasta 1M en planes pagos con modelos compatibles), código, razonamiento (modo **Thinking**) y aprendizaje (modo **Learning**, que guía en vez de dar la respuesta).
- Superficies: claude.ai (web, escritorio, móvil), Claude Code, Claude Tag (Slack), Claude Design y Claude para Microsoft 365. Conversaciones, proyectos, memoria y preferencias se sincronizan entre dispositivos.

## Primera conversación

**Estructura de un buen prompt** (adaptada del marco 4D de AI Fluency):

| Elemento | Pregunta | Ejemplo |
|----------|----------|---------|
| Preparar el escenario | ¿Cuál es mi rol, objetivo y contexto? | "Soy líder de marketing de una startup de streaming y preparo un deck para inversionistas Serie A" |
| Definir la tarea | ¿Qué acción quiero: escribir, analizar, construir? | "Investiga el mercado de streaming independiente: tendencias, competidores, oportunidades" |
| Especificar reglas | ¿Qué formato, tono, ejemplos? | "Con investigación web y citas, como informe de máximo 5 páginas con resumen ejecutivo" |

- **Contexto adicional:** subir archivos (PDF, DOCX, CSV, TXT, imágenes); Claude analiza texto y elementos visuales.
- **Iterar:** preguntas de seguimiento, feedback concreto ("el tono es muy formal"), redirigir o empezar un chat nuevo. El lápiz permite editar y reenviar un mensaje.
- **Personalizar:** *Settings > Account > Instructions for Claude* para preferencias globales; **Memoria** guarda rol, preferencias y decisiones (activa por defecto en Free/Pro/Max; en Team/Enterprise la habilita el Owner); **Skills** para flujos reutilizables.
- **Modelos:** Opus para lo más complejo; Sonnet como predeterminado diario. Thinking extendido mejora el análisis a costa de latencia.

## Obtener mejores resultados

| Problema | Causa | Solución |
|----------|-------|----------|
| Respuesta genérica | Falta contexto | Agregar audiencia, rol y restricciones |
| Muy larga o muy corta | Claude adivina la extensión | Pedirla explícita ("menos de 100 palabras") |
| No siguió el formato | Entendió el qué, no el cómo | Mostrar un ejemplo o describir la estructura |
| Dato seguro pero falso | Alucinación en datos específicos | Verificar, pedir fuentes o nivel de confianza, activar búsqueda web |
| Tono equivocado | Por defecto es profesional y servicial | Describir el tono o dar un ejemplo |

**Mentalidad de iteración:** el primer borrador es un punto de partida; el feedback específico ("quita los dos primeros párrafos y haz la conclusión más accionable") rinde más que "hazlo más corto"; si la conversación se desvió, a veces conviene empezar de cero.

**Marco 4D de AI Fluency** (Dakan y Feller):

- **Delegación:** qué hace la persona, qué hace la IA y cómo se reparte.
- **Descripción:** comunicar bien salidas, procesos y comportamientos esperados.
- **Discernimiento:** evaluar críticamente calidad, precisión y pertinencia.
- **Diligencia:** uso responsable, transparente y con rendición de cuentas.

**Evals sencillos** para decidir si delegar una tarea: reunir 5–10 ejemplos reales ya resueltos, escribir prompts equivalentes, comparar contra lo conocido y refinar. Ejemplo del curso: un director de programa reproduce con IA el análisis del trimestre anterior (asistencia vs. empleo), detecta qué contexto faltaba (tipo de programa) y qué no debe inferir la IA (fechas de inscripción). Validar da confianza, pero **la responsabilidad sigue siendo mía**.

## Claude en el escritorio: tres formas de trabajo

| Voy a… | Forma | Dónde vive |
|--------|-------|------------|
| Preguntar, idear, redactar turno a turno | Trabajar con Claude, ida y vuelta | **Chat** (entrada rápida, dictado, capturas, conectores locales) |
| Delegar algo de varios pasos que termina en un entregable, cruza herramientas o se programa | Delegar el trabajo | **Cowork** (acceso a carpetas, tareas programadas, subagentes, proyectos, navegador, computer use, plugins) |
| Escribir, probar y publicar código | Construir software | Pestaña **Code** (local o nube; modos aprobar manual, aceptar ediciones, plan) |

- En Cowork Claude muestra un plan, deja dirigir en cualquier momento y pide aprobación antes de acciones sensibles (enviar un correo, compartir un archivo).
- Las tareas programadas corren en remoto aunque el equipo esté apagado; si usan archivos locales, la app debe estar abierta.
- En la experiencia nueva de Claude ya no hay Chat y Cowork separados: ambos tipos de trabajo ocurren en cualquier conversación.

!!! tip "Para recordar"
    - Hablarle como a un colega: natural, conciso, conversacional. **Claude aporta inteligencia; yo aporto el contexto y la experiencia.**
    - Contexto + tarea + reglas. Si sale genérico, falta contexto.
    - Antes de delegar algo recurrente, **probarlo con un caso cuya respuesta ya conozco**.
    - Si la tarea tiene varios pasos, deja archivos o se repite, es para **delegar**, no para preguntarla de a pedazos.
