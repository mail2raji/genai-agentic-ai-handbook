# 🎓 GenAI & Agentic AI — Beginner to Advanced Handbook

> **Who is this for?** A complete beginner with **zero** prior knowledge of AI, LangChain, agents, or Git — but who is willing to type code and run exercises.
>
> **Promise:** By the end you will be able to (1) version code with Git + GitHub, (2) ship CI/CD with GitHub Actions, (3) pair with GitHub Copilot at every layer, (4) talk to LLMs from Python, (5) build a RAG pipeline over your own documents, (6) build single and multi-agent systems with LangChain / LangGraph / CrewAI, and (7) ship a production agent to Kubernetes — with GHAS security on top.

---

## 📚 The book has **two tracks** — pick the one that fits how you learn

| Track | Best for | Format |
|---|---|---|
| **[Part I — Hands-On Code Lessons](PartI_HandsOn/index.md)** | "Drop me into runnable `.py` and `git` exercises I can execute today" | 18 Phases → ~67 runnable lessons + 4 capstones + GitHub + production track |
| **[Part II — Concept Curriculum](Module1_GenAI_Foundations/01_Introduction_to_GenAI.md)** | "Teach me the ideas first with worked examples + advanced labs" | 5 Modules → 19 lessons + 5 Advanced Labs |

You can read them in any order. Many people skim **Part II** first for the vocabulary, then live inside **Part I**.

> 📥 Prefer offline? Each push builds a downloadable **[PDF + DOCX export](https://github.com/mail2raji/genai-agentic-ai-handbook/actions/workflows/export.yml)** of the entire book — grab the artifact from the latest workflow run.

---

## 🛠️ Part I — The 18-Phase Hands-On Roadmap

Every lesson is a **runnable `.py` file** (or Git exercise) with concept → analogy → example → exercise → solution. Most Python lessons run **offline** in `MOCK_MODE=1` so no API key is needed to start.

| Block | Phases | Theme | Outcome |
|---|---|---|---|
| **Python core** | [Phase 1](PartI_HandsOn/Phase1_Python_Fundamentals/00_START_HERE.md) – [Phase 3](PartI_HandsOn/Phase3_Python_for_AI/00_START_HERE.md) | Python Fundamentals → Intermediate → AI/Data | Log Analyzer, Weather Chatbot, CSV Analyst |
| **GenAI** | [Phase 4](PartI_HandsOn/Phase4_GenAI_Fundamentals/00_START_HERE.md) | LLMs, prompts, embeddings, RAG | Doc Q&A (RAG) |
| **Agents** | [Phase 5](PartI_HandsOn/Phase5_Agentic_AI/00_START_HERE.md) | Function-calling, ReAct, memory, multi-agent, LangGraph | IT Triage Agent |
| **Capstones** | [Phase 6](PartI_HandsOn/Phase6_Capstone_Projects/00_START_HERE.md) | 3 IT-ops capstones | SPN renewal • PowerShell doc buddy • Incident reporter |
| **Production** | [Phase 7](PartI_HandsOn/Phase7_Production_Agents/00_START_HERE.md) | MCP, eval, observability, K8s deploy | FastAPI agent on AKS |
| **Git + GitHub** | [Phase 8](PartI_HandsOn/Phase8_GitHub_Setup/index.md) – [Phase 11](PartI_HandsOn/Phase11_Intermediate_Git/index.md) | Setup, Git, GitHub basics, intermediate Git | Confident multi-person Git workflows |
| **CI/CD + Copilot** | [Phase 12](PartI_HandsOn/Phase12_GitHub_Actions/index.md) – [Phase 15](PartI_HandsOn/Phase15_Agentic_AI_Copilot/index.md) | Actions, Copilot + GenAI, Copilot CLI, Agentic Copilot | Automated pipelines + AI pair-programming |
| **Security + Exam** | [Phase 16](PartI_HandsOn/Phase16_GHAS_Admin/index.md) – [Phase 18](PartI_HandsOn/Phase18_Capstone/index.md) | GHAS, Exam Prep, final Capstone | GH Advanced Security cert-ready |

> 💡 Jump to the full **[hands-on lab menu](PartI_HandsOn/LAB_MENU.md)** — every exercise in one checklist.

---

## 🗺️ Part II — The 5-Module Concept Roadmap

| Module | What you learn | Why it matters | Time |
|---|---|---|---|
| **1. GenAI Foundations** | What LLMs are, prompts, fine-tuning, RAG, agents | The vocabulary everyone uses | 1 week |
| **2. Python for GenAI** | Python basics, files/DBs, APIs, calling LLMs | Without Python you can't build | 2 weeks |
| **3. LangChain Core** | LangChain, LCEL, prompts, I/O | The most-used GenAI framework | 1 week |
| **4. RAG & Frameworks** | RAG pipelines, LangChain vs LangGraph vs CrewAI | Make AI use *your* data | 1 week |
| **5. Agentic AI** | Design patterns + 4 agents you build from scratch | The frontier of AI in 2026 | 2 weeks |

### 🧪 Advanced Labs (one per module)

Every concept module ends with a **production-flavoured capstone lab** built around a real-world scenario. These are the labs you can put in your portfolio.

| Lab | Scenario | What you build |
|---|---|---|
| [M1 — Support Triage Assistant](Module1_GenAI_Foundations/99_Advanced_Lab_Support_Triage.md) | NimbusCloud (SaaS) drowning in tickets | Schema-first JSON triage + audit pass + human-review queue |
| [M2 — Invoice → Insights CLI](Module2_Python_for_GenAI/99_Advanced_Lab_Invoice_Pipeline.md) | PixelLatte CFO needs monthly expense report | 6-stage pipeline: PDF/CSV → SQLite → FX → LLM enrichment → CFO Markdown |
| [M3 — Onboarding Wizard](Module3_LangChain/99_Advanced_Lab_Onboarding_Wizard.md) | AuroraBank HR onboards in 12 countries | LCEL chain with extract → route → parallel plan/video → memory chat |
| [M4 — Legal RAG with Reranker](Module4_RAG_and_Frameworks/99_Advanced_Lab_Legal_RAG.md) | OrbitLegal reviews 200 NDAs/month | Clause-aware chunking + hybrid BM25/vector + cross-encoder + citations |
| [M5 — Friday Ship Engineering Crew](Module5_Agentic_AI/99_Advanced_Lab_Engineering_Crew.md) | NovaDB CEO demands a tool by Monday | 5-agent crew (PM/Architect/Coder/Tester/Reviewer) with RAG + reflection |

---

## 🧒 How each lesson is written

Every lesson uses **the same 6 sections** so your brain knows what to expect:

1. **🍭 Imagine this…** — a tiny story to explain the idea (5-year-old level)
2. **🧠 The real concept** — the technical bit, in plain English
3. **🌍 Real-world scenario** — where you'd actually use it (IT support, banking, healthcare, etc.)
4. **💻 The code** — copy-paste ready, *with every line explained*
5. **🏋️ Exercises** — 3 to 5 challenges that grow in difficulty
6. **✅ Solutions** — complete, working answers with explanation

---

## 🚀 How to use this handbook

1. **Start with [SETUP](SETUP.md)** — install Python, Git, and get an API key.
2. **Read in order** within each Part. Phases assume the previous ones.
3. **Type the code yourself.** Don't just copy. Your fingers learn what your eyes can't.
4. **Do every exercise** before peeking at the solution.
5. **Build a tiny project** at the end of each phase — even just a 20-line one.

---

## 🛠️ Tools we'll use

- **Python 3.10+** — the language
- **Git + GitHub CLI** — version control and collaboration
- **GitHub Copilot** + **Copilot CLI** — your AI pair-programmer
- **GitHub Actions** + **GHAS** — CI/CD and security scanning
- **OpenAI SDK** *or* **Azure OpenAI** — to call GPT-4o / GPT-4o-mini
- **LangChain + LangGraph** — orchestration framework
- **CrewAI** — multi-agent framework
- **ChromaDB / FAISS** — vector databases for RAG
- **VS Code** — your IDE

---

## 💸 Will this cost money?

- LLM API calls cost cents. A whole phase rarely costs more than **$1**.
- You can swap in **free local models** (Ollama + Llama 3) — instructions are in [SETUP](SETUP.md).

---

## 🏁 Where to go next

When you finish all 18 phases + 5 modules:

- Build a portfolio project (e.g., *"Personal finance Q&A agent over my bank statements"*).
- Learn **evaluation** (Ragas, DeepEval) and **observability** (LangSmith, Langfuse).
- Explore production deployment on **Azure AI Foundry** or **AWS Bedrock**.

---

Happy learning! 🎉 Open **[SETUP](SETUP.md)** to begin, or jump straight into **[Phase 1 — Hello World](PartI_HandsOn/Phase1_Python_Fundamentals/01_hello_world.md)**.
