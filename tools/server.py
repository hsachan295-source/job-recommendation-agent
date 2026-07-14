#!/usr/bin/env python3
import os
import json
import uvicorn
import subprocess
from datetime import datetime
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="AI Job Search Agent Server")

# Ensure correct workspace directories
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(WORKSPACE_DIR, "tools", "applied_jobs.json")
CV_DIR = os.path.join(WORKSPACE_DIR, "cv")

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import CV Customization content from auto_applier
from auto_applier import tailor_cv, log_application

class ApplicationPayload(BaseModel):
    url: str
    company: str
    role: str
    category: str

# Serve CV folder for PDF downloads
@app.get("/cv/{pdf_name}")
def get_pdf_file(pdf_name: str):
    pdf_path = os.path.join(CV_DIR, pdf_name)
    
    # If the PDF does not exist, compile it on-demand!
    if not os.path.exists(pdf_path):
        if pdf_name.startswith("main_") and pdf_name.endswith(".pdf"):
            clean_company = pdf_name[5:-4]
            # Search database for matching company information
            company_name = clean_company.capitalize()
            category = "DS"
            role = "Data Scientist"
            
            if os.path.exists(DB_PATH):
                try:
                    with open(DB_PATH, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    for app_record in data:
                        rec_clean = "".join(c for c in app_record["company"] if c.isalnum()).lower()
                        if rec_clean == clean_company:
                            company_name = app_record["company"]
                            category = app_record["category"]
                            role = app_record["role"]
                            break
                except Exception:
                    pass
            
            print(f"\n[On-Demand Server] Compiling dynamic resume for {company_name} ({role})...")
            tailor_cv(company_name, category, role)
            
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path)
    else:
        tex_path = pdf_path.replace(".pdf", ".tex")
        if os.path.exists(tex_path):
            return FileResponse(tex_path, media_type="text/plain")
        raise HTTPException(status_code=404, detail="PDF resume not found and compilation failed.")
app.mount("/tools", StaticFiles(directory=os.path.join(WORKSPACE_DIR, "tools")), name="tools")

@app.get("/")
def read_root():
    return RedirectResponse(url="/tools/dashboard.html")

@app.get("/api/applications")
def get_applications():
    if not os.path.exists(DB_PATH):
        return []
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database read error: {e}")

@app.post("/api/apply")
def api_apply(payload: ApplicationPayload):
    print(f"\nAPI Apply Triggered: {payload.role} at {payload.company} ({payload.category})")
    
    # 1. Tailor and Compile CV
    # Change directories to compile correctly if needed, tailor_cv handles paths locally
    cv_path = tailor_cv(payload.company, payload.category, payload.role)
    
    if not cv_path:
        raise HTTPException(status_code=500, detail="Error tailoring or compiling CV")

    # 2. Log in JSON Database
    new_app = log_application(payload.role, payload.company, payload.url, payload.category, cv_path)

    # 3. Launch Chrome with Job URL
    print(f"Opening target job application URL: {payload.url}")
    try:
        import sys
        if sys.platform == "win32":
            os.system(f'start chrome "{payload.url}"')
        elif sys.platform == "darwin":
            os.system(f'open -a "Google Chrome" "{payload.url}"')
        else:
            os.system(f'google-chrome "{payload.url}" &')
    except Exception as e:
        print(f"Could not automatically launch Chrome: {e}")

    return {"status": "success", "data": new_app}

@app.post("/api/status")
def update_status(id: int, status: str):
    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=404, detail="Database not found")

    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        found = False
        for app_record in data:
            if app_record["id"] == id:
                app_record["status"] = status
                found = True
                break
                
        if not found:
            raise HTTPException(status_code=404, detail="Application record not found")
            
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        return {"status": "success", "message": f"Updated application {id} status to {status}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/delete")
def delete_application(id: int):
    if not os.path.exists(DB_PATH):
        raise HTTPException(status_code=404, detail="Database not found")

    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        new_data = [app_record for app_record in data if app_record["id"] != id]
        
        # Re-index
        for idx, app_record in enumerate(new_data):
            app_record["id"] = idx + 1
            
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=2)
            
        return {"status": "success", "message": f"Deleted application {id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print("\n-----------------------------------------------------")
    print("[Server] Starting AI Job Search Agent Dashboard Server...")
    print("URL: http://localhost:8000")
    print("-----------------------------------------------------\n")
    uvicorn.run(app, host="127.0.0.1", port=8000)
