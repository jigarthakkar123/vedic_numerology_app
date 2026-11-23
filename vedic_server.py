# -*- coding: utf-8 -*-
"""
Vedic Numerology Studio - Web Server & API
FastAPI backend providing interactive chart calculation, trilingual PDF generation,
and report management.
"""

import os
import sys
import glob
import time
import hmac
import hashlib
import base64
import json
import urllib.request
import urllib.error
from typing import Optional, List
from datetime import datetime
from fastapi import FastAPI, HTTPException, Query, Body, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, Response
from pydantic import BaseModel

# Add current folder to sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from vedic_engine import compile_full_numerology_profile
from vedic_pdf_builder import build_report_html, render_pdf_from_html
from vedic_mailer import send_report_email

# Payment Gateway Configuration
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID", "").strip()
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "").strip()

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

# ==============================================================================
# Instagram Automated Sales Funnel Endpoints (₹499 Package)
# ==============================================================================

class FunnelOrderRequest(BaseModel):
    name: str
    dob: str
    gender: Optional[str] = "Male"
    lang: Optional[str] = "en"
    email: str
    phone: Optional[str] = ""
    amount: Optional[int] = 499

class FunnelVerifyRequest(BaseModel):
    order_id: str
    payment_id: str
    signature: Optional[str] = ""
    name: str
    dob: str
    gender: Optional[str] = "Male"
    lang: Optional[str] = "en"
    email: str
    phone: Optional[str] = ""

@app.get("/order")
async def get_sales_funnel_page():
    """Serves the high-converting Instagram Sales Funnel landing page."""
    order_page = os.path.join(STATIC_DIR, "order.html")
    if os.path.exists(order_page):
        return FileResponse(order_page, media_type="text/html")
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), media_type="text/html")

@app.get("/order/success")
async def get_order_success_page():
    """Serves the instant download and confirmation page after checkout."""
    success_page = os.path.join(STATIC_DIR, "order_success.html")
    if os.path.exists(success_page):
        return FileResponse(success_page, media_type="text/html")
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), media_type="text/html")

@app.get("/privacy")
@app.get("/terms")
@app.get("/refund-policy")
@app.get("/shipping-policy")
@app.get("/contact")
@app.get("/legal")
async def get_legal_policies():
    """Serves the mandatory Razorpay compliance policy pages."""
    legal_path = os.path.join(STATIC_DIR, "legal.html")
    if os.path.exists(legal_path):
        return FileResponse(legal_path, media_type="text/html")
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), media_type="text/html")

@app.get("/api/funnel/config")
async def get_funnel_config():
    """Returns gateway configuration status."""
    has_keys = bool(RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET)
    return {
        "gateway": "razorpay",
        "is_live": has_keys,
        "key_id": RAZORPAY_KEY_ID if has_keys else "demo_key",
        "price_inr": 499,
        "consultant_phone": "+91 9377614772",
        "consultant_email": "jigar93776@gmail.com"
    }

@app.post("/api/funnel/create-order")
async def create_funnel_order(req: FunnelOrderRequest):
    """
    Creates an order for ₹499 via Razorpay API if keys are present,
    or generates a demo order for simulator testing.
    """
    amount_in_paise = (req.amount or 499) * 100
    receipt_id = f"rcpt_{int(time.time())}_{clean_filename(req.name)[:8]}"

    # Check if live Razorpay keys are configured
    if RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET:
        try:
            url = "https://api.razorpay.com/v1/orders"
            payload = json.dumps({
                "amount": amount_in_paise,
                "currency": "INR",
                "receipt": receipt_id,
                "notes": {
                    "client_name": req.name,
                    "dob": req.dob,
                    "lang": req.lang,
                    "email": req.email,
                    "phone": req.phone
                }
            }).encode("utf-8")

            auth_str = base64.b64encode(f"{RAZORPAY_KEY_ID}:{RAZORPAY_KEY_SECRET}".encode("utf-8")).decode("utf-8")
            http_req = urllib.request.Request(
                url,
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Basic {auth_str}"
                }
            )

            with urllib.request.urlopen(http_req, timeout=15) as res:
                rz_data = json.loads(res.read().decode("utf-8"))
                return {
                    "success": True,
                    "order_id": rz_data["id"],
                    "amount": amount_in_paise,
                    "currency": "INR",
                    "key_id": RAZORPAY_KEY_ID,
                    "is_live": True,
                    "receipt": receipt_id
                }
        except Exception as e:
            print(f"[RAZORPAY ERROR] Failed to create live order: {e}")

    # Sandbox / Demo Mode fallback
    demo_order_id = f"order_demo_{int(time.time())}"
    return {
        "success": True,
        "order_id": demo_order_id,
        "amount": amount_in_paise,
        "currency": "INR",
        "key_id": "demo_key",
        "is_live": False,
        "receipt": receipt_id,
        "note": "Simulator Mode: Live Razorpay credentials pending in environment variables."
    }

@app.post("/api/funnel/verify-payment")
async def verify_funnel_payment(req: FunnelVerifyRequest, background_tasks: BackgroundTasks):
    """
    Verifies payment signature, generates the 4-page Vedic Numerology PDF report,
    and delivers it via email and on-screen download.
    """
    if RAZORPAY_KEY_SECRET and not req.order_id.startswith("order_demo_"):
        try:
            expected_sig = hmac.new(
                RAZORPAY_KEY_SECRET.encode("utf-8"),
                f"{req.order_id}|{req.payment_id}".encode("utf-8"),
                hashlib.sha256
            ).hexdigest()

            if not hmac.compare_digest(expected_sig, req.signature or ""):
                raise HTTPException(status_code=400, detail="Invalid payment verification signature.")
        except HTTPException:
            raise
        except Exception as e:
            print(f"[SIGNATURE VERIFY WARNING] {e}")

    try:
        profile = compile_full_numerology_profile(
            name=req.name.strip() or "Client",
            dob_str=req.dob,
            gender=req.gender or "Male",
            lang=req.lang or "en"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to calculate Vedic profile: {str(e)}")

    try:
        html_content = build_report_html(profile)
        c_name = clean_filename(req.name.strip() or "Client")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_filename = f"Vedic_Report_{c_name}_{req.lang}_{timestamp}.pdf"
        html_filename = f"Vedic_Report_{c_name}_{req.lang}_{timestamp}.html"

        pdf_path = os.path.join(REPORTS_DIR, pdf_filename)
        html_path = os.path.join(REPORTS_DIR, html_filename)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        render_pdf_from_html(html_content, pdf_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report rendering error: {str(e)}")

    if req.email and "@" in req.email:
        background_tasks.add_task(
            send_report_email,
            recipient_email=req.email.strip(),
            recipient_name=req.name.strip(),
            lang=req.lang or "en",
            pdf_path=pdf_path
        )

    return {
        "success": True,
        "filename": pdf_filename,
        "download_url": f"/api/download/{pdf_filename}",
        "html_url": f"/api/view-html/{html_filename}",
        "client_name": req.name,
        "email": req.email,
        "lang": req.lang,
        "order_id": req.order_id,
        "payment_id": req.payment_id
    }

# Mount static files to serve the frontend Single Page Application
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    print(f"Starting Vedic Numerology Studio on http://127.0.0.1:8765 ...")
    uvicorn.run(app, host="127.0.0.1", port=8765)
