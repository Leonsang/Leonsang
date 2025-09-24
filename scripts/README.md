# 🤖 Sistema de Automatización de Documentación

Este sistema detecta automáticamente nuevos archivos `.md` y `.ipynb`, los categoriza inteligentemente y actualiza la navegación de MkDocs.

## 🚀 Funcionalidades

### ✨ Detección Inteligente
- Escanea archivos nuevos no trackeados por Git
- Categoriza automáticamente por contenido y nombre
- Actualiza `mkdocs.yml` con navegación apropiada

### 🗂️ Categorización Automática
- **Fundamentos**: Conceptos básicos y introducciones
- **Orquestación**: Airflow, workflows
- **Procesamiento**: Databricks, Spark, Delta Lake
- **Streaming**: Kafka, arquitecturas event-driven
- **Plataformas**: Microsoft Fabric, cloud services
- **Notebooks**: Separados en práctica vs avanzado

### 📅 Programación Automática
- **GitHub Actions**: Ejecuta mensualmente en la nube
- **Cron Local**: Script Python para ejecución local
- **Task Scheduler**: Automatización en Windows

## 🔧 Configuración

### Opción 1: GitHub Actions (Recomendado)
El workflow ya está configurado en `.github/workflows/auto-update-docs.yml`:
- Se ejecuta el 1ro de cada mes
- Detecta cambios automáticamente
- Hace commit y push sin intervención

### Opción 2: Script Local

```bash
# Ejecutar una vez
python scripts/auto-update-docs.py

# Solo probar sin push
python scripts/auto-update-docs.py --no-push

# Configurar automatización Windows
scripts/setup-automation.bat
```

### Opción 3: Cron (Linux/Mac)

```bash
# Editar crontab
crontab -e

# Agregar línea (1ro de cada mes, medianoche)
0 0 1 * * cd /path/to/repo && python scripts/auto-update-docs.py
```

## 📝 Uso Manual

### Agregar Nuevos Documentos

1. **Crear archivo**: Simplemente agrega archivos `.md` o `.ipynb` en `docs/`
2. **Naming convention**: Usa nombres descriptivos:
   - `airflow-advanced-patterns.md`
   - `spark-optimization-guide.md`
   - `kafka-streaming-tutorial.ipynb`

3. **El sistema automáticamente**:
   - Detecta el archivo nuevo
   - Lo categoriza basado en contenido
   - Actualiza la navegación
   - Crea commit descriptivo

### Forzar Ejecución

```bash
# Ejecutar inmediatamente
python scripts/auto-update-docs.py

# Solo ver qué haría (dry run)
git status --porcelain | grep "^??"
```

## 🎯 Reglas de Categorización

El sistema usa estas reglas para categorizar automáticamente:

```python
# Ejemplos de categorización
'airflow-dag-patterns.md' → 'Orquestación'
'databricks-delta-lake.md' → 'Procesamiento'
'kafka-streaming-101.md' → 'Streaming'
'advanced-spark-joins.ipynb' → 'Spark - Avanzado'
'basic-transformations.ipynb' → 'Spark - Práctica'
'microsoft-fabric-guide.md' → 'Plataformas'
```

## 📊 Logs y Monitoreo

### Ver Últimas Ejecuciones
```bash
# GitHub Actions
gh run list --workflow=auto-update-docs.yml

# Logs locales
git log --grep="Auto-update" --oneline -10
```

### Verificar Tarea Programada (Windows)
```cmd
schtasks /query /tn "AutoUpdateDocs" /v
```

## 🔧 Personalización

### Modificar Categorías
Edita `scripts/auto-update-docs.py`, función `categorize_file()`:

```python
categories = {
    'Tu Categoría': ['keyword1', 'keyword2'],
    'Otra Categoría': ['otro', 'keyword']
}
```

### Cambiar Frecuencia
- **GitHub Actions**: Modifica cron en `.github/workflows/auto-update-docs.yml`
- **Local**: Edita crontab o Task Scheduler

## 🚨 Troubleshooting

### Archivo No Detectado
- Verificar que esté en `docs/`
- Confirmar extensión `.md` o `.ipynb`
- Revisar que no esté en `.gitignore`

### No Se Actualiza Navegación
- Verificar permisos de escritura en `mkdocs.yml`
- Revisar sintaxis YAML
- Ejecutar con `--no-push` para debugging

### Commit Fallido
```bash
# Configurar Git si es necesario
git config user.email "tu@email.com"
git config user.name "Tu Nombre"
```

## 📈 Estadísticas

El sistema trackea:
- ✅ Archivos procesados
- 📊 Categorías detectadas
- 🕐 Tiempo de ejecución
- 📝 Commits generados

¡Ahora tu documentación se mantiene organizada automáticamente! 🎉