!!! info "Curso SENA · Ciberseguridad"
    Apropiación de los conceptos en ciberseguridad · Programa 23310008 · Ficha 3640188 · Centro de Comercio y Turismo, Regional Quindío

# Trucos, Tips & Cheat Sheet Técnico de Ciberseguridad

Compendio práctico con comandos reales de auditoría, scripts de hardening, listas de verificación OWASP y consejos mnemotécnicos para evaluaciones del SENA y certificaciones profesionales.

---

## 🐧 1. Hardening & Auditoría Rápida en Linux

Comandos esenciales para inspeccionar servidores expuestos y detectar configuraciones peligrosas:

=== "Auditoría de Cuentas y Privilegios"
    ```bash
    # 1. Buscar cuentas con UID 0 (privilegios root ocultos)
    awk -F: '($3 == "0") {print $1}' /etc/passwd

    # 2. Verificar permisos de archivos sensibles (deben ser estrictos)
    chmod 600 /etc/shadow
    chmod 644 /etc/passwd
    ls -l /etc/shadow /etc/passwd

    # 3. Detectar binarios con bit SUID activado (pueden permitir escalada de privilegios)
    find / -perm -4000 -type f 2>/dev/null
    ```

=== "Detección de Conexiones y Puertos Abiertos"
    ```bash
    # 1. Ver puertos TCP/UDP a la escucha con el proceso responsable
    ss -tulpn

    # 2. Detectar conexiones activas hacia IPs sospechosas
    ss -tna state established

    # 3. Listar archivos abiertos por la red
    lsof -i -P -n
    ```

=== "Análisis Rápido de Intentos de Intrusión (Logs)"
    ```bash
    # 1. Ver IPs con mayor número de contraseñas fallidas por SSH
    grep "Failed password" /var/log/auth.log 2>/dev/null | awk '{print $11}' | sort | uniq -c | sort -nr | head -n 10

    # 2. Rastrear comandos ejecutados mediante sudo
    grep "COMMAND" /var/log/auth.log 2>/dev/null | tail -n 25

    # 3. Revisar reinicios y últimos usuarios conectados
    last -n 15
    lastb -n 15  # Intentos de inicio de sesión fallidos
    ```

---

## 🔍 2. Reconocimiento Defensivo con Nmap

Usa Nmap desde la perspectiva del defensor para verificar qué ve un atacante desde el exterior:

```bash
# Escaneo de puertos estándar con detección de versiones y scripts de seguridad básicos
nmap -sV -sC -O -T4 192.168.1.100

# Escaneo silencioso SYN (requiere root)
sudo nmap -sS -p 1-1024 192.168.1.100

# Verificación de vulnerabilidades conocidas con la base de scripts NSE
nmap --script "vuln" -p 80,443,22 192.168.1.100
```

!!! tip "Tip Profesional: Evita falsos positivos en auditorías"
    Nunca uses banderas de máxima velocidad (`-T5`) en redes de producción o clínicas veterinarias/hospitales, ya que pueden colapsar routers antiguos o equipos médicos IoT. Mantén siempre `-T3` o `-T4`.

---

## 🧱 3. Reglas Esenciales de Firewall con UFW e iptables

El principio fundamental es: **Denegar todo por defecto y abrir solo lo necesario**.

=== "UFW (Uncomplicated Firewall)"
    ```bash
    # 1. Configurar política por defecto
    sudo ufw default deny incoming
    sudo ufw default allow outgoing

    # 2. Permitir SSH solo con límite de tasa contra fuerza bruta
    sudo ufw limit ssh

    # 3. Permitir tráfico web seguro
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp

    # 4. Activar y verificar estado
    sudo ufw enable
    sudo ufw status verbose
    ```

=== "iptables (Reglas Base Anti-Ataques)"
    ```bash
    # Bloquear paquetes nulos (escaneo sigiloso)
    sudo iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP

    # Mitigar ataques SYN Flood
    sudo iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT

    # Bloquear paquetes malformados de escaneo XMAS
    sudo iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
    ```

---

## 🔒 4. Integridad Criptográfica de Respaldos (Regla 3-2-1)

Garantiza que tus copias de seguridad de historias clínicas o expedientes no hayan sido alteradas ni corrompidas:

```bash
# 1. Generar suma de comprobación SHA-256 del archivo de respaldo
sha256sum backup_historias_clinicas_2026.zip > backup.sha256

# 2. Verificar integridad en cualquier momento antes de restaurar
sha256sum -c backup.sha256
# Salida esperada: backup_historias_clinicas_2026.zip: OK

# 3. Cifrar el respaldo con AES-256 antes de subir a la nube
openssl enc -aes-256-cbc -salt -pbkdf2 -iter 100000 -in backup.zip -out backup_cifrado.enc
```

---

## 🎯 5. Mnemotecnias Clave para Evaluaciones del SENA

!!! question "¿Cómo memorizar la diferencia entre RPO y RTO?"
    * **RPO (Recovery Point Objective / Pérdida máxima de datos tolerada):** ¿Cuántas horas de datos puedo perder sin quebrar? (Ej. backup cada 24 horas = RPO de 24 horas).
    * **RTO (Recovery Time Objective / Tiempo máximo de recuperación):** ¿Cuánto tiempo puedo tardar en volver a levantar el servidor? (Ej. RTO de 4 horas).
    * **Mnemotecnia:** **P** de R**P**O = **P**érdida de datos. **T** de R**T**O = **T**iempo de parada.

!!! question "¿Cuáles son las 3 dimensiones de MAGERIT y su ampliación?"
    * Tríada base: **C**onfidencialidad, **I**ntegridad, **D**isponibilidad (**CID**).
    * Ampliación MAGERIT v3: Añade **Autenticidad** (certeza de quién emitió el trámite) y **Trazabilidad** (registro imborrable de qué se hizo).
    * Sigla completa: **C-I-D-A-T**.

## Fuentes y aviso legal

- **Fuente:** formación del SENA en la plataforma Zajuna; las evidencias son trabajos propios del aprendiz. Sitios oficiales: [sena.edu.co](https://www.sena.edu.co).
- **Uso:** apuntes personales de estudio, sin fines comerciales y con redacción propia. Las imágenes del curso son fragmentos breves citados con fines educativos; sus derechos son de sus titulares.
- **Sin afiliación:** sitio no oficial, no afiliado ni respaldado por el SENA. Las marcas pertenecen a sus dueños.
- Más detalles y cómo pedir el retiro de contenido en el [aviso legal](../../aviso-legal.md).
