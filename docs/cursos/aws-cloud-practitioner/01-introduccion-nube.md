# Módulo 1 · Introducción a la nube

Curso *AWS Cloud Practitioner Essentials (Español LATAM)* de AWS Skill Builder. Lo dictan Anabel Montero, César Mendoza y Aldo Zúñiga, con la analogía de una **cafetería** que se repite en todo el curso. Ruta de AWS Entrena Bogotá.

## Modelo cliente-servidor

- El **cliente** (el consumidor) hace una solicitud. El **servidor** (el barista) la valida y responde con lo pedido. En AWS, el barista sería un **servidor virtual**.
- La computación en la nube **no reemplaza** este modelo: funciona dentro de él, ofreciendo servidores remotos y escalables a los que se accede por Internet.
- **Pagar solo por lo que se usa:** a los baristas se les paga solo por las horas que trabajan. Contratar 10 baristas para todo el día por un lanzamiento deja gente ociosa en las horas flojas, que es justo lo que pasa en un centro de datos propio. En AWS se aprovisiona cuando se necesita y se desaprovisiona apenas sobra, y en ese momento se deja de pagar.

## ¿Qué es la computación en la nube?

- **Historia:** Amazon.com estandarizó herramientas para escalar su propio sitio. En 2003 vio que eso le servía a otras empresas.
  - **2004:** primer servicio público, **Amazon SQS**.
  - **2006:** **Amazon S3** y **Amazon EC2**.
  - Hoy AWS tiene más de 300 servicios y millones de clientes.
- **Definición:** la computación en la nube es la **entrega bajo demanda de recursos de TI a través de Internet con precios de pago por uso**.

| Parte de la definición | Significado |
|---|---|
| **Bajo demanda** | Recursos en segundos, cuando se necesitan; se escalan sin procesos largos de aprovisionamiento |
| **Recursos de TI** | Servidores, almacenamiento, bases de datos, redes, IA/ML… |
| **A través de Internet** | Acceso remoto desde cualquier lugar, sin mantener hardware propio |
| **Pago por uso** | Se paga lo consumido, sin contratos fijos a largo plazo |

### Tipos de implementación

| Tipo | Cuándo se usa |
|---|---|
| **Nube** | Todo en la nube: migrar lo existente, crear aplicaciones nuevas o ambas |
| **En las instalaciones** (*on-premises*) | Virtualización en centro de datos propio. Casi no da los beneficios de la nube, pero ofrece recursos dedicados y baja latencia |
| **Híbrida** | Nube e instalaciones propias conectadas. Útil cuando sistemas heredados o regulados deben quedarse en casa. Las implementaciones **multinube** también cuentan como híbridas |

*Ejemplo:* una organización con datos que por cumplimiento no pueden salir del país, pero que necesita escalar en temporada alta, usa una implementación **híbrida**.

## Los seis beneficios de la nube de AWS

1. **Gastos variables en lugar de gastos fijos** (inversión inicial). Las facturas cambian según el consumo y se puede empezar pequeño.
2. **Economías de escala masivas.** AWS compra hardware en volumen y traslada el menor costo a los clientes.
3. **Dejar de adivinar la capacidad.** Si se calcula hardware para 10 millones de usuarios y llegan 500 000, se desperdicia; si se subestima, se pierden clientes. En la nube se escala en minutos.
4. **Más velocidad y agilidad.** Se crean entornos de prueba, se experimenta y se borra lo que no funcionó.
5. **Dejar de gastar en operar y mantener centros de datos.** Menos tiempo en montar y alimentar servidores; más tiempo para los clientes.
6. **Global en minutos.** Expandirse, por ejemplo de EE. UU. a India, usando una región de AWS en lugar de construir un centro de datos.

## Infraestructura global

- **Alta disponibilidad:** la aplicación sigue accesible aunque falle un componente.
  - Analogía: si se derrama un latte sobre la caja y una tienda cierra, la cadena tiene otras sucursales a pocas cuadras.
- **Tolerancia a errores:** el sistema sigue operando aunque fallen **varios** componentes; hay resiliencia en cada capa.
- **Región:** ubicación física con grupos de centros de datos. Ejemplos: Querétaro, São Paulo, Virginia, Tokio, España. Cada región tiene **mínimo tres zonas de disponibilidad**.
- **Zona de disponibilidad (AZ):** uno o más centros de datos con energía, red y conectividad redundantes. Las AZ están separadas por decenas de kilómetros: suficiente para que un desastre no afecte a varias, pero con latencia despreciable entre ellas.
- **Buena práctica:** distribuir los recursos en **varias AZ**. Para estar a prueba de desastres, también en **varias regiones**.

## Modelo de responsabilidad compartida

- **AWS = seguridad *de* la nube:**
  - capa física (hardware, instalaciones);
  - red;
  - hipervisor (virtualización).
- **Cliente = seguridad *en* la nube:**
  - **sus datos** y quién accede a ellos;
  - **cifrado del lado del cliente**;
  - sistema operativo y parches;
  - aplicaciones.
- AWS **no tiene acceso** al sistema operativo del cliente. Si descubre una vulnerabilidad puede avisar, pero no aplicar el parche.
- **Analogía:** el constructor hace paredes y puertas sólidas; el dueño cierra la puerta con llave.
- **Responsabilidades que varían según el servicio:**
  - cifrado del lado del servidor;
  - protección del tráfico de red;
  - administración de la plataforma y las aplicaciones;
  - configuración del SO, la red y el *firewall*.

## La nube en la vida real

Una tienda en línea de Seattle quiere clientes en Europa y Asia:

- Despliega en **eu-west-1 (Irlanda)** y en Singapur, más cerca de los usuarios, lo que reduce la latencia.
- Usa **dos AZ** en cada región para tener alta disponibilidad y tolerancia a errores.
- No se ocupa de la seguridad física de esos centros de datos. Se concentra en proteger y cifrar sus datos y en cumplir normas como las de tarjetas de crédito.

!!! tip "Para recordar"
    - Definición exacta: **entrega bajo demanda de recursos de TI por Internet con pago por uso**.
    - Híbrida = parte en casa (cumplimiento, sistemas heredados) y parte en la nube (escalado).
    - Región ≥ **3 AZ**; AZ = **1 o más centros de datos** redundantes.
    - Beneficios de la infraestructura global: **alta disponibilidad** y **tolerancia a errores**.
    - Parches del SO y cifrado del cliente → **cliente**. Seguridad física y hardware → **AWS**.

## Fuentes y aviso legal

- **Fuente:** curso *AWS Cloud Practitioner Essentials* (AWS Skill Builder), ofrecido en AWS Entrena Bogotá. Sitios oficiales: [skillbuilder.aws](https://skillbuilder.aws) · [bogota.awsentrena.com](https://bogota.awsentrena.com) · [docs.aws.amazon.com](https://docs.aws.amazon.com).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por AWS. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../aviso-legal.md).
