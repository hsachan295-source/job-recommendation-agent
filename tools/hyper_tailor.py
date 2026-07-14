#!/usr/bin/env python3
import os
import sys

# Ensure python path includes tools folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auto_applier import tailor_cv, log_application

# Detailed company requirements mapping for hyper-personalized resume tailoring
COMPANY_REQUIREMENTS = {
    "ByteDance": {
        "projects_latex": r"""\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Microsoft Excel, Power Query, Pivot Tables, Slicers, User Engagement Analytics} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables and Pivot Charts to analyze high-volume player/team match data.}
\resumeItem{Leveraged Power Query for automated cleaning and structured normalization, matching ByteDance's focus on user engagement metrics.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Database Optimization} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Implemented complex JOINs, GROUP BY/HAVING statements, and Window Functions to optimize large transactional databases.}
\resumeItem{Surfaced recommendation-ready features using structured database views, mirroring ByteDance's data architecture pipelines.}
\end{itemize}
"""
    },
    "C2FO": {
        "projects_latex": r"""\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Transaction Analytics} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Performed comprehensive transaction reconciliation and cash-flow reporting on commercial business databases using advanced MySQL.}
\resumeItem{Optimized query runtime performance by 35\% using Common Table Expressions (CTEs) and partition-based Window Functions.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{HR Attrition Analysis Dashboard} $|$ \textit{Microsoft Excel, Pivot Tables, Charts, Financial Modeling} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Developed an interactive HR analytics dashboard to monitor employee attrition trends, salary brackets, and cost projections.}
\resumeItem{Utilized conditional formatting and advanced Excel charts to surface payroll and budget optimization insights for management.}
\end{itemize}
"""
    },
    "Toddle": {
        "projects_latex": r"""\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Excel, Power Query, Pivot Tables, Education/User Analytics} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built interactive dashboards displaying user progress metrics, team stats, and activity timelines for dynamic visualization.}
\resumeItem{Created clean data modeling structures using Power Query, aligning with Toddle's product-focused learning systems.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{AI-Powered Discord Assistant} $|$ \textit{LangChain, LangGraph, Gemini, Tavily, ReAct} \hfill
\href{https://github.com/hsachan295-source/AI-Powered-Discord-Assistant}{\small GitHub}
\begin{itemize}
\resumeItem{Built an intelligent Discord chatbot with ReAct-based agent workflows, teaching assistance capabilities, and web search integrations.}
\resumeItem{Integrated Google Gemini APIs to handle multi-turn conversational responses, ideal for interactive classroom scenarios.}
\end{itemize}
"""
    },
    "Accenture": {
        "projects_latex": r"""\noindent\textbf{AI \& ML Jobs Market Analytics Dashboard} $|$ \textit{Power BI, DAX, Star Schema, Data Modeling} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Designed and published a Power BI dashboard analyzing global hiring trends, salaries, and remote job distributions in AI/ML.}
\resumeItem{Engineered a robust Star Schema model, mapping active/inactive relationships and optimization cross-filter propagation.}
\resumeItem{Wrote calculated measures and dynamic time-intelligence KPI formulas in DAX, matching Accenture's consulting standards.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Database Optimization} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Optimized backend reporting schemas for client transactional databases using stored procedures and parameterized views.}
\resumeItem{Standardized database performance checks by implementing structured queries for global business units.}
\end{itemize}
"""
    },
    "Tiger Analytics": {
        "projects_latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Predictive Modeling, Scikit-Learn} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time price predictions.}
\resumeItem{Built end-to-end data pipelines with StandardScaler preprocessing, one-hot encoding, and hyperparameter tuning.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{AI \& ML Jobs Market Analytics Dashboard} $|$ \textit{Power BI, DAX, Star Schema, Advanced Analytics} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Designed a Power BI dashboard analyzing salary distributions and remote job demand using statistical forecasting models.}
\resumeItem{Wrote complex DAX formulas to perform cohort analysis and market trend distributions across global regions.}
\resumeItem{Applied structured database schemas to unify disparate survey data sources into a single star schema.}
\resumeItem{Created visual presentations of regression findings to assist cross-functional strategy groups.}
\end{itemize}
"""
    },
    "Quantiphi": {
        "projects_latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Keras, GCP-Ready, Docker} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Developed an Artificial Neural Network (ANN) using TensorFlow/Keras to perform predictive pricing models on computer hardware.}
\resumeItem{Containerized application using Docker, ensuring cloud-ready portability for scalable deployments on GCP/AWS platforms.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{Astra DB PDF RAG with Ollama} $|$ \textit{Astra DB, Ollama, LangChain, PyPDF2, RAG} \hfill
\href{https://github.com/hsachan295-source/astra-db-pdf-rag-ollama}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation (RAG) system using Astra DB for cloud vector database storage.}
\resumeItem{Integrated Ollama locally for generating vector embeddings and chat response generation using LangChain structures.}
\end{itemize}
"""
    },
    "Cognizant": {
        "projects_latex": r"""\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Database Optimization} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Optimized database performance by structured schema modeling and leveraging Common Table Expressions (CTEs) and Window Functions.}
\resumeItem{Designed stored procedures and views to retrieve, aggregate, and normalize patient/transaction datasets efficiently.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{HR Attrition Analysis Dashboard} $|$ \textit{Microsoft Excel, Pivot Tables, Charts, Slicers, HR Analytics} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Developed an interactive HR analytics dashboard to monitor employee attrition trends, department metrics, and job roles.}
\resumeItem{Utilized conditional formatting and advanced Excel charts to surface actionable workforce retention insights.}
\end{itemize}
"""
    },
    "TCS": {
        "projects_latex": r"""\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Database Optimization} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Performed comprehensive data analysis and business reporting on transactional databases using advanced MySQL queries.}
\resumeItem{Implemented complex JOINs, GROUP BY/HAVING statements, Subqueries, Stored Procedures, and Database Views.}
\resumeItem{Optimized query runtime performance by structured schema modeling and leveraging Common Table Expressions (CTEs).}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Microsoft Excel, Power Query, Pivot Tables, Slicers, Data Analysis} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables, Pivot Charts, Slicers, and dynamic Excel charting.}
\resumeItem{Leveraged Power Query for automated data cleaning, merging, and structural transformations of raw datasets.}
\end{itemize}
"""
    },
    "Fractal Analytics": {
        "projects_latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Predictive Modeling, Scikit-Learn} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time laptop price prediction.}
\resumeItem{Built end-to-end pipeline with StandardScaler preprocessing, one-hot encoding, and model performance evaluations.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{HR Attrition Analysis Dashboard} $|$ \textit{Microsoft Excel, Pivot Tables, Charts, Decision Science} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Developed an interactive HR analytics dashboard to monitor employee attrition trends using advanced statistical charts.}
\resumeItem{Visualized attrition metrics dynamically by department, age group, gender, salary brackets, and specific job roles.}
\end{itemize}
"""
    },
    "Mu Sigma": {
        "projects_latex": r"""\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Decision Analytics} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Optimized query performance by structured schema modeling and leveraging Common Table Expressions (CTEs) and Window Functions.}
\resumeItem{Designed and implemented stored procedures to extract key business metrics from raw transactional databases.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{AI \& ML Jobs Market Analytics Dashboard} $|$ \textit{Power BI, DAX, Star Schema, Quantitative Analysis} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Designed and published a Power BI dashboard analyzing global hiring trends, salaries, and remote job distributions in AI/ML.}
\resumeItem{Engineered a robust Star Schema model, mapping active/inactive relationships and optimization cross-filter propagation.}
\end{itemize}
"""
    },
    "Wipro": {
        "projects_latex": r"""\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Microsoft Excel, Power Query, Pivot Tables, Slicers, Data Analysis} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables, Pivot Charts, Slicers, and dynamic Excel charting.}
\resumeItem{Leveraged Power Query for automated data cleaning, merging, and structural transformations of raw datasets.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Database Optimization} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Performed comprehensive data analysis and business reporting on transactional databases using advanced MySQL queries.}
\resumeItem{Implemented complex JOINs, GROUP BY/HAVING statements, Subqueries, Stored Procedures, and Database Views.}
\end{itemize}
"""
    },
    "Infosys": {
        "projects_latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Scikit-Learn, Software Engineering} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time laptop price prediction.}
\resumeItem{Built end-to-end pipeline with StandardScaler preprocessing, one-hot encoding, Docker containerization, and Hugging Face deployment.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{Astra DB PDF RAG with Ollama} $|$ \textit{Astra DB, Ollama, LangChain, PyPDF2, Software Architecture} \hfill
\href{https://github.com/hsachan295-source/astra-db-pdf-rag-ollama}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation (RAG) system using Astra DB for cloud vector database storage.}
\resumeItem{Integrated Ollama locally for generating vector embeddings (nomic-embed-text) and chat response generation.}
\end{itemize}
"""
    },
    "Tech Mahindra": {
        "projects_latex": r"""\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Database Optimization} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Performed comprehensive data analysis and business reporting on transactional databases using advanced MySQL queries.}
\resumeItem{Optimized query performance by structured schema modeling and leveraging Common Table Expressions (CTEs) and Window Functions.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Microsoft Excel, Power Query, Pivot Tables, Slicers, Data Analysis} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables, Pivot Charts, Slicers, and dynamic Excel charting.}
\resumeItem{Leveraged Power Query for automated data cleaning, merging, and structural transformations.}
\resumeItem{Created visual presentations of team statistics to assist operations teams.}
\end{itemize}
"""
    },
    "HCLTech": {
        "projects_latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Predictive Modeling, Scikit-Learn} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time laptop price prediction.}
\resumeItem{Built end-to-end pipeline with StandardScaler preprocessing, one-hot encoding, and model performance evaluations.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{AI-Powered Discord Assistant} $|$ \textit{LangChain, LangGraph, Gemini, Tavily, ReAct} \hfill
\href{https://github.com/hsachan295-source/AI-Powered-Discord-Assistant}{\small GitHub}
\begin{itemize}
\resumeItem{Built an intelligent Discord chatbot with ReAct-based agent workflows, real-time Tavily web search, and Google Gemini LLM.}
\resumeItem{Designed custom logic layers for automated dialog routing and multi-agent interaction systems.}
\end{itemize}
"""
    },
    "Databricks": {
        "projects_latex": r"""\noindent\textbf{Astra DB PDF RAG with Ollama} $|$ \textit{Astra DB, Ollama, Vector Databases, LangChain, RAG Systems} \hfill
\href{https://github.com/hsachan295-source/astra-db-pdf-rag-ollama}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation (RAG) system using Astra DB for cloud vector database storage.}
\resumeItem{Integrated Ollama locally for generating vector embeddings (nomic-embed-text) and similarity queries, aligned with Lakehouse concepts.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{SQL Data Analysis Project} $|$ \textit{SQL, MySQL, Window Functions, CTEs, Schema Design} \hfill
\href{https://github.com/hsachan295-source/smart-business-dashboard}{\small GitHub}
\begin{itemize}
\resumeItem{Performed data modeling and business reporting on transactional databases using advanced MySQL and structured schema design.}
\resumeItem{Optimized query runtime performance by structured schema modeling and leveraging Common Table Expressions (CTEs) and Window Functions.}
\end{itemize}
"""
    },
    "Pinecone": {
        "projects_latex": r"""\noindent\textbf{Agentic RAG with Gemini and Pinecone} $|$ \textit{RAG, Pinecone, Vector Database, Similarity Search, LangChain} \hfill
\href{https://github.com/hsachan295-source/Agentic-RAG-with-Gemini-and-Pinecone}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation system using Gemini and Pinecone for semantic vector storage and similarity search.}
\resumeItem{Optimized similarity indexing query latencies by implementing custom chunking strategies and indexing namespaces.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{Astra DB PDF RAG with Ollama} $|$ \textit{Astra DB, Ollama, LangChain, Vector Database, RAG} \hfill
\href{https://github.com/hsachan295-source/astra-db-pdf-rag-ollama}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation (RAG) system using cloud vector databases for text chunk indexing.}
\resumeItem{Integrated Ollama locally for generating vector embeddings (nomic-embed-text) and chat response generation.}
\end{itemize}
"""
    },
    "IBM India": {
        "projects_latex": r"""\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Predictive Modeling, Scikit-Learn} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time laptop price prediction.}
\resumeItem{Built end-to-end pipeline with StandardScaler preprocessing, one-hot encoding, and model performance evaluations.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{Agentic RAG with Gemini and Pinecone} $|$ \textit{RAG, Pinecone, LangChain, Watson-Style AI Pipelines} \hfill
\href{https://github.com/hsachan295-source/Agentic-RAG-with-Gemini-and-Pinecone}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation system using Gemini and Pinecone for semantic vector storage and similarity search.}
\resumeItem{Created automated orchestration flows for similarity lookup and contextual document extraction.}
\end{itemize}
"""
    },
    "Microsoft India": {
        "projects_latex": r"""\noindent\textbf{AI \& ML Jobs Market Analytics Dashboard} $|$ \textit{Power BI, DAX, Star Schema, Microsoft Stack} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Designed a Power BI dashboard analyzing AI/ML hiring trends, salary distributions, and remote job demand across global markets.}
\resumeItem{Engineered a robust Star Schema model, mapping active/inactive relationships and optimization cross-filter propagation.}
\resumeItem{Wrote calculated measures and dynamic time-intelligence KPI formulas in DAX, utilizing Power BI cloud service publishing.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Microsoft Excel, Power Query, Pivot Tables, Slicers, Data Analysis} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables, Pivot Charts, Slicers, and dynamic Excel charting.}
\resumeItem{Leveraged Power Query for automated data cleaning, merging, and structural transformations of raw datasets.}
\end{itemize}
"""
    },
    "Google India": {
        "projects_latex": r"""\noindent\textbf{Agentic RAG with Gemini and Pinecone} $|$ \textit{Gemini Pro, RAG, Pinecone, LangChain, Vector Embeddings} \hfill
\href{https://github.com/hsachan295-source/Agentic-RAG-with-Gemini-and-Pinecone}{\small GitHub}
\begin{itemize}
\resumeItem{Developed a Retrieval-Augmented Generation system using Gemini and Pinecone for semantic vector storage and similarity search.}
\resumeItem{Optimized chat responses by leveraging Google Gemini's reasoning capabilities and advanced system prompt engineering.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{NeuralPrice -- AI Laptop Price Predictor} $|$ \textit{ANN, TensorFlow, Keras, Scikit-Learn, Predictive AI} \hfill
\href{https://huggingface.co/spaces/Harsh0809/laptop-price-predictor-Ann}{\small Live} $|$
\href{https://github.com/hsachan295-source/Laptop-Price-Prediction-ANN}{\small GitHub}
\begin{itemize}
\resumeItem{Engineered a 4-layer ANN with 337 engineered features using TensorFlow and Scikit-Learn for real-time laptop price prediction.}
\resumeItem{Implemented deep learning pipeline with learning rate decay, Adam optimizer, and cross-validation checkpoints.}
\end{itemize}
"""
    },
    "Optimspace": {
        "projects_latex": r"""\noindent\textbf{IPL Performance Dashboard} $|$ \textit{Microsoft Excel, Power Query, Pivot Tables, Slicers, Web/Product Analytics} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Built an interactive IPL performance dashboard using Pivot Tables, Pivot Charts, Slicers, and dynamic Excel charting.}
\resumeItem{Leveraged Power Query for automated data cleaning, merging, and structural transformations of raw datasets.}
\end{itemize}

\vspace{1.5pt}
\noindent\textbf{HR Attrition Analysis Dashboard} $|$ \textit{Microsoft Excel, Pivot Tables, Charts, User Retention Analytics} \hfill
\href{https://github.com/hsachan295-source/Power-BI-Portfolio}{\small GitHub}
\begin{itemize}
\resumeItem{Developed an interactive HR analytics dashboard to monitor employee attrition trends, job satisfaction, and churn indicators.}
\resumeItem{Utilized conditional formatting and advanced Excel charts to surface actionable workforce retention insights.}
\end{itemize}
"""
    }
}

def hyper_tailor_cv(company, content_dict):
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

    # Select project block based on company override, fallback to standard tailor_cv if not found
    project_block = content_dict.get("projects_latex")

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

    print(f"Hyper-Tailored CV written: {tex_path}")

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
        return tex_path

def run_hyper_bulk():
    print(f"[Agent] Starting Hyper-Tailoring Resumes for all 20 companies...")
    
    cv_paths_to_stage = []
    
    for idx, (company, details) in enumerate(COMPANY_REQUIREMENTS.items()):
        print(f"\n[{idx+1}/{len(COMPANY_REQUIREMENTS)}] Hyper-Tailoring CV for: {company}...")
        
        # Compile hyper-tailored CV
        cv_path = hyper_tailor_cv(company, details)
        
        if cv_path:
            clean_company = "".join(c for c in company if c.isalnum()).lower()
            tex_path = f"cv/main_{clean_company}.tex"
            pdf_path = f"cv/main_{clean_company}.pdf"
            cv_paths_to_stage.extend([tex_path, pdf_path])
            print(f"Success: {company} resume tailored and compiled.")
        else:
            print(f"Failed: {company} resume generation failed.")

    return cv_paths_to_stage

if __name__ == "__main__":
    import subprocess
    staged_files = run_hyper_bulk()
    print("\n-----------------------------------------------------")
    print("[Done] Hyper-Tailored Resume compilation finished!")
    print("-----------------------------------------------------")
