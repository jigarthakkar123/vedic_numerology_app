# -*- coding: utf-8 -*-
"""
Vedic Numerology PDF Report Generator
Authored & Certified by: Jigar Thakkar, Certified Numerologist (+91 9377614772 | jigar93776@gmail.com)
Generates luxury, authenticated 4-page PDF reports in English, Hindi, and Gujarati.
Cross-platform: Supports Microsoft Edge on Windows and Chromium/Chrome on Linux cloud deployments.
"""

import os
import subprocess
import shutil
from typing import Dict, Any

def get_browser_binary() -> str:
    """Auto-detects browser binary across Windows and Linux cloud environments."""
    if os.name == 'nt':
        candidates = [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
        for c in candidates:
            if os.path.exists(c):
                return c
        return "msedge.exe"
    else:
        candidates = [
            "/usr/bin/google-chrome-stable",
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser",
            "/usr/bin/chromium"
        ]
        for c in candidates:
            if os.path.exists(c):
                return c
        return shutil.which("chromium") or shutil.which("google-chrome") or "chromium"

def build_report_html(data: Dict[str, Any]) -> str:
    """
    Constructs a complete HTML document for the luxury Vedic Numerology Report.
    Features Jigar Thakkar's branding, certification stamp, legal copyright, and trilingual support.
    """
    client = data["client"]
    consultant = data.get("consultant", {
        "name": "Jigar Thakkar",
        "phone": "+91 9377614772",
        "email": "jigar93776@gmail.com",
        "title": "Certified Vedic Numerologist & Vastu Consultant",
        "copyright": "© 2026 Jigar Thakkar. All Rights Reserved."
    })
    core = data["core_numbers"]
    compass = data.get("compass", {})
    grid = data["grid"]
    vibrations = data["vibrations"]
    m_qualities = data["moolank_qualities"]
    m_precautions = data["moolank_precautions"]
    b_qualities = data["bhagyank_qualities"]
    b_precautions = data["bhagyank_precautions"]
    dasha = data["dasha"]
    yogas = data["yogas"]
    preds = data["predictions"]
    remedies = data["remedies"]
    ui = data["ui"]
    lang = client["lang"]

    # Fonts definition based on language
    font_family = "'Plus Jakarta Sans', -apple-system, sans-serif"
    if lang == "hi":
        font_family = "'Plus Jakarta Sans', 'Noto Sans Devanagari', 'Mangal', -apple-system, sans-serif"
    elif lang == "gu":
        font_family = "'Plus Jakarta Sans', 'Shruti', 'Noto Sans Gujarati', -apple-system, sans-serif"

    # Vedic Grid Cells HTML (3x3)
    grid_html = ""
    for cell in grid["cells"]:
        if cell["count"] > 0:
            grid_html += f'<div class="vedic-cell active">{cell["str"]}</div>\n'
        else:
            grid_html += f'<div class="vedic-cell empty">-</div>\n'

    # Moolank Qualities List HTML
    m_qual_html = "".join([f'<li class="quality-item-single">{q}</li>\n' for q in m_qualities])

    # Moolank Precautions Grid HTML
    m_prec_html = "".join([f'<li>{p}</li>\n' for p in m_precautions])

    # Bhagyank Qualities List HTML
    b_qual_html = "".join([f'<li class="quality-item-single">{q}</li>\n' for q in b_qualities])

    # Bhagyank Precautions Grid HTML
    b_prec_html = "".join([f'<li>{p}</li>\n' for p in b_precautions])

    # Yogas Cards HTML
    yogas_html = ""
    for y in yogas[:4]:
        yogas_html += f"""
        <div class="yoga-card-quad">
            <div class="yoga-card-quad-header">
                <div class="yoga-card-quad-title">{y['name']}</div>
                <span class="yoga-tag-mini gold">{y['tag']}</span>
            </div>
            <div class="yoga-card-quad-body">
                <div class="yoga-line-mini">{y['desc']}</div>
            </div>
        </div>
        """

    # Vibration badges on Page 2
    vibe_badges_html = ""
    for v in vibrations:
        badge_cls = "badge-pos" if v["type"] == "+" else "badge-neg"
        vibe_badges_html += f"""
        <div class="vibe-item {badge_cls}">
            <div class="vibe-header">
                <span class="vibe-num">{v['type']}{v['number']}</span>
                <span class="vibe-type">{v['type_label']}</span>
            </div>
            <div class="vibe-text">{v['text']}</div>
        </div>
        """

    # Predictions Cards HTML (Page 3)
    pred_categories = ["finance", "property", "vehicle", "education", "travel", "litigation", "relationship", "health"]
    preds_html = ""
    for cat in pred_categories:
        if cat in preds:
            p_data = preds[cat]
            preds_html += f"""
            <div class="pred-card">
                <div class="pred-header">
                    <span class="pred-icon">✦</span>
                    <span class="pred-title">{p_data['title']}</span>
                </div>
                <div class="pred-body">{p_data['desc']}</div>
            </div>
            """

    # Remedies Cards HTML (Page 4)
    remedy_items = [
        {"num": 1, "label": ui["gemstone_remedy"], "text": f"{remedies['moolank_gem']} (Crystal: {remedies['moolank_crystal']})"},
        {"num": 2, "label": ui["mantra_remedy"], "text": remedies["moolank_mantra"]},
        {"num": 3, "label": ui["fasting_remedy"], "text": remedies["moolank_fasting"]},
        {"num": 4, "label": ui["donation_remedy"], "text": remedies["moolank_donation"]},
        {"num": 5, "label": ui["seva_remedy"], "text": remedies["moolank_seva"]},
        {"num": 6, "label": ui["general_remedies"], "text": f"<strong>Health:</strong> {remedies['general_health']} <br><strong>Wealth:</strong> {remedies['general_wealth']} <br><strong>Harmony:</strong> {remedies['general_harmony']}"}
    ]
    remedies_html = ""
    for r in remedy_items:
        remedies_html += f"""
        <div class="remedy-card-seq">
            <div class="remedy-num-seq">{r['num']}</div>
            <div class="remedy-content-seq">
                <div class="remedy-label-seq">{r['label']}</div>
                <div class="remedy-text-seq">{r['text']}</div>
            </div>
        </div>
        """

    # Consultant Notes Block HTML
    consultant_notes_html = ""
    if client.get("consultant_notes"):
        consultant_notes_html = f"""
        <div class="consultant-notes-box">
            <div class="consultant-notes-header">✍ {ui['consultant_notes']}</div>
            <div class="consultant-notes-body">{client['consultant_notes']}</div>
        </div>
        """

    name_harmony_text = client.get("name_harmony", {}).get("text", "")

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{ui['report_title']} - {client['name']}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

@page {{
    size: A4;
    margin: 0;
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}}

body {{
    font-family: {font_family};
    color: #1e293b;
    background-color: #ffffff;
    font-size: 10.3px;
    line-height: 1.44;
}}

.page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    padding: 12mm 15mm 11mm 15mm;
    background: #ffffff;
    position: relative;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

/* Ornamental Borders */
.page-border {{
    position: absolute;
    top: 5mm;
    left: 5mm;
    right: 5mm;
    bottom: 5mm;
    border: 1.5px solid #d4af37;
    pointer-events: none;
    z-index: 1;
}}
.page-border-inner {{
    position: absolute;
    top: 6.5mm;
    left: 6.5mm;
    right: 6.5mm;
    bottom: 6.5mm;
    border: 0.5px solid #e2c275;
    pointer-events: none;
    z-index: 1;
}}
.corner-ornament {{
    position: absolute;
    width: 14px;
    height: 14px;
    border-color: #b38728;
    z-index: 2;
}}
.corner-tl {{ top: 4.5mm; left: 4.5mm; border-top: 3px solid #b38728; border-left: 3px solid #b38728; }}
.corner-tr {{ top: 4.5mm; right: 4.5mm; border-top: 3px solid #b38728; border-right: 3px solid #b38728; }}
.corner-bl {{ bottom: 4.5mm; left: 4.5mm; border-bottom: 3px solid #b38728; border-left: 3px solid #b38728; }}
.corner-br {{ bottom: 4.5mm; right: 4.5mm; border-bottom: 3px solid #b38728; border-right: 3px solid #b38728; }}

.page-content {{
    position: relative;
    z-index: 5;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

/* Main Header */
.report-main-header {{
    text-align: center;
    padding-bottom: 6px;
    border-bottom: 1.5px solid #e8dec9;
    margin-bottom: 8px;
}}
.om-symbol {{
    font-size: 15px;
    color: #b38728;
    font-weight: 700;
    letter-spacing: 2px;
}}
.main-title {{
    font-family: 'Cinzel', serif;
    font-size: 18px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 1px 0;
}}
.sub-title {{
    font-size: 9.5px;
    color: #854d0e;
    letter-spacing: 0.5px;
    font-weight: 600;
}}
.sub-title strong {{
    color: #0f172a;
    font-weight: 700;
}}

/* Mini Header for subsequent pages */
.page-header-mini {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 4px;
    border-bottom: 1px solid #e2c275;
    margin-bottom: 8px;
}}
.page-header-mini .mini-title {{
    font-family: 'Cinzel', serif;
    font-size: 11px;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: 0.8px;
}}
.page-header-mini .consultant-tag {{
    font-size: 9px;
    color: #854d0e;
    background: #fef9c3;
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: 600;
    border: 1px solid #fde047;
}}

/* Section Titles */
.section-title {{
    font-family: 'Cinzel', serif;
    font-size: 11.5px;
    font-weight: 700;
    color: #0f172a;
    border-left: 3.5px solid #b38728;
    padding-left: 7px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    letter-spacing: 0.4px;
}}

/* Profile Card */
.profile-card {{
    background: linear-gradient(135deg, #fdfbf7 0%, #f7f3e8 100%);
    border: 1.5px solid #d4af37;
    border-radius: 7px;
    padding: 8px 12px;
    margin-bottom: 8px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.03);
}}
.profile-grid-container {{
    display: grid;
    grid-template-columns: 1fr 165px;
    gap: 12px;
    align-items: center;
}}
.client-data-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 8px;
}}
.data-pill {{
    background: #ffffff;
    border: 1px solid #e2d7ba;
    border-radius: 4px;
    padding: 3px 6px;
}}
.data-pill .label {{
    font-size: 7.5px;
    color: #64748b;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.3px;
}}
.data-pill .value {{
    font-size: 11px;
    font-weight: 700;
    color: #0f172a;
}}
.data-pill.highlight {{
    background: #fffbeb;
    border-color: #f59e0b;
}}
.data-pill.highlight .value {{
    color: #b45309;
}}

/* 3x3 Vedic Grid */
.vedic-grid-wrapper {{
    display: flex;
    flex-direction: column;
    align-items: center;
}}
.grid-caption {{
    font-size: 8px;
    font-weight: 700;
    color: #854d0e;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
}}
.vedic-grid {{
    display: grid;
    grid-template-columns: repeat(3, 38px);
    grid-template-rows: repeat(3, 30px);
    gap: 2px;
    background: #b38728;
    padding: 2.5px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(179, 135, 40, 0.2);
}}
.vedic-cell {{
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11.5px;
    font-weight: 700;
    color: #0f172a;
    border-radius: 2px;
}}
.vedic-cell.active {{
    background: #fef3c7;
    color: #92400e;
    font-size: 12.5px;
    font-weight: 800;
}}
.vedic-cell.empty {{
    color: #cbd5e1;
    font-size: 9px;
}}

/* Planetary Friendship Compass Box */
.compass-box {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #3b82f6;
    border-radius: 6px;
    padding: 6px 10px;
    margin-bottom: 8px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6px;
}}
.compass-item {{
    display: flex;
    flex-direction: column;
}}
.compass-label {{
    font-size: 7.5px;
    text-transform: uppercase;
    color: #64748b;
    font-weight: 700;
}}
.compass-val {{
    font-size: 10px;
    font-weight: 700;
    color: #0f172a;
}}
.compass-val.green {{ color: #166534; }}
.compass-val.orange {{ color: #b45309; }}
.compass-val.red {{ color: #991b1b; }}

.name-harmony-bar {{
    background: #f0fdf4;
    border: 1px solid #86efac;
    border-radius: 5px;
    padding: 4px 8px;
    font-size: 8.8px;
    color: #166534;
    margin-bottom: 8px;
    line-height: 1.35;
}}

/* Badges Bar */
.meta-badge-bar {{
    display: flex;
    gap: 6px;
    margin-bottom: 7px;
}}
.meta-badge {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 3px 6px;
    font-size: 9px;
    font-weight: 600;
    color: #334155;
    flex: 1;
    text-align: center;
}}
.meta-badge span {{
    color: #b45309;
    font-weight: 700;
}}

/* Quality List */
.quality-list-single {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 4.5px;
    margin-bottom: 8px;
}}
.quality-item-single {{
    position: relative;
    padding-left: 13px;
    font-size: 9.6px;
    color: #334155;
    line-height: 1.38;
}}
.quality-item-single::before {{
    content: "◆";
    position: absolute;
    left: 0;
    top: 0;
    color: #d4af37;
    font-size: 7px;
}}

/* Precautions Box */
.root-precautions-box {{
    background: #fffaf0;
    border: 1.5px solid #fed7aa;
    border-radius: 6px;
    padding: 8px 12px;
    margin-top: 3px;
}}
.root-precautions-header {{
    font-family: 'Cinzel', serif;
    font-size: 10.5px;
    font-weight: 700;
    color: #b45309;
    margin-bottom: 4px;
    padding-bottom: 2px;
    border-bottom: 1px solid #fed7aa;
}}
.root-precautions-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3.5px 12px;
    list-style: none;
}}
.root-precautions-grid li {{
    position: relative;
    padding-left: 11px;
    font-size: 9.1px;
    color: #334155;
    line-height: 1.32;
}}
.root-precautions-grid li::before {{
    content: "•";
    position: absolute;
    left: 1px;
    top: -2px;
    font-size: 12px;
    color: #ea580c;
}}

/* Dasha Banner */
.dasha-summary-bar {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 7px;
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 6px;
    padding: 6px 9px;
    margin-bottom: 8px;
}}
.dasha-box {{
    text-align: center;
}}
.dasha-box .d-label {{
    font-size: 7.5px;
    text-transform: uppercase;
    color: #64748b;
    font-weight: 700;
}}
.dasha-box .d-val {{
    font-size: 12px;
    font-weight: 800;
    color: #1e3a8a;
    margin: 1px 0;
}}
.dasha-box .d-span {{
    font-size: 7.5px;
    color: #475569;
}}

/* Yogas Quad Grid */
.yogas-quad-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-bottom: 7px;
}}
.yoga-card-quad {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 6px 8px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}}
.yoga-card-quad-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3px;
    padding-bottom: 2px;
    border-bottom: 1px dashed #e2e8f0;
}}
.yoga-card-quad-title {{
    font-size: 10px;
    font-weight: 700;
    color: #0f172a;
}}
.yoga-tag-mini {{
    font-size: 7.5px;
    font-weight: 700;
    padding: 1.5px 4px;
    border-radius: 3px;
    background: #f1f5f9;
    color: #475569;
    border: 1px solid #cbd5e1;
}}
.yoga-tag-mini.gold {{
    background: #fef3c7;
    color: #92400e;
    border-color: #fde047;
}}
.yoga-card-quad-body {{
    display: flex;
    flex-direction: column;
    gap: 2px;
}}
.yoga-line-mini {{
    font-size: 9px;
    color: #334155;
    line-height: 1.32;
}}

/* Vibrations Grid */
.vibrations-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
    margin-bottom: 7px;
}}
.vibe-item {{
    border-radius: 4px;
    padding: 4px 7px;
    font-size: 8.8px;
}}
.vibe-item.badge-pos {{
    background: #f0fdf4;
    border: 1px solid #86efac;
}}
.vibe-item.badge-neg {{
    background: #fef2f2;
    border: 1px solid #fecaca;
}}
.vibe-header {{
    display: flex;
    justify-content: space-between;
    font-weight: 700;
    margin-bottom: 1px;
}}
.badge-pos .vibe-num {{ color: #166534; }}
.badge-neg .vibe-num {{ color: #991b1b; }}
.vibe-text {{
    font-size: 8.5px;
    color: #334155;
    line-height: 1.28;
}}

/* Predictions 2x4 Grid */
.preds-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6.5px;
    margin-bottom: 7px;
}}
.pred-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 6.5px 9px;
    display: flex;
    flex-direction: column;
    gap: 2px;
}}
.pred-header {{
    display: flex;
    align-items: center;
    gap: 4px;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 2px;
}}
.pred-icon {{
    color: #d4af37;
    font-size: 8.5px;
}}
.pred-title {{
    font-size: 9.6px;
    font-weight: 700;
    color: #0f172a;
}}
.pred-body {{
    font-size: 8.9px;
    color: #334155;
    line-height: 1.33;
}}

/* Remedies Sequence */
.remedies-sequence {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 7px;
}}
.remedy-card-seq {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 5.5px 9px;
    display: flex;
    gap: 8px;
    align-items: center;
}}
.remedy-num-seq {{
    width: 20px;
    height: 20px;
    min-width: 20px;
    border-radius: 50%;
    background: #fef3c7;
    color: #92400e;
    border: 1px solid #d4af37;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 9.5px;
    font-weight: 800;
}}
.remedy-content-seq {{
    flex: 1;
}}
.remedy-label-seq {{
    font-size: 8.5px;
    font-weight: 700;
    color: #854d0e;
    text-transform: uppercase;
    margin-bottom: 1px;
}}
.remedy-text-seq {{
    font-size: 9px;
    color: #334155;
    line-height: 1.33;
}}

/* Consultant Notes Box */
.consultant-notes-box {{
    background: #fdfbf7;
    border: 1.5px dashed #d4af37;
    border-radius: 6px;
    padding: 6px 10px;
    margin-bottom: 7px;
}}
.consultant-notes-header {{
    font-family: 'Cinzel', serif;
    font-size: 9.5px;
    font-weight: 700;
    color: #92400e;
    margin-bottom: 2px;
}}
.consultant-notes-body {{
    font-size: 9px;
    color: #334155;
    line-height: 1.33;
}}

/* Master Deluxe Certification & Copyright Card */
.cert-stamp-card-deluxe {{
    background: linear-gradient(135deg, #091124 0%, #1e293b 100%);
    border: 1.5px solid #d4af37;
    border-radius: 7px;
    padding: 9px 13px;
    color: #f8fafc;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
    margin-bottom: 2px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}}
.cert-title {{
    font-family: 'Cinzel', serif;
    font-size: 10.5px;
    color: #fbbf24;
    font-weight: 700;
    letter-spacing: 0.8px;
    margin-bottom: 2px;
}}
.cert-desc {{
    font-size: 8.5px;
    color: #cbd5e1;
    line-height: 1.32;
    max-width: 470px;
}}
.cert-contact-bar {{
    display: flex;
    gap: 12px;
    margin-top: 4px;
    font-size: 8.5px;
    color: #fde047;
    font-weight: 600;
}}
.cert-seal-deluxe {{
    border: 1.5px dashed #d4af37;
    border-radius: 50%;
    width: 52px;
    height: 52px;
    min-width: 52px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 7px;
    font-weight: 700;
    color: #fbbf24;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    line-height: 1.1;
    background: rgba(212, 175, 55, 0.05);
}}

/* Footer */
.page-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 4px;
    border-top: 1px solid #e2c275;
    font-size: 8px;
    color: #64748b;
    margin-top: auto;
}}
.footer-stamp {{
    font-weight: 600;
    color: #b38728;
    letter-spacing: 0.3px;
}}
</style>
</head>
<body>

<!-- ==================== PAGE 1: CLIENT DETAILS & MOOLANK PROFILE ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            <!-- Header -->
            <div class="report-main-header">
                <div class="om-symbol">॥ श्री गणेशाय नमः ॥</div>
                <h1 class="main-title">{ui['report_title']}</h1>
                <div class="sub-title">Prepared by: <strong>{consultant['name']}</strong> ({consultant['title']}) • 📞 {consultant['phone']} • ✉ {consultant['email']}</div>
            </div>

            <!-- Profile Card -->
            <div class="profile-card">
                <div class="profile-grid-container">
                    <div class="client-data-grid">
                        <div class="data-pill">
                            <div class="label">{ui['full_name']}</div>
                            <div class="value">{client['name']}</div>
                        </div>
                        <div class="data-pill">
                            <div class="label">{ui['dob']}</div>
                            <div class="value">{client['dob']} ({client['weekday']})</div>
                        </div>
                        <div class="data-pill highlight">
                            <div class="label">{ui['basic_number']}</div>
                            <div class="value">{core['bn']} • {core['bn_planet']}</div>
                        </div>
                        <div class="data-pill highlight">
                            <div class="label">{ui['destiny_number']}</div>
                            <div class="value">{core['dn']} • {core['dn_planet']}</div>
                        </div>
                        <div class="data-pill">
                            <div class="label">{ui['name_number']} (Namank)</div>
                            <div class="value">{core.get('namank', 1)} • {core['bn_planet'].split()[0]}</div>
                        </div>
                        <div class="data-pill">
                            <div class="label">{ui['dasha_timeline']}</div>
                            <div class="value">MD: {dasha['active_md']['number']} | AD: {dasha['active_ad']['ad_number']} | PD: {dasha['active_pd']['number']}</div>
                        </div>
                    </div>

                    <div class="vedic-grid-wrapper">
                        <div class="grid-caption">{ui['vedic_grid_title']}</div>
                        <div class="vedic-grid">
                            {grid_html}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Planetary Friendship Compass Box -->
            <div class="compass-box">
                <div class="compass-item">
                    <span class="compass-label">{ui['friendly_numbers']}</span>
                    <span class="compass-val green">{compass.get('friendly_nums', '1, 5, 6')}</span>
                </div>
                <div class="compass-item">
                    <span class="compass-label">{ui['neutral_numbers']}</span>
                    <span class="compass-val orange">{compass.get('neutral_nums', '3, 7')}</span>
                </div>
                <div class="compass-item">
                    <span class="compass-label">{ui['enemy_numbers']}</span>
                    <span class="compass-val red">{compass.get('enemy_nums', '8, 9')}</span>
                </div>
                <div class="compass-item">
                    <span class="compass-label">{ui['auspicious_direction']}</span>
                    <span class="compass-val">{compass.get('direction', 'North')}</span>
                </div>
                <div class="compass-item">
                    <span class="compass-label">{ui['auspicious_metal']}</span>
                    <span class="compass-val">{compass.get('metal', 'Silver')}</span>
                </div>
                <div class="compass-item">
                    <span class="compass-label">{ui['gemstone']}</span>
                    <span class="compass-val">{core['gemstone']}</span>
                </div>
            </div>

            {f'<div class="name-harmony-bar"><strong>{ui["name_harmony"]}:</strong> {name_harmony_text}</div>' if name_harmony_text else ''}

            <!-- Moolank Qualities -->
            <div class="section-title">{ui['moolank_qualities']} (No. {core['bn']})</div>
            <ul class="quality-list-single">
                {m_qual_html}
            </ul>

            <!-- Moolank Precautions -->
            <div class="root-precautions-box">
                <div class="root-precautions-header">⚠ {ui['moolank_precautions']} (No. {core['bn']})</div>
                <ul class="root-precautions-grid">
                    {m_prec_html}
                </ul>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-stamp">CONSULTATION BY JIGAR THAKKAR (📞 +91 9377614772) • {client['name'].upper()}</span>
            <span>{ui['page']} 1 {ui['of']} 4</span>
        </div>
    </div>
</div>

<!-- ==================== PAGE 2: BHAGYANK, DASHA & YOGAS ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            <div class="page-header-mini">
                <div class="mini-title">{ui['bhagyank_qualities']} • {ui['active_yogas']}</div>
                <div class="consultant-tag">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <!-- Dasha Timeline Bar -->
            <div class="dasha-summary-bar">
                <div class="dasha-box">
                    <div class="d-label">{ui['mahadasha']}</div>
                    <div class="d-val">No. {dasha['active_md']['number']}</div>
                    <div class="d-span">{dasha['active_md']['start_str']} - {dasha['active_md']['end_str']}</div>
                </div>
                <div class="dasha-box">
                    <div class="d-label">{ui['antardasha']}</div>
                    <div class="d-val">No. {dasha['active_ad']['ad_number']}</div>
                    <div class="d-span">{dasha['active_ad']['start_str']} - {dasha['active_ad']['end_str']}</div>
                </div>
                <div class="dasha-box">
                    <div class="d-label">{ui['pratyantar_dasha']}</div>
                    <div class="d-val">No. {dasha['active_pd']['number']}</div>
                    <div class="d-span">{dasha['active_pd']['start_str']} - {dasha['active_pd']['end_str']}</div>
                </div>
            </div>

            <!-- Bhagyank Qualities -->
            <div class="section-title">{ui['bhagyank_qualities']} (No. {core['dn']} - {core['dn_planet']})</div>
            <ul class="quality-list-single">
                {b_qual_html}
            </ul>

            <!-- Bhagyank Precautions -->
            <div class="root-precautions-box" style="margin-bottom: 7px;">
                <div class="root-precautions-header">⚠ {ui['bhagyank_precautions']} (No. {core['dn']})</div>
                <ul class="root-precautions-grid">
                    {b_prec_html}
                </ul>
            </div>

            <!-- Active Yogas Quad -->
            <div class="section-title">{ui['active_yogas']}</div>
            <div class="yogas-quad-grid">
                {yogas_html}
            </div>

            <!-- Planetary Vibrations -->
            <div class="section-title">{ui['active_vibrations']}</div>
            <div class="vibrations-grid">
                {vibe_badges_html}
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-stamp">CONSULTATION BY JIGAR THAKKAR (📞 +91 9377614772) • {client['name'].upper()}</span>
            <span>{ui['page']} 2 {ui['of']} 4</span>
        </div>
    </div>
</div>

<!-- ==================== PAGE 3: COMPREHENSIVE LIFE PREDICTIONS ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            <div class="page-header-mini">
                <div class="mini-title">{ui['predictions_title']}</div>
                <div class="consultant-tag">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <div class="preds-grid">
                {preds_html}
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-stamp">CONSULTATION BY JIGAR THAKKAR (📞 +91 9377614772) • {client['name'].upper()}</span>
            <span>{ui['page']} 3 {ui['of']} 4</span>
        </div>
    </div>
</div>

<!-- ==================== PAGE 4: REMEDIAL MEASURES & CERTIFICATION ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            <div class="page-header-mini">
                <div class="mini-title">{ui['remedies_title']}</div>
                <div class="consultant-tag">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <div class="section-title">{ui['remedies_title']}</div>
            <div class="remedies-sequence">
                {remedies_html}
            </div>

            {consultant_notes_html}

            <!-- Master Deluxe Certification & Copyright Card -->
            <div class="cert-stamp-card-deluxe">
                <div>
                    <div class="cert-title">{ui['certified_box_title']}</div>
                    <div class="cert-desc">{ui['certified_box_text']}</div>
                    <div class="cert-contact-bar">
                        <span>📞 {ui['phone_label']}: {consultant['phone']}</span>
                        <span>✉ {ui['email_label']}: {consultant['email']}</span>
                    </div>
                    <div style="font-size:7.5px;color:#94a3b8;margin-top:4px;">{consultant['copyright']}</div>
                </div>
                <div class="cert-seal-deluxe">
                    <span>VEDIC</span>
                    <span>CERTIFIED</span>
                    <span>JIGAR T.</span>
                    <span>✦ 2026 ✦</span>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-stamp">{consultant['copyright']}</span>
            <span>{ui['page']} 4 {ui['of']} 4</span>
        </div>
    </div>
</div>

</body>
</html>
"""
    return html

def render_pdf_from_html(html_content: str, output_pdf_path: str) -> bool:
    """
    Renders an HTML string into a high-precision A4 PDF.
    Auto-detects browser engine (Edge on Windows, Chromium on Linux cloud).
    """
    abs_pdf_path = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(abs_pdf_path), exist_ok=True)
    abs_html_path = abs_pdf_path.replace(".pdf", ".html")
    
    with open(abs_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    browser_bin = get_browser_binary()

    try:
        cmd = [
            browser_bin,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={abs_pdf_path}",
            abs_html_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=40)
        return os.path.exists(abs_pdf_path) and os.path.getsize(abs_pdf_path) > 1000
    except Exception as e:
        print(f"Error rendering PDF with browser '{browser_bin}': {e}")
        return False
