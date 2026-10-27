# 02 · Proyectos, artefactos y skills

**Lecciones:** Introducción a proyectos · Crear con artefactos · Trabajar con skills · **Estado:** Completado

## Proyectos

Espacios autocontenidos con su propio historial de chats, **base de conocimiento** e **instrucciones**. Sirven para trabajo continuo, no para preguntas sueltas.

- **Cuándo crear uno:** material de referencia que se reutiliza, requisitos de respuesta constantes (tono, plantilla, citar fuentes) o trabajo en equipo sobre la misma base.
- **Crear:** *Projects > + New Project* → nombre y descripción (la descripción no la ve Claude) → visibilidad.
- **Instrucciones:** contexto, proceso, tono y requisitos. Se aplican a todos los chats del proyecto y pueden automatizar flujos ("cuando suba una transcripción, resúmela con esta plantilla").
- **Conocimiento:** PDF, DOCX, CSV, TXT, HTML o Google Drive. Nombrar los archivos de forma descriptiva ("Q4-2025-Sales-Report.pdf"), porque Claude usa los nombres para recuperar.
- **Escala con RAG:** cuando el conocimiento se acerca al límite de contexto, Claude busca y trae solo lo relevante, ampliando la capacidad hasta **10x**.
- Lo que se sube dentro de un chat queda fuera del conocimiento del proyecto; el contexto no se comparte entre chats salvo que esté en la base.
- **Permisos (Team/Enterprise):** *Can view* (leer y chatear), *Can edit* (modificar instrucciones, conocimiento y miembros) y *Owner* (controla todo y la visibilidad).

## Artefactos

Los **entregables** creados con Claude (documento, deck, diseño, dashboard, prototipo) en una ventana junto a la conversación. Se guardan en la pestaña **Artifacts**, independientes del chat que los creó.

| Tipo | Para qué | Exporta a |
|------|----------|-----------|
| **Claude Design** | Landing pages, one-pagers, mockups y prototipos; edición en lienzo y design system propio | .pptx, .pdf, .html |
| **Claude Slides** | Presentaciones a partir de notas o informes; se editan y se presentan sin salir de Claude | .pptx, Google Slides, .pdf |
| **Claude Docs** | Documentos vivos, coedición en tiempo real, comentarios y gráficos desde conectores (instantánea, no en vivo) | Google Docs, .docx |
| Artefacto genérico | Gráficos, diagramas de flujo, páginas interactivas, código | — |

- Se distinguen de la **creación de archivos** (Word, Excel, PowerPoint, PDF descargables): el artefacto se abre y actualiza en Claude y se comparte por enlace.
- Tres formas de cambiarlo: **editar directo**, **comentar** sobre el elemento exacto (en Docs, @Claude responde explicando el cambio) o **pedirlo** en la conversación.
- **Compartir:** privados por defecto. Por persona con permiso de ver, comentar o editar. En Pro/Max, privado o "cualquiera con el enlace". En Team/Enterprise los enlaces se quedan en la organización salvo que el Owner active el compartido externo.
- **Consejos:** pedir el entregable y no solo el contenido; ser específico; describir al usuario final; crear el artefacto al final de la conversación, cuando Claude ya entiende el problema; pedir que refresque los datos de los gráficos.

## Skills

Carpetas de **instrucciones, scripts y recursos** que Claude carga dinámicamente para hacer una tarea especializada de forma repetible.

- **Skills de Anthropic:** creación de Excel, Word, PowerPoint y PDF; se invocan solas.
- **Skills personalizadas:** flujos propios (lineamientos de marca, formato de actas, análisis de varianza trimestral, checklist de cumplimiento).
- **Activar:** *Settings > Capabilities* → *Code execution and file creation* activo → *Customize > Skills*. Requieren el sandbox de ejecución.
- **Crear conversando:** decirle a Claude qué skill quiero → responder su entrevista → subir plantillas o ejemplos → **Save skill**. Si no aparece, descargar el archivo y subirlo en *Customize > Skills > Add > Upload skill*.
- **Seguridad:** pueden ejecutar código; instalar solo de fuentes confiables y revisar su contenido.
- Con archivos subidos en Chat, Claude crea una **versión nueva**, no edita el original.

| | Proyectos | Skills |
|---|-----------|--------|
| Propósito | Guardar conocimiento | Definir procesos que Claude ejecuta |
| Ideal para | Contexto de largo plazo, referencia, equipo | Flujos repetibles, tareas de varios pasos, metodología consistente |
| Persistencia | En todos los chats del proyecto | Cuando se invoca la skill |

!!! tip "Para recordar"
    - **Proyecto = el qué (información); skill = el cómo (proceso).** Se complementan: una skill puede usar el conocimiento de un proyecto.
    - Nombres de archivo descriptivos y conocimiento actualizado; documentos viejos dan respuestas viejas.
    - Pide "**un one-pager para el comité**", no "resume los resultados": así obtienes un artefacto que se comparte y se sigue editando.
    - RAG en proyectos: hasta **10x** de capacidad sin perder calidad.
