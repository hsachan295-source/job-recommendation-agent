# Job Application Assistant for [YOUR_NAME]

<!-- SETUP: This file is populated by running /setup -->
<!-- After running /setup, all [PLACEHOLDER] tokens will be replaced with your actual information -->

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for [YOUR_NAME], helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

<!-- This section is auto-populated by /setup. You can also fill it in manually. -->

### Identity
- **Name:** Harsh Sachan
- **Location:** Greater Noida, UP, India (Open to remote or hybrid positions)
- **Languages:** English (Professional), Hindi (Native)
- **Status:** Final year B.Tech CSE (AI Specialization) student (Graduating June 2026), seeking Data Scientist, ML Engineer, AI Engineer, and Data Analyst roles
- **LinkedIn headline:** "Data Scientist | Machine Learning Engineer | AI Engineer | Data Analyst"

### Education
- **Bachelor of Technology in Computer Science Engineering (AI Specialization)** (2022-2026) - **Galgotias College of Engineering and Technology** (Greater Noida, UP)
  - CGPA: 8.12 / 10.0
  - Topics: Machine Learning, Deep Learning, Natural Language Processing, Computer Vision, Generative AI & Agents, Database Management (SQL, NoSQL, Vector DBs).

### Professional Experience
- **Lead Developer & AI Architect** (2024 - Present) - **Independent Projects** (Greater Noida, UP)
  - Engineered **NexCart**, a full-stack FastAPI & Streamlit system with Pydantic v2 cross-field validators.
  - Built **Agentic RAG System** with LangChain, Pinecone, and Gemini API for PDF question-answering.
  - Built **Ollama Code Assistant**, an interactive local AI code teaching assistant named "AmitCodes" using Python, Gradio, and Ollama.
  - Developed **Astra DB PDF RAG with Ollama**, a RAG workflow using Astra DB, local Ollama embeddings/models, and LangChain.
  - Designed **NeuralPrice** (4-layer ANN with 337 features, Docker, Hugging Face) and **NeuralClass** (GRU NLP Classifier, FastAPI).
  - Developed **SavorShield** (CNN Computer Vision Freshness Classifier) and **AuraWeather** (Real-Time Weather Analytics).
  - Architected **AI \& ML Jobs Market Analytics** Power BI dashboard with star-schema models.

### Technical Skills
- **Primary:** Python, SQL, Machine Learning (Supervised/Unsupervised), Generative AI, RAG, Agentic AI, FastAPI, Streamlit, Power BI
- **Secondary:** C++, Java, Deep Learning (ANN, CNN, GRU, LSTM), TensorFlow, Keras, Scikit-Learn, LangChain, LangGraph, Pandas, NumPy
- **Domain:** Natural Language Processing (NLP), Computer Vision, BI Dashboard Engineering, Vector Databases (Pinecone, ChromaDB), REST API Development
- **Software:** Git, GitHub, Docker, Hugging Face, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI), PostgreSQL, MySQL, MongoDB

### Certifications
- **Oracle Certified Data Science Professional 2025** - Oracle Cloud Infrastructure
- **Oracle Certified AI Foundations Associate 2025** - Oracle Cloud Infrastructure
- **HackerRank Advanced SQL & Problem Solving** - HackerRank
- **Google Cloud Introduction to Generative AI** - Google Cloud
- **Virtual Experience Certifications** - TATA (GenAI Data Analytics), Deloitte (Data Analytics), Walmart (Advanced Software Engineering)

### Publications
- *None*

### Awards
- **Problem Solving (Advanced) and SQL (Advanced)** - HackerRank Certified

### Behavioral Profile
- **Analytical & Research-Driven:** Methodical approach to training, evaluating, and deploying machine learning models.
- **Proactive Learner:** Continuously upskilling in GenAI and Agentic workflows (e.g. LangChain, LangGraph).
- **Strengths:** End-to-end ML lifecycle ownership (EDA, modeling, APIs, containerization, deployment), dashboard design, and database engineering.
- **Growth areas:** Scaling small-scale production systems to high-concurrency enterprise applications.
- **Thrives in:** Collaborative, high-autonomy teams working on cutting-edge AI and Data products.

### What Excites You
- Building and deploying intelligent agentic AI systems that solve real-world automation tasks.
- Deriving actionable business intelligence from complex, unstructured datasets.

### Target Sectors
- **AI & Tech startups:** Building next-gen LLM / Agentic solutions
- **Enterprise Tech Companies:** Implementing Data Science & Machine Learning pipelines
- **FinTech / E-commerce:** Analyzing customer behavior and predictive pricing models

### Deal-breakers
- Roles with no technical development (pure administrative work)
- Companies that discourage continuous learning or upskilling


## Repo Structure
- `cv/` - LaTeX CV variants (moderncv template, banking style)
- `cover_letters/` - LaTeX cover letters (custom cover.cls template)
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - Job search CLI tools

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: skills match, experience match, behavioral/culture match. Present this assessment to the user before proceeding.
3. If good fit: create targeted CV (`cv/main_<company>.tex`) and cover letter (`cover_letters/cover_<company>_<role>.tex`)
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and your strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] CV follows the standard 2-page moderncv/banking format
- [ ] Cover letter uses cover.cls template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits approximately one page

### Compiled PDF verification (MANDATORY - never skip)
Both documents MUST be compiled and visually inspected via the Read tool on the PDF output. "Looks fine in the .tex" is not acceptable - LaTeX page-break decisions are unpredictable. Iterate until these all pass:
- [ ] CV compiled with **lualatex** (pdflatex often fails on modern MiKTeX with fontawesome5 font-expansion errors). Cover letter compiled with **xelatex** (cover.cls requires fontspec).
- [ ] **CV is exactly 2 pages** - not 1, not 3
- [ ] **No orphaned `\cventry` titles** - a job/education title must never sit at the bottom of a page with its bullets spilling to the next page. Use `\needspace{5\baselineskip}` before each `\cventry` to prevent this, and `\enlargethispage{2-3\baselineskip}` to rescue a trailing section that just barely spills
- [ ] **Cover letter is exactly 1 page** - signature block must fit with the body, never overflow
- [ ] **Cover letter bullet font matches body font** - `\lettercontent{}` must not wrap `\begin{itemize}...\end{itemize}` (the command's trailing `\\` errors on `\end{itemize}`, and moving itemize outside loses the Raleway font). Standard pattern: close `\lettercontent{}`, then wrap the list in `{\raggedright\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont \begin{itemize}...\end{itemize}\par}`

### ATS & keyword verification (CV)
ATS parsers read the PDF's embedded text layer, not the rendered page. Extract it with `pdftotext -layout` and verify what a parser sees. `pdftotext` (poppler) is optional - if missing, skip the parseability items with a warning and check keyword coverage from the visual PDF read instead.
- [ ] CV text layer extracts cleanly - no `(cid:*)` markers, `�` replacement characters, or text visible in the PDF but absent from the extraction
- [ ] Email and phone appear as **literal text** in the extraction (icon-glyph noise like `MOBILE-ALT`/`Envelope` is harmless, but a contact detail carried only by an icon or hyperlink is invisible to ATS)
- [ ] Reading order of the extracted text matches the visual order (single-column stock template is safe; multi-column custom templates are where this breaks)
- [ ] Posting keywords covered or honestly absent - synonym-only matches tightened to the posting's exact term where truthfully applicable, keywords the profile genuinely supports added to experience bullets, genuine gaps left visible and **never stuffed**
