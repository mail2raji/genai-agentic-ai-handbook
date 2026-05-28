# 🎓 GenAI & Agentic AI — Beginner to Advanced Handbook

<p align="center" markdown>
  <em>From <strong>zero</strong> to a production-shipped AI agent — <strong>23 chapters · 6 stages · one continuous flow.</strong></em>
</p>

<p align="center" markdown>
  ![Chapters](https://img.shields.io/badge/chapters-23-6f42c1?style=for-the-badge)
  ![Stages](https://img.shields.io/badge/stages-6-blue?style=for-the-badge)
  ![Capstones](https://img.shields.io/badge/capstones-5-success?style=for-the-badge)
  ![Built with](https://img.shields.io/badge/built%20with-MkDocs%20Material-526CFE?style=for-the-badge&logo=materialformkdocs)
  ![License](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)
</p>

<p align="center" markdown>
[:material-rocket-launch: &nbsp; Quick Start](SETUP.md){ .md-button .md-button--primary }
[:material-book-open-variant: &nbsp; Open Chapter 1](curriculum/Chapter01_Python_Fundamentals/00_START_HERE.md){ .md-button }
[:material-flask: &nbsp; Lab Menu](curriculum/LAB_MENU.md){ .md-button }
[:fontawesome-brands-github: &nbsp; Source on GitHub](https://github.com/mail2raji/genai-agentic-ai-handbook){ .md-button }
</p>

---

!!! success "📦 One repo · one continuous flow · 23 chapters in six stages"
    Everything — Python, GenAI, Agents, **and** Git/GitHub/Copilot/GHAS — lives in **one** repository as **one** numbered curriculum: **[mail2raji/genai-agentic-ai-handbook](https://github.com/mail2raji/genai-agentic-ai-handbook)**.

    No more juggling "Part I phase X" vs "Part II module Y" — just **Chapter 1 → Chapter 23**. Read it cover-to-cover, or jump to any chapter and the table-of-contents shows you exactly where you are in the journey.

    ```bash
    git clone https://github.com/mail2raji/genai-agentic-ai-handbook.git
    ```

    …gives you the whole library — code samples, exercises, capstones, the MkDocs source for this site, and the workflows that build it.

??? abstract "🎯 What you'll be able to do after Chapter 23"
    1. **Version code** with Git + GitHub like a pro
    2. **Ship CI/CD** pipelines with GitHub Actions
    3. **Pair with GitHub Copilot** at every layer (chat, CLI, agent mode)
    4. **Talk to LLMs** from Python (OpenAI / Azure / Ollama)
    5. **Build a RAG pipeline** over your own documents
    6. **Build single and multi-agent systems** with LangChain / LangGraph / CrewAI
    7. **Ship a production agent** to Kubernetes — with **GHAS** security on top

---

## 🗺️ The 23-chapter map — six stages, one journey

Each card below is one **stage**. Click any chapter to jump straight in.

<div class="grid cards" markdown>

-   :material-language-python:{ .lg .middle } &nbsp; __Stage A · Python foundations__

    ---

    *Get fluent in the language we'll use for everything.*

    - **[Chapter 1 — Python Fundamentals](curriculum/Chapter01_Python_Fundamentals/00_START_HERE.md)** &nbsp;:material-arrow-right-bold-circle-outline:&nbsp; *Log Analyzer* mini-project
    - **[Chapter 2 — Intermediate Python](curriculum/Chapter02_Intermediate_Python/00_START_HERE.md)** &nbsp;:material-arrow-right-bold-circle-outline:&nbsp; *Weather Chatbot*
    - **[Chapter 3 — Python for AI & Data](curriculum/Chapter03_Python_for_AI_Data/00_START_HERE.md)** &nbsp;:material-arrow-right-bold-circle-outline:&nbsp; *CSV Analyst*
    - **[Chapter 4 — Python for GenAI · deep dive](curriculum/Chapter04_Python_for_GenAI/01_Intro_to_Python.md)** &nbsp;:material-flask-outline:&nbsp; *Invoice → Insights* lab

-   :material-robot-happy:{ .lg .middle } &nbsp; __Stage B · GenAI core__

    ---

    *From "what is a token?" to running real RAG.*

    - **[Chapter 5 — GenAI Fundamentals · hands-on](curriculum/Chapter05_GenAI_Fundamentals/00_START_HERE.md)** &nbsp;:material-arrow-right-bold-circle-outline:&nbsp; *Doc Q&A* mini-project
    - **[Chapter 6 — GenAI Foundations · deep dive](curriculum/Chapter06_GenAI_Foundations/01_Introduction_to_GenAI.md)** &nbsp;:material-flask-outline:&nbsp; *Support Triage Assistant* lab
    - **[Chapter 7 — LangChain Core](curriculum/Chapter07_LangChain_Core/01_Introduction_to_LangChain.md)** &nbsp;:material-flask-outline:&nbsp; *Onboarding Wizard* lab

-   :material-database-search:{ .lg .middle } &nbsp; __Stage C · RAG__

    ---

    *Make AI answer from **your** data.*

    - **[Chapter 8 — RAG Systems & Frameworks](curriculum/Chapter08_RAG_Systems_Frameworks/01_RAG_System_Essentials.md)** &nbsp;:material-flask-outline:&nbsp; *Legal RAG with Reranker* lab

    ??? tip "What you'll learn"
        RAG essentials · LangChain vs LangGraph vs CrewAI · clause-aware chunking · hybrid BM25 + vector · cross-encoder rerank · citations.

-   :material-brain:{ .lg .middle } &nbsp; __Stage D · Agentic AI__

    ---

    *Make AI **do things**, not just answer.*

    - **[Chapter 9 — Agentic AI · hands-on](curriculum/Chapter09_Agentic_AI_HandsOn/00_START_HERE.md)** &nbsp;:material-arrow-right-bold-circle-outline:&nbsp; *IT Triage Agent*
    - **[Chapter 10 — Agentic AI Patterns · deep dive](curriculum/Chapter10_Agentic_AI_Patterns/01_Agentic_Design_Patterns.md)** &nbsp;:material-flask-outline:&nbsp; *Engineering Crew* capstone lab
    - **[Chapter 11 — Capstone Projects (IT-ops)](curriculum/Chapter11_Capstones_ITops/00_START_HERE.md)** &nbsp;:material-trophy-outline:&nbsp; SPN renewal · PowerShell doc buddy · Incident reporter

-   :material-rocket-launch:{ .lg .middle } &nbsp; __Stage E · Production__

    ---

    *Take an agent from notebook to Kubernetes.*

    - **[Chapter 12 — Production Agents](curriculum/Chapter12_Production_Agents/00_START_HERE.md)** &nbsp;:material-trophy-outline:&nbsp; *Production SPN Agent on AKS*

    ??? tip "What you'll learn"
        MCP · evaluation · observability (logs / traces / metrics) · failure modes · production architecture · LangGraph on Kubernetes.

-   :fontawesome-brands-github:{ .lg .middle } &nbsp; __Stage F · Git · GitHub · Copilot · Security__

    ---

    *The professional toolchain you'll use forever.*

    - **[Chapter 13 — GitHub Setup](curriculum/Chapter13_GitHub_Setup/index.md)**
    - **[Chapter 14 — Git Fundamentals · 12 labs + capstone](curriculum/Chapter14_Git_Fundamentals/exercises.md)**
    - **[Chapter 15 — GitHub Basics · 12 labs + capstone](curriculum/Chapter15_GitHub_Basics/exercises.md)**
    - **[Chapter 16 — Intermediate Git](curriculum/Chapter16_Intermediate_Git/index.md)**
    - **[Chapter 17 — GitHub Actions](curriculum/Chapter17_GitHub_Actions/index.md)**
    - **[Chapter 18 — Copilot + GenAI](curriculum/Chapter18_Copilot_GenAI/index.md)**
    - **[Chapter 19 — Copilot CLI](curriculum/Chapter19_Copilot_CLI/index.md)**
    - **[Chapter 20 — Agentic AI with Copilot](curriculum/Chapter20_Agentic_AI_Copilot/index.md)**
    - **[Chapter 21 — GHAS Admin & Security](curriculum/Chapter21_GHAS_Admin_Security/index.md)**
    - **[Chapter 22 — Exam Prep](curriculum/Chapter22_Exam_Prep/index.md)**
    - **[Chapter 23 — Final Capstone](curriculum/Chapter23_Final_Capstone/index.md)** &nbsp;:material-trophy-outline:

</div>

!!! tip "Just want the flat list?"
    Open the **[📚 Curriculum overview](curriculum/index.md)** for a single-page chapter-by-chapter breakdown with lesson-level links and reading-order suggestions.

> 💡 **Index of every exercise** → [Lab menu](curriculum/LAB_MENU.md) · **Setup first** → [SETUP](SETUP.md) · **Prefer offline?** Grab the latest **[PDF + DOCX export](https://github.com/mail2raji/genai-agentic-ai-handbook/actions/workflows/export.yml)**.

---

## 🎯 Three honest paths through the 23 chapters

Not everyone needs to read cover-to-cover. Pick the path that matches your goal:

=== "🐍 I'm here to learn GenAI / Agentic AI"
    **Chapters 1 → 12** is the full GenAI engineering path. Add Chapters 14–15 (Git/GitHub) before Chapter 11 (capstones) so you can ship your work properly.

    Time-box: **6–8 weeks** part-time.

=== "🛠️ I'm here to master GitHub + Copilot + GHAS"
    **Chapters 13 → 23** is the full GitHub track. Skim Chapter 5 (GenAI Fundamentals) before Chapter 18 (Copilot + GenAI) so the AI parts make sense.

    Time-box: **3–4 weeks** part-time.

=== "🚀 I want both — the long path"
    Read **Chapter 1 → 23 in order**. The chapters are arranged so each one unlocks the next. You'll graduate able to ship a production AI agent **and** the CI/CD pipeline + security scans around it.

    Time-box: **3 months** part-time, **6 weeks** full-time.

---

## 🧒 How each lesson is written

Every lesson (and lab) uses **the same beats** so your brain knows what to expect:

1. **🍭 Imagine this…** — a tiny story to explain the idea (5-year-old level)
2. **🧠 The real concept** — the technical bit, in plain English
3. **🌍 Real-world scenario** — where you'd actually use it (IT support, banking, healthcare, etc.)
4. **💻 The code** — copy-paste ready, *with every line explained*
5. **🏋️ Exercises** — 3 to 5 challenges that grow in difficulty
6. **✅ Solutions** — complete, working answers with explanation

The Git/GitHub labs (Chapters 14–15) add a **🎯 Why this matters → ▶️ Annotated steps → ✅ Expected output → 🧠 Use case in the wild → ⚠️ Gotchas** beat on top — see the rich lab packs for examples.

---

## 🚀 How to use this handbook

1. **Start with [SETUP](SETUP.md)** — install Python, Git, an editor, and (optionally) get an API key.
2. **Pick a path** above (GenAI track, GitHub track, or the full 23).
3. **Type the code yourself.** Don't just copy. Your fingers learn what your eyes can't.
4. **Do every exercise** before peeking at the solution.
5. **Build one tiny project** at the end of each stage — even just a 20-line one.

---

## 🛠️ Tools we'll use & costs

<div class="grid cards" markdown>

-   :material-toolbox-outline:{ .lg .middle } &nbsp; __Your toolbox__

    ---

    - **Python 3.10+** — the language
    - **Git + GitHub CLI (`gh`)** — version control & collab
    - **GitHub Copilot** + **Copilot CLI** — AI pair-programmer
    - **GitHub Actions + GHAS** — CI/CD & security scanning
    - **OpenAI SDK** *or* **Azure OpenAI** — call GPT-4o / GPT-4o-mini
    - **LangChain + LangGraph** — orchestration framework
    - **CrewAI** — multi-agent framework
    - **ChromaDB / FAISS** — vector databases for RAG
    - **VS Code** — your IDE

-   :material-cash-multiple:{ .lg .middle } &nbsp; __Will this cost money?__

    ---

    - :material-check-circle:{ .green } LLM API calls cost **cents** — a whole chapter rarely tops **\$1**.
    - :material-check-circle:{ .green } Swap in **free local models** (Ollama + Llama 3) — instructions in [SETUP](SETUP.md).
    - :material-check-circle:{ .green } All Git/GitHub/Actions/Copilot Free-tier features work end-to-end.
    - :material-information-outline: GHAS features require a **public repo** (free) or a paid org.

</div>

---

## 🏁 Where to go after Chapter 23

<div class="grid cards" markdown>

-   :material-briefcase-outline: &nbsp; __Build a portfolio project__

    *"Personal finance Q&A agent over my bank statements" · "Codebase explainer over my company repo" · "On-call runbook agent".*

-   :material-chart-line: &nbsp; __Add evaluation + observability__

    Plug in **Ragas**, **DeepEval**, **LangSmith**, or **Langfuse** so you can measure quality, latency, and cost in production.

-   :material-cloud-upload-outline: &nbsp; __Deploy beyond AKS__

    Try **Azure AI Foundry**, **AWS Bedrock**, or **Vertex AI** — port one capstone and compare the developer experience.

-   :material-certificate-outline: &nbsp; __Get certified__

    Earn the **GitHub Advanced Security** certification — Chapter 22 is purpose-built prep for it.

</div>

---

<p align="center" markdown>
  **Happy learning! 🎉**
  <br/>
  [:material-rocket-launch: &nbsp; Open SETUP](SETUP.md){ .md-button .md-button--primary }
  [:material-hand-wave: &nbsp; Jump to Chapter 1 — Hello World](curriculum/Chapter01_Python_Fundamentals/01_hello_world.md){ .md-button }
</p>
