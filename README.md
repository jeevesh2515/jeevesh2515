<div align="center">

# Jeevesh Singale

### **AI & Systems Engineer | Voice AI, Agentic Systems, Evidence-Grounded RAG & 3D WebGL**
*I build AI systems that can be audited: grounded answers, bounded tools, tenant isolation, and evaluation suites that are published along with their limitations.*

Nottingham, UK &nbsp;•&nbsp; [LinkedIn](https://linkedin.com/in/jeevesh-singale07) &nbsp;•&nbsp; [Portfolio](https://jeevesh-portfolio-website-00.vercel.app/) &nbsp;•&nbsp; [Email](mailto:jeevesh2515@gmail.com) &nbsp;•&nbsp; [Sponsor](https://github.com/sponsors/jeevesh2515)

<br/>

<a href="https://github.com/jeevesh2515?tab=followers"><img src="./assets/badges/followers.svg" alt="Followers: 6" height="28" /></a>
<a href="https://github.com/jeevesh2515?tab=repositories"><img src="./assets/badges/stars.svg" alt="Stars: 41" height="28" /></a>
<a href="https://github.com/jeevesh2515"><img src="./assets/badges/views.svg" alt="Profile Views: 235+" height="28" /></a>
<a href="https://github.com/sponsors/jeevesh2515"><img src="./assets/badges/sponsor.svg" alt="Sponsor on GitHub" height="28" /></a>
<a href="https://opensource.org/licenses/MIT"><img src="./assets/badges/license.svg" alt="License: MIT" height="28" /></a>

</div>

---

## 🧭 How I Engineer AI Systems

- **Ground the output.** A model can only say what a tool, a calculator, or a retrieved source supports. If the evidence is missing, the system escalates or refuses.
- **Bound the agent.** Tools are classed by read and write risk. Writes need explicit confirmation, every query is scoped to a tenant, and gates fail closed.
- **Measure, then claim.** Each flagship has a test suite, an evaluation harness, and a written list of what it does *not* yet do.

---

## ⚡ Featured Engineering & Flagship Architectures

<table width="100%">
  <!-- ROW 1: WWB (TOP LEFT) & VOXFLOW -->
  <tr>
    <td width="50%" valign="top">
      <h3>🎮 <a href="https://jeevesh2515.github.io/WWB/">World War B: Bugfront</a></h3>
      <p><b>Style-ranked 3D browser FPS built with Three.js and Rapier physics compiled to WebAssembly (playable live).</b></p>
      <ul>
        <li><b>Engine & 3D WebGL:</b> Custom Three.js PBR rendering pipeline paired with Rapier3D WASM physics, procedural M4 viewmodels, wet-surface shaders, and sub-22 MB assets.</li>
        <li><b>Combat & Style Systems:</b> 8 escalating waves ending in The Warden boss, 7 DMC-style ranks (<code>D</code> &rarr; <code>FRONTBREAKER</code>), 8 stackable augment perks, and Overdrive state.</li>
        <li><b>Duel Mode & Backend:</b> Supabase RLS profiles, match persistence, and a Realtime 1v1 bot-race duel room featuring live peer discovery, state broadcast, and CPU fallback.</li>
      </ul>
      <p>
        <a href="https://jeevesh2515.github.io/WWB/"><img src="https://img.shields.io/badge/PLAY_NOW-In_Browser-FF9A2E?style=flat-square&logo=googlechrome&logoColor=white" /></a>
        <a href="https://github.com/jeevesh2515/WWB"><img src="https://img.shields.io/badge/Repo-WWB-blue?style=flat-square&logo=github&logoColor=white" /></a>
        <img src="https://img.shields.io/badge/Three.js-WebGL-black?style=flat-square&logo=threedotjs&logoColor=white" />
        <img src="https://img.shields.io/badge/Rapier3D-WASM-E05D44?style=flat-square" />
        <img src="https://img.shields.io/badge/Supabase-Realtime-3ECF8E?style=flat-square&logo=supabase&logoColor=white" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🎙️ <a href="https://github.com/jeevesh2515/voxflow-voice-agent-case-study">VoxFlow Voice Agent</a></h3>
      <p><b>Supervised-pilot inbound voice agent for logistics desks handling PO status, stock, and dock bookings.</b></p>
      <ul>
        <li><b>Telephony Pipeline:</b> Amazon Connect + Lex V2 (<code>eu-west-2</code>) bridge &rarr; HMAC-SHA256 Lambda &rarr; FastAPI turn engine &rarr; custom <code>AgentRunner</code> state machine on Groq LLMs.</li>
        <li><b>Tool Safety Contract:</b> 22 identity-scoped tools, 2FA caller verification, PBKDF2 PIN binding (310k iterations), exact-DID tenant routing, and spoken-fact grounding guards.</li>
        <li><b>Audited Evidence:</b> <b>963 backend tests passing</b> on the snapshot, public case study with 19 contract tests, 21 deterministic synthetic runs, threat model, and limitations.</li>
      </ul>
      <p>
        <a href="https://github.com/jeevesh2515/voxflow-voice-agent-case-study"><img src="https://img.shields.io/badge/Case_Study-Public-0ea5e9?style=flat-square&logo=github&logoColor=white" /></a>
        <a href="https://www.voxflow.cc/"><img src="https://img.shields.io/badge/Site-voxflow.cc-0ea5e9?style=flat-square&logo=vercel&logoColor=white" /></a>
        <img src="https://img.shields.io/badge/Tests-963_Passing-22c55e?style=flat-square&logo=pytest&logoColor=white" />
        <img src="https://img.shields.io/badge/Amazon_Connect-Lex_V2-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white" />
        <img src="https://img.shields.io/badge/FastAPI-Groq-009688?style=flat-square&logo=fastapi&logoColor=white" />
      </p>
    </td>
  </tr>
  <!-- ROW 2: FINSENTINEL & CLINICAL RAG -->
  <tr>
    <td width="50%" valign="top">
      <h3>🛡️ <a href="https://github.com/jeevesh2515/finsentinel-case-study">FinSentinel AML Investigation Engine</a></h3>
      <p><b>Local-first AML investigation assistant: deterministic triage, evidence packs, and audit-logged cases.</b></p>
      <ul>
        <li><b>Tenant Isolation:</b> Python backend backed by PostgreSQL row-level security (RLS), tenant-scoped transaction ingestion, and an append-only cryptographic audit trail.</li>
        <li><b>Performance Engineering:</b> Fixed an O(n&sup2;) ranking defect, cutting evidence-pack assembly from <b>1,070 ms to 43.86 ms p50</b>, locked in by a CI benchmark gate (p95 &lt; 60 ms).</li>
        <li><b>Verification & Rigour:</b> <b>771 tests (585 unit + 186 integration)</b>, 7 Playwright E2E suites, 29/29 release checks on synthetic data; explicitly disclaims unverified fraud rates.</li>
      </ul>
      <p>
        <a href="https://github.com/jeevesh2515/finsentinel-case-study"><img src="https://img.shields.io/badge/Case_Study-Public-0ea5e9?style=flat-square&logo=github&logoColor=white" /></a>
        <a href="https://finsentinel-chi.vercel.app/"><img src="https://img.shields.io/badge/Showcase-Vercel-0ea5e9?style=flat-square&logo=vercel&logoColor=white" /></a>
        <img src="https://img.shields.io/badge/Tests-771_Passing-22c55e?style=flat-square&logo=pytest&logoColor=white" />
        <img src="https://img.shields.io/badge/Postgres-RLS-336791?style=flat-square&logo=postgresql&logoColor=white" />
        <img src="https://img.shields.io/badge/Next.js-15-black?style=flat-square&logo=next.js&logoColor=white" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🏥 <a href="https://clinical-workflows.vercel.app">Clinical RAG Agent</a></h3>
      <p><b>Evidence-based clinical workflow assistant for hypertension care, built with safety-first guardrails.</b></p>
      <ul>
        <li><b>Knowledge Spine:</b> Curated Open Knowledge Format (OKF) clinical concepts with hybrid retrieval (dense embeddings + BM25 + Cohere rerank) orchestrated via LangGraph.</li>
        <li><b>Deterministic Calculators:</b> Clinical formulas (eGFR CKD-EPI, MAP, pulse pressure, BMI) exposed as external MCP tools, ensuring the LLM never performs clinical arithmetic.</li>
        <li><b>Evaluated & Traced:</b> <b>250+ automated tests</b>, 55-question golden evaluation dataset, and LangSmith tracing with RAGAS metrics; prominently labelled not clinically validated.</li>
      </ul>
      <p>
        <a href="https://clinical-workflows.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-Vercel-0ea5e9?style=flat-square&logo=vercel&logoColor=white" /></a>
        <a href="https://github.com/jeevesh2515/clinical-rag-agent"><img src="https://img.shields.io/badge/Repo-clinical--rag--agent-blue?style=flat-square&logo=github&logoColor=white" /></a>
        <img src="https://img.shields.io/badge/LangGraph-Orchestrated-1C3C3C?style=flat-square" />
        <img src="https://img.shields.io/badge/MCP-Calculators-6366F1?style=flat-square" />
        <img src="https://img.shields.io/badge/Tests-250+_Passing-22c55e?style=flat-square&logo=pytest&logoColor=white" />
      </p>
    </td>
  </tr>
  <!-- ROW 3: EXPERTIQ & DEV TOOLING -->
  <tr>
    <td width="50%" valign="top">
      <h3>🔍 <a href="https://expertiq-copilot.vercel.app">ExpertIQ Copilot</a></h3>
      <p><b>Expert discovery and research platform combining hybrid vector search with interactive knowledge graphs.</b></p>
      <ul>
        <li><b>Hybrid RAG Pipeline:</b> 6-node LangGraph workflow (analyse &rarr; vector search &rarr; graph expand &rarr; rerank &rarr; summarise &rarr; respond) over ChromaDB and NetworkX with HyDE.</li>
        <li><b>Interactive 3D UI:</b> Next.js 16 + React 19 interface featuring a 3D force-directed knowledge graph for visualizing co-authorship networks, clusters, and citation paths.</li>
        <li><b>Production Harness:</b> Multi-tiered Redis caching, Docker Compose containerization, LangSmith-traced RAGAS evals, and a verified 47-case unit and integration test suite.</li>
      </ul>
      <p>
        <a href="https://expertiq-copilot.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-Vercel-0ea5e9?style=flat-square&logo=vercel&logoColor=white" /></a>
        <a href="https://github.com/jeevesh2515/expertiq-copilot"><img src="https://img.shields.io/badge/Repo-expertiq--copilot-blue?style=flat-square&logo=github&logoColor=white" /></a>
        <img src="https://img.shields.io/badge/Next.js-16-black?style=flat-square&logo=next.js&logoColor=white" />
        <img src="https://img.shields.io/badge/LangGraph-6_Nodes-1C3C3C?style=flat-square" />
        <img src="https://img.shields.io/badge/Tests-47_Passing-22c55e?style=flat-square&logo=pytest&logoColor=white" />
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🧰 <a href="https://github.com/jeevesh2515/pre-push-verify">Developer Tooling for AI Coding Agents</a></h3>
      <p><b>Zero-telemetry local guardrails that block credential leaks, enforce test gates, and audit README facts.</b></p>
      <ul>
        <li><b>Leak Prevention & Gates:</b> <code>pre-push-verify</code> intercepts commits using 30+ regex rules and Shannon entropy to halt leaks, blocking pushes on failed tests with 5 pruning rules.</li>
        <li><b>README Verification CLI:</b> <code>readme-guardian</code> v1.1.2 on PyPI and npm (<code>pipx install readme-guardian</code>) audits repository metrics and claims using <code>--check</code> and <code>--status</code>.</li>
        <li><b>Agent Native Design:</b> Local-first architecture engineered for Claude Code and Antigravity slash commands with Git hook integration to ensure auditable AI pair programming.</li>
      </ul>
      <p>
        <a href="https://github.com/jeevesh2515/pre-push-verify"><img src="https://img.shields.io/badge/Repo-pre--push--verify-blue?style=flat-square&logo=github&logoColor=white" /></a>
        <a href="https://pypi.org/project/readme-guardian/"><img src="https://img.shields.io/badge/PyPI-readme--guardian-3775A9?style=flat-square&logo=pypi&logoColor=white" /></a>
        <a href="https://www.npmjs.com/package/readme-guardian"><img src="https://img.shields.io/badge/npm-readme--guardian-CB3837?style=flat-square&logo=npm&logoColor=white" /></a>
        <img src="https://img.shields.io/badge/Zero-Telemetry-555555?style=flat-square" />
        <img src="https://img.shields.io/badge/Hooks-Claude_Code_%26_AGY-0ea5e9?style=flat-square" />
      </p>
    </td>
  </tr>
</table>

---

## 🚀 Additional Projects

| Project | Highlights & Architecture | Links |
| :--- | :--- | :--- |
| **🧠 Cortex** | Local-first second brain for Obsidian. Hybrid retrieval (LanceDB dense + BM25 + wikilink-graph expansion) fused with RRF, then reranking and cited synthesis. A privacy gate refuses to send sensitive notes to a provider whose data policy does not allow it. A four-state thermal governor schedules indexing on a fanless MacBook Air. It exposes 5 MCP tools. | [Repo](https://github.com/jeevesh2515/cortex) |
| **🎬 Shorts Autopilot (`shorty`)** | Operator-first YouTube Shorts pipeline. Groq Llama 70B writes scripts (OpenRouter and NVIDIA NIM as fallbacks), the YouTube Data API v3 finds topics, and FFmpeg renders. Includes a research-grounding gate, stock-media licence checks, and scheduled OAuth uploads. | [Live Demo](https://shorty-alpha-three.vercel.app) &bull; [Repo](https://github.com/jeevesh2515/shorty) |
| **💸 Splittrack (`expense-tracker`)** | Multi-currency group expense tracker that settles debts with the minimum number of peer-to-peer transfers. Built with Next.js 14 App Router, Turso libSQL, Drizzle ORM, and NextAuth (JWT + bcrypt). | [Repo](https://github.com/jeevesh2515/expense-tracker) |
| **🗺️ AI Engineering Roadmap** | Full-stack learning app with an SSE-streaming AI tutor, an interview simulator, and a 5-phase roadmap. React 19 + Vite 7 frontend, Express 5 + PostgreSQL + Drizzle backend, and OpenAI-compatible providers (Groq, Ollama, OpenRouter, Gemini). | [Repo](https://github.com/jeevesh2515/AI-Engineering-roadmap) |

---

## 🛠️ Technical Stack & Engineering Capabilities

```
Agents & LLMs      : LangGraph, LangChain, custom agent runners, MCP servers & tools, tool-use contracts, structured outputs, Groq
Retrieval & RAG    : Hybrid dense + BM25, RRF fusion, Cohere rerank, HyDE, parent-child chunking, ChromaDB, LanceDB, Pinecone, NetworkX
Voice & Realtime   : Amazon Connect, Lex V2, Amazon Polly, AWS Lambda, WebSockets, Supabase Realtime
Evals & Safety     : LangSmith, RAGAS, golden eval sets, grounding guards, fail-closed gates, threat modelling, HMAC request signing
Backend & Data     : Python, FastAPI, PostgreSQL (RLS), Redis, Supabase, Turso/libSQL, Drizzle, Docker, GitHub Actions
Frontend & 3D      : TypeScript, Next.js 16, React 19, TailwindCSS v4, Vite, Three.js, Rapier3D (WASM)
ML & Analytics     : scikit-learn, XGBoost, PyTorch, SHAP/LIME, Databricks, Apache Spark, Power BI
Testing            : Pytest, Vitest, Playwright, Ruff, mypy
```

---

## 💖 Support & GitHub Sponsors

<div align="center">

[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor_@jeevesh2515-GitHub_Sponsors-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/jeevesh2515)

<p>
I build evidence-grounded clinical AI, safety-bounded voice agents, WASM 3D engines, and open-source guardrails for AI coding agents. Sponsorship pays for evaluation compute, public demo hosting, and ongoing open-source maintenance.
</p>

| Tier | Focus | Impact |
| :--- | :--- | :--- |
| **Supporter & Backer** | Open-source stewardship | Backs open research datasets and public web demo hosting |
| **Startup & Tooling Sponsor** | Developer ecosystems | Sponsor logo and link featured on project READMEs & documentation |
| **Corporate Advisory Partner** | Architecture consulting | 1-on-1 technical advisory on voice agents, RAG guardrails & agent orchestration |

<a href="https://github.com/sponsors/jeevesh2515"><b>Become a GitHub Sponsor &rarr;</b></a>

</div>

---

## 📈 Activity & Contribution Velocity

<table width="100%">
  <tr>
    <td width="50%" align="center" valign="top">
      <img src="./assets/stats.svg" width="100%" alt="GitHub Statistics" />
    </td>
    <td width="50%" align="center" valign="top">
      <img src="./assets/languages.svg" width="100%" alt="My Programming Languages" />
    </td>
  </tr>
  <tr>
    <td colspan="2" width="100%" align="center" valign="top">
      <img src="./assets/activity-graph.svg" width="100%" alt="Contribution Graph" />
    </td>
  </tr>
</table>

---

<div align="center">
  <sub>Built with precision by Jeevesh Singale &bull; Open to AI engineering roles and agent architecture collaborations &bull; Nottingham, UK</sub>
</div>
