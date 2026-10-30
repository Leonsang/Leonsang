# Azure Data Factory · Activities & Pipelines

Colección de plantillas JSON y patrones de diseño para actividades estándar en Azure Data Factory (ADF). Cada plantilla contiene la definición nativa de la canalización lista para importar o desplegar mediante ARM/Bicep y Azure DevOps.

---

## 📋 Catálogo de Plantillas de Actividades

| Plantilla | Actividad / Concepto | Propósito |
| :--- | :--- | :--- |
| [`00-simpleCopyData.json`](00-simpleCopyData.json) | **Copy Data Activity** | Copia básica de datos binarios o tabulares entre orígenes y destinos con mapeos automáticos. |
| [`01-eventTriggerSchedule.json`](01-eventTriggerSchedule.json) | **Event-based Triggers** | Desencadenador reactivo ante eventos en Azure Blob / ADLS Gen2 (creación/eliminación de blobs). |
| [`02-filterActivityArray.json`](02-filterActivityArray.json) | **Filter Activity** | Filtrado en memoria de arreglos de metadatos o salidas de actividades previas mediante expresiones ADF. |
| [`03-forEach.json`](03-forEach.json) | **ForEach Loop** | Iteración secuencial o paralela (hasta 50 lotes concurrentes) sobre colecciones de archivos o tablas. |
| [`04-masterChildDependency.json`](04-masterChildDependency.json) | **Execute Pipeline** | Orquestación jerárquica con canalizaciones maestras y dependencias condicionales (Success, Failure, Completion). |
| [`05-metaDataActivity.json`](05-metaDataActivity.json) | **Get Metadata Activity** | Inspección de existencia de archivos, tamaño de blob, lista de particiones y estructura de esquemas. |
| [`06-parameterizedPipeline.json`](06-parameterizedPipeline.json) | **Pipeline Parameters** | Parametrización dinámica para reutilizar un único pipeline en múltiples entornos (Dev, Test, Prod). |
| [`07-set-append-activity.json`](07-set-append-activity.json) | **Set / Append Variable** | Manejo de estado en tiempo de ejecución: contadores de registros, acumuladores y banderas lógicas. |
| [`08-switchActivity.json`](08-switchActivity.json) | **Switch Activity** | Enrutamiento condicional multicamino basado en valores de configuración o tipo de carga de datos. |
| [`09-systemVariables.json`](09-systemVariables.json) | **System Variables** | Uso de `@pipeline().RunId`, `@pipeline().TriggerTime`, `@pipeline().DataFactory` para trazabilidad y auditoría. |
| [`10-untilActivity.json`](10-untilActivity.json) | **Until Loop Activity** | Bucle de espera activa (polling) hasta que una condición externa (API status, lock file) se cumpla. |

---

## 🛠️ Cómo importar en Azure Data Factory Studio

1. En **ADF Studio**, navega a **Author > Pipelines**.
2. Haz clic en el menú contextual de tres puntos (`...`) y selecciona **Pipeline code** o **Import pipeline from JSON template**.
3. Pega el contenido JSON de la plantilla deseada.
4. Vincula tus **Linked Services** (Azure SQL, ADLS Gen2, Databricks, REST API) según corresponda.
5. Valida y publica los cambios.
