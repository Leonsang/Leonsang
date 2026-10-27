# 03 · Conectores, Enterprise Search y Research

**Lecciones:** Conectar tus herramientas · Enterprise Search · Research para análisis profundos · **Estado:** Completado

## Conectores

Permiten que Claude llegue a las herramientas donde vive el trabajo (la hoja de cálculo, el hilo de correo, el tablero de tareas) en vez de pegar copias. Según los permisos, Claude **busca, lee y actúa** (crear tareas, actualizar registros).

- Funcionan con el **Model Context Protocol (MCP)**: un estándar abierto, "como USB-C para la IA".
- **Conectores web:** servicios en la nube (Gmail, Notion, Slack, Asana, Linear, Stripe…). Un conector puede cubrir varias apps (Atlassian Rovo = Jira + Confluence). Si no existe, se agrega como conector personalizado.
- **Extensiones de escritorio:** corren localmente en la app de escritorio (archivos locales, control del navegador, apps nativas como Figma); se instalan en *Settings > Extensions*.
- **Conectar:** *Customize > Connectors* o **+ > Connectors** → Connect (en Team/Enterprise el Owner lo habilita primero) → iniciar sesión en el servicio → revisar permisos → probar ("¿puedes acceder a mi …?").
- Conectar una fuente no hace que Claude busque por su cuenta: **amplía lo que puedo pedirle**.

**Seguridad:** acceso acotado por conector y permiso; Claude **solo ve lo que yo puedo ver**; se revoca en *Customize > Connectors* o desde el servicio. Igual que con las skills, instalar solo conectores confiables.

## Enterprise Search

Disponible en Team y Enterprise. Agrega un "**Ask {Organización}**" en la barra lateral: un proyecto preconfigurado para toda la empresa que busca y sintetiza conocimiento entre SharePoint, Slack, Gmail, Drive, etc., **siempre con citas**.

- **Usos:** ponerse al día ("¿qué pasó ayer?"), políticas y procesos, investigación interna, onboarding, seguimiento de proyectos.
- **Configuración:** primero el **Owner** (elige un conector de Documentos y uno de Chat; correo opcional; nombre y descripción); luego cada usuario se autentica con sus cuentas.
- Respeta los permisos originales; los datos conectados no se indexan ni se almacenan aparte.

## Research

Convierte a Claude en un **investigador sistemático** (planes pagos). Trabaja de forma agéntica:

1. **Planea** el enfoque (con Thinking) y divide la pregunta.
2. Hace **muchas búsquedas encadenadas** que se construyen entre sí, a veces sobre cientos de fuentes.
3. **Sintetiza** web e integraciones (Gmail, Calendar, Drive) en un informe.
4. Entrega **citas** verificables para cada afirmación.

| Herramienta | Cuándo |
|-------------|--------|
| **Research** | Informes de varias fuentes, comparativos (proveedores, competencia), planeación compleja, briefings con citas |
| **Búsqueda web** | Un dato puntual; una o dos fuentes; la velocidad importa más |
| **Thinking** | Razonamiento profundo sin información externa (matemáticas, depuración, lógica) |
| **Enterprise Search** | Conocimiento interno de la organización |

- **Activar:** botón **+** → Research (requiere búsqueda web; en la experiencia nueva Claude busca cuando hace falta).
- **Buenos prompts:** metas específicas, la estructura de secciones deseada, restricciones (presupuesto, fechas, geografía); se puede pedir a Claude que ayude a afinar el prompt antes de lanzarlo.
- Con integraciones se puede orientar: "trae contexto de mi Google Drive", "incluye lo de mis correos recientes".

!!! tip "Para recordar"
    - **MCP = USB-C de la IA**: un estándar, muchos conectores.
    - Los conectores **heredan mis permisos**: no dan acceso a nada que yo no tenga.
    - Research tarda minutos porque hace muchas búsquedas: invertir en el prompt **vale la pena**.
    - Dato puntual → web; razonar → Thinking; muchas fuentes con citas → Research; lo interno → Enterprise Search.
