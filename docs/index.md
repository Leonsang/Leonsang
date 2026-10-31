---
hide:
  - navigation
  - toc
---

<div class="hero-section">
  <div class="hero-content">
    <div class="hero-badge">
      <span class="badge-dot"></span>
      Repositorio Técnico & Segunda Memoria Digital
    </div>
    <h1 class="hero-title">
      Base de Conocimiento
    </h1>
    <p class="hero-subtitle">
      Arquitecturas Lakehouse, Ingeniería de Datos en Cloud e Inteligencia Artificial Generativa aplicada a entornos reales de producción.
    </p>
    <div class="hero-pills">
      <span class="hero-pill">⚡ Apache Spark & DLT</span>
      <span class="hero-pill">🏢 Databricks Unity Catalog</span>
      <span class="hero-pill">🤖 Claude 3.5 & MCP</span>
      <span class="hero-pill">☁️ AWS · Azure · GCP</span>
      <span class="hero-pill">🐍 Python & SQL Moderno</span>
    </div>
    <div class="hero-buttons">
      <a href="cursos/" class="hero-button primary">
        🏆 Explorar Cursos & Certificaciones
      </a>
      <a href="#ecosistemas-tecnologicos" class="hero-button secondary">
        🧭 Explorar Ecosistemas
      </a>
      <a href="humano-conocimiento/" class="hero-button tertiary">
        🧠 Mapa 3D Interactivo
      </a>
    </div>
  </div>
</div>

<div class="stats-strip">
  <div class="stat-card">
    <div class="stat-number">15+</div>
    <div class="stat-label">Cursos & Certificaciones</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">25+</div>
    <div class="stat-label">Notebooks Hands-On Spark</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">3</div>
    <div class="stat-label">Nubes Empresariales</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">100%</div>
    <div class="stat-label">Práctica & Código Real</div>
  </div>
</div>

<h2 id="ecosistemas-tecnologicos" style="text-align: center; margin-top: 3.5rem; margin-bottom: 0.5rem; font-weight: 800; font-size: 2rem;">
  Ecosistemas de Especialización
</h2>
<p style="text-align: center; color: var(--md-default-fg-color--light); margin-bottom: 2.2rem; max-width: 680px; margin-left: auto; margin-right: auto; font-size: 1rem;">
  Estructura centralizada de documentación, arquitecturas de referencia, notas técnicas y laboratorios ejecutables.
</p>

<div class="ecosystem-grid">
  <!-- Tarjeta 1: Big Data & Lakehouse -->
  <div class="eco-card">
    <div class="eco-header">
      <div class="eco-icon">🐘</div>
      <h3>Data Engineering & Lakehouse</h3>
    </div>
    <p class="eco-desc">
      Diseño de pipelines analíticos batch y streaming, lakehouses transaccionales ACID con Delta Lake y Databricks Unity Catalog, orquestación con Apache Airflow y transformaciones modernas con dbt.
    </p>
    <div class="eco-tags">
      <span class="eco-tag">Apache Spark</span>
      <span class="eco-tag">Databricks</span>
      <span class="eco-tag">Delta Lake</span>
      <span class="eco-tag">Kafka</span>
      <span class="eco-tag">Airflow</span>
      <span class="eco-tag">dbt</span>
    </div>
    <div class="eco-links">
      <a href="data-engineering/" class="eco-link-btn">Fundamentos →</a>
      <a href="spark/" class="eco-link-btn">Apache Spark →</a>
      <a href="databricks/" class="eco-link-btn">Databricks →</a>
      <a href="kafka/" class="eco-link-btn">Streaming Kafka →</a>
    </div>
  </div>

  <!-- Tarjeta 2: IA Generativa & Agentes -->
  <div class="eco-card">
    <div class="eco-header">
      <div class="eco-icon">🤖</div>
      <h3>IA Generativa & Agentes Autónomos</h3>
    </div>
    <p class="eco-desc">
      Construcción de agentes de software con Claude de Anthropic, diseño de herramientas tipadas (Tool Use), adopción del Model Context Protocol (MCP), Prompt Caching, evals con Promptfoo y despliegue multi-cloud.
    </p>
    <div class="eco-tags">
      <span class="eco-tag">Claude 3.5</span>
      <span class="eco-tag">Model Context Protocol</span>
      <span class="eco-tag">Tool Use</span>
      <span class="eco-tag">Prompt Caching</span>
      <span class="eco-tag">Promptfoo</span>
    </div>
    <div class="eco-links">
      <a href="cursos/claude-academy/" class="eco-link-btn">Claude Academy →</a>
      <a href="cursos/building-claude-api/" class="eco-link-btn">Building Claude API →</a>
      <a href="cursos/mcp-intro/" class="eco-link-btn">Protocolo MCP →</a>
    </div>
  </div>

  <!-- Tarjeta 3: Cloud & DevOps -->
  <div class="eco-card">
    <div class="eco-header">
      <div class="eco-icon">☁️</div>
      <h3>Multi-Cloud & DevOps</h3>
    </div>
    <p class="eco-desc">
      Arquitectura de nube empresarial y despliegue distribuido en Amazon Web Services (Bedrock, S3, IAM), Microsoft Azure (ADLS Gen2, Data Factory, Bicep/ARM), Google Cloud (BigQuery, Vertex AI) y Microsoft Fabric.
    </p>
    <div class="eco-tags">
      <span class="eco-tag">AWS Bedrock</span>
      <span class="eco-tag">Azure ADLS & ADF</span>
      <span class="eco-tag">Google Vertex AI</span>
      <span class="eco-tag">Microsoft Fabric</span>
      <span class="eco-tag">Bicep / ARM</span>
    </div>
    <div class="eco-links">
      <a href="cloud/" class="eco-link-btn">Cloud Computing →</a>
      <a href="cursos/claude-bedrock/" class="eco-link-btn">AWS Bedrock →</a>
      <a href="cursos/claude-google-cloud/" class="eco-link-btn">GCP Vertex AI →</a>
      <a href="microsoft-fabric/" class="eco-link-btn">Fabric →</a>
    </div>
  </div>

  <!-- Tarjeta 4: Analítica & Programación -->
  <div class="eco-card">
    <div class="eco-header">
      <div class="eco-icon">📊</div>
      <h3>Data Analysis & Desarrollo</h3>
    </div>
    <p class="eco-desc">
      Técnicas avanzadas de programación en Python, consultas analíticas optimizadas en SQL, modelado dimensional (Estrella y Copo de nieve), bases de datos NoSQL con MongoDB Atlas y dashboards en Power BI.
    </p>
    <div class="eco-tags">
      <span class="eco-tag">Python Avanzado</span>
      <span class="eco-tag">SQL Analítico</span>
      <span class="eco-tag">Power BI</span>
      <span class="eco-tag">MongoDB Atlas</span>
      <span class="eco-tag">DuckDB</span>
    </div>
    <div class="eco-links">
      <a href="python/" class="eco-link-btn">Python →</a>
      <a href="sql/" class="eco-link-btn">SQL →</a>
      <a href="bi/" class="eco-link-btn">Power BI →</a>
      <a href="cursos/mongodb-atlas/" class="eco-link-btn">MongoDB Atlas →</a>
    </div>
  </div>
</div>

---

<div class="author-card">
  <div class="author-avatar">👨‍💻</div>
  <div class="author-info">
    <h3>Erick Sang Cifuentes</h3>
    <div class="author-role">Data Engineer & Cloud AI Architect</div>
    <p class="author-bio">
      Especializado en arquitecturas Lakehouse, plataformas cloud-native e integración de inteligencia artificial generativa en producción. Este espacio opera como bitácora técnica de aprendizaje continuo, certificaciones y buenas prácticas de ingeniería de datos y software.
    </p>
    <div style="margin-top: 1rem; display: flex; gap: 1.25rem; flex-wrap: wrap;">
      <a href="https://linkedin.com/in/esangc" target="_blank" rel="noopener" class="eco-link-btn" style="color: #0a66c2 !important;">
        <strong>LinkedIn</strong> ↗
      </a>
      <a href="https://github.com/Leonsang" target="_blank" rel="noopener" class="eco-link-btn" style="color: var(--md-default-fg-color) !important;">
        <strong>GitHub</strong> ↗
      </a>
      <a href="mailto:ericksang@gmail.com" class="eco-link-btn" style="color: var(--md-primary-fg-color) !important;">
        <strong>Contacto Directo</strong> ✉
      </a>
      <a href="aviso-legal/" class="eco-link-btn" style="color: var(--md-default-fg-color--light) !important;">
        Aviso Legal & Fuentes →
      </a>
    </div>
  </div>
</div>
