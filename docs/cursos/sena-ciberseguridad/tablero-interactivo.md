!!! info "Curso SENA · Ciberseguridad"
    Apropiación de los conceptos en ciberseguridad · Programa 23310008 · Ficha 3640188 · Centro de Comercio y Turismo, Regional Quindío

# Tablero Interactivo de Ciberseguridad & Refuerzo

Herramientas interactivas desarrolladas para poner a prueba los conceptos aprendidos en el programa del SENA: simulación de incidentes, cálculo dinámico de nivel de riesgo y tarjetas de autoevaluación interactiva.

---

## 🎮 1. Simulador de Incidentes: Amenaza vs. Controles

Selecciona un vector de ataque para ver cómo afecta la tríada **Confidencialidad, Integridad y Disponibilidad (CID)**, su fase en MITRE ATT&CK y las medidas de mitigación requeridas por **ISO 27001** y **NIST SP 800-30**.

<div class="cyber-simulator-wrap">
  <div class="sim-threat-selector">
    <button type="button" class="sim-btn active" onclick="loadSimThreat('ransomware')">🦠 Ransomware</button>
    <button type="button" class="sim-btn" onclick="loadSimThreat('phishing')">🎣 Phishing / Smishing</button>
    <button type="button" class="sim-btn" onclick="loadSimThreat('sqli')">💉 Inyección SQL</button>
    <button type="button" class="sim-btn" onclick="loadSimThreat('mitm')">📡 Man-in-the-Middle</button>
    <button type="button" class="sim-btn" onclick="loadSimThreat('insider')">👤 Fuga Interna de Datos</button>
    <button type="button" class="sim-btn" onclick="loadSimThreat('power')">⚡ Falla Eléctrica / Servidor</button>
  </div>

  <div class="sim-card" id="simDisplayCard">
    <!-- Se llena dinámicamente con JS -->
  </div>
</div>

---

## 🧮 2. Calculadora Interactiva de Nivel de Riesgo 5×5

La fórmula fundamental aplicada en el curso es:

$$\text{Riesgo} = \text{Impacto} \times \text{Probabilidad}$$

Mueve los controles o haz clic en cualquier celda de la matriz para calcular el puntaje de severidad, el estado de aceptación y el plan de mitigación exigido:

<div class="risk-calc-wrap">
  <div class="risk-controls">
    <div class="rc-group">
      <label for="rcProb"><strong>Probabilidad de Ocurrencia (1 a 5):</strong> <span id="lblProb" class="badge info">3 - Media</span></label>
      <input type="range" id="rcProb" min="1" max="5" value="3" oninput="updateRiskCalc()" style="width:100%;" />
    </div>
    <div class="rc-group" style="margin-top:14px;">
      <label for="rcImp"><strong>Impacto sobre el Activo / CID (1 a 5):</strong> <span id="lblImp" class="badge info">4 - Alto</span></label>
      <input type="range" id="rcImp" min="1" max="5" value="4" oninput="updateRiskCalc()" style="width:100%;" />
    </div>
  </div>

  <div class="risk-result-box" id="riskResultBox">
    <div class="rrb-score">Puntaje de Riesgo: <span id="rrbVal" style="font-size:2rem; font-weight:700;">12</span> / 25</div>
    <div class="rrb-badge"><span id="rrbLevel" class="badge danger" style="font-size:1.1rem; padding:6px 14px;">Riesgo Alto</span></div>
    <div class="rrb-desc" id="rrbDesc" style="margin-top:10px; font-size:0.95rem;">Riesgo no tolerable. Requiere plan de tratamiento formal con controles específicos y reducción de exposición en menos de 30 días.</div>
    <div class="rrb-sla" id="rrbSla" style="margin-top:8px; font-weight:600; color:var(--md-primary-fg-color);">SLA de Atención: Inmediata (< 48 horas)</div>
  </div>
</div>

---

## 🃏 3. Flashcards 3D de Refuerzo de Conceptos

Pon a prueba tu dominio técnico antes de las evaluaciones del SENA. Haz clic en **Voltear Tarjeta** para revelar la respuesta y el truco mnemotécnico:

<div class="flashcard-deck-wrap">
  <div class="flashcard-nav">
    <button type="button" class="btn-fc-nav" onclick="prevFlashcard()">◀ Anterior</button>
    <span id="fcCounter" class="fc-counter">Tarjeta 1 de 6</span>
    <button type="button" class="btn-fc-nav" onclick="nextFlashcard()">Siguiente ▶</button>
  </div>

  <div class="flashcard-scene" onclick="flipActiveCard()">
    <div class="flashcard" id="activeFlashcard">
      <div class="flashcard-face flashcard-front">
        <div class="fc-category" id="fcCat">TRÍADA DE SEGURIDAD</div>
        <div class="fc-question" id="fcQ">¿Cuál es la diferencia fundamental entre una Amenaza y una Vulnerabilidad?</div>
        <div class="fc-tap-hint">👆 Clic para voltear</div>
      </div>
      <div class="flashcard-face flashcard-back">
        <div class="fc-answer" id="fcA">
          Una <strong>Amenaza</strong> es un evento externo o interno que tiene el potencial de dañar un activo (ej. un ciberdelincuente, un sismo o un corte eléctrico).<br/><br/>
          Una <strong>Vulnerabilidad</strong> es la debilidad o falla interna del sistema que la amenaza puede aprovechar (ej. software sin parchar o falta de copias fuera del sitio).
        </div>
        <div class="fc-tip" id="fcTip">💡 <strong>Truco mnemotécnico:</strong> La amenaza es el peligro que acecha afuera; la vulnerabilidad es la puerta que dejaste sin candado.</div>
      </div>
    </div>
  </div>
</div>

<script>
// DATOS DEL SIMULADOR
const THREAT_DB = {
  ransomware: {
    name: "Ransomware / Secuestro de Datos",
    icon: "🦠",
    cia: { c: "Media", i: "Crítica", a: "Crítica" },
    mitre: "T1486 - Data Encrypted for Impact (Impact)",
    vuln: "Puertos RDP expuestos a internet, falta de autenticación MFA y copias de seguridad conectadas a la misma red local.",
    controls: "ISO 27001 A.8.7 (Protección contra malware), A.8.13 (Copias de seguridad desconectadas/inmutables - regla 3-2-1), segmentación de red VLAN.",
    caseExample: "En Huellitas: el atacante cifra el software veterinario y las historias clínicas. Sin el disco externo desconectado, la clínica queda paralizada."
  },
  phishing: {
    name: "Phishing / Smishing (Ingeniería Social)",
    icon: "🎣",
    cia: { c: "Crítica", i: "Alta", a: "Baja" },
    mitre: "T1566 - Phishing (Initial Access)",
    vuln: "Falta de capacitación en concientización del personal y ausencia de filtrado estricto SPF/DKIM/DMARC en el correo corporativo.",
    controls: "ISO 27001 A.6.3 (Concienciación en seguridad de la información), A.5.15 (Control de acceso), autenticación multifactor obligatoria (FIDO2/TOTP).",
    caseExample: "En Huellitas: recepcionista abre un falso adjunto 'Factura DIAN pendiente' que roba credenciales del correo y WhatsApp Business."
  },
  sqli: {
    name: "Inyección SQL (SQL Injection)",
    icon: "💉",
    cia: { c: "Crítica", i: "Crítica", a: "Media" },
    mitre: "T1190 - Exploit Public-Facing Application",
    vuln: "Consultas SQL concatenadas con cadenas del usuario sin parametrización ni validación en el formulario web de citas.",
    controls: "Uso estricto de ORMs o Prepared Statements, Web Application Firewall (WAF), principio de menor privilegio en el usuario de base de datos.",
    caseExample: "En Proyecto ASEGURA: atacante inyecta `' OR '1'='1` en la consulta del portal web y extrae el listado completo de expedientes confidenciales."
  },
  mitm: {
    name: "Man-in-the-Middle (Intercepción de Red)",
    icon: "📡",
    cia: { c: "Crítica", i: "Alta", a: "Baja" },
    mitre: "T1557 - Adversary-in-the-Middle",
    vuln: "Wifi abierto sin cifrado WPA3 o red de invitados sin aislamiento de red (client isolation) mezclada con equipos médicos y datáfonos.",
    controls: "ISO 27001 A.8.20 (Seguridad en redes), cifrado obligatorio HTTPS con HSTS, segmentación de VLAN para invitados y certificados TLS robustos.",
    caseExample: "En Huellitas: un cliente en la sala de espera usa la red wifi compartida para esnifar el tráfico entre el computador y el datáfono."
  },
  insider: {
    name: "Fuga Interna de Información (Insider Threat)",
    icon: "👤",
    cia: { c: "Crítica", i: "Media", a: "Baja" },
    mitre: "T1052 - Exfiltration Over Physical Medium",
    vuln: "Puertos USB habilitados sin restricción en computadores de recepción y falta de acuerdos de confidencialidad y control de accesos (RBAC).",
    controls: "ISO 27001 A.5.12 (Clasificación de información), A.8.1 (Dispositivos de usuario final - bloqueo de almacenamiento masivo USB), registro de auditoría de descargas.",
    caseExample: "Un empleado que renuncia copia la base de datos de 2.000 propietarios en una memoria USB para ofrecerla a otra clínica veterinaria competidora."
  },
  power: {
    name: "Corte Eléctrico / Falla de Servidor",
    icon: "⚡",
    cia: { c: "Baja", i: "Alta", a: "Crítica" },
    mitre: "Amenaza del Entorno / Falla de Infraestructura",
    vuln: "Servidor conectado directo al tomacorriente sin Sistema de Alimentación Ininterrumpida (UPS/SAI) ni contrato de respaldo eléctrico.",
    controls: "ISO 27001 A.7.11 (Suministro de energía e instalaciones de soporte), redundancia de fuentes de poder, plan de continuidad de negocio (BCP).",
    caseExample: "En Huellitas: un apagón en Armenia apaga bruscamente el servidor durante una cirugía, corrompiendo la base de datos de historias clínicas activas."
  }
};

function loadSimThreat(key) {
  const t = THREAT_DB[key];
  if (!t) return;
  document.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');

  const card = document.getElementById('simDisplayCard');
  card.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--md-default-fg-color--lightest); padding-bottom:10px; margin-bottom:14px;">
      <h3 style="margin:0; font-size:1.3rem; display:flex; align-items:center; gap:8px;"><span>${t.icon}</span> ${t.name}</h3>
      <span class="badge info">${t.mitre}</span>
    </div>

    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; margin-bottom:16px;">
      <div style="background:var(--md-code-bg-color); padding:10px; border-radius:6px; text-align:center;">
        <span style="font-size:0.8rem; font-weight:600; color:var(--md-default-fg-color--light);">CONFIDENCIALIDAD</span>
        <div style="font-weight:700; color:${t.cia.c === 'Crítica' ? '#dc3545' : t.cia.c === 'Alta' ? '#fd7e14' : '#28a745'}">${t.cia.c}</div>
      </div>
      <div style="background:var(--md-code-bg-color); padding:10px; border-radius:6px; text-align:center;">
        <span style="font-size:0.8rem; font-weight:600; color:var(--md-default-fg-color--light);">INTEGRIDAD</span>
        <div style="font-weight:700; color:${t.cia.i === 'Crítica' ? '#dc3545' : t.cia.i === 'Alta' ? '#fd7e14' : '#28a745'}">${t.cia.i}</div>
      </div>
      <div style="background:var(--md-code-bg-color); padding:10px; border-radius:6px; text-align:center;">
        <span style="font-size:0.8rem; font-weight:600; color:var(--md-default-fg-color--light);">DISPONIBILIDAD</span>
        <div style="font-weight:700; color:${t.cia.a === 'Crítica' ? '#dc3545' : t.cia.a === 'Alta' ? '#fd7e14' : '#28a745'}">${t.cia.a}</div>
      </div>
    </div>

    <p><strong>Vulnerabilidad Explotada:</strong> ${t.vuln}</p>
    <p><strong>Controles Obligatorios (ISO 27001 / NIST):</strong> ${t.controls}</p>
    <div style="background:rgba(63, 81, 181, 0.08); border-left:4px solid var(--md-primary-fg-color); padding:10px 14px; border-radius:4px; margin-top:12px;">
      <strong>Ejemplo en el Caso Real:</strong> ${t.caseExample}
    </div>
  `;
}

// CALCULADORA DE RIESGO
function updateRiskCalc() {
  const p = parseInt(document.getElementById('rcProb').value, 10);
  const i = parseInt(document.getElementById('rcImp').value, 10);
  const score = p * i;

  const pLabels = ["", "1 - Rara vez", "2 - Improbable", "3 - Media / Posible", "4 - Alta / Frecuente", "5 - Casi seguro"];
  const iLabels = ["", "1 - Insignificante", "2 - Menor", "3 - Moderado", "4 - Crítico / Alto", "5 - Catastrófico"];

  document.getElementById('lblProb').textContent = pLabels[p];
  document.getElementById('lblImp').textContent = iLabels[i];
  document.getElementById('rrbVal').textContent = score;

  const lvlEl = document.getElementById('rrbLevel');
  const descEl = document.getElementById('rrbDesc');
  const slaEl = document.getElementById('rrbSla');

  if (score <= 4) {
    lvlEl.className = "badge success";
    lvlEl.textContent = "Riesgo Bajo";
    descEl.textContent = "Riesgo asumible. Mantener procedimientos actuales y monitoreo periódico anual.";
    slaEl.textContent = "SLA de Atención: Monitoreo rutinario (> 90 días)";
  } else if (score <= 9) {
    lvlEl.className = "badge warning";
    lvlEl.textContent = "Riesgo Medio";
    descEl.textContent = "Riesgo tolerable. Se deben programar controles de mitigación estándar dentro del ciclo regular de trabajo.";
    slaEl.textContent = "SLA de Atención: Planificado (< 60 días)";
  } else if (score <= 15) {
    lvlEl.className = "badge danger";
    lvlEl.style.backgroundColor = "#fd7e14";
    lvlEl.textContent = "Riesgo Alto";
    descEl.textContent = "Riesgo no tolerable. Exige asignación formal de responsables, presupuesto y despliegue de controles prioritarios.";
    slaEl.textContent = "SLA de Atención: Prioritario (< 30 días)";
  } else {
    lvlEl.className = "badge danger";
    lvlEl.style.backgroundColor = "#dc3545";
    lvlEl.textContent = "Riesgo Crítico / Catastrófico";
    descEl.textContent = "Riesgo inadmisible. Compromete la viabilidad legal, financiera o reputacional de la entidad. Requiere mitigación urgente y escalamiento a Dirección.";
    slaEl.textContent = "SLA de Atención: Inmediata (< 24 a 48 horas)";
  }
}

// FLASHCARDS
const FLASHCARDS = [
  {
    cat: "CONCEPTOS FUNDAMENTALES",
    q: "¿Cuál es la diferencia fundamental entre una Amenaza y una Vulnerabilidad?",
    a: "Una <strong>Amenaza</strong> es un evento externo o interno que puede causar daño (ej. ransomware, inundación, hacker).<br/><br/>Una <strong>Vulnerabilidad</strong> es la debilidad intrínseca del activo que permite que la amenaza tenga éxito (ej. puertos abiertos, falta de backup fuera de sitio).",
    tip: "💡 Truco: La amenaza ataca; la vulnerabilidad permite el golpe."
  },
  {
    cat: "TRÍADA CID",
    q: "Si un atacante modifica el diagnóstico en una historia clínica sin borrarla, ¿qué pilar CID se quebrantó principalmente?",
    a: "El pilar de <strong>INTEGRIDAD</strong>, porque la información fue adulterada y dejó de ser exacta y verídica, induciendo a tratamientos médicos potencialmente fatales.",
    tip: "💡 Confidencialidad = Nadie no autorizado la lee. Integridad = Nadie la altera. Disponibilidad = Está accesible cuando se necesita."
  },
  {
    cat: "METODOLOGÍA NIST SP 800-30",
    q: "¿Cuáles son las 3 categorías obligatorias de amenazas según la guía del SENA y NIST?",
    a: "1. <strong>Naturales:</strong> Terremotos, inundaciones, tormentas eléctricas.<br/>2. <strong>Humanas:</strong> Hackers, phishing, virus, robo, errores operativos.<br/>3. <strong>Del Entorno:</strong> Cortes eléctricos, fugas de agua, fallas de hardware, polvo/temperatura.",
    tip: "💡 Truco mnemotécnico: 'N-H-E' (Naturaleza, Hombre, Entorno)."
  },
  {
    cat: "NORMATIVA ISO 27001",
    q: "¿En qué consiste el principio de Menor Privilegio (Least Privilege)?",
    a: "Garantiza que cada usuario, servicio o proceso tenga <strong>únicamente los permisos estrictamente indispensables</strong> para cumplir sus funciones laborales, nada más.",
    tip: "💡 Si un recepcionista solo agenda citas, jamás debe tener permisos de administrador ni acceso al servidor de base de datos."
  },
  {
    cat: "GESTIÓN DE ACTIVOS",
    q: "¿Por qué en MAGERIT un servidor sin datos propios puede ser calificado como Crítico?",
    a: "Por el <strong>principio de dependencia de activos</strong>: el servidor sostiene la aplicación y la base de datos de expedientes legales; si cae el servidor, cae el servicio esencial.",
    tip: "💡 El valor de un activo esencial se propaga hacia abajo a sus activos de soporte."
  },
  {
    cat: "TRATAMIENTO DEL RIESGO",
    q: "¿Cuáles son las 4 opciones de tratamiento del riesgo según ISO 27005?",
    a: "1. <strong>Mitigar / Reducir:</strong> Aplicar controles técnicos/organizacionales.<br/>2. <strong>Transferir / Compartir:</strong> Contratar pólizas de ciberseguridad o tercerizar en la nube.<br/>3. <strong>Evitar:</strong> Cancelar la actividad que causa el riesgo.<br/>4. <strong>Aceptar:</strong> Asumir el riesgo residual documentado.",
    tip: "💡 Recuerda las 4 T en inglés: Treat, Transfer, Terminate, Tolerate."
  }
];

let fcIndex = 0;
function showCard(idx) {
  const card = FLASHCARDS[idx];
  document.getElementById('fcCat').textContent = card.cat;
  document.getElementById('fcQ').textContent = card.q;
  document.getElementById('fcA').innerHTML = card.a;
  document.getElementById('fcTip').innerHTML = card.tip;
  document.getElementById('fcCounter').textContent = `Tarjeta ${idx + 1} de ${FLASHCARDS.length}`;
  document.getElementById('activeFlashcard').classList.remove('is-flipped');
}

function flipActiveCard() {
  document.getElementById('activeFlashcard').classList.toggle('is-flipped');
}

function nextFlashcard() {
  fcIndex = (fcIndex + 1) % FLASHCARDS.length;
  showCard(fcIndex);
}

function prevFlashcard() {
  fcIndex = (fcIndex - 1 + FLASHCARDS.length) % FLASHCARDS.length;
  showCard(fcIndex);
}

// Iniciar al cargar
document.addEventListener('DOMContentLoaded', () => {
  loadSimThreat('ransomware');
  updateRiskCalc();
  showCard(0);
});
</script>
