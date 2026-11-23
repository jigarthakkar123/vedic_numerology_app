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

    # 1. Dual Vedic Grids HTML
    natal_grid = data.get("natal_grid", grid)
    dasha_grid = data.get("dasha_grid", {})
    three_tier = data.get("three_tier_forecast", {})

    # Natal Grid Cells HTML (3x3)
    natal_grid_html = ""
    for cell in natal_grid["cells"]:
        if cell["count"] > 0:
            natal_grid_html += f'<div class="vedic-cell natal-cell active">{cell["str"]}</div>\n'
        else:
            natal_grid_html += f'<div class="vedic-cell natal-cell empty">-</div>\n'

    # Dasha Grid Cells HTML (3x3) with multi-color chips
    dasha_grid_html = ""
    for cell in dasha_grid.get("cells", natal_grid["cells"]):
        items = cell.get("items", [])
        if items:
            chips_html = "".join([f'<span class="chip chip-{it["source"]}">{it["val"]}</span>' for it in items])
            dasha_grid_html += f'<div class="vedic-cell dasha-cell active">{chips_html}</div>\n'
        else:
            dasha_grid_html += f'<div class="vedic-cell dasha-cell empty">-</div>\n'

    # Moolank Qualities List HTML
    m_qual_html = "".join([f'<li class="quality-item-single">{q}</li>\n' for q in m_qualities])

    # Moolank Precautions Grid HTML
    m_prec_html = "".join([f'<li>{p}</li>\n' for p in m_precautions])

    # Bhagyank Qualities List HTML
    b_qual_html = "".join([f'<li class="quality-item-single">{q}</li>\n' for q in b_qualities])

    # Bhagyank Precautions Grid HTML
    b_prec_html = "".join([f'<li>{p}</li>\n' for p in b_precautions])

    # 3-Tier Forecast HTML for Page 2
    md_data = three_tier.get("mahadasha", {})
    ad_data = three_tier.get("antardasha", {})
    pd_data = three_tier.get("pratyantar_dasha", {})
    roadmap_data = three_tier.get("pd_roadmap", [])

    # Road map table rows
    roadmap_rows_html = ""
    for r in roadmap_data:
        active_cls = "active-phase" if r.get("is_active") else ""
        badge_txt = "★ ACTIVE" if r.get("is_active") else r.get("tone", "")
        roadmap_rows_html += f"""
        <tr class="{active_cls}">
            <td style="font-weight:700;">Phase {r['phase']} ({r['planet']})</td>
            <td style="text-align:center;"><strong>No. {r['number']}</strong></td>
            <td style="text-align:center;">{r['duration_days']} Days</td>
            <td style="text-align:center;">{r['start_str']}</td>
            <td style="text-align:center;">{r['end_str']}</td>
            <td style="text-align:center;"><span class="status-chip {'active' if r.get('is_active') else ''}">{badge_txt}</span></td>
        </tr>
        """

    # Yogas Cards HTML (Page 3)
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

    # Vibration badges on Page 3
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

    # Predictions Cards HTML (Page 4)
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

    pd_dos_html = "".join([f"<li>{d}</li>" for d in pd_data.get("dos", [])])
    pd_donts_html = "".join([f"<li>{d}</li>" for d in pd_data.get("donts", [])])

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

/* Dual Vedic Grids Layout */
.dual-grids-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 6px;
}}
.grid-box-card {{
    background: #fdfbf7;
    border: 1.2px solid #d4af37;
    border-radius: 5px;
    padding: 5px 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
}}
.grid-box-card.dasha {{
    border-color: #38bdf8;
    background: #f0f9ff;
}}
.grid-caption {{
    font-size: 8px;
    font-weight: 800;
    color: #854d0e;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 2px;
    text-align: center;
}}
.grid-caption.dasha {{
    color: #0369a1;
}}
.grid-subtext {{
    font-size: 6.8px;
    color: #64748b;
    margin-bottom: 3px;
    text-align: center;
}}
.vedic-grid {{
    display: grid;
    grid-template-columns: repeat(3, 40px);
    grid-template-rows: repeat(3, 26px);
    gap: 2px;
    background: #b38728;
    padding: 2px;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}}
.vedic-grid.dasha {{
    background: #0284c7;
}}
.vedic-cell {{
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 2px;
    font-size: 11px;
    font-weight: 700;
    color: #0f172a;
    overflow: hidden;
}}
.vedic-cell.natal-cell.active {{
    background: #fef3c7;
    color: #92400e;
    font-size: 11.5px;
    font-weight: 800;
}}
.vedic-cell.dasha-cell {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2px;
    flex-wrap: wrap;
    padding: 1px;
}}
.vedic-cell.empty {{
    color: #cbd5e1;
    font-size: 8.5px;
}}
.chip {{
    font-size: 8.5px;
    font-weight: 800;
    padding: 1px 3px;
    border-radius: 3px;
    line-height: 1;
    border: 1px solid transparent;
}}
.chip-natal {{ background: #fef3c7; color: #854d0e; border-color: #fde047; }}
.chip-md {{ background: #e0f2fe; color: #0284c7; border-color: #38bdf8; }}
.chip-ad {{ background: #dcfce7; color: #15803d; border-color: #22c55e; }}
.chip-pd {{ background: #ffedd5; color: #c2410c; border-color: #fb923c; }}

.grid-legend-bar {{
    display: flex;
    justify-content: center;
    gap: 10px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 2.5px 8px;
    margin-bottom: 6px;
    font-size: 7.2px;
    font-weight: 700;
}}
.legend-pill {{ display: inline-flex; align-items: center; gap: 3px; }}
.legend-dot {{ width: 6px; height: 6px; border-radius: 50%; display: inline-block; }}
.dot-natal {{ background: #d4af37; }}
.dot-md {{ background: #38bdf8; }}
.dot-ad {{ background: #22c55e; }}
.dot-pd {{ background: #fb923c; }}

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

/* 3-Tier Period Forecast Cards */
.tier-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 6px 9px;
    margin-bottom: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}}
.tier-card.tier-md {{ border-left: 3.5px solid #0284c7; }}
.tier-card.tier-ad {{ border-left: 3.5px solid #16a34a; }}
.tier-card.tier-pd {{ border-left: 3.5px solid #ea580c; }}

.tier-header-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3px;
    border-bottom: 1px dashed #e2e8f0;
    padding-bottom: 2.5px;
}}
.tier-badge {{
    font-size: 7.5px;
    font-weight: 800;
    text-transform: uppercase;
    padding: 1.5px 5px;
    border-radius: 3px;
    letter-spacing: 0.3px;
}}
.badge-md {{ background: #e0f2fe; color: #0284c7; border: 1px solid #7dd3fc; }}
.badge-ad {{ background: #dcfce7; color: #16a34a; border: 1px solid #86efac; }}
.badge-pd {{ background: #ffedd5; color: #ea580c; border: 1px solid #fdba74; }}

.tier-title-main {{ font-size: 9.5px; font-weight: 800; color: #0f172a; }}
.tier-date-span {{ font-size: 7.5px; font-weight: 700; color: #475569; }}

.tier-text-content {{ font-size: 8.5px; color: #1e293b; line-height: 1.35; margin-bottom: 2.5px; }}
.tier-note-bar {{ font-size: 7.8px; color: #0369a1; background: #f0f9ff; padding: 2px 5px; border-radius: 3px; margin-top: 2px; }}
.tier-subgrid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px;
    margin-top: 3px;
    font-size: 8px;
    color: #334155;
}}
.tier-dos-donts-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-top: 3px;
}}
.do-box {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 4px;
    padding: 3.5px 6px;
    font-size: 7.8px;
}}
.dont-box {{
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-radius: 4px;
    padding: 3.5px 6px;
    font-size: 7.8px;
}}
.do-title {{ font-weight: 800; color: #166534; font-size: 8px; margin-bottom: 2px; }}
.dont-title {{ font-weight: 800; color: #991b1b; font-size: 8px; margin-bottom: 2px; }}
.do-box ul, .dont-box ul {{ list-style: none; padding-left: 0; }}
.do-box li {{ padding-left: 8px; position: relative; margin-bottom: 1.5px; line-height: 1.25; }}
.do-box li::before {{ content: "✔"; position: absolute; left: 0; font-size: 7px; color: #16a34a; }}
.dont-box li {{ padding-left: 8px; position: relative; margin-bottom: 1.5px; line-height: 1.25; }}
.dont-box li::before {{ content: "✖"; position: absolute; left: 0; font-size: 7px; color: #dc2626; }}

/* Roadmap Calendar Table */
.roadmap-table-wrap {{
    margin-top: 5px;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    overflow: hidden;
}}
.roadmap-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.5px;
}}
.roadmap-table th {{
    background: #f8fafc;
    color: #475569;
    font-weight: 800;
    padding: 3px 5px;
    border-bottom: 1px solid #e2e8f0;
    text-transform: uppercase;
}}
.roadmap-table td {{
    padding: 2.5px 5px;
    border-bottom: 1px solid #f1f5f9;
    color: #1e293b;
}}
.roadmap-table tr.active-phase {{
    background: #fffbeb;
    font-weight: 700;
}}
.roadmap-table tr.active-phase td {{
    color: #854d0e;
    border-bottom: 1px solid #fef08a;
}}
.status-chip {{
    font-size: 6.8px;
    font-weight: 800;
    padding: 1px 4px;
    border-radius: 2px;
    display: inline-block;
    background: #f1f5f9;
    color: #475569;
}}
.status-chip.active {{ background: #fef08a; color: #854d0e; border: 1px solid #facc15; }}

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
    gap: 4.5px 6px;
    margin-bottom: 6px;
}}
.pred-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 4px 7px;
    display: flex;
    flex-direction: column;
    gap: 1.5px;
}}
.pred-header {{
    display: flex;
    align-items: center;
    gap: 3px;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 1.5px;
}}
.pred-icon {{
    color: #d4af37;
    font-size: 8px;
}}
.pred-title {{
    font-size: 9px;
    font-weight: 700;
    color: #0f172a;
}}
.pred-body {{
    font-size: 8.2px;
    color: #334155;
    line-height: 1.28;
}}

/* Remedies 2-Column Grid */
.remedies-sequence {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 6px;
    margin-bottom: 5px;
}}
.remedy-card-seq {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 3.5px 6px;
    display: flex;
    gap: 6px;
    align-items: center;
}}
.remedy-num-seq {{
    width: 17px;
    height: 17px;
    min-width: 17px;
    border-radius: 50%;
    background: #fef3c7;
    color: #92400e;
    border: 1px solid #d4af37;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 8.5px;
    font-weight: 800;
}}
.remedy-content-seq {{
    flex: 1;
}}
.remedy-label-seq {{
    font-size: 7.8px;
    font-weight: 700;
    color: #854d0e;
    text-transform: uppercase;
    margin-bottom: 1px;
}}
.remedy-text-seq {{
    font-size: 8.2px;
    color: #334155;
    line-height: 1.25;
}}
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

<!-- ==================== PAGE 1: CLIENT DETAILS & DUAL VEDIC GRIDS ==================== -->
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

            <!-- Profile Card with Dual Grids -->
            <div class="profile-card">
                <div class="client-data-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 5px;">
                    <div class="data-pill">
                        <div class="label">{ui['full_name']}</div>
                        <div class="value">{client['name']}</div>
                    </div>
                    <div class="data-pill">
                        <div class="label">{ui['dob']}</div>
                        <div class="value">{client['dob']} ({client['weekday']})</div>
                    </div>
                    <div class="data-pill">
                        <div class="label">{ui['name_number']} (Namank)</div>
                        <div class="value">{core.get('namank', 1)} • {core['bn_planet'].split()[0]}</div>
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
                        <div class="label">{ui['dasha_timeline']}</div>
                        <div class="value">MD: {dasha['active_md']['number']} | AD: {dasha['active_ad']['ad_number']} | PD: {dasha['active_pd']['number']}</div>
                    </div>
                </div>

                <!-- Dual Grids Side-by-Side (Natal vs Dasha Activation) -->
                <div class="dual-grids-row">
                    <div class="grid-box-card">
                        <div class="grid-caption">👑 {ui['natal_grid_title']}</div>
                        <div class="grid-subtext">{ui['natal_grid_sub']}</div>
                        <div class="vedic-grid">
                            {natal_grid_html}
                        </div>
                    </div>
                    <div class="grid-box-card dasha">
                        <div class="grid-caption dasha">🌌 {ui['dasha_grid_title']}</div>
                        <div class="grid-subtext">{ui['dasha_grid_sub']}</div>
                        <div class="vedic-grid dasha">
                            {dasha_grid_html}
                        </div>
                    </div>
                </div>

                <!-- Color Legend Bar -->
                <div class="grid-legend-bar">
                    <span class="legend-pill"><span class="legend-dot dot-natal"></span> {ui['legend_natal']}</span>
                    <span class="legend-pill"><span class="legend-dot dot-md"></span> {ui['legend_md']}</span>
                    <span class="legend-pill"><span class="legend-dot dot-ad"></span> {ui['legend_ad']}</span>
                    <span class="legend-pill"><span class="legend-dot dot-pd"></span> {ui['legend_pd']}</span>
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

<!-- ==================== PAGE 2: 3-TIER VEDIC PERIOD FORECAST & CALENDAR ROADMAP ==================== -->
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
                <div class="mini-title">{ui['tier_mahadasha_title']} • {ui['tier_antardasha_title']}</div>
                <div class="consultant-tag">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <!-- Tier 1: Mahadasha (Macro Multi-Year Cycle) -->
            <div class="section-title">🌌 {ui['tier_mahadasha_title']}</div>
            <div class="tier-card tier-md">
                <div class="tier-header-bar">
                    <span class="tier-badge badge-md">Mahadasha {md_data.get('number')}</span>
                    <span class="tier-title-main">{md_data.get('planet')} • {md_data.get('duration')}</span>
                    <span class="tier-date-span">Active: {md_data.get('start_str')} — {md_data.get('end_str')}</span>
                </div>
                <div class="tier-text-content">{md_data.get('description', '')}</div>
                <div class="tier-note-bar"><strong>💰 {ui['pred_finance']}:</strong> {md_data.get('rule_note', '')}</div>
            </div>

            <!-- Tier 2: Antardasha (Annual 1-Year Forecast) -->
            <div class="section-title">📅 {ui['tier_antardasha_title']}</div>
            <div class="tier-card tier-ad">
                <div class="tier-header-bar">
                    <span class="tier-badge badge-ad">Antardasha {ad_data.get('number')}</span>
                    <span class="tier-title-main">{ad_data.get('planet')} • Annual Cycle</span>
                    <span class="tier-date-span">Active: {ad_data.get('start_str')} — {ad_data.get('end_str')}</span>
                </div>
                <div class="tier-text-content">{ad_data.get('annual_theme', '')}</div>
                <div class="tier-subgrid">
                    <div><strong>✈ {ui['pred_travel']}:</strong> {ad_data.get('travel_forecast', '')}</div>
                    <div><strong>🏢 {ui['pred_property']}:</strong> {ad_data.get('asset_forecast', '')}</div>
                </div>
            </div>

            <!-- Tier 3: Pratyantar Dasha (Active Monthly Sub-Phase) -->
            <div class="section-title">🌙 {ui['tier_pratyantar_title']}</div>
            <div class="tier-card tier-pd">
                <div class="tier-header-bar">
                    <span class="tier-badge badge-pd">Pratyantar {pd_data.get('number')}</span>
                    <span class="tier-title-main">{pd_data.get('planet')} • Active {pd_data.get('duration_days')} Days</span>
                    <span class="tier-date-span">Active Window: {pd_data.get('start_str')} — {pd_data.get('end_str')}</span>
                </div>
                <div class="tier-dos-donts-grid">
                    <div class="do-box">
                        <div class="do-title">✔ {ui['monthly_dos']}:</div>
                        <ul>{pd_dos_html}</ul>
                    </div>
                    <div class="dont-box">
                        <div class="dont-title">⚠ {ui['monthly_donts']}:</div>
                        <ul>{pd_donts_html}</ul>
                    </div>
                </div>
            </div>

            <!-- Annual 9-Phase Roadmap Table -->
            <div class="section-title">📅 {ui['pd_roadmap_title']}</div>
            <div class="roadmap-table-wrap">
                <table class="roadmap-table">
                    <thead>
                        <tr>
                            <th>Phase / Planet</th>
                            <th style="text-align:center;">No.</th>
                            <th style="text-align:center;">Days</th>
                            <th style="text-align:center;">Start Date</th>
                            <th style="text-align:center;">End Date</th>
                            <th style="text-align:center;">Tone / Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {roadmap_rows_html}
                    </tbody>
                </table>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-stamp">CONSULTATION BY JIGAR THAKKAR (📞 +91 9377614772) • {client['name'].upper()}</span>
            <span>{ui['page']} 2 {ui['of']} 4</span>
        </div>
    </div>
</div>

<!-- ==================== PAGE 3: BHAGYANK, YOGAS & PLANETARY VIBRATIONS ==================== -->
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
            <span>{ui['page']} 3 {ui['of']} 4</span>
        </div>
    </div>
</div>

<!-- ==================== PAGE 4: PREDICTIONS, REMEDIES & CERTIFICATION ==================== -->
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
                <div class="mini-title">{ui['predictions_title']} • {ui['remedies_title']}</div>
                <div class="consultant-tag">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <div class="section-title">{ui['predictions_title']}</div>
            <div class="preds-grid">
                {preds_html}
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
                    <div style="font-size:7.5px;color:#94a3b8;margin-top:3px;">{consultant['copyright']}</div>
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
