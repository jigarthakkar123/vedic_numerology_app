# -*- coding: utf-8 -*-
"""
Vedic Numerology Studio - Web Server & API
FastAPI backend providing interactive chart calculation, trilingual PDF generation,
and report management.
"""

import os
import sys
import glob
from typing import Optional, List
from datetime import datetime
from fastapi import FastAPI, HTTPException, Query, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, Response
from pydantic import BaseModel

# Add current folder to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from vedic_engine import compile_full_numerology_profile
from vedic_pdf_builder import build_report_html, render_pdf_from_html

app = FastAPI(
    title="Vedic Numerology Studio API",
    description="Automated Vedic Numerology Calculation & Trilingual PDF Generation Engine",
    version="2.0.0"
)

STATIC_DIR = os.path.join(BASE_DIR, "static")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

class ClientProfileRequest(BaseModel):
    name: str
    dob: str  # YYYY-MM-DD or DD/MM/YYYY
    gender: Optional[str] = "Male"
    target_date: Optional[str] = None
    lang: Optional[str] = "en"
    consultant_notes: Optional[str] = ""

def clean_filename(name: str) -> str:
    """Removes special characters to produce safe filenames."""
    return "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).rstrip().replace(' ', '_')

@app.get("/favicon.ico")
async def get_favicon():
    fav_path = os.path.join(STATIC_DIR, "favicon.ico")
    if os.path.exists(fav_path):
        return FileResponse(fav_path, media_type="image/x-icon")
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y=".9em" font-size="90">🕉️</text></svg>'
    return Response(content=svg, media_type="image/svg+xml")

@app.post("/api/analyze")
async def analyze_chart(req: ClientProfileRequest):
    """Calculates all Vedic numerology parameters and returns structured profile."""
    try:
        profile = compile_full_numerology_profile(
            name=req.name.strip() or "Client",
            dob_str=req.dob,
            gender=req.gender or "Male",
            target_date_str=req.target_date,
            lang=req.lang or "en",
            consultant_notes=req.consultant_notes or ""
        )
        return {"success": True, "data": profile}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/generate-pdf")
async def generate_pdf(req: ClientProfileRequest):
    """Generates a luxury Vedic PDF report in the specified language."""
    try:
        profile = compile_full_numerology_profile(
            name=req.name.strip() or "Client",
            dob_str=req.dob,
            gender=req.gender or "Male",
            target_date_str=req.target_date,
            lang=req.lang or "en",
            consultant_notes=req.consultant_notes or ""
        )
        
        safe_name = clean_filename(req.name.strip() or "Client")
        lang_tag = {"en": "English", "hi": "Hindi", "gu": "Gujarati"}.get(req.lang, req.lang)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Vedic_Report_{safe_name}_{lang_tag}_{timestamp}.pdf"
        pdf_path = os.path.join(REPORTS_DIR, filename)
        
        html_content = build_report_html(profile)
        success = render_pdf_from_html(html_content, pdf_path)
        
        if not success:
            raise HTTPException(status_code=500, detail="Failed to render PDF using Edge engine.")
            
        return {
            "success": True,
            "filename": filename,
            "download_url": f"/api/download/{filename}",
            "html_url": f"/api/view-html/{filename.replace('.pdf', '.html')}",
            "lang": req.lang,
            "lang_name": lang_tag,
            "size": os.path.getsize(pdf_path)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-all-pdfs")
async def generate_all_pdfs(req: ClientProfileRequest):
    """Batch generates English, Hindi, and Gujarati reports in one execution."""
    results = []
    safe_name = clean_filename(req.name.strip() or "Client")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for lang in ["en", "hi", "gu"]:
        try:
            profile = compile_full_numerology_profile(
                name=req.name.strip() or "Client",
                dob_str=req.dob,
                gender=req.gender or "Male",
                target_date_str=req.target_date,
                lang=lang,
                consultant_notes=req.consultant_notes or ""
            )
            lang_tag = {"en": "English", "hi": "Hindi", "gu": "Gujarati"}.get(lang, lang)
            filename = f"Vedic_Report_{safe_name}_{lang_tag}_{timestamp}.pdf"
            pdf_path = os.path.join(REPORTS_DIR, filename)
            
            html_content = build_report_html(profile)
            success = render_pdf_from_html(html_content, pdf_path)
            
            if success:
                results.append({
                    "lang": lang,
                    "lang_name": lang_tag,
                    "filename": filename,
                    "download_url": f"/api/download/{filename}",
                    "html_url": f"/api/view-html/{filename.replace('.pdf', '.html')}",
                    "size": os.path.getsize(pdf_path)
                })
        except Exception as e:
            results.append({
                "lang": lang,
                "error": str(e)
            })
            
    return {"success": True, "reports": results}

@app.get("/api/download/{filename}")
async def download_report(filename: str):
    """Direct PDF download endpoint."""
    file_path = os.path.join(REPORTS_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Requested report file not found.")
    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=filename
    )

@app.get("/api/view-html/{html_filename}")
async def view_report_html(html_filename: str):
    """View generated HTML report directly in the browser."""
    file_path = os.path.join(REPORTS_DIR, html_filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Requested HTML report file not found.")
    return FileResponse(
        path=file_path,
        media_type="text/html"
    )

@app.get("/api/history")
async def list_generated_reports():
    """Lists recent reports generated in the session."""
    pdf_files = glob.glob(os.path.join(REPORTS_DIR, "*.pdf"))
    reports = []
    for f in sorted(pdf_files, key=os.path.getmtime, reverse=True)[:30]:
        base = os.path.basename(f)
        reports.append({
            "filename": base,
            "download_url": f"/api/download/{base}",
            "html_url": f"/api/view-html/{base.replace('.pdf', '.html')}",
            "size_kb": round(os.path.getsize(f) / 1024, 1),
            "created": datetime.fromtimestamp(os.path.getmtime(f)).strftime("%d/%m/%Y %H:%M:%S")
        })
    return {"reports": reports}

# Mount static files to serve the frontend Single Page Application
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    print(f"Starting Vedic Numerology Studio on http://127.0.0.1:8765 ...")
    uvicorn.run(app, host="127.0.0.1", port=8765)
