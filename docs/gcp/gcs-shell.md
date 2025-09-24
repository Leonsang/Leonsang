# Google Cloud Shell: Entorno de Desarrollo en la Nube

> "Cloud Shell es un entorno de desarrollo y operaciones interactivo basado en navegador que te permite administrar tus recursos de Google Cloud directamente desde el navegador."

---

## 🌟 ¿Qué es Google Cloud Shell?

Google Cloud Shell es una máquina virtual basada en Debian que proporciona acceso de línea de comandos a los recursos de Google Cloud. Incluye herramientas preinstaladas, autenticación automática y un entorno de desarrollo completo accesible desde cualquier navegador.

---

## ⚡ Características Principales

### **🚀 Acceso Instantáneo**
- Sin configuración necesaria
- Accesible desde cualquier navegador
- Autenticación automática con Google Cloud

### **🛠️ Herramientas Preinstaladas**
- **Google Cloud CLI** (gcloud)
- **Docker** para contenedores
- **kubectl** para Kubernetes
- **Terraform** para infraestructura como código
- **Git, Python, Node.js, Go** y más

### **💾 Almacenamiento Persistente**
- **5 GB** de almacenamiento persistente en `$HOME`
- Los archivos se mantienen entre sesiones
- Modo efímero disponible para trabajo temporal

---

## 🚀 Primeros Pasos

### 1. Acceder a Cloud Shell

```bash
# Desde Google Cloud Console:
# 1. Ve a console.cloud.google.com
# 2. Haz clic en el ícono de Cloud Shell (terminal) en la barra superior
# 3. Espera a que se inicie la sesión
```

### 2. Verificar Autenticación

```bash
# Verificar cuenta activa
gcloud auth list

# Salida esperada:
# Credentialed Accounts
# ACTIVE  ACCOUNT
# *       tu-email@gmail.com
```

### 3. Confirmar Proyecto Actual

```bash
# Ver proyecto configurado
gcloud config list project

# Cambiar proyecto si es necesario
gcloud config set project MI-PROYECTO-ID
```

---

## 💻 Comandos Esenciales

### Configuración Básica

```bash
# Ver todas las configuraciones
gcloud config list

# Ver todas las propiedades disponibles
gcloud config list --all

# Configurar región por defecto
gcloud config set compute/region us-central1

# Configurar zona por defecto
gcloud config set compute/zone us-central1-a
```

### Exploración y Ayuda

```bash
# Ver comandos disponibles
gcloud -h

# Ayuda específica para configuración
gcloud config --help

# Ayuda detallada
gcloud help config

# Listar servicios disponibles
gcloud services list --available
```

### Gestión de Proyectos

```bash
# Listar proyectos
gcloud projects list

# Crear nuevo proyecto
gcloud projects create mi-nuevo-proyecto --name="Mi Proyecto"

# Cambiar proyecto activo
gcloud config set project mi-nuevo-proyecto

# Ver información del proyecto actual
gcloud projects describe $(gcloud config get-value project)
```

---

## 🌐 Cloud Shell Editor

### Acceso al Editor

```bash
# Abrir editor desde Cloud Shell
cloudshell edit archivo.py

# Abrir editor web
# Clic en "Open Editor" en la barra de herramientas
```

### Funcionalidades del Editor

- **Syntax highlighting** para múltiples lenguajes
- **IntelliSense** y autocompletado
- **Terminal integrada**
- **Git integration** nativa
- **Live preview** para aplicaciones web

```bash
# Comandos útiles del editor
# Ctrl+` : Abrir/cerrar terminal
# Ctrl+P : Buscar archivos
# Ctrl+Shift+P : Paleta de comandos
```

---

## 🔧 Casos de Uso Prácticos

### 1. Desarrollo de Aplicaciones

```bash
# Clonar repositorio
git clone https://github.com/usuario/mi-app.git
cd mi-app

# Instalar dependencias
npm install

# Ejecutar aplicación
npm start

# Preview web en puerto 8080
cloudshell web-preview --port=8080
```

### 2. Administración de Compute Engine

```bash
# Listar instancias
gcloud compute instances list

# Crear nueva instancia
gcloud compute instances create mi-vm \
    --machine-type=e2-medium \
    --zone=us-central1-a \
    --image-family=debian-11 \
    --image-project=debian-cloud

# Conectar por SSH
gcloud compute ssh mi-vm --zone=us-central1-a

# Eliminar instancia
gcloud compute instances delete mi-vm --zone=us-central1-a
```

### 3. Gestión de Google Kubernetes Engine

```bash
# Crear cluster GKE
gcloud container clusters create mi-cluster \
    --num-nodes=3 \
    --zone=us-central1-a

# Obtener credenciales
gcloud container clusters get-credentials mi-cluster \
    --zone=us-central1-a

# Ver nodos
kubectl get nodes

# Desplegar aplicación
kubectl create deployment hello-server \
    --image=gcr.io/google-samples/hello-app:1.0

# Exponer servicio
kubectl expose deployment hello-server \
    --type=LoadBalancer \
    --port=8080
```

### 4. Trabajo con Cloud Storage

```bash
# Crear bucket
gsutil mb gs://mi-bucket-unico-123

# Subir archivo
gsutil cp archivo.txt gs://mi-bucket-unico-123/

# Listar contenido
gsutil ls gs://mi-bucket-unico-123/

# Descargar archivo
gsutil cp gs://mi-bucket-unico-123/archivo.txt ./

# Hacer bucket público
gsutil iam ch allUsers:objectViewer gs://mi-bucket-unico-123
```

---

## ⚙️ Configuración Avanzada

### Personalización del Entorno

```bash
# Crear aliases útiles
echo 'alias ll="ls -la"' >> ~/.bashrc
echo 'alias k="kubectl"' >> ~/.bashrc
echo 'alias g="gcloud"' >> ~/.bashrc

# Configurar Git
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Instalar herramientas adicionales
sudo apt-get update
sudo apt-get install htop tree
```

### Modo Efímero

```bash
# Iniciar Cloud Shell en modo efímero
# Agrega ?ephemeral=true a la URL de Cloud Console

# Ventajas del modo efímero:
# - Inicio más rápido
# - Ideal para tareas temporales
# - Se reinicia limpio cada vez
```

### Variables de Entorno Útiles

```bash
# Variables predefinidas importantes
echo $GOOGLE_CLOUD_PROJECT  # Proyecto actual
echo $DEVSHELL_GCLOUD_CONFIG  # Configuración gcloud
echo $HOME  # Directorio home persistente

# Configurar variables personalizadas
export MY_REGION=us-central1
export MY_ZONE=us-central1-a

# Hacer persistentes las variables
echo 'export MY_REGION=us-central1' >> ~/.bashrc
```

---

## 🔍 Monitoreo y Debugging

### Logs y Debugging

```bash
# Ver logs de operaciones
gcloud logging read "resource.type=gce_instance" --limit=50

# Debug de configuración
gcloud info

# Ver versión de herramientas
gcloud version
kubectl version --client
docker --version
terraform --version
```

### Performance y Recursos

```bash
# Ver uso de recursos
htop

# Espacio en disco
df -h

# Información del sistema
uname -a
cat /proc/cpuinfo | grep processor | wc -l  # CPUs
cat /proc/meminfo | grep MemTotal  # RAM total
```

---

## 🛡️ Mejores Prácticas de Seguridad

### Gestión de Credenciales

```bash
# NUNCA hardcodear credenciales
# Usar Service Accounts cuando sea apropiado

# Crear Service Account
gcloud iam service-accounts create mi-service-account \
    --description="Para mi aplicación" \
    --display-name="Mi Service Account"

# Crear y descargar key
gcloud iam service-accounts keys create ~/key.json \
    --iam-account=mi-service-account@mi-proyecto.iam.gserviceaccount.com

# Activar Service Account
gcloud auth activate-service-account \
    --key-file=~/key.json
```

### Control de Permisos

```bash
# Ver permisos del usuario actual
gcloud projects get-iam-policy $(gcloud config get-value project)

# Listar roles disponibles
gcloud iam roles list --filter="stage:GA"

# Ver permisos de un rol específico
gcloud iam roles describe roles/editor
```

---

## 📚 Tutoriales Interactivos

### Ejecutar Tutoriales Oficiales

```bash
# Listar tutoriales disponibles
cloudshell tutorials list

# Ejecutar tutorial específico
cloudshell launch-tutorial tutorial.md

# Crear tu propio tutorial
cloudshell edit tutorial.md
```

### Estructura de Tutorial

```markdown
# Mi Tutorial Cloud Shell

## Paso 1: Configuración
cloudshell:
Ejecuta el siguiente comando:
```
gcloud config list
```

## Paso 2: Crear Recursos
<walkthrough-editor-open-file
    filePath="mi-archivo.yaml">
    Abrir archivo de configuración
</walkthrough-editor-open-file>
```

---

## 💡 Tips y Trucos

### Atajos de Teclado

```bash
# En Cloud Shell:
# Ctrl+C : Terminar proceso
# Ctrl+D : Cerrar sesión
# Ctrl+L : Limpiar pantalla
# Ctrl+R : Buscar en historial
# Tab : Autocompletar comandos

# En Cloud Shell Editor:
# Ctrl+` : Toggle terminal
# Ctrl+P : Quick file open
# Ctrl+Shift+P : Command palette
```

### Comandos de Productividad

```bash
# Historial persistente
history | grep "gcloud"

# Búsqueda rápida
find ~/mi-proyecto -name "*.yaml" -type f

# Comprimir y descomprimir
tar -czvf backup.tar.gz ~/mi-proyecto/
tar -xzvf backup.tar.gz

# Monitoreo en tiempo real
watch -n 2 'gcloud compute instances list'
```

---

## 🚀 Integración con CI/CD

### GitHub Actions con Cloud Shell

```yaml
# .github/workflows/deploy.yml
name: Deploy to GCP
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - id: 'auth'
      uses: 'google-github-actions/auth@v1'
      with:
        credentials_json: '${{ secrets.GCP_SA_KEY }}'

    - name: 'Set up Cloud SDK'
      uses: 'google-github-actions/setup-gcloud@v1'

    - name: 'Deploy to GKE'
      run: |
        gcloud container clusters get-credentials mi-cluster --zone us-central1-a
        kubectl apply -f k8s/
```

### Cloud Build Integration

```bash
# Crear build trigger
gcloud builds triggers create github \
    --repo-name=mi-repo \
    --repo-owner=mi-usuario \
    --branch-pattern="^main$" \
    --build-config=cloudbuild.yaml
```

---

## 📊 Mejores Prácticas

!!! tip "Productividad"
    - Usa aliases para comandos frecuentes
    - Aprovecha el autocompletado con Tab
    - Configura tu entorno una sola vez
    - Usa el modo efímero para pruebas rápidas

!!! info "Desarrollo"
    - Organiza proyectos en carpetas separadas
    - Usa Git para control de versiones
    - Configura linting y formatting
    - Aprovecha la preview web para desarrollo

!!! success "Operaciones"
    - Mantén scripts de automatización
    - Usa Service Accounts para producción
    - Monitorea costos regularmente
    - Documenta procedures complejos

---

¡Google Cloud Shell es tu entorno de desarrollo completo en la nube! 🌟