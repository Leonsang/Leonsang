# Hub Central de Aprendizajes & Cursos

<div class="courses-hero-banner">
  <div class="courses-hero-badge">PLATAFORMA INTEGRAL DE FORMACIÓN TÉCNICA · ERICK SANG</div>
  <h2>Base de Conocimiento y Certificaciones</h2>
  <p>Rutas de aprendizaje completadas y en curso: Ciberseguridad, Inteligencia Artificial, Cloud Computing, Arquitectura de Datos y Desarrollo de Software con enfoque práctico en producción.</p>
  <div style="margin-top: 1.2rem; display: flex; gap: 10px; flex-wrap: wrap;">
    <a href="../humano-conocimiento/" class="md-button" style="background: rgba(255,255,255,0.18); border: 1px solid rgba(255,255,255,0.3); color: #ffffff !important; backdrop-filter: blur(8px); display: inline-flex; align-items: center; gap: 6px;">
      <span>🧠 Explorar Mapa Neuro-Cognitivo 3D</span>
    </a>
  </div>
</div>

<div class="courses-controls-wrap">
  <input type="text" id="courseSearch" class="courses-search-input" placeholder="🔍 Buscar curso, habilidad o tecnología (ej: Spark, ISO 27001, AWS, MCP, Python, Polars...)" oninput="filterAllCourses()">
  <div class="courses-filter-bar">
    <button type="button" class="cf-btn active" data-cat="all" onclick="setCategory('all')">Todos (25)</button>
    <button type="button" class="cf-btn" data-cat="sena" onclick="setCategory('sena')">🏛️ SENA (2)</button>
    <button type="button" class="cf-btn" data-cat="aws" onclick="setCategory('aws')">☁️ AWS (3)</button>
    <button type="button" class="cf-btn" data-cat="google" onclick="setCategory('google')">🤖 Google GEAR (6)</button>
    <button type="button" class="cf-btn" data-cat="anthropic" onclick="setCategory('anthropic')">🧠 Anthropic & MCP (13)</button>
    <button type="button" class="cf-btn" data-cat="data" onclick="setCategory('data')">🍃 Bases de Datos (2)</button>
    <button type="button" class="cf-btn" data-cat="ubits" onclick="setCategory('ubits')">💡 UBITS (2)</button>
  </div>
</div>

<div class="courses-grid" id="coursesGrid">

  <div class="course-card" data-cat="sena">
    <div class="cc-header">
      <span class="cc-badge sena">SENA · Ciberseguridad</span>
      <span class="cc-status done">Calificado A</span>
    </div>
    <h3>Apropiación de Conceptos en Ciberseguridad</h3>
    <p>Valuación de activos con MAGERIT/ISO 27005, mapa de amenazas NIST SP 800-30, matriz formal de riesgo ISO 27001 y tablero interactivo de ciberdefensa.</p>
    <div class="cc-skills">
      <span>ISO 27001</span>
      <span>MAGERIT v3</span>
      <span>NIST 800-30</span>
      <span>CID Triad</span>
      <span>Hardening</span>
    </div>
    <div class="cc-links">
      <a href="sena-ciberseguridad/" class="cc-btn primary">Ver Curso</a>
      <a href="sena-ciberseguridad/tablero-interactivo/" class="cc-btn secondary">🎮 Tablero</a>
    </div>
  </div>

  <div class="course-card" data-cat="sena">
    <div class="cc-header">
      <span class="cc-badge sena">SENA · IA & Datos</span>
      <span class="cc-status done">Completado 100%</span>
    </div>
    <h3>Aplicación de la IA en la Integración de Datos</h3>
    <p>Pipeline completo con Polars y DuckDB, ingeniería de prompts verificados, modelado estrella y analítica avanzada en Power BI (PBIP/TMDL).</p>
    <div class="cc-skills">
      <span>Polars</span>
      <span>DuckDB</span>
      <span>Power BI</span>
      <span>DAX / TMDL</span>
      <span>Prompt Eng.</span>
    </div>
    <div class="cc-links">
      <a href="sena-ia-integracion-datos/" class="cc-btn primary">Ver Curso</a>
      <a href="sena-ia-integracion-datos/aa2-ev03-powerbi/" class="cc-btn secondary">📊 Tablero</a>
    </div>
  </div>

  <div class="course-card" data-cat="aws">
    <div class="cc-header">
      <span class="cc-badge aws">AWS · Generative AI</span>
      <span class="cc-status done">Completado 100%</span>
    </div>
    <h3>AWS Entrena · IA sin Límites</h3>
    <p>Fundamentos de IA generativa, ciclo de desarrollo AI-DLC, modelos fundacionales en AWS Bedrock y taller avanzado de agentes de IA.</p>
    <div class="cc-skills">
      <span>AWS Bedrock</span>
      <span>Claude 3.5 Sonnet</span>
      <span>AI Agents</span>
      <span>Responsible AI</span>
    </div>
    <div class="cc-links">
      <a href="aws-agentes-ia/" class="cc-btn primary">Ver Ruta AWS</a>
    </div>
  </div>

  <div class="course-card" data-cat="aws">
    <div class="cc-header">
      <span class="cc-badge aws">AWS · Cloud Computing</span>
      <span class="cc-status done">Completado 100%</span>
    </div>
    <h3>AWS Entrena · Nube para Empresas</h3>
    <p>Fundamentos de computación en la nube, infraestructura global de AWS, modelos de servicio (IaaS, PaaS, SaaS) y modernización empresarial.</p>
    <div class="cc-skills">
      <span>Cloud Adoption</span>
      <span>Well-Architected</span>
      <span>EC2 & S3</span>
      <span>Seguridad Nube</span>
    </div>
    <div class="cc-links">
      <a href="aws-nube-empresas/" class="cc-btn primary">Ver Ruta AWS</a>
    </div>
  </div>

  <div class="course-card" data-cat="aws">
    <div class="cc-header">
      <span class="cc-badge aws">AWS · Cloud Practitioner</span>
      <span class="cc-status done">13 de 13 módulos · 100% en evaluaciones</span>
    </div>
    <h3>AWS Cloud Practitioner Essentials</h3>
    <p>Curso oficial de AWS: computación, redes, almacenamiento, bases de datos, IA/ML, seguridad y gobernanza, con tarjetas de estudio y preguntas de cada evaluación.</p>
    <div class="cc-skills">
      <span>EC2 & Lambda</span>
      <span>VPC</span>
      <span>S3 & RDS</span>
      <span>IAM</span>
      <span>CloudWatch</span>
    </div>
    <div class="cc-links">
      <a href="aws-cloud-practitioner/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="google">
    <div class="cc-header">
      <span class="cc-badge google">Google · GEAR</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>GEAR Agentes: Fundamentos y Empresas</h3>
    <p>Arquitectura de agentes autónomos con modelos Gemini, razonamiento ReAct, orquestación de herramientas y despliegue empresarial.</p>
    <div class="cc-skills">
      <span>Gemini 1.5 Pro</span>
      <span>ReAct Framework</span>
      <span>Tool Calling</span>
      <span>Enterprise</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-agentes/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="google">
    <div class="cc-header">
      <span class="cc-badge google">Google · Agent SDK</span>
      <span class="cc-status done">Insignia GSP540 (100/100)</span>
    </div>
    <h3>GEAR ADK: Kit de Desarrollo de Agentes</h3>
    <p>Laboratorio de desafío superado con 100 puntos: control de memoria, sesiones de usuario, estado persistente y herramientas externas.</p>
    <div class="cc-skills">
      <span>Agent SDK</span>
      <span>Memory & State</span>
      <span>Custom Tools</span>
      <span>GSP540 Lab</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-adk/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="google">
    <div class="cc-header">
      <span class="cc-badge google">Google · Producción</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>GEAR Producción: Implementación Real</h3>
    <p>Implementación de agentes con alta disponibilidad, observabilidad, manejo de latencia, fallbacks y patrones resilientes.</p>
    <div class="cc-skills">
      <span>Production Readiness</span>
      <span>Observability</span>
      <span>Latency Optimization</span>
      <span>Fault Tolerance</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-produccion/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="google">
    <div class="cc-header">
      <span class="cc-badge google">Google · Escala</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>GEAR Escala: Agentes Empresariales</h3>
    <p>Transformación organizacional con agentes, IA centrada en el humano y flujos de trabajo multiagente con Gemini Enterprise.</p>
    <div class="cc-skills">
      <span>Enterprise Scale</span>
      <span>Human-in-the-Loop</span>
      <span>Workflows</span>
      <span>Gemini Enterprise</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-escala/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="google">
    <div class="cc-header">
      <span class="cc-badge google">Google · Multiagente</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>GEAR Multiagente: Alto Rendimiento</h3>
    <p>Sistemas multiagente colaborativos con ADK y MCP, reparto de tareas especializadas, protocolos de comunicación inter-agente y evaluación.</p>
    <div class="cc-skills">
      <span>Multiagent Systems</span>
      <span>ADK + MCP</span>
      <span>Agent Communication</span>
      <span>Benchmarking</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-multiagente/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="google">
    <div class="cc-header">
      <span class="cc-badge google">Google · Seguridad IA</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>GEAR Gobierno y Seguridad: Protección</h3>
    <p>Protección de agentes corporativos con Model Armor, mitigación de inyecciones de prompt, prevención de fuga de datos y auditoría.</p>
    <div class="cc-skills">
      <span>Model Armor</span>
      <span>Prompt Injection</span>
      <span>Data Leak Prevention</span>
      <span>Governance</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-gobierno-seguridad/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Academy</span>
      <span class="cc-status done">Ruta Central</span>
    </div>
    <h3>Claude Academy: Insignias y Rutas</h3>
    <p>Centro de insignias oficiales de Anthropic, seguimiento curricular y estándares de ingeniería de software asistida por IA.</p>
    <div class="cc-skills">
      <span>Claude 3.5 Sonnet</span>
      <span>Anthropic API</span>
      <span>Artifacts</span>
      <span>Projects</span>
    </div>
    <div class="cc-links">
      <a href="claude-academy/" class="cc-btn primary">Ver Academy</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Tips</span>
      <span class="cc-status done">Guía Práctica</span>
    </div>
    <h3>Tips & Tricks de Claude</h3>
    <p>Recetario de patrones avanzados de prompting, razonamiento estructurado XML, metaprompts, encadenamiento de tareas y optimización.</p>
    <div class="cc-skills">
      <span>XML Prompting</span>
      <span>Metaprompts</span>
      <span>Reasoning Chains</span>
      <span>Token Efficiency</span>
    </div>
    <div class="cc-links">
      <a href="claude-tips/" class="cc-btn primary">Ver Guía</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Fundamentos</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>Claude 101: Conocer y Dominar Claude</h3>
    <p>Arquitectura de Claude, proyectos colaborativos, artefactos dinámicos, conectores de datos y búsqueda de nivel empresarial.</p>
    <div class="cc-skills">
      <span>Claude 101</span>
      <span>Artifacts</span>
      <span>Enterprise Search</span>
      <span>Connectors</span>
    </div>
    <div class="cc-links">
      <a href="claude-101/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · CLI Tool</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>Claude Code 101: Terminal & Autonomía</h3>
    <p>Instalación, configuración y flujos de trabajo terminales con la herramienta oficial Claude Code para desarrollo de software autónomo.</p>
    <div class="cc-skills">
      <span>Claude Code CLI</span>
      <span>Pair Programming</span>
      <span>Terminal Workflows</span>
      <span>Context Memory</span>
    </div>
    <div class="cc-links">
      <a href="claude-code-101/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Colaboración</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>Introduction to Claude Cowork</h3>
    <p>Patrones de interacción humano-IA en tiempo real, colaboración en documentos, diseño de software y refactorizaciones conjuntas.</p>
    <div class="cc-skills">
      <span>Coworking Patterns</span>
      <span>Iterative Refinement</span>
      <span>Review Cycles</span>
    </div>
    <div class="cc-links">
      <a href="claude-cowork/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Etiquetado</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>Introduction to Claude Tag</h3>
    <p>Clasificación y etiquetado masivo de datos mediante Claude, estructuración de metadatos y curaduría automatizada de datasets.</p>
    <div class="cc-skills">
      <span>Tagging</span>
      <span>Data Classification</span>
      <span>Dataset Curation</span>
      <span>Taxonomies</span>
    </div>
    <div class="cc-links">
      <a href="claude-tag/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Práctica CLI</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>Claude Code in Action: Pair Programming</h3>
    <p>Desarrollo asistido extremo: depuración de repositorios complejos, creación de pruebas unitarias y migraciones de código completas.</p>
    <div class="cc-skills">
      <span>Full-stack Debugging</span>
      <span>Automated Testing</span>
      <span>Code Migration</span>
    </div>
    <div class="cc-links">
      <a href="claude-code-in-action/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Plataforma</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>Claude Platform 101: API & Tools</h3>
    <p>Integración vía API de Anthropic, configuración de tool calling, streaming responses, autenticación y control de costos.</p>
    <div class="cc-skills">
      <span>Anthropic API</span>
      <span>Tool Calling</span>
      <span>Streaming</span>
      <span>Cost Controls</span>
    </div>
    <div class="cc-links">
      <a href="claude-platform-101/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · MCP</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>Introduction to Model Context Protocol</h3>
    <p>El protocolo estándar abierto para conectar modelos con herramientas, bases de datos y APIs externas de forma segura.</p>
    <div class="cc-skills">
      <span>MCP Protocol</span>
      <span>JSON-RPC</span>
      <span>Resources & Prompts</span>
      <span>MCP Tools</span>
    </div>
    <div class="cc-links">
      <a href="mcp-intro/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · MCP Avanzado</span>
      <span class="cc-status done">Insignia Obtenida</span>
    </div>
    <h3>MCP: Advanced Topics & Orchestration</h3>
    <p>Orquestación multi-servidor MCP, transporte stdio vs SSE, seguridad perimetral, proxies y control de concurrencia.</p>
    <div class="cc-skills">
      <span>Multi-server MCP</span>
      <span>Transport SSE/Stdio</span>
      <span>MCP Security</span>
      <span>Orchestration</span>
    </div>
    <div class="cc-links">
      <a href="mcp-advanced/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · API 1P</span>
      <span class="cc-status done">Completado</span>
    </div>
    <h3>Building with the Claude API</h3>
    <p>Messages API, alternancia de roles, ingeniería de prompts, XML tags, CoT (&lt;thinking&gt;), prefill, mitigación de alucinaciones, evals sistemáticos, Tool Use y Prompt Caching.</p>
    <div class="cc-skills">
      <span>Messages API</span>
      <span>Prompt Engineering</span>
      <span>Prompt Caching</span>
      <span>Tool Use</span>
      <span>Evals</span>
    </div>
    <div class="cc-links">
      <a href="building-claude-api/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · AWS Bedrock</span>
      <span class="cc-status done">Completado</span>
    </div>
    <h3>Claude with Amazon Bedrock</h3>
    <p>Despliegue empresarial de Claude en AWS: arquitectura VPC, IAM, KMS, SDK AnthropicBedrock, boto3 Converse API, perfiles de inferencia cross-region y toolConfig.</p>
    <div class="cc-skills">
      <span>AWS Bedrock</span>
      <span>Converse API</span>
      <span>Cross-Region</span>
      <span>IAM & KMS</span>
    </div>
    <div class="cc-links">
      <a href="claude-bedrock/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="anthropic">
    <div class="cc-header">
      <span class="cc-badge anthropic">Anthropic · Google Cloud</span>
      <span class="cc-status done">Completado</span>
    </div>
    <h3>Claude on Google Cloud</h3>
    <p>Integración de Claude en Vertex AI Model Garden: SDK AnthropicVertex, autenticación ADC y cuentas de servicio, modelos con @, streaming y conexión con BigQuery.</p>
    <div class="cc-skills">
      <span>Vertex AI</span>
      <span>AnthropicVertex</span>
      <span>GCP ADC</span>
      <span>BigQuery Integration</span>
    </div>
    <div class="cc-links">
      <a href="claude-google-cloud/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="data">
    <div class="cc-header">
      <span class="cc-badge mongo">MongoDB · Atlas</span>
      <span class="cc-status done">Completado</span>
    </div>
    <h3>Getting Started with MongoDB Atlas</h3>
    <p>Despliegue y configuración de clusters multirregión en Atlas, seguridad de red, gestión de usuarios y monitoreo de rendimiento.</p>
    <div class="cc-skills">
      <span>MongoDB Atlas</span>
      <span>Cluster Config</span>
      <span>Network Peering</span>
      <span>Security Rules</span>
    </div>
    <div class="cc-links">
      <a href="mongodb-atlas/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="data">
    <div class="cc-header">
      <span class="cc-badge mongo">MongoDB · Python</span>
      <span class="cc-status done">Insignias CRUD</span>
    </div>
    <h3>MongoDB Python Developer Path</h3>
    <p>Modelo de documentos, operaciones CRUD con PyMongo, índices compuestos (ESR), pipelines de agregación y transacciones ACID.</p>
    <div class="cc-skills">
      <span>PyMongo</span>
      <span>Aggregation Pipeline</span>
      <span>Indexing (ESR)</span>
      <span>Transactions</span>
    </div>
    <div class="cc-links">
      <a href="mongodb-python-path/" class="cc-btn primary">Ver Ruta MongoDB</a>
    </div>
  </div>

  <div class="course-card" data-cat="ubits">
    <div class="cc-header">
      <span class="cc-badge ubits">UBITS · Tendencias</span>
      <span class="cc-status done">Completado 100%</span>
    </div>
    <h3>El Futuro de la IA: AI 2041 & Ética</h3>
    <p>Visión prospectiva hacia el 2041, impacto en el empleo, gobernanza ética de algoritmos y técnicas de formulación estratégica de prompts.</p>
    <div class="cc-skills">
      <span>AI 2041</span>
      <span>AI Ethics</span>
      <span>Strategic Prompting</span>
      <span>Future Trends</span>
    </div>
    <div class="cc-links">
      <a href="ubits-futuro-ia/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <div class="course-card" data-cat="ubits">
    <div class="cc-header">
      <span class="cc-badge ubits">UBITS · Plan Experis IA</span>
      <span class="cc-status progress">En curso</span>
    </div>
    <h3>Plan de formación en IA generativa 2026</h3>
    <p>32 cursos: IA generativa, prompt engineering, agentes, ChatGPT aplicado a negocios, finanzas y analítica, y habilidades de comunicación y gestión de conflictos.</p>
    <div class="cc-skills">
      <span>GenAI</span>
      <span>Prompting</span>
      <span>Business Analytics</span>
      <span>Soft Skills</span>
    </div>
    <div class="cc-links">
      <a href="ubits-experis-ia/" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

</div>

<script>
let currentCat = 'all';

function setCategory(cat) {
  currentCat = cat;
  document.querySelectorAll('.cf-btn').forEach(b => {
    if (b.getAttribute('data-cat') === cat) {
      b.classList.add('active');
    } else {
      b.classList.remove('active');
    }
  });
  filterAllCourses();
}

function filterAllCourses() {
  const query = (document.getElementById('courseSearch').value || '').toLowerCase().trim();
  const cards = document.querySelectorAll('.course-card');

  cards.forEach(card => {
    const cardCat = card.getAttribute('data-cat');
    const text = card.textContent.toLowerCase();
    const matchCat = (currentCat === 'all' || cardCat === currentCat);
    const matchQuery = (!query || text.includes(query));

    if (matchCat && matchQuery) {
      card.style.display = 'flex';
      card.style.animation = 'fadeInUp 0.25s ease';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>
