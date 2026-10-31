# Claude Academy · Deploying Claude Enterprise with Confidence

Es un curso de Anthropic con 14 lecciones y un quiz, pensado para quien administra el despliegue de Claude Enterprise, en concreto con el rol **Owner**. No enseña clics, sino **criterio**: las cinco decisiones de todo despliegue, en el orden en que hay que tomarlas. Lo acompaña un plan de despliegue, el *work-along companion*, que se llena lección a lección. El ejemplo que recorre todo el curso es **Pluto**, una fintech ficticia con cinco unidades de negocio, una de ellas regulada (Payments & Trust).

**Estado:** Lecciones leídas · Quiz pendiente

## El marco

**Un objetivo de despliegue con dos mitades:**

1. **Cómo se ve el éxito:** una sola ambición para toda la empresa, concreta.
2. **La restricción que debe cumplirse siempre.**

**El ejemplo de Pluto:**

- **Éxito:** las cinco unidades usan Claude a diario al terminar el trimestre, medido como uso activo semanal por unidad.
- **Restricción:** **ni un solo escalamiento de seguridad** desde Payments & Trust.
- **Cuando chocan:** si una opción acelera la adopción pero arriesga la restricción, se toma el camino lento.

**Las cinco decisiones, en orden** (cada una acota a las siguientes):

| # | Decisión | Pregunta | Dueño típico |
|---|---|---|---|
| 1 | **Estructura e identidad** | ¿Cuántas organizaciones y qué grupos? | Owner + equipo del proveedor de identidad (Okta, Entra ID…) |
| 2 | **Acceso** | ¿Qué superficies y conectores recibe cada grupo? | Owner + líderes de equipo; quien responde por el riesgo firma la escritura |
| 3 | **Gobernanza** | ¿Quién crea y comparte personalizaciones, y con cuánta libertad? | Centro de Excelencia de IA o quien gestiona el cambio |
| 4 | **Gasto** | ¿Dónde van los topes y quién atiende los escalamientos? | **Quien tiene el presupuesto** (p. ej., un delegado del CFO) |
| 5 | **Visibilidad** | ¿Qué se mide y cuánto tiempo se guarda? | **Quien responde por el riesgo de datos** |

**Cómo se trata cada decisión:** con tres pasos.

1. **La decisión.**
2. **Las opciones.**
3. **Qué pasa si se cambia después.**

**Una decisión sin dueño frena el despliegue.**

**Cuatro ajustes difíciles de deshacer:**

1. **Reclamar el dominio:** es **irreversible**.
2. **La topología:** cuántas organizaciones se usan. Fusionar o dividir obliga a reaprovisionar a todos.
3. **El mapeo grupo del IdP → rol:** cambiarlo cambia el acceso de todos los que cubre.
4. **La retención:** lo que se borró con una ventana corta no vuelve.

## Requisitos previos

**Dónde se administra:**

- **Organization settings:** permisos;
- **el proveedor de identidad (IdP):** quién está en cada grupo;
- **Claude Console:** claves de la API, como una organización aparte;
- **los *managed settings* de Claude Code:** los maneja el líder de plataforma.

**Los seis requisitos:**

| Requisito | ¿Bloquea? |
|---|---|
| **Al menos dos Owners asignados directamente**, no por grupo. Es el seguro contra quedar fuera por un error de sincronización | Sí |
| Dominio verificado | Sí |
| IdP conectado y **SSO obligatorio** | Sí |
| App de aprovisionamiento en el IdP | Sí |
| Convención de nombres de grupos | No, va en paralelo |
| Dueño de la facturación identificado | No |

**Primary Owner:** queda **fuera del día a día**. Tiene acciones exclusivas, como exportar datos o ceder el rol.

**Reclamar el dominio (opcional e irreversible):**

- **Qué hace:** trae a la organización las cuentas personales creadas con el correo de la empresa.
- **Requisitos:** dominio verificado, «Restrict organization creation» activado, SSO obligatorio y aprovisionamiento en marcha.
- **Ventana de 30 días:** cada persona elige migrar sus conversaciones o empezar de cero. Si no elige, empieza de cero.
- **Lo que no se transfiere:** las skills propias y las apps conectadas.
- **Hay que avisar antes.**

## 1. Estructura e identidad

**Organización:** es el **límite** de miembros, grupos, configuración y datos. **Las organizaciones no comparten contenido.**

**Una organización, salvo tres casos:**

- **Contratos separados** con Anthropic;
- **proveedores de identidad distintos** que no se pueden unir;
- **aislamiento de datos** exigido por regulación o contrato.

**Separar después es caro:** cuesta menos agregar una organización nueva que dividir una ya consolidada.

**Aprovisionamiento:**

- **JIT:** crea al miembro cuando entra por primera vez. Los grupos se mantienen a mano.
- **SCIM:** sincroniza miembros y grupos desde el directorio, **sin mantenimiento manual**.

**RBAC:**

- **Miembros → grupos → roles.**
- **Tipos de rol:** de administración (Primary Owner, Owner, Admin), de usuario (User) y **roles personalizados**.
- **Qué controla un rol personalizado:** capacidades, acceso a modelos, permisos de conectores y permisos de administración.
- **Solo aplica a quien tiene rol Custom.** Los roles predefinidos reciben todo lo que esté activo.

**Regla de la unión:**

- Si alguien está en dos grupos, **recibe la suma** de lo que dan sus roles.
- **Un grupo más estrecho no quita** lo que da uno amplio.
- **Para un límite estricto:** crear un **grupo dedicado** y sacar a esas personas del grupo amplio.

| Patrón de grupos | Cuándo |
|---|---|
| Espejo del organigrama | Los controles solo varían por departamento |
| Por nivel de riesgo | Una función regulada necesita algo más estricto que su departamento |
| **Híbrido** | Departamentos para lo cotidiano, más un grupo dedicado donde está el límite. Así lo resolvió Pluto con `payments-eng` |

## 2. Acceso

**Superficies (chat, Cowork, Claude Code, Microsoft 365…):** el acceso tiene **dos capas**.

- **El interruptor de la organización** es el techo.
- **La concesión por rol** decide quién lo usa debajo de ese techo.
- **Claude Code** además necesita los límites que fija el líder de plataforma en *managed settings*: archivos, comandos y red.

**Modelos:**

- **Modelo por defecto:** de la organización o por rol.
- **Nivel de esfuerzo por defecto.**
- **Límites:** modelos permitidos y tope de esfuerzo por modelo. Haiku siempre está disponible.
- **El modelo por defecto decide la mayor parte del gasto**, porque casi nadie cambia el selector.

| Estrategia | Cuándo |
|---|---|
| Lo amplio primero y lo especializado donde haga falta | Lo habitual |
| Piloto y después ampliar | El objetivo pide probar con un equipo |
| Gradual, detrás de una revisión | Una restricción obliga a esperar (Pluto: Claude Code para `payments-eng` después de tener los reportes de visibilidad) |

**Dar acceso es barato; quitarlo rompe flujos de trabajo.**

**Conectores: tres puertas, y las tres deben estar abiertas.**

1. **Organización:** la abre un Owner.
2. **Rol:** la abre un Owner.
3. **Miembro:** la persona conecta su cuenta. Con **Enterprise-managed authorization (EMA)** se aprovisiona de forma central desde el IdP.

**Cómo funcionan:**

- **Claude hereda los permisos del miembro** en el sistema conectado.
- **Lectura frente a escritura:** cada herramienta de escritura o borrado puede estar en *Always allow*, *Needs approval* o *Blocked*.
- **Lo común:** solo lectura para los grupos cuyo trabajo vive en ese sistema. La **escritura llega después, con la firma de quien responde por el riesgo**.

## 3. Gobernanza de personalizaciones

**Qué se gobierna:**

- **Skills y plugins:** flujos de trabajo empaquetados;
- **Proyectos:** contexto y archivos compartidos;
- **Instrucciones de la organización:** contexto que va siempre en cada conversación.

**Los riesgos:** proliferación de skills casi duplicadas, flujos sin probar que parecen revisados, y proyectos sensibles compartidos con toda la organización.

**Detalle técnico:** las skills necesitan **ejecución de código** activada en la organización.

**Cuatro controles de distribución:**

- aprovisionamiento por un Owner;
- compartir con personas;
- compartir con grupos;
- **publicación** (*Off*, *Requires review* u *Open*).

| Postura | Cuándo | Ajustes |
|---|---|---|
| **Construcción libre, difusión revisada** | Hay un Centro de Excelencia o un grupo de referentes | Compartir activado; Publishing en *Requires review* |
| Centralizada | Un equipo central ya controla las herramientas internas | Compartir desactivado; Publishing en *Off* |
| Totalmente abierta | Organización pequeña o de mucha confianza | Todo activado; *Open* |

**Ojo al endurecer las reglas:**

- desactivar «Public projects» **vuelve privados** los proyectos existentes;
- un Publishing más estricto **no retira** lo que ya se publicó.

## 4. Gasto

**Topes en tres niveles:**

1. **techo de la organización;**
2. **tope de grupo:** el límite **por miembro** que hereda cada integrante. **No es un fondo compartido**;
3. **excepción por miembro.**

**Cuando alguien está en dos grupos con tope:** un ajuste decide si gana el más alto o el más bajo. Aquí **lo decido yo**, a diferencia de la regla de la unión.

**Al llegar al tope:** el uso **se pausa** y la persona puede pedir más. Aprueban los Owners o quien tenga *Billing* en «Can manage». Las organizaciones grandes suelen pasar esas solicitudes por su sistema de tickets, con la **Spend Limits API**.

**Si las excepciones se multiplican,** esas personas necesitan su propio grupo.

**Niveles de consumo (guía de consumo):** **ligero, estándar y avanzado**, según el tipo de rol. El trabajo con agentes (Claude Code, Cowork) consume más.

**Facturación:**

- una tarifa por puesto más un consumo de tokens agrupado;
- el fondo es de toda la organización, así que **un grupo puede agotarlo para todos** si no tiene tope.

**Palancas que mueven el gasto antes de llegar al tope:**

- un **modelo intermedio por defecto** con un esfuerzo moderado;
- **instrucciones de la organización** que piden respuestas cortas y trabajar solo con los archivos necesarios;
- **skills y proyectos para reutilizar** contexto;
- **hábitos con agentes:** acotar las tareas y borrar las tareas programadas que ya nadie usa.

**Antes de subir un tope:**

- **cuestionar cada aumento** y cada aumento repetido: ¿crece el uso o el tope estaba mal puesto?
- revisar con regularidad **en ambas direcciones**.

**El caso Pluto:** el mes 2, Platform llegó a su tope. La causa era el modelo más caro haciendo resúmenes rutinarios de *pull requests*. **Bajaron el modelo por defecto del rol y dejaron el tope igual.**

**Dónde se lee el gasto:** el panel de análisis, Analytics chat y la Analytics API (que sirve para reconciliar y repartir costos).

## 5. Visibilidad

**Se activa antes de dar acceso:** un periodo sin registro **no se puede reconstruir** después.

| Pieza | Responde | Notas |
|---|---|---|
| **Compliance API** | **Qué se dijo y qué se compartió**: contenido, eventos y archivos, incluidas las sesiones de Cowork y Claude Code | La activa el Primary Owner. Se envía al SIEM o a la revisión de seguridad que ya existe. **Un registro que nadie lee no es un control** |
| Logs de auditoría | Quién hizo qué y cuándo | **Solo metadatos**, sin prompts |
| OpenTelemetry | **Cómo están funcionando** las superficies | Operativo. Puede llevar contenido solo si se activa de forma explícita |
| **Retención** | Cuánto tiempo se guarda el contenido | Por defecto, indefinida. **Mínimo 30 días**, sin opción de cero. **Es una sola para toda la organización:** si un área regulada necesita una ventana más corta, todos reciben esa |

- **Eventos de actividad y transcripciones remotas:** se guardan seis años, sin importar la ventana.
- **Ganchos de inferencia (*inference hooks*):** permiten o bloquean cada prompt **antes** de que llegue a Claude.

**Señales de adopción:** son **diagnósticos, no metas**.

| Señal | Tipo | Si es baja, mirar… |
|---|---|---|
| Miembros activos por grupo | Amplitud | Acceso y conocimiento del producto |
| Miembros que vuelven cada semana | Amplitud | La primera experiencia y las expectativas |
| Chats por miembro activo | Profundidad | Si las superficies y conectores encajan con el trabajo |
| Skills y proyectos en uso | Profundidad | La postura de gobernanza |
| Uso de conectores | Profundidad | El alcance de los conectores |

- **Fijar una meta de ritmo concreta:** «todos los grupos con acceso vuelven cada semana en 8 semanas», no «buena adopción pronto».
- **El caso Pluto:** Ops estaba estancado en un 10 %. Era un problema de **capacitación, no de configuración**.

## Cuando llega un producto nuevo

**Lo que se mantiene:** la organización, los grupos y roles, la gobernanza, los topes y la visibilidad.

**Tres preguntas para cada producto nuevo:**

1. **¿Quién lo recibe?**
2. **¿Qué trae consigo?** Configuración o conectores propios.
3. **¿Cambia el riesgo?** Nuevos datos, más autonomía o personas nuevas frente a Claude. Si es así, se consulta a quien responde por el riesgo.

**El caso Pluto con Claude Tag:**

- **Quién:** lo restringió por rol y solo lo activó en los canales de las unidades que ya trabajan en Slack.
- **Qué trae:** se configura por canal y **se factura a la organización**.
- **Riesgo:** sí lo cambia. Mantuvo bloqueados los canales con invitados (y con eso Slack Connect) y lo dejó apagado para el área regulada.

## Práctica: mi plan de despliegue (empresa ficticia)

Llené el *work-along companion* para **Andina**, una distribuidora ficticia (la misma de mis ejercicios de datos del SENA). Tiene 120 personas en Comercial, Logística, Finanzas y TI. Finanzas maneja datos de pago de clientes.

**Objetivo:** que las cuatro áreas usen Claude cada semana en 90 días, **sin exponer datos de pago fuera de Finanzas**.

| Decisión | Mi respuesta | Por qué |
|---|---|---|
| Estructura | **Una organización** con SCIM. Grupos por área, más `finanzas-pagos` como grupo dedicado. Dos Owners asignados directamente; el Primary Owner con la gerencia | Un solo contrato, un solo IdP y sin aislamiento legal. La regla de la unión obliga a sacar a Finanzas de los grupos amplios |
| Acceso | Chat y Cowork para todos el día 1. Claude Code solo para TI. Drive y wiki en **solo lectura** para todos; el sistema de tickets con escritura solo para TI, con la firma del responsable de riesgo. `finanzas-pagos` sin conectores de escritura | Lo amplio primero. La escritura llega cuando haya un flujo de trabajo que la justifique |
| Gobernanza | **Construcción libre, difusión revisada** (*Requires review*). Finanzas: **aprobar primero**. Instrucciones de la organización: quiénes somos, tono de los textos para clientes y «cita el documento fuente cuando uses material interno» | Hay un equipo de TI pequeño que puede revisar |
| Gasto | Comercial y Logística en nivel ligero, Finanzas en estándar, TI en avanzado. Modelo intermedio por defecto con esfuerzo moderado. Revisión semanal el primer mes y mensual después | Sin historial de uso: **topes bajos que se suben con evidencia** |
| Visibilidad | Compliance API activa **antes** de dar acceso, enviada al responsable de seguridad. Retención alineada con la política de datos de Finanzas, que manda sobre toda la organización | Primero el registro, después el acceso |

**Revisión de los cuatro ajustes irreversibles:**

- **Reclamar el dominio:** sí, después de avisar con 2 semanas.
- **Topología:** una organización.
- **Mapeo grupo → rol:** revisado antes de guardarlo.
- **Retención:** la aprueba el responsable de riesgo.

!!! tip "Para recordar"
    - **Orden:** estructura → acceso → gobernanza → gasto → visibilidad. Cada una acota a la siguiente.
    - **Regla de la unión:** un grupo estrecho no resta. Lo sensible va en su propio grupo.
    - Lectura primero; **escritura con la firma del responsable de riesgo**.
    - Antes de subir un tope, **revisar el modelo por defecto**.
    - **Visibilidad antes del acceso.** La retención corta es irreversible para lo que ya se borró.
    - Las métricas de adopción son diagnósticos, no cuotas.

## Fuentes y aviso legal

- **Fuente:** curso «Deploying Claude Enterprise with Confidence» de Anthropic Academy (Claude Academy) y los artículos del centro de ayuda que enlaza. Pluto y Andina son empresas ficticias. Sitios oficiales: [anthropic.com/learn](https://www.anthropic.com/learn) · [support.claude.com](https://support.claude.com).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por Anthropic. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../aviso-legal.md).
