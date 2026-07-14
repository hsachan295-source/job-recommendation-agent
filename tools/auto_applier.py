#!/usr/bin/env python3
import os
import sys
import json
import argparse
import subprocess
import urllib.request
from bs4 import BeautifulSoup  # bs4 is installed in standard workspaces
from datetime import datetime

# Reference list of technical skills for ATS keyword matching
SKILLS_DB = [
    "excel", "power bi", "tableau", "sql", "mysql", "python", "tensorflow", 
    "keras", "docker", "fastapi", "langchain", "gemini", "pinecone", "git", 
    "pandas", "numpy", "statistics", "machine learning", "deep learning", 
    "nlp", "llm", "rag", "dax", "power query", "slicers", "pivot tables", 
    "matplotlib", "seaborn", "scikit-learn", "data visualization", "predictive modeling"
]

# Modular projects with keywords and dynamic placeholders
PROJECTS_POOL = [
    {
        "id": "ipl_excel",
        "title": "IPL Performance Dashboard",
        "keywords": ["excel", "power query", "pivot", "slicers", "data analyst", "da", "reporting", "dashboard", "visual"],
        "base_latex": r"""\noindent\textbf{IPL Performance Dashboard} $|$ \textit{{[TOOLS]}} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables, Pivot Charts, Slicers, and dynamic Excel charting.}
\resumeItem{Analyzed team, player, and match metrics (runs, wickets, strike rate, win margins) across multi-year datasets.}
\resumeItem{Leveraged Power Query for automated data cleaning, merging, and structural transformations of raw IPL datasets.}
\end{itemize}""",
        "default_tools": "Microsoft Excel, Power Query, Pivot Tables, Slicers, Data Analysis"
    },
    {
        "id": "hr_excel",
        "title": "HR Attrition Analysis Dashboard",
        "keywords": ["excel", "pivot", "attrition", "hr", "charts", "data analyst", "da", "reporting", "dashboard", "retention"],
        "base_latex": r"""\noindent\textbf{HR Attrition Analysis Dashboard} $|$ \textit{{[TOOLS]}} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Developed an interactive HR analytics dashboard to monitor and analyze employee attrition trends.}
\resumeItem{Visualized attrition metrics dynamically by department, age group, gender, salary brackets, and specific job roles.}
\resumeItem{Utilized conditional formatting and advanced Excel charts to surface payroll and retention insights.}
\end{itemize}""",
        "default_tools": "Microsoft Excel, Pivot Tables, Charts, Slicers, HR Analytics"
    },
    {
        "id": "sql_analysis",
        "title": "SQL Data Analysis Project",
        "keywords": ["sql", "mysql", "database", "query", "queries", "join", "cte", "schema", "optimize", "data analyst", "da"],
        "base_latex": r"""\noindent\textbf{SQL Data Analysis Project} $|$ \textit{{[TOOLS]}} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Performed comprehensive data analysis and business reporting on transactional databases using advanced MySQL queries.}
\resumeItem{Implemented complex JOINs, GROUP BY/HAVING statements, Subqueries, Stored Procedures, and Database Views.}
\resumeItem{Optimized query performance by structured schema modeling and leveraging Common Table Expressions (CTEs) and Window Functions.}
\resumeItem{[DYNAMIC_BULLET]}
\end{itemize}""",
        "default_tools": "SQL, MySQL, Window Functions, CTEs, Database Optimization"
    },
    {
        "id": "job_market_bi",
        "title": "AI & ML Jobs Market Analytics Dashboard",
        "keywords": ["power bi", "dax", "bi", "dashboard", "visualization", "modeling", "star schema", "report", "data analyst", "da"],
        "base_latex": r"""\noindent\textbf{AI \& ML Jobs Market Analytics Dashboard} $|$ \textit{{[TOOLS]}} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Designed and published a Power BI dashboard analyzing global hiring trends, salaries, and remote job distributions in AI/ML.}
\resumeItem{Engineered a robust Star Schema model, mapping active/inactive relationships and optimization cross-filter propagation.}
\resumeItem{Wrote calculated measures and dynamic time-intelligence KPI formulas in DAX.}
\end{itemize}""",
        "default_tools": "Power BI, DAX, Star Schema, Data Modeling"
    },
    {
        "id": "neural_price",
        "title": "NeuralPrice -- AI Laptop Price Predictor",
        "keywords": ["tensorflow", "keras", "ann", "neural", "predict", "predictive", "machine learning", "ml", "deep learning", "python"],
        "base_latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{{[TOOLS]}} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time laptop price prediction.}
\resumeItem{Built end-to-end pipeline with StandardScaler preprocessing, one-hot encoding, Docker containerization, and Hugging Face deployment.}
\resumeItem{[DYNAMIC_BULLET]}
\end{itemize}""",
        "default_tools": "ANN, TensorFlow, Docker, Hugging Face"
    },
    {
        "id": "neural_class",
        "title": "NeuralClass -- NLP Text Classifier",
        "keywords": ["nlp", "text", "classifier", "gru", "spam", "tensorflow", "fastapi", "machine learning", "ml", "python"],
        "base_latex": r"""\noindent\textbf{NeuralClass -- NLP Text Classifier} $|$ \textit{{[TOOLS]}} \hfill
\href{https://huggingface.co/spaces/Harsh0809/gru-text-classifier}{\small Live} $|$
\href{https://github.com/hsachan295-source/Email-Spam-Detector}{\small GitHub}
\begin{itemize}
\resumeItem{Built a GRU-based spam/ham classification model using TensorFlow/Keras with confidence scoring and prediction logging.}
\resumeItem{Developed FastAPI inference APIs with Docker containerization and Hugging Face Spaces deployment.}
\end{itemize}""",
        "default_tools": "GRU, TensorFlow, FastAPI, Docker"
    },
    {
        "id": "discord_assistant",
        "title": "AI-Powered Discord Assistant",
        "keywords": ["discord", "bot", "assistant", "agent", "gemini", "tavily", "react", "langchain", "llm", "ai"],
        "base_latex": r"""\noindent\textbf{AI-Powered Discord Assistant} $|$ \textit{{[TOOLS]}} \hfill
\href{https://github.com/hsachan295-source/AI-Powered-Discord-Assistant}{\small GitHub}
\begin{itemize}
\resumeItem{Built an intelligent Discord chatbot with ReAct-based agent workflows, real-time Tavily web search, and Google Gemini LLM.}
\end{itemize}""",
        "default_tools": "LangChain, LangGraph, Gemini, Tavily, ReAct"
    },
    {
        "id": "gemini_rag",
        "title": "Agentic RAG with Gemini and Pinecone",
        "keywords": ["rag", "pinecone", "gemini", "vector", "similarity", "embedding", "search", "langchain", "llm", "ai"],
        "base_latex": r"""\noindent\textbf{Agentic RAG with Gemini and Pinecone} $|$ \textit{{[TOOLS]}} \hfill
\href{https://github.com/hsachan295-source/Agentic-RAG-with-Gemini-and-Pinecone}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation system using Gemini and Pinecone for semantic vector storage and similarity search.}
\resumeItem{[DYNAMIC_BULLET]}
\end{itemize}""",
        "default_tools": "RAG, Pinecone, LangChain, Gemini"
    }
]

def scrape_jd_keywords(url):
    print(f"[Agent] Attempting to fetch and scan JD keywords from: {url}")
    matched_skills = []
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text().lower()
            
            for skill in SKILLS_DB:
                if skill in text:
                    matched_skills.append(skill)
        print(f"[Agent] Matched JD skills: {matched_skills}")
    except Exception as e:
        print(f"[Agent] Warning: Could not scrape JD content ({e}). Using default search text.")
    return matched_skills

def get_ats_optimized_projects(role_title, company_name, url=""):
    search_text = f"{role_title} {company_name}".lower()
    
    # Get matching skills from URL scraping
    jd_skills = []
    if url and url.startswith("http"):
        jd_skills = scrape_jd_keywords(url)
        
    # Fallback to scanning role title/company name if scraping yields nothing
    if not jd_skills:
        for skill in SKILLS_DB:
            if skill in search_text:
                jd_skills.append(skill)

    # Calculate scoring based on matching skills
    scored_projects = []
    for proj in PROJECTS_POOL:
        score = 0
        for kw in proj["keywords"]:
            if kw in search_text or kw in jd_skills:
                score += 1
        scored_projects.append((score, proj))
        
    # Sort projects by score descending
    scored_projects.sort(key=lambda x: x[0], reverse=True)
    
    # Pick top 4 projects
    selected_projects = []
    for score, proj in scored_projects[:4]:
        # Perform dynamic tool lists replacement in LaTeX content
        # Find intersection of project keywords & matched skills from JD
        intersect_skills = [s.title() for s in jd_skills if s in proj["keywords"]]
        
        # Build optimized tools string
        tools_list = proj["default_tools"]
        if intersect_skills:
            # Prepend matching JD skills to default tools list to increase ATS match
            unique_new = [s for s in intersect_skills if s.lower() not in tools_list.lower()]
            if unique_new:
                tools_list = f"{', '.join(unique_new)}, {tools_list}"
                
        # Handle dynamic bullet points if present (highlighting JD skills matches)
        latex_content = proj["base_latex"].replace("[TOOLS]", tools_list)
        
        if "[DYNAMIC_BULLET]" in latex_content:
            bullet_text = "Tailored project implementation to align with target role guidelines."
            if jd_skills:
                bullet_text = f"Optimized execution models using {', '.join([s.title() for s in jd_skills[:3]])} mapping role requirements."
            latex_content = latex_content.replace("[DYNAMIC_BULLET]", f"\\resumeItem{{{bullet_text}}}")
            
        selected_projects.append(latex_content)
        
    return "\n\n\\vspace{1.5pt}\n".join(selected_projects)

def tailor_cv(company, category, role_title="", url=""):
    base_cv_path = os.path.join("cv", "main_harsh.tex")
    if not os.path.exists(base_cv_path):
        print(f"Error: Base CV template {base_cv_path} not found.")
        return None

    with open(base_cv_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split template into header and footer
    project_sec_start = content.find(r"\section{Projects}")
    cert_sec_start = content.find(r"\section{Certifications}")

    if project_sec_start == -1 or cert_sec_start == -1:
        print("Error: Could not parse CV LaTeX template structure.")
        return None

    header = content[:project_sec_start + len(r"\section{Projects}")]
    footer = content[cert_sec_start:]

    # Dynamically select ATS optimized projects using job URL details
    use_role = role_title if role_title else category
    project_block = get_ats_optimized_projects(use_role, company, url)

    # Build new LaTeX content
    new_latex = f"{header}\n\n{project_block}\n\n\\vspace{{-2mm}}\n\n{footer}"

    # Target filenames
    clean_company = "".join(c for c in company if c.isalnum()).lower()
    tex_filename = f"main_{clean_company}.tex"
    pdf_filename = f"main_{clean_company}.pdf"
    
    tex_path = os.path.join("cv", tex_filename)
    pdf_path = os.path.join("cv", pdf_filename)

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(new_latex)

    print(f"Dynamically tailored CV written: {tex_path}")

    # Compile using lualatex
    print(f"Compiling {tex_path} to PDF using lualatex...")
    try:
        # Run pass 1
        subprocess.run(
            ["lualatex", "--interaction=nonstopmode", tex_filename],
            cwd="cv",
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Run pass 2 for cross references
        subprocess.run(
            ["lualatex", "--interaction=nonstopmode", tex_filename],
            cwd="cv",
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"Successful compilation. PDF written: {pdf_path}")
        
        # Clean up auxiliary files
        for ext in [".aux", ".log", ".out"]:
            aux_file = os.path.join("cv", f"main_{clean_company}{ext}")
            if os.path.exists(aux_file):
                os.remove(aux_file)
                
        return pdf_path
    except Exception as e:
        print(f"Warning: LaTeX compilation failed: {e}. Source file {tex_path} was saved.")
        return tex_path  # Return tex path if pdf compilation failed


def log_application(role, company, url, category, cv_path):
    db_path = os.path.join("tools", "applied_jobs.json")
    if os.path.exists(db_path):
        try:
            with open(db_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
    else:
        data = []

    new_app = {
        "id": len(data) + 1,
        "role": role,
        "company": company,
        "url": url,
        "category": category.upper(),
        "cv_path": cv_path.replace("\\", "/"),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "status": "Applied"
    }

    data.append(new_app)

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Logged application to database: {company} - {role}")
    return new_app


def main():
    parser = argparse.ArgumentParser(description="Auto-Apply Job Agent")
    parser.add_argument("--url", required=True, help="Job description URL")
    parser.add_argument("--company", required=True, help="Hiring company name")
    parser.add_argument("--role", required=True, help="Job role title")
    parser.add_argument("--category", required=True, choices=["DS", "AI", "ML", "DA"], help="Job category focus")

    args = parser.parse_args()

    print(f"\n[Agent] Launching Auto-Applier for {args.role} at {args.company}...")
    
    # 1. Tailor and Compile CV (passing role title and URL for dynamic ATS selection)
    cv_path = tailor_cv(args.company, args.category, args.role, args.url)
    
    if not cv_path:
        print("Error tailoring CV. Aborting application logging.")
        sys.exit(1)

    # 2. Log in JSON Database
    log_application(args.role, args.company, args.url, args.category, cv_path)

    # 3. Launch Chrome with Job URL
    print(f"Opening target job application URL: {args.url}")
    try:
        if sys.platform == "win32":
            os.system(f'start chrome "{args.url}"')
        elif sys.platform == "darwin":
            os.system(f'open -a "Google Chrome" "{args.url}"')
        else:
            os.system(f'google-chrome "{args.url}" &')
    except Exception as e:
        print(f"Could not automatically launch Chrome: {e}")

    print("\n[Done] Use the Autofill Bookmarklet on Chrome to complete the form.")


if __name__ == "__main__":
    main()
