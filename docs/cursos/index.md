# Hub Central de Aprendizajes & Cursos

<div class="cyber-hero-banner" style="background: linear-gradient(135deg, #1e1e38 0%, #303f9f 50%, #1a237e 100%);">
  <div class="cyber-hero-badge">PLATAFORMA INTEGRAL DE FORMACIÓN TÉCNICA · ERICK SANG</div>
  <h2 style="color:#fff; border:none; margin:10px 0;">Base de Conocimiento y Certificaciones</h2>
  <p style="color:rgba(255,255,255,0.9);">Rutas de aprendizaje completadas y en curso: Ciberseguridad, Inteligencia Artificial, Cloud Computing, Arquitectura de Datos y Desarrollo de Software.</p>
</div>

---

## 🧭 Explorar por Categoría

<div class="courses-filter-bar">
  <button type="button" class="cf-btn active" onclick="filterCourses('all')">Todos (21)</button>
  <button type="button" class="cf-btn" onclick="filterCourses('sena')">🏛️ SENA (2)</button>
  <button type="button" class="cf-btn" onclick="filterCourses('aws')">☁️ AWS (2)</button>
  <button type="button" class="cf-btn" onclick="filterCourses('google')">🤖 Google GEAR (6)</button>
  <button type="button" class="cf-btn" onclick="filterCourses('anthropic')">🧠 Anthropic & MCP (8)</button>
  <button type="button" class="cf-btn" onclick="filterCourses('data')">🍃 Bases de Datos (2)</button>
  <button type="button" class="cf-btn" onclick="filterCourses('ubits')">💡 UBITS (1)</button>
</div>

<div class="courses-grid" id="coursesGrid">

  <!-- SENA CIBERSEGURIDAD -->
  <div class="course-card" data-cat="sena">
    <div class="cc-badge sena">SENA · CIBERSEGURIDAD</div>
    <div class="cc-status done">Calificado A / En Curso</div>
    <h3>Apropiación de Conceptos en Ciberseguridad</h3>
    <p>Valuación de activos de información, mapa de amenazas según NIST SP 800-30, matriz formal de riesgo ISO 27001 y tablero interactivo de ciberdefensa.</p>
    <div class="cc-skills">
      <span>ISO 27001</span>
      <span>MAGERIT v3</span>
      <span>NIST 800-30</span>
      <span>CID Triad</span>
      <span>Hardening</span>
    </div>
    <div class="cc-links">
      <a href="sena-ciberseguridad/index.md" class="cc-btn primary">Ver Curso</a>
      <a href="sena-ciberseguridad/tablero-interactivo.md" class="cc-btn secondary">🎮 Tablero Interactivo</a>
    </div>
  </div>

  <!-- SENA IA INTEGRACIÓN DATOS -->
  <div class="course-card" data-cat="sena">
    <div class="cc-badge sena">SENA · IA & DATOS</div>
    <div class="cc-status done">Completado 100%</div>
    <h3>Aplicación de la IA en la Integración de Datos</h3>
    <p>Pipeline completo con Polars, DuckDB, generación de prompts verificados, esquema estrella y proyecto de analítica en Power BI (PBIP/TMDL).</p>
    <div class="cc-skills">
      <span>Polars</span>
      <span>DuckDB</span>
      <span>Power BI</span>
      <span>DAX / TMDL</span>
      <span>Prompt Eng.</span>
    </div>
    <div class="cc-links">
      <a href="sena-ia-integracion-datos/index.md" class="cc-btn primary">Ver Curso</a>
      <a href="sena-ia-integracion-datos/aa2-ev03-powerbi.md" class="cc-btn secondary">📊 Tablero Power BI</a>
    </div>
  </div>

  <!-- AWS IA SIN LÍMITES -->
  <div class="course-card" data-cat="aws">
    <div class="cc-badge aws">AWS · AGENTES & IA</div>
    <div class="cc-status done">Completado 100%</div>
    <h3>AWS Entrena · IA sin Límites</h3>
    <p>Fundamentos de IA generativa, ciclo de desarrollo AI-DLC, modelos fundacionales en AWS Bedrock y taller avanzado de agentes de IA.</p>
    <div class="cc-skills">
      <span>AWS Bedrock</span>
      <span>Claude 3.5</span>
      <span>AI Agents</span>
      <span>Responsible AI</span>
    </div>
    <div class="cc-links">
      <a href="aws-agentes-ia/index.md" class="cc-btn primary">Ver Ruta AWS</a>
    </div>
  </div>

  <!-- AWS NUBE EMPRESAS -->
  <div class="course-card" data-cat="aws">
    <div class="cc-badge aws">AWS · CLOUD COMPUTING</div>
    <div class="cc-status done">Completado 100%</div>
    <h3>AWS Entrena · Nube para Empresas</h3>
    <p>Fundamentos de computación en la nube, infraestructura global, modelos de servicio (IaaS, PaaS, SaaS) y webinars de modernización.</p>
    <div class="cc-skills">
      <span>EC2 / S3</span>
      <span>Cloud Adoption</span>
      <span>Well-Architected</span>
    </div>
    <div class="cc-links">
      <a href="aws-nube-empresas/index.md" class="cc-btn primary">Ver Ruta AWS</a>
    </div>
  </div>

  <!-- GOOGLE GEAR AGENTES -->
  <div class="course-card" data-cat="google">
    <div class="cc-badge google">GOOGLE · GEAR</div>
    <div class="cc-status done">Insignia Obtenida</div>
    <h3>GEAR Agentes: Fundamentos y Empresas</h3>
    <p>Arquitectura de agentes autónomos con modelos Gemini, razonamiento ReAct, orquestación de herramientas y despliegue empresarial.</p>
    <div class="cc-skills">
      <span>Gemini 1.5</span>
      <span>ReAct</span>
      <span>Tool Calling</span>
      <span>Enterprise</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-agentes/index.md" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <!-- GOOGLE GEAR ADK -->
  <div class="course-card" data-cat="google">
    <div class="cc-badge google">GOOGLE · AGENT SDK</div>
    <div class="cc-status done">Insignia GSP540 (100/100)</div>
    <h3>GEAR ADK: Kit de Desarrollo de Agentes</h3>
    <p>Laboratorio de desafío superado con 100 puntos: control de memoria, sesiones de usuario, estado persistente y extensión con APIs externas.</p>
    <div class="cc-skills">
      <span>Agent SDK</span>
      <span>Memory / State</span>
      <span>Tools API</span>
      <span>GSP540</span>
    </div>
    <div class="cc-links">
      <a href="google-gear-adk/index.md" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <!-- ANTHROPIC CLAUDE CODE -->
  <div class="course-card" data-cat="anthropic">
    <div class="cc-badge anthropic">ANTHROPIC · CLAUDE</div>
    <div class="cc-status done">Completado</div>
    <h3>Claude Code in Action & Cowork</h3>
    <p>Desarrollo asistido por agentes en terminal con Claude Code, workflows avanzados de pair-programming, contexto persistente y automatización.</p>
    <div class="cc-skills">
      <span>Claude Code</span>
      <span>CLI Workflows</span>
      <span>Autonomous Refactor</span>
    </div>
    <div class="cc-links">
      <a href="claude-code-in-action/index.md" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <!-- MODEL CONTEXT PROTOCOL -->
  <div class="course-card" data-cat="anthropic">
    <div class="cc-badge anthropic">ANTHROPIC · MCP</div>
    <div class="cc-status done">Completado</div>
    <h3>Model Context Protocol (MCP) · Intro & Advanced</h3>
    <p>Creación de servidores y clientes MCP para conectar modelos de lenguaje con bases de datos, APIs y herramientas de sistema operativo.</p>
    <div class="cc-skills">
      <span>MCP Protocol</span>
      <span>JSON-RPC</span>
      <span>Tools & Resources</span>
    </div>
    <div class="cc-links">
      <a href="mcp-intro/index.md" class="cc-btn primary">Ver Curso MCP</a>
    </div>
  </div>

  <!-- MONGODB DEVELOPER PATH -->
  <div class="course-card" data-cat="data">
    <div class="cc-badge mongo">MONGODB UNIVERSITY</div>
    <div class="cc-status done">Insignias CRUD</div>
    <h3>MongoDB Python Developer Path</h3>
    <p>Modelo de documentos, operaciones CRUD avanzadas con PyMongo, índices, pipelines de agregación y conexión segura con MongoDB Atlas.</p>
    <div class="cc-skills">
      <span>MongoDB Atlas</span>
      <span>PyMongo</span>
      <span>Aggregation</span>
      <span>Data Modeling</span>
    </div>
    <div class="cc-links">
      <a href="mongodb-python-path/index.md" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

  <!-- UBITS FUTURO IA -->
  <div class="course-card" data-cat="ubits">
    <div class="cc-badge ubits">UBITS · TENDENCIAS</div>
    <div class="cc-status done">Completado 100%</div>
    <h3>El Futuro de la IA: AI 2041 & Ética</h3>
    <p>Impacto socioeconómico de la inteligencia artificial, casos de estudio hacia el 2041, sustitución laboral, marcos éticos y prompteado estratégico.</p>
    <div class="cc-skills">
      <span>AI 2041</span>
      <span>AI Ethics</span>
      <span>Strategic Prompts</span>
    </div>
    <div class="cc-links">
      <a href="ubits-futuro-ia/index.md" class="cc-btn primary">Ver Curso</a>
    </div>
  </div>

</div>

<script>
function filterCourses(cat) {
  document.querySelectorAll('.cf-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');

  const cards = document.querySelectorAll('.course-card');
  cards.forEach(c => {
    if (cat === 'all' || c.getAttribute('data-cat') === cat) {
      c.style.display = 'flex';
      c.style.animation = 'fadeInUp 0.3s ease';
    } else {
      c.style.display = 'none';
    }
  });
}
</script>
