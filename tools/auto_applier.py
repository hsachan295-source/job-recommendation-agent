#!/usr/bin/env python3
import os
import sys
import json
import argparse
import subprocess
from datetime import datetime

# Definition of all 8 modular projects with search keywords for dynamic matching
PROJECTS_POOL = [
    {
        "id": "ipl_excel",
        "title": "IPL Performance Dashboard",
        "keywords": ["excel", "power query", "pivot", "slicers", "data analyst", "da", "reporting", "dashboard", "visual"],
        "latex": r"""\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Microsoft Excel, Power Query, Pivot Tables, Slicers, Data Analysis} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables, Pivot Charts, Slicers, and dynamic Excel charting.}
\resumeItem{Analyzed team, player, and match metrics (runs, wickets, strike rate, win margins) across multi-year datasets.}
\resumeItem{Leveraged Power Query for automated data cleaning, merging, and structural transformations of raw IPL datasets.}
\end{itemize}"""
    },
    {
        "id": "hr_excel",
        "title": "HR Attrition Analysis Dashboard",
        "keywords": ["excel", "pivot", "attrition", "hr", "charts", "data analyst", "da", "reporting", "dashboard", "retention"],
        "latex": r"""\noindent\textbf{HR Attrition Analysis Dashboard} $|$ \textit{Microsoft Excel, Pivot Tables, Charts, Slicers, HR Analytics} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Developed an interactive HR analytics dashboard to monitor and analyze employee attrition trends.}
\resumeItem{Visualized attrition metrics dynamically by department, age group, gender, salary brackets, and specific job roles.}
\resumeItem{Utilized conditional formatting and advanced Excel charts to surface payroll and retention insights.}
\end{itemize}"""
    },
    {
        "id": "sql_analysis",
        "title": "SQL Data Analysis Project",
        "keywords": ["sql", "mysql", "database", "query", "queries", "join", "cte", "schema", "optimize", "data analyst", "da"],
        "latex": r"""\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Database Optimization} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Performed comprehensive data analysis and business reporting on transactional databases using advanced MySQL queries.}
\resumeItem{Implemented complex JOINs, GROUP BY/HAVING statements, Subqueries, Stored Procedures, and Database Views.}
\resumeItem{Optimized query performance by structured schema modeling and leveraging Common Table Expressions (CTEs) and Window Functions.}
\end{itemize}"""
    },
    {
        "id": "job_market_bi",
        "title": "AI & ML Jobs Market Analytics Dashboard",
        "keywords": ["power bi", "dax", "bi", "dashboard", "visualization", "modeling", "star schema", "report", "data analyst", "da"],
        "latex": r"""\noindent\textbf{AI \& ML Jobs Market Analytics Dashboard} $|$ \textit{Power BI, DAX, Star Schema, Data Modeling} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Designed and published a Power BI dashboard analyzing global hiring trends, salaries, and remote job distributions in AI/ML.}
\resumeItem{Engineered a robust Star Schema model, mapping active/inactive relationships and optimization cross-filter propagation.}
\resumeItem{Wrote calculated measures and dynamic time-intelligence KPI formulas in DAX.}
\end{itemize}"""
    },
    {
        "id": "neural_price",
        "title": "NeuralPrice -- AI Laptop Price Predictor",
        "keywords": ["tensorflow", "keras", "ann", "neural", "predict", "predictive", "machine learning", "ml", "deep learning", "python"],
        "latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Docker, Hugging Face} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time laptop price prediction.}
\resumeItem{Built end-to-end pipeline with StandardScaler preprocessing, one-hot encoding, Docker containerization, and Hugging Face deployment.}
\end{itemize}"""
    },
    {
        "id": "neural_class",
        "title": "NeuralClass -- NLP Text Classifier",
        "keywords": ["nlp", "text", "classifier", "gru", "spam", "tensorflow", "fastapi", "machine learning", "ml", "python"],
        "latex": r"""\noindent\textbf{NeuralClass -- NLP Text Classifier} $|$ \textit{GRU, TensorFlow, FastAPI, Docker} \hfill
\href{https://huggingface.co/spaces/Harsh0809/gru-text-classifier}{\small Live} $|$
\href{https://github.com/hsachan295-source/Email-Spam-Detector}{\small GitHub}
\begin{itemize}
\resumeItem{Built a GRU-based spam/ham classification model using TensorFlow/Keras with confidence scoring and prediction logging.}
\resumeItem{Developed FastAPI inference APIs with Docker containerization and Hugging Face Spaces deployment.}
\end{itemize}"""
    },
    {
        "id": "discord_assistant",
        "title": "AI-Powered Discord Assistant",
        "keywords": ["discord", "bot", "assistant", "agent", "gemini", "tavily", "react", "langchain", "llm", "ai"],
        "latex": r"""\noindent\textbf{AI-Powered Discord Assistant} $|$ \textit{LangChain, LangGraph, Gemini, Tavily, ReAct} \hfill
\href{https://github.com/hsachan295-source/AI-Powered-Discord-Assistant}{\small GitHub}
\begin{itemize}
\resumeItem{Built an intelligent Discord chatbot with ReAct-based agent workflows, real-time Tavily web search, and Google Gemini LLM.}
\end{itemize}"""
    },
    {
        "id": "gemini_rag",
        "title": "Agentic RAG with Gemini and Pinecone",
        "keywords": ["rag", "pinecone", "gemini", "vector", "similarity", "embedding", "search", "langchain", "llm", "ai"],
        "latex": r"""\noindent\textbf{Agentic RAG with Gemini and Pinecone} $|$ \textit{RAG, Pinecone, LangChain, Gemini} \hfill
\href{https://github.com/hsachan295-source/Agentic-RAG-with-Gemini-and-Pinecone}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation system using Gemini and Pinecone for semantic vector storage and similarity search.}
\end{itemize}"""
    }
]

def get_dynamic_projects(role_title, company_name):
    # Combine texts to analyze keywords
    search_text = f"{role_title} {company_name}".lower()
    
    # Calculate keyword scores for each project in pool
    scored_projects = []
    for proj in PROJECTS_POOL:
        score = 0
        for kw in proj["keywords"]:
            if kw in search_text:
                score += 1
        scored_projects.append((score, proj))
        
    # Sort projects by score descending
    scored_projects.sort(key=lambda x: x[0], reverse=True)
    
    # Select the top projects matching keywords (we will select exactly 4 projects for resume balance)
    selected_projects = []
    for score, proj in scored_projects[:4]:
        selected_projects.append(proj["latex"])
        
    # If no keyword matches were found (all scores are 0), fall back to standard category-based templates
    total_score = sum(score for score, _ in scored_projects[:4])
    if total_score == 0:
        print("[Agent] No specific keywords matched. Falling back to default category projects.")
        # Fallback based on job role keywords
        is_da = any(k in search_text for k in ["analyst", "da", "excel", "sql", "power bi", "bi", "reporting"])
        if is_da:
            # Return DA defaults
            selected_projects = [
                PROJECTS_POOL[0]["latex"], # IPL
                PROJECTS_POOL[1]["latex"], # HR Attrition
                PROJECTS_POOL[2]["latex"], # SQL Analysis
                PROJECTS_POOL[3]["latex"]  # Power BI
            ]
        else:
            # Return DS/ML defaults
            selected_projects = [
                PROJECTS_POOL[4]["latex"], # NeuralPrice
                PROJECTS_POOL[5]["latex"], # NeuralClass
                PROJECTS_POOL[6]["latex"], # Discord Assistant
                PROJECTS_POOL[7]["latex"]  # Gemini RAG
            ]
            
    return "\n\n\\vspace{1.5pt}\n".join(selected_projects)

def tailor_cv(company, category, role_title=""):
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

    # Dynamically select tailored projects
    use_role = role_title if role_title else category
    project_block = get_dynamic_projects(use_role, company)

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
    
    # 1. Tailor and Compile CV (passing role title for dynamic selection)
    cv_path = tailor_cv(args.company, args.category, args.role)
    
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
