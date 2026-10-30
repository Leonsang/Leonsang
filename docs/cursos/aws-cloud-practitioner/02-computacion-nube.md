# Módulo 2 · Computación en la nube

*AWS Cloud Practitioner Essentials*, módulo 2: Amazon EC2, sus tipos y precios, escalado, balanceo de carga y mensajería.

## Amazon EC2

- **Amazon Elastic Compute Cloud (EC2):** servidores virtuales, llamados **instancias**, que se lanzan en minutos, se detienen o terminan cuando se quiera y se pagan solo **mientras están en ejecución**.
- **Tenencia múltiple (*multitenancy*):** varias instancias comparten el mismo host físico, pero aisladas entre sí. El **hipervisor** se encarga de compartir y aislar, y lo administra AWS.
- El cliente elige el sistema operativo (Windows o Linux), el software, la red (acceso público o privado) y el tamaño. *Elastic* significa que la instancia se puede agrandar o achicar (**escalado vertical**).
- **Lanzar → conectarse → usar:**
  - **Lanzar:** elegir la **AMI** y el **tipo de instancia**.
  - **Conectarse:** por **SSH** (Linux), **RDP** (Windows) o **AWS Systems Manager**.
  - **Usar:** instalar software, agregar almacenamiento y ejecutar comandos.
- **Demostración (servidor web):**
  - nombre, AMI de Amazon Linux, tipo **t2.micro** (1 vCPU, 1 GB, capa gratuita);
  - **par de claves** para iniciar sesión;
  - red que permite HTTP;
  - 8 GB en un volumen **EBS gp3**;
  - **datos de usuario** con un script que instala Nginx al arrancar.

### Imágenes de máquina de Amazon (AMI)

- Plantilla con **sistema operativo**, configuración de almacenamiento, arquitectura, permisos de lanzamiento y software preinstalado.
- Hay tres fuentes: **AMI propias** (personalizadas), **AMI de AWS** preconfiguradas y **AWS Marketplace** (de terceros).
- Garantizan **repetibilidad**: todas las instancias nuevas son idénticas, lo que facilita escalar y reduce errores.

## Tipos de instancias

| Familia | Ideal para |
|---|---|
| **Uso general** | Equilibrio de CPU, memoria y red: servidores web, repositorios de código, cargas inciertas |
| **Optimizadas para computación** | CPU intensiva: servidores de juegos, HPC, ML, modelado científico |
| **Optimizadas para memoria** | Grandes conjuntos de datos en RAM: análisis en tiempo real, bases de datos |
| **Computación acelerada** | Aceleradores de hardware (GPU): punto flotante, gráficos, renderizado, ML |
| **Optimizadas para almacenamiento** | Mucha E/S sobre datos locales: bases grandes, *data warehousing* |

Después se elige el **tamaño**, buscando el equilibrio entre rendimiento y costo. Se puede cambiar cuando haga falta.

## Cómo interactuar con AWS

**Todo es una llamada a la API**, y hay tres formas de hacerla:

| Herramienta | Para quién |
|---|---|
| **Consola de administración** | Interfaz web visual (y app móvil): aprender, pruebas, facturación |
| **AWS CLI** | Comandos en terminal (también **AWS CloudShell**); automatización con *scripts*, menos errores manuales |
| **AWS SDK** | Integrar AWS en código: Python, Java, .NET, C++… |

**Responsabilidad compartida en EC2:** EC2 es un servicio **no administrado**. El cliente configura la seguridad, el **SO invitado** y sus parches, la red y los **grupos de seguridad**, y las aplicaciones.

## Precios de EC2

| Opción | Descuento | Cuándo |
|---|---|---|
| **Bajo demanda** | — | Por hora o segundo, sin compromiso. Para empezar, probar o cuando no se conoce el uso |
| **Savings Plans** | hasta **72 %** | Compromiso de gasto por hora durante 1 o 3 años. Cubre EC2 de cualquier familia y región, además de **Fargate, Lambda** y SageMaker AI |
| **Instancias reservadas** | hasta **75 %** | Cargas estables y predecibles, 1 o 3 años. Se pagan todo, parte o nada por adelantado. El descuento se aplica a otros tamaños de la misma familia y a otras AZ de la región |
| **Instancias de spot** | hasta **90 %** | Capacidad sobrante. AWS puede recuperarla con **aviso de 2 minutos**: solo para trabajos que toleran interrupciones |
| **Hosts dedicados** | — | Un **servidor físico entero** para el cliente, con control de la ubicación. Sirve para licencias (Windows, SQL Server) y cumplimiento |
| **Instancias dedicadas** | — | Hardware aislado de otras cuentas, **sin** elegir el servidor físico |
| **Reservas de capacidad** | — | Garantizan capacidad en una AZ concreta para cargas críticas. Se cobran a tarifa bajo demanda, se usen o no |

## Escalado y elasticidad

- **Escalabilidad:** capacidad de crecer agregando recursos. Es planificación a largo plazo.
  - **Vertical:** una máquina más potente.
  - **Horizontal:** más máquinas.
- **Elasticidad:** ajuste **automático** en tiempo real: escalar horizontalmente con la demanda y reducir cuando baja.
- En la cafetería, una cajera «más grande» no toma pedidos más rápido; hacen falta **más cajeras**. Cada capa (pedidos, preparación) escala **por separado**.
- **Instancias redundantes en varias AZ** eliminan el punto único de falla.
- **Amazon EC2 Auto Scaling:**
  - Agrega o quita instancias según métricas que recoge **CloudWatch**: CPU, latencia y otras.
  - Puede ser **dinámico** (en tiempo real) o **predictivo** (programa la capacidad según la demanda prevista).
  - Un grupo de Auto Scaling define capacidad **mínima** (se lanza al crearlo), **deseada** (la que intenta mantener; por defecto igual a la mínima) y **máxima** (tope de costos).

## Elastic Load Balancing (ELB)

- El **anfitrión** de la cafetería manda a cada cliente a la fila más corta.
- ELB reparte el tráfico entre instancias. Es **administrado** por AWS (parches, conmutación por error), **regional**, escala solo y sirve de **punto único de contacto** para el grupo de Auto Scaling.
- **Desacopla** capas: el *frontend* solo conoce la URL del ELB. Las instancias nuevas del *backend* se registran y empiezan a recibir tráfico sin avisar a nadie.
- **Métodos de enrutamiento:**
  - **Round Robin:** reparte por turnos.
  - **Least Connections:** al servidor con menos conexiones.
  - **IP Hash:** el mismo cliente va siempre al mismo servidor.
  - **Least Response Time:** al servidor que responde más rápido.
- **Auto Scaling + ELB:** Auto Scaling decide **cuántas** instancias hay; ELB **reparte** el tráfico entre ellas.

## Mensajería y colas

- **Acoplamiento ajustado:** si un componente falla, arrastra a los demás (como en un **monolito**).
- **Acoplamiento débil:** con un *buffer* o cola en medio, los componentes siguen funcionando aunque uno falle (como en los **microservicios**).

| Servicio | Modelo | En la cafetería |
|---|---|---|
| **Amazon SQS** | **Cola**: guarda mensajes (la carga útil) hasta que el consumidor los procesa y los borra; no se pierden aunque el consumidor esté caído | El **tablero de pedidos** |
| **Amazon SNS** | **Publicar/suscribir** por **temas**. Entrega inmediata a suscriptores: correo, SMS, *push*, Lambda, HTTP | El barista que **grita** «¡chocolate caliente listo!» |
| **Amazon EventBridge** | **Bus de eventos** sin servidor: dirige eventos de apps, servicios de AWS y SaaS a otros destinos; filtra, transforma y reintenta | Un pedido de comida dispara pago, restaurante, inventario y reparto a la vez |

!!! tip "Para recordar"
    - EC2 = **no administrado**: el cliente parchea el SO y configura los grupos de seguridad.
    - Lanzar una instancia exige **AMI + tipo de instancia** (y almacenamiento).
    - Precios: incierto → **bajo demanda**; estable 1–3 años → **reservadas / Savings Plans**; tolera cortes → **spot**; licencias o control físico → **hosts dedicados**.
    - Simulaciones con GPU → **computación acelerada**; CPU intensiva → **optimizadas para computación**; datos en RAM → **memoria**; E/S local → **almacenamiento**.
    - **SQS** retiene mensajes (*pull*); **SNS** notifica al instante (*push*); **EventBridge** enruta eventos.

## Evaluación del módulo

Resultado: **100 %** (se aprueba con 80 %).

??? note "Preguntas y respuestas correctas"

    **1.** ¿Qué opción describe MEJOR cómo se aprovisionan y administran los recursos de computación en la nube?

    ✔ Los recursos se aprovisionan según la demanda, lo que permite el escalado y la administración.

    **2.** Una empresa de medios está trabajando en un proyecto que implica renderizar simulaciones y efectos visuales complejos. El proceso de renderizado requiere una potencia de computación significativa y aceleradores de hardware para gestionar la intensa carga de trabajo de manera eficiente. ¿Qué tipo de instancia de Amazon EC2 sería la MEJOR opción para esta tarea?

    ✔ De computación acelerada

    **3.** Una startup está creando una nueva aplicación web y elige instancias de Amazon EC2 de uso general para alojar la aplicación. ¿Por qué eligieron este tipo de instancia?

    ✔ Proporciona una combinación equilibrada de recursos de computación, memoria y redes, a la vez que mantiene la eficiencia de los costos a medida que escalan su base de usuarios.

    **4.** Un equipo de investigación universitario está realizando simulaciones de modelos climáticos que requieren una potencia de CPU considerable para procesar algoritmos complejos y analizar grandes conjuntos de datos. ¿Por qué las instancias de Amazon EC2 optimizadas para la computación son ideales para esta tarea?

    ✔ Son ideales para tareas que requieren una potencia de CPU significativa para realizar los cálculos.

    **5.** ¿A qué se refiere la tenencia múltiple en el contexto de Amazon EC2?

    ✔ Varios usuarios comparten la misma instancia de EC2 mientras mantienen el aislamiento

    **6.** ¿Qué herramienta se puede utilizar para interactuar con los servicios de AWS a través de una interfaz gráfica de usuario (GUI)?

    ✔ Consola de administración de AWS

    **7.** Una empresa tiene cargas de trabajo críticas en estado estable y trabajos por lotes que no son urgentes. ¿Cómo deberían optimizar los costos con Savings Plans y las instancias de spot de Amazon EC2?

    ✔ Usar Savings Plans para cargas de trabajo críticas e instancias de spot para trabajos que no sean urgentes a fin de maximizar los ahorros.

    **8.** Una agencia de marketing está desarrollando una nueva aplicación web y espera un crecimiento constante, pero no tiene certeza sobre el tráfico en los primeros meses. Quiere flexibilidad sin asumir un compromiso a largo plazo. ¿Qué opción de precios debería usar?

    ✔ Bajo demanda

    **9.** Una empresa de fabricación ejecutará un conjunto de cargas de trabajo predecibles para los próximos 3 años y quiere optimizar los costos. ¿Qué opción deben elegir?

    ✔ Instancias reservadas

    **10.** ¿Cuál es el rol principal de una imagen de máquina de Amazon (AMI) a la hora de escalar aplicaciones?

    ✔ Proporciona una imagen coherente para lanzar nuevas instancias.

    **11.** ¿Cómo funciona Amazon EC2 Auto Scaling en AWS?

    ✔ Amazon EC2 Auto Scaling agrega o elimina instancias automáticamente según los datos de rendimiento y las métricas de las aplicaciones.

    **12.** ¿Cómo funcionan en conjunto Amazon EC2 Auto Scaling y Elastic Load Balancing (ELB) en AWS?

    ✔ Amazon EC2 Auto Scaling ajusta la cantidad de instancias, mientras que ELB distribuye el tráfico de manera uniforme entre ellas.

    **13.** ¿Qué ocurre si un componente falla en una arquitectura de acoplamiento débil?

    ✔ El sistema puede seguir funcionando ya que los demás componentes son independientes.

    **14.** Una empresa de desarrollo de software debe notificar al equipo de ingeniería cada vez que se informa de un nuevo error en su sistema de seguimiento de errores. Algunos miembros del equipo deben recibir una notificación inmediata, mientras que otros pueden procesar los informes de errores más adelante. ¿Qué servicio debería elegir la empresa de desarrollo de software según los requisitos?

    ✔ Amazon Simple Notification Service (Amazon SNS)

## Fuentes y aviso legal

- **Fuente:** curso *AWS Cloud Practitioner Essentials* (AWS Skill Builder), ofrecido en AWS Entrena Bogotá. Sitios oficiales: [skillbuilder.aws](https://skillbuilder.aws) · [bogota.awsentrena.com](https://bogota.awsentrena.com) · [docs.aws.amazon.com](https://docs.aws.amazon.com).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por AWS. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../aviso-legal.md).
