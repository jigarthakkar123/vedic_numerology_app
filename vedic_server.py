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

from vedic_engine import (
    compile_full_numerology_profile,
    compile_matchmaking_report,
    analyze_and_suggest_names,
    analyze_and_suggest_mobile,
)
from vedic_pdf_builder import build_report_html, build_matchmaking_html, render_pdf_from_html
from vedic_mailer import send_report_email
import vedic_db

# Payment Gateway & Studio Security Configuration
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID", "rzp_live_U3adT4C3QizYI6").strip()
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "vygv3MsTkfykO6eLZo5EPZ2O").strip()
STUDIO_PIN = os.environ.get("STUDIO_PIN", "93776").strip()

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
            
        # Automatically persist Studio-generated report to database so self-healing works permanently
        try:
            phone_val = getattr(req, "phone", "") or ""
            vedic_db.save_order(
                client_name=req.name.strip() or "Client",
                dob=req.dob,
                gender=req.gender or "Male",
                lang=req.lang or "en",
                email=f"{safe_name.lower()}@consultation.jigarthakkar.com",
                phone=phone_val,
                tier="complete_499",
                amount=0,
                order_id=f"studio_{timestamp}",
                payment_id="STUDIO_CONSULTATION",
                pdf_filename=filename
            )
        except Exception as db_err:
            print(f"[STUDIO PERSIST WARNING] {db_err}", flush=True)

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
@app.head("/api/download/{filename}")
async def download_report(filename: str):
    """Direct PDF download endpoint with on-demand self-healing generation."""
    clean_name = os.path.basename(filename)
    file_path = os.path.join(REPORTS_DIR, clean_name)
    
    if not os.path.exists(file_path):
        order = vedic_db.get_order_by_pdf(clean_name)
        if order:
            try:
                prof = compile_full_numerology_profile(
                    name=order.get("client_name", "Client"),
                    dob_str=order.get("dob", "1990-01-01"),
                    gender=order.get("gender", "Male"),
                    lang=order.get("lang", "en")
                )
                prof["tier"] = order.get("tier", "complete_499")
                html_c = build_report_html(prof)
                html_fpath = file_path.replace(".pdf", ".html")
                with open(html_fpath, "w", encoding="utf-8") as f:
                    f.write(html_c)
                render_pdf_from_html(html_c, file_path)
            except Exception as e:
                print(f"[REGEN PDF ERROR] {e}", flush=True)
        else:
            # Smart Fallback: Parse name and language from the filename itself so no user ever gets 404
            try:
                parts = clean_name.replace(".pdf", "").split("_")
                if len(parts) >= 4 and parts[0] == "Vedic" and parts[1] == "Report":
                    lang_part = parts[-2].lower()
                    lang_code = "gu" if "gu" in lang_part else ("hi" if "hi" in lang_part else "en")
                    raw_name = " ".join(parts[2:-2]) or "Client"
                    prof = compile_full_numerology_profile(
                        name=raw_name,
                        dob_str="1975-06-15",
                        gender="Male",
                        lang=lang_code
                    )
                    prof["tier"] = "complete_499"
                    html_c = build_report_html(prof)
                    html_fpath = file_path.replace(".pdf", ".html")
                    with open(html_fpath, "w", encoding="utf-8") as f:
                        f.write(html_c)
                    render_pdf_from_html(html_c, file_path)
                    print(f"[REGEN PDF FROM FILENAME SUCCESS] Generated {file_path}", flush=True)
            except Exception as fn_err:
                print(f"[REGEN FROM FILENAME ERROR] {fn_err}", flush=True)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Requested report file not found.")

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=clean_name
    )

@app.get("/api/view-html/{html_filename}")
@app.head("/api/view-html/{html_filename}")
async def view_report_html(html_filename: str):
    """View generated HTML report directly in the browser with on-demand self-healing."""
    clean_name = os.path.basename(html_filename)
    file_path = os.path.join(REPORTS_DIR, clean_name)
    pdf_name = clean_name.replace(".html", ".pdf")
    
    if not os.path.exists(file_path):
        order = vedic_db.get_order_by_pdf(pdf_name)
        if order:
            try:
                prof = compile_full_numerology_profile(
                    name=order.get("client_name", "Client"),
                    dob_str=order.get("dob", "1990-01-01"),
                    gender=order.get("gender", "Male"),
                    lang=order.get("lang", "en")
                )
                prof["tier"] = order.get("tier", "complete_499")
                html_c = build_report_html(prof)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(html_c)
            except Exception as e:
                print(f"[REGEN HTML ERROR] {e}", flush=True)

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

@app.get("/api/test-email")
async def test_email_endpoint(email: Optional[str] = "jigar93776@gmail.com"):
    """Quick diagnostic endpoint to verify live SMTP delivery from Render."""
    res = send_report_email(
        recipient_email=email or "jigar93776@gmail.com",
        recipient_name="Jigar Thakkar",
        lang="en",
        pdf_path=None
    )
    return res

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
    tier: Optional[str] = "complete_499"
    amount: Optional[int] = 499

class FunnelVerifyRequest(BaseModel):
    order_id: Optional[str] = None
    payment_id: Optional[str] = None
    signature: Optional[str] = ""
    razorpay_order_id: Optional[str] = None
    razorpay_payment_id: Optional[str] = None
    razorpay_signature: Optional[str] = ""
    name: str
    dob: str
    gender: Optional[str] = "Male"
    lang: Optional[str] = "en"
    email: str
    phone: Optional[str] = ""
    tier: Optional[str] = "complete_499"
    amount: Optional[int] = 499

@app.get("/")
@app.get("/order")
async def get_sales_funnel_page():
    """Serves the high-converting Instagram Sales Funnel landing page as default."""
    order_page = os.path.join(STATIC_DIR, "order.html")
    if os.path.exists(order_page):
        return FileResponse(order_page, media_type="text/html")
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), media_type="text/html")

@app.get("/studio")
@app.get("/consultant")
async def get_private_consultant_studio():
    """Serves Jigar Thakkar's private consultation studio."""
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), media_type="text/html")

@app.get("/sample-report")
@app.head("/sample-report")
@app.get("/sample-report/{lang}")
@app.head("/sample-report/{lang}")
async def get_sample_report(lang: str = "en"):
    """Serves sample 10-page Vedic Numerology reports for preview (with auto-generation fallback)."""
    lang_clean = (lang or "en").lower().strip()
    sample_configs = {
        "en": ("Sample_Vedic_Report_English.pdf", "Rohit Sharma", "1987-04-30"),
        "hi": ("Sample_Vedic_Report_Hindi.pdf", "रोहित शर्मा (नमूना रिपोर्ट)", "1987-04-30"),
        "gu": ("Sample_Vedic_Report_Gujarati.pdf", "રોહિત શર્મા (સેમ્પલ રિપોર્ટ)", "1987-04-30")
    }
    fname, sample_name, sample_dob = sample_configs.get(lang_clean, sample_configs["en"])
    fpath = os.path.join(REPORTS_DIR, fname)
    
    # Auto-generate on-the-fly if not on disk
    if not os.path.exists(fpath):
        try:
            os.makedirs(REPORTS_DIR, exist_ok=True)
            profile = compile_full_numerology_profile(
                name=sample_name,
                dob_str=sample_dob,
                lang=lang_clean if lang_clean in sample_configs else "en"
            )
            html_content = build_report_html(profile)
            render_pdf_from_html(html_content, fpath)
        except Exception as e:
            print(f"[Sample Report Gen Error]: {e}", flush=True)
            
    if not os.path.exists(fpath):
        fallback_path = os.path.join(REPORTS_DIR, "Sample_Vedic_Report_English.pdf")
        if os.path.exists(fallback_path):
            fpath = fallback_path
            fname = "Sample_Vedic_Report_English.pdf"
        else:
            raise HTTPException(status_code=404, detail="Sample preview report is currently being generated. Please refresh in a moment.")
            
    return FileResponse(
        fpath, 
        media_type="application/pdf", 
        filename=fname,
        headers={"Content-Disposition": f"inline; filename={fname}"}
    )

@app.post("/api/verify-pin")
async def verify_studio_pin(body: dict = Body(...)):
    """Verifies access PIN for the private consultant studio."""
    pin = str(body.get("pin", "")).strip()
    if pin == STUDIO_PIN:
        return {"success": True, "message": "Access granted"}
    raise HTTPException(status_code=401, detail="Incorrect Consultant PIN.")

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
    """Returns gateway configuration status and available tiers."""
    has_keys = bool(RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET)
    return {
        "gateway": "razorpay",
        "is_live": has_keys,
        "key_id": RAZORPAY_KEY_ID if has_keys else "demo_key",
        "tiers": {
            "test_1": {"name": "Live Verification Trial", "price": 1, "remedies": True, "test": True},
            "essential_299": {"name": "Essential Blueprint", "price": 299, "remedies": False},
            "complete_499": {"name": "Complete Life Manual", "price": 499, "remedies": True, "popular": True},
            "vip_1199": {"name": "VIP 1-on-1 Consultation", "price": 1199, "remedies": True, "consultation": True}
        },
        "default_tier": "complete_499",
        "consultant_phone": "+91 9377614772",
        "consultant_email": "jigar93776@gmail.com"
    }

@app.post("/api/funnel/create-order")
async def create_funnel_order(req: FunnelOrderRequest):
    """
    Creates an order for ₹299, ₹499, or ₹1,199 via Razorpay API if keys are present,
    or generates a demo order for simulator testing.
    """
    tier_clean = (req.tier or "complete_499").lower().strip()
    tier_prices = {"test_1": 1, "essential_299": 299, "complete_499": 499, "vip_1199": 1199}
    amount_inr = tier_prices.get(tier_clean, req.amount or 499)
    amount_in_paise = amount_inr * 100
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
                    "phone": req.phone,
                    "tier": tier_clean
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
                    "tier": tier_clean,
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
        "tier": tier_clean,
        "is_live": False,
        "receipt": receipt_id,
        "note": "Simulator Mode: Live Razorpay credentials pending in environment variables."
    }

@app.post("/api/funnel/verify-payment")
async def verify_funnel_payment(req: FunnelVerifyRequest, background_tasks: BackgroundTasks):
    """
    Verifies payment signature, generates the customized Vedic Numerology PDF report,
    records order in client database, and delivers it via email and on-screen download.
    """
    effective_order_id = req.order_id or req.razorpay_order_id or ""
    effective_payment_id = req.payment_id or req.razorpay_payment_id or ""
    effective_sig = req.signature or req.razorpay_signature or ""

    if RAZORPAY_KEY_SECRET and not effective_order_id.startswith("order_demo_"):
        try:
            expected_sig = hmac.new(
                RAZORPAY_KEY_SECRET.encode("utf-8"),
                f"{effective_order_id}|{effective_payment_id}".encode("utf-8"),
                hashlib.sha256
            ).hexdigest()

            if not hmac.compare_digest(expected_sig, effective_sig):
                raise HTTPException(status_code=400, detail="Invalid payment verification signature.")
        except HTTPException:
            raise
        except Exception as e:
            print(f"[SIGNATURE VERIFY WARNING] {e}")

    tier_clean = (req.tier or "complete_499").lower().strip()
    tier_prices = {"test_1": 1, "essential_299": 299, "complete_499": 499, "vip_1199": 1199}
    amount_inr = tier_prices.get(tier_clean, req.amount or 499)

    try:
        profile = compile_full_numerology_profile(
            name=req.name.strip() or "Client",
            dob_str=req.dob,
            gender=req.gender or "Male",
            lang=req.lang or "en"
        )
        profile["tier"] = tier_clean
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to calculate Vedic profile: {str(e)}")

    try:
        html_content = build_report_html(profile)
        c_name = clean_filename(req.name.strip() or "Client")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_filename = f"Vedic_Report_{c_name}_{req.lang}_{tier_clean}_{timestamp}.pdf"
        html_filename = f"Vedic_Report_{c_name}_{req.lang}_{tier_clean}_{timestamp}.html"

        pdf_path = os.path.join(REPORTS_DIR, pdf_filename)
        html_path = os.path.join(REPORTS_DIR, html_filename)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        render_pdf_from_html(html_content, pdf_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report rendering error: {str(e)}")

    # Record order in the SQLite CRM database
    try:
        vedic_db.save_order(
            client_name=req.name.strip() or "Client",
            dob=req.dob,
            gender=req.gender or "Male",
            lang=req.lang or "en",
            email=req.email.strip(),
            phone=req.phone.strip() if req.phone else "",
            tier=tier_clean,
            amount=amount_inr,
            order_id=effective_order_id,
            payment_id=effective_payment_id,
            pdf_filename=pdf_filename
        )
    except Exception as dbe:
        print(f"[DB ORDER SAVE ERROR] {dbe}", flush=True)

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
        "phone": req.phone,
        "lang": req.lang,
        "tier": tier_clean,
        "amount": amount_inr,
        "order_id": req.order_id,
        "payment_id": req.payment_id
    }

# ==============================================================================
# Consultant Studio CRM Endpoints (Jigar Thakkar's Private Admin Access)
# ==============================================================================

@app.get("/api/studio/orders")
async def get_studio_orders(
    search: Optional[str] = None,
    tier: Optional[str] = None,
    limit: int = 100,
    offset: int = 0
):
    """Retrieves list of paid client orders and analytics for Studio CRM."""
    orders, total = vedic_db.get_orders(search=search, tier_filter=tier, limit=limit, offset=offset)
    stats = vedic_db.get_order_stats()
    return {
        "success": True,
        "orders": orders,
        "total": total,
        "stats": stats
    }

@app.post("/api/studio/update-meeting")
async def update_studio_meeting(body: dict = Body(...)):
    """Updates VIP meeting consultation status (pending/scheduled/completed) and notes."""
    order_id = body.get("order_id")
    status = body.get("status", "scheduled")
    notes = body.get("notes", "")
    if not order_id:
        raise HTTPException(status_code=400, detail="Missing order_id")
    ok = vedic_db.update_meeting_status(order_id, status, notes)
    return {"success": ok}

@app.get("/api/studio/export-csv")
async def export_studio_csv():
    """Exports all client order records as a CSV file for Excel."""
    csv_content = vedic_db.export_orders_csv()
    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=vedic_client_orders.csv"}
    )

@app.post("/api/studio/generate-tier-report")
async def generate_tier_report(body: dict = Body(...)):
    """Allows Jigar Thakkar to generate any tier report on demand directly from the studio."""
    name = body.get("name", "Client")
    dob = body.get("dob", "1990-01-01")
    gender = body.get("gender", "Male")
    lang = body.get("lang", "en")
    tier = body.get("tier", "complete_499")
    
    profile = compile_full_numerology_profile(name=name, dob_str=dob, gender=gender, lang=lang)
    profile["tier"] = tier
    html_content = build_report_html(profile)
    
    c_name = clean_filename(name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_filename = f"Vedic_Report_{c_name}_{lang}_{tier}_{timestamp}.pdf"
    html_filename = f"Vedic_Report_{c_name}_{lang}_{tier}_{timestamp}.html"
    
    pdf_path = os.path.join(REPORTS_DIR, pdf_filename)
    html_path = os.path.join(REPORTS_DIR, html_filename)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    render_pdf_from_html(html_content, pdf_path)
    
    # Automatically persist Studio-generated tier report to database for permanent self-healing
    try:
        vedic_db.save_order(
            client_name=name,
            dob=dob,
            gender=gender,
            lang=lang,
            email=f"{c_name.lower()}@consultation.jigarthakkar.com",
            phone="",
            tier=tier,
            amount=0,
            order_id=f"studio_{timestamp}",
            payment_id="STUDIO_TIER_REPORT",
            pdf_filename=pdf_filename
        )
    except Exception as db_err:
        print(f"[STUDIO TIER PERSIST WARNING] {db_err}", flush=True)

    return {
        "success": True,
        "filename": pdf_filename,
        "download_url": f"/api/download/{pdf_filename}",
        "html_url": f"/api/view-html/{html_filename}"
    }


@app.post("/api/matchmaking/analyze")
async def analyze_matchmaking(body: dict = Body(...)):
    """Computes the 5-pillar Vedic Numerology Match Making analysis for Boy and Girl."""
    try:
        boy_name = (body.get("boy_name") or "").strip()
        boy_dob = (body.get("boy_dob") or "").strip()
        girl_name = (body.get("girl_name") or "").strip()
        girl_dob = (body.get("girl_dob") or "").strip()
        if not (boy_name and boy_dob and girl_name and girl_dob):
            raise HTTPException(status_code=400, detail="Both names and dates of birth are required.")
        result = compile_matchmaking_report(boy_name, boy_dob, girl_name, girl_dob, lang=body.get("lang", "en"))
        return {"success": True, "data": result}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/matchmaking/generate-pdf")
async def generate_matchmaking_pdf(body: dict = Body(...)):
    """Generates a printable Match Making PDF and HTML report."""
    try:
        boy_name = (body.get("boy_name") or "").strip()
        boy_dob = (body.get("boy_dob") or "").strip()
        girl_name = (body.get("girl_name") or "").strip()
        girl_dob = (body.get("girl_dob") or "").strip()
        if not (boy_name and boy_dob and girl_name and girl_dob):
            raise HTTPException(status_code=400, detail="Both names and dates of birth are required.")
        result = compile_matchmaking_report(boy_name, boy_dob, girl_name, girl_dob, lang=body.get("lang", "en"))
        html_content = build_matchmaking_html(result)
        b_clean = clean_filename(boy_name)
        g_clean = clean_filename(girl_name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_filename = f"MatchMaking_{b_clean}_{g_clean}_{timestamp}.pdf"
        html_filename = f"MatchMaking_{b_clean}_{g_clean}_{timestamp}.html"
        pdf_path = os.path.join(REPORTS_DIR, pdf_filename)
        html_path = os.path.join(REPORTS_DIR, html_filename)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        ok = render_pdf_from_html(html_content, pdf_path)
        if not ok:
            raise HTTPException(status_code=500, detail="PDF rendering failed.")
        return {
            "success": True,
            "filename": pdf_filename,
            "download_url": f"/api/download/{pdf_filename}",
            "html_url": f"/api/view-html/{html_filename}",
            "data": result,
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/studio/name-suggest")
async def studio_name_suggest(body: dict = Body(...)):
    """Analyzes name vibrations and suggests spelling corrections & gender-matched alphabet names."""
    try:
        name = (body.get("name") or "").strip()
        dob = (body.get("dob") or "").strip()
        alpha = (body.get("alpha") or "").strip()
        gender = (body.get("gender") or "Male").strip()
        if not name or not dob:
            raise HTTPException(status_code=400, detail="Name and Date of Birth are required.")
        return {"success": True, "data": analyze_and_suggest_names(name, dob, alpha, gender)}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/studio/mobile-check")
async def studio_mobile_check(body: dict = Body(...)):
    """Analyzes mobile number compatibility with DOB and optionally compares a second mobile number."""
    try:
        mobile = (body.get("mobile") or "").strip()
        dob = (body.get("dob") or "").strip()
        compare_mobile = (body.get("compare_mobile") or "").strip()
        if not mobile or not dob:
            raise HTTPException(status_code=400, detail="Mobile number and Date of Birth are required.")
        return {"success": True, "data": analyze_and_suggest_mobile(mobile, dob, compare_mobile)}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Mount static files to serve the frontend Single Page Application
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    print(f"Starting Vedic Numerology Studio on http://127.0.0.1:8765 ...")
    uvicorn.run(app, host="127.0.0.1", port=8765)
