!!! info "Curso SENA"
    Aplicación de la inteligencia artificial en la integración de datos · ficha 3635322 · octubre de 2026

# AA1-EV02 · Cuestionario sobre el archivo fuente — guía de estudio

**Formato:** 10 preguntas de selección múltiple con única respuesta · 60 minutos · cierra el 8 de noviembre de 2026, 23:59.
**Fuente:** componente formativo *Recolección, tratamiento y visualización de datos para inteligencia artificial* (CF1).

> Esta guía resume el componente para repasar antes de presentar el cuestionario. El cuestionario lo
> responde el aprendiz en Zajuna; aquí no hay respuestas del examen, solo los conceptos que evalúa.

## 1. Dato, información y naturaleza de los datos

- **Dato**: hecho u observación en bruto (cifra, palabra, imagen). **Información**: dato procesado, con contexto y utilidad.
- Ciclo: datos dispersos → limpios en una base de datos → analizados → presentados visualmente → explicados con una historia.

| Estructura | Qué es | Ejemplos |
|---|---|---|
| Estructurados | Filas y columnas, esquema fijo | Bases relacionales, encuestas cerradas |
| Semiestructurados | Estructura flexible con etiquetas o jerarquías; traen metadatos | XML, JSON, YAML |
| No estructurados | Sin esquema ni forma tabular | Texto libre, imágenes, audio, video, redes sociales |

**Tipos de dato:** bits y bytes · enteros · decimales · texto (ASCII/UTF) · fecha y hora · imagen (JPG, PNG) · video (MP4, AVI, MOV) · booleano.

**Características complementarias:** formato (CSV, Excel, JSON) · estructura · origen · volumen · velocidad · veracidad · valor.

## 2. Técnicas de definición de datos

- **Perfiles:** *Data Scientist* (modelos predictivos sobre datos preparados), *Data Analyst* (convierte datos en informes comprensibles), *Data Engineer* (infraestructura para recibir, procesar y organizar).
- **Metadatos:** datos que describen otros datos; eliminan ambigüedades ("son a los datos lo que la etiqueta es al producto").
- **Seguridad:** *anonimización* (elimina identificadores) frente a *seudonimización* (los reemplaza por códigos); *cifrado* en reposo y en tránsito (HTTPS con SSL/TLS).
- **Propiedades del dato:** físicas (dominio/tipo, variabilidad), estructurales (estructura, granularidad, dispersión, medida), funcionales y de exposición (formato, internacionalización, localización).

## 3. Fuentes de información

| Tipo | Definición | Ejemplos |
|---|---|---|
| **Primarias** | Documentos originales, datos de primera mano, sin interpretación | Investigaciones, informes técnicos, estadísticas oficiales, entrevistas, registros |
| **Secundarias** | Analizan, interpretan o sintetizan primarias | Artículos de revisión, libros de texto, ensayos, enciclopedias |
| **Terciarias** | Recopilan y organizan primarias y secundarias para localizarlas | Manuales, catálogos, índices, guías temáticas, bases de datos |

- **Según procedencia:** académicas (revisión por pares, rigor), institucionales, gubernamentales, comerciales, populares (blogs y redes: posible sesgo).
- **Según contenido:** cuantitativo (numérico, medible) o cualitativo (descripciones, opiniones); estructurado o no estructurado.
- **Seis criterios de calidad:** autoridad · exactitud · actualidad · objetividad · cobertura · verificabilidad.

## 4. Principios éticos (Ley 1581 de 2012 en Colombia)

Legalidad · **consentimiento informado** (libre, específico, informado e inequívoco) · finalidad · seguridad · transparencia (acceso, rectificación, cancelación y oposición) · **minimización** (solo los datos estrictamente necesarios).
Riesgos de la IA sin marco ético: sesgos algorítmicos, violación de la privacidad, discriminación.

## 5. Procesamiento y preparación

**Técnicas de limpieza:** eliminación o imputación de faltantes (media, mediana, moda) · corrección de valores erróneos · eliminación de duplicados · **normalización** (rango 0 a 1) frente a **estandarización** (media 0, desviación estándar 1) · conversión de tipos · tratamiento de valores atípicos.

**Preparación para IA:** integrar fuentes, seleccionar variables, tratar faltantes, convertir formatos, transformar variables categóricas.

**Estadística descriptiva**

- Cualitativos (categóricos) y cuantitativos (discretos o continuos).
- Niveles de medición: **nominal** (sin orden) · **ordinal** (con jerarquía) · **intervalo** (sin cero absoluto: °C) · **razón** (con cero absoluto: ingresos).
- Herramientas: histograma (distribución de una variable continua) · tabla de contingencia (dos categóricas) · diagrama de barras · diagrama de caja (mediana, cuartiles, atípicos) · medidas de tendencia central y dispersión · diagrama de dispersión (relación entre dos numéricas).

## 6. Inteligencia artificial aplicada a los datos

| | IA descriptiva | IA generativa |
|---|---|---|
| Objetivo | Analizar y describir datos existentes | Crear contenido nuevo |
| Resultado | Informes, visualizaciones, resúmenes | Texto, imágenes, música, modelos 3D |
| Técnica base | Estadística, minería de datos, ML supervisado | Redes neuronales profundas, GAN, *transformers* |
| Ejemplos | Tableau, Power BI | ChatGPT, DALL·E, MidJourney, GitHub Copilot |

**Hitos:** 1950 Test de Turing · 1956 Conferencia de Dartmouth (se acuña el término) · años 80 sistemas expertos (MYCIN, XCON) · 1997 Deep Blue vence a Kasparov · 2016 AlphaGo · modelos generativos (GPT, BERT, DALL·E).

**Prompt:** entrada o instrucción que se da al modelo. Elementos de un buen prompt: objetivo claro, restricciones (extensión, formato, estilo), rol asignado a la IA, contexto y ejemplos.

## 7. Autoevaluación rápida (preguntas propias de repaso)

1. ¿Un archivo JSON es estructurado, semiestructurado o no estructurado? ¿Por qué?
2. ¿Una enciclopedia es fuente primaria, secundaria o terciaria? ¿Y un catálogo bibliográfico?
3. ¿Qué diferencia hay entre anonimizar y seudonimizar?
4. ¿Qué criterio de calidad se evalúa al revisar la fecha de publicación? ¿Y al revisar si cita referencias?
5. ¿Qué nivel de medición tiene "nivel de satisfacción (bajo, medio, alto)"?
6. ¿Qué gráfico usaría para ver valores atípicos? ¿Y para relacionar dos variables numéricas?
7. ¿Qué principio ético pide recolectar solo lo necesario?
8. ¿Normalizar y estandarizar son lo mismo?

??? note "Respuestas del repaso"

    1. Semiestructurado: tiene etiquetas y jerarquía, pero no esquema tabular fijo.
    2. Secundaria; el catálogo es terciaria.
    3. Anonimizar elimina los identificadores; seudonimizar los sustituye por códigos.
    4. Actualidad; verificabilidad.
    5. Ordinal.
    6. Diagrama de caja; diagrama de dispersión.
    7. Minimización.
    8. No: normalizar lleva los valores a un rango (0 a 1); estandarizar los lleva a media 0 y desviación estándar 1.
