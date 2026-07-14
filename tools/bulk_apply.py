#!/usr/bin/env python3
import os
import sys

# Ensure python path includes tools folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auto_applier import tailor_cv, log_application

# List of 20 realistic AI / DS / DA target roles for 2026 graduates in India
JOBS_LIST = [
    {
        "company": "ByteDance",
        "role": "Data Analyst Project Intern (Training & Quality) - 2026 Start",
        "category": "DA",
        "url": "https://joinbytedance.com/search/7654066732550785333"
    },
    {
        "company": "C2FO",
        "role": "Data Specialist-Intern",
        "category": "DA",
        "url": "https://www.c2fo.com/amer/us/en-us/about-us/careers"
    },
    {
        "company": "Toddle",
        "role": "Data Analyst Intern (Remote)",
        "category": "DA",
        "url": "https://toddle.keka.com/careers"
    },
    {
        "company": "Accenture",
        "role": "Data Analyst Trainee",
        "category": "DA",
        "url": "https://www.accenture.com/in-en/careers/jobsearch?is=entry-level"
    },
    {
        "company": "Tiger Analytics",
        "role": "Associate Data Scientist",
        "category": "DS",
        "url": "https://www.tigeranalytics.com/careers/"
    },
    {
        "company": "Quantiphi",
        "role": "Machine Learning Trainee",
        "category": "ML",
        "url": "https://careers.quantiphi.com/"
    },
    {
        "company": "Cognizant",
        "role": "Programmer Analyst (Data Science & BI)",
        "category": "DA",
        "url": "https://careers.cognizant.com/"
    },
    {
        "company": "TCS",
        "role": "Data Science Trainee (Ignite Program)",
        "category": "DS",
        "url": "https://www.tcs.com/careers/india"
    },
    {
        "company": "Fractal Analytics",
        "role": "Junior Decision Scientist / Data Scientist",
        "category": "DS",
        "url": "https://fractal.ai/careers/"
    },
    {
        "company": "Mu Sigma",
        "role": "Trainee Decision Scientist",
        "category": "DS",
        "url": "https://www.mu-sigma.com/careers"
    },
    {
        "company": "Wipro",
        "role": "Data Analyst Graduate Trainee",
        "category": "DA",
        "url": "https://careers.wipro.com/"
    },
    {
        "company": "Infosys",
        "role": "Junior Machine Learning Engineer",
        "category": "ML",
        "url": "https://careers.infosys.com/"
    },
    {
        "company": "Tech Mahindra",
        "role": "Associate Data Engineer / Analyst",
        "category": "DA",
        "url": "https://careers.techmahindra.com/"
    },
    {
        "company": "HCLTech",
        "role": "Graduate Engineer Trainee (Artificial Intelligence)",
        "category": "AI",
        "url": "https://www.hcltech.com/careers/"
    },
    {
        "company": "Databricks",
        "role": "Associate Solution Architect (Data & AI)",
        "category": "DS",
        "url": "https://www.databricks.com/company/careers"
    },
    {
        "company": "Pinecone",
        "role": "Developer Relations Intern (AI/ML & Vector DB)",
        "category": "AI",
        "url": "https://www.pinecone.io/careers/"
    },
    {
        "company": "IBM India",
        "role": "Associate Data Scientist",
        "category": "DS",
        "url": "https://www.ibm.com/careers/in-en"
    },
    {
        "company": "Microsoft India",
        "role": "Data Analyst Intern (University Hiring)",
        "category": "DA",
        "url": "https://careers.microsoft.com/us/en"
    },
    {
        "company": "Google India",
        "role": "Software Engineer (AI/ML) Intern",
        "category": "ML",
        "url": "https://careers.google.com/"
    },
    {
        "company": "Optimspace",
        "role": "Data Science & Analytics Intern (Remote)",
        "category": "DS",
        "url": "https://in.indeed.com/jobs?q=Optimspace+Data+Science"
    }
]

def run_bulk():
    print(f"[Agent] Starting Bulk Resume Tailoring and Application Logger for {len(JOBS_LIST)} positions...")
    
    cv_paths_to_stage = []
    
    for idx, job in enumerate(JOBS_LIST):
        print(f"\n[{idx+1}/{len(JOBS_LIST)}] Processing: {job['role']} at {job['company']} ({job['category']})...")
        
        # 1. Tailor and Compile CV
        cv_path = tailor_cv(job["company"], job["category"])
        
        if cv_path:
            # 2. Log in JSON Database
            log_application(job["role"], job["company"], job["url"], job["category"], cv_path)
            
            # Store paths to stage to git later
            clean_company = "".join(c for c in job["company"] if c.isalnum()).lower()
            tex_path = f"cv/main_{clean_company}.tex"
            pdf_path = f"cv/main_{clean_company}.pdf"
            cv_paths_to_stage.extend([tex_path, pdf_path])
        else:
            print(f"Failed to generate CV for {job['company']}")

    # Return list of files to stage
    return cv_paths_to_stage

if __name__ == "__main__":
    staged_files = run_bulk()
    print("\n-----------------------------------------------------")
    print("[Done] Bulk Tailoring Finished successfully!")
    print("-----------------------------------------------------")
    # Write files to stdout so shell can catch and stage them
    with open("tools/staged_files.txt", "w") as f:
        f.write(" ".join(staged_files))
