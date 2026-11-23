# -*- coding: utf-8 -*-
"""
Vedic Numerology PDF Report Generator - Luxury Step-by-Step Edition
Authored & Certified by: Jigar Thakkar, Certified Numerologist (+91 9377614772 | jigar93776@gmail.com)
Generates user-friendly, progressive 4-page PDF reports in English, Hindi, and Gujarati.
Structured in 4 guided steps with curiosity hooks, clean visual breathing room, and high-contrast readability.
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
    Features progressive 4-step narrative flow, curiosity hooks, and crisp typography.
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
    m_qual_html = "".join([f'<li class="quality-item-clean"><span class="bullet-icon">✦</span><span>{q}</span></li>\n' for q in m_qualities[:4]])

    # Moolank Precautions Grid HTML
    m_prec_html = "".join([f'<li class="precaution-item-clean"><span class="precaution-icon">⚠</span><span>{p}</span></li>\n' for p in m_precautions[:4]])

    # Bhagyank Qualities List HTML
    b_qual_html = "".join([f'<li class="quality-item-clean"><span class="bullet-icon">✦</span><span>{q}</span></li>\n' for q in b_qualities[:4]])

    # Bhagyank Precautions Grid HTML
    b_prec_html = "".join([f'<li class="precaution-item-clean"><span class="precaution-icon">⚠</span><span>{p}</span></li>\n' for p in b_precautions[:4]])

    # 3-Tier Forecast HTML for Page 2
    md_data = three_tier.get("mahadasha", {})
    ad_data = three_tier.get("antardasha", {})
    pd_data = three_tier.get("pratyantar_dasha", {})
    roadmap_data = three_tier.get("pd_roadmap", [])

    # Roadmap table rows
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

    # Yogas Cards HTML (Page 3) - Auspicious & Inauspicious Doshas
    auspicious_list = data.get("auspicious_yogas", [])
    if not auspicious_list:
        auspicious_list = [y for y in yogas if y.get("category") != "inauspicious"]
    inauspicious_list = data.get("inauspicious_yogas", [])
    if not inauspicious_list:
        inauspicious_list = [y for y in yogas if y.get("category") == "inauspicious"]

    # Auspicious HTML (Top 2-3)
    auspicious_yogas_html = ""
    for y in auspicious_list[:3]:
        auspicious_yogas_html += f"""
        <div class="yoga-card-clean auspicious">
            <div class="yoga-card-header">
                <div class="yoga-title">{y['name']}</div>
                <span class="yoga-pill gold">{y['tag']}</span>
            </div>
            <div class="yoga-desc">{y['desc']}</div>
        </div>
        """

    # Inauspicious Doshas HTML (Top 2)
    inauspicious_doshas_html = ""
    if inauspicious_list:
        for y in inauspicious_list[:2]:
            remedy_text = y.get('remedy', '')
            remedy_html = f'<div class="yoga-remedy-strip"><strong>{ui.get("mitigation_remedy", "Remedial Mitigation Key:")}</strong> {remedy_text}</div>' if remedy_text else ''
            inauspicious_doshas_html += f"""
            <div class="yoga-card-clean inauspicious">
                <div class="yoga-card-header">
                    <div class="yoga-title" style="color: #991b1b;">{y['name']}</div>
                    <span class="yoga-pill ruby">{y['tag']}</span>
                </div>
                <div class="yoga-desc">{y['desc']}</div>
                {remedy_html}
            </div>
            """
    else:
        no_dosha_text = {
            "en": "No Adverse Karmic Doshas Active in Chart • The planetary frequencies remain protected by divine harmony.",
            "hi": "जन्म चक्र में कोई प्रतिकूल ग्रहीय दोष सक्रिय नहीं है • ग्रह ऊर्जा पूर्णतः शांत एवं अनुकूल बनी हुई है।",
            "gu": "જન્મ કુંડળીમાં કોઈ પ્રતિકૂળ ગ્રહીય દોષ સક્રિય નથી • ગ્રહ ઉર્જા પૂર્ણપણે શાંત અને અનુકૂળ રહે છે."
        }.get(lang, "No Adverse Karmic Doshas Active in Chart")
        inauspicious_doshas_html = f'<div style="font-size: 8.5px; color: #15803d; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 6px 10px; font-weight: 600;">✔ {no_dosha_text}</div>'

    # Vibration badges on Page 3 (Active Dasha Period Vibrations)
    vibe_badges_html = ""
    for v in vibrations[:8]:
        badge_cls = "badge-pos" if v["type"] == "+" else "badge-neg"
        shift_tag = ""
        if v.get("shifted") and v.get("shift_label"):
            shift_color = "#15803d" if v["type"] == "+" else "#b45309"
            shift_tag = f'<div class="vibe-shift-tag" style="color: {shift_color};">★ {v["shift_label"]}</div>'
        count_str = f" ({v.get('count', 1)}x)" if v.get("count") else ""
        vibe_badges_html += f"""
        <div class="vibe-card {badge_cls}">
            <div class="vibe-header">
                <span class="vibe-num">No. {v['number']}{count_str}</span>
                <span class="vibe-type-badge">{v['type_label']}</span>
            </div>
            {shift_tag}
            <div class="vibe-body">{v['text']}</div>
        </div>
        """

    # Predictions Cards HTML (Page 4)
    pred_categories = ["finance", "property", "vehicle", "education", "travel", "litigation", "relationship", "health"]
    pred_icons = {
        "finance": "💰",
        "property": "🏠",
        "vehicle": "🚗",
        "education": "📚",
        "travel": "✈️",
        "litigation": "⚖️",
        "relationship": "❤️",
        "health": "🌿"
    }
    preds_html = ""
    for cat in pred_categories:
        if cat in preds:
            p_data = preds[cat]
            icon = pred_icons.get(cat, "✦")
            preds_html += f"""
            <div class="pred-card">
                <div class="pred-header">
                    <span class="pred-icon">{icon}</span>
                    <span class="pred-title">{p_data['title']}</span>
                </div>
                <div class="pred-body">{p_data['desc']}</div>
            </div>
            """

    pd_dos_html = "".join([f"<li>{d}</li>" for d in pd_data.get("dos", [])[:3]])
    pd_donts_html = "".join([f"<li>{d}</li>" for d in pd_data.get("donts", [])[:3]])

    # Remedies Cards HTML (Page 4)
    remedy_items = [
        {"num": 1, "icon": "💎", "label": ui["gemstone_remedy"], "text": f"{remedies['moolank_gem']} (Crystal: {remedies['moolank_crystal']})"},
        {"num": 2, "icon": "📿", "label": ui["mantra_remedy"], "text": remedies["moolank_mantra"]},
        {"num": 3, "icon": "🌾", "label": ui["fasting_remedy"], "text": remedies["moolank_fasting"]},
        {"num": 4, "icon": "🤝", "label": ui["donation_remedy"], "text": remedies["moolank_donation"]},
        {"num": 5, "icon": "🕊️", "label": ui["seva_remedy"], "text": remedies["moolank_seva"]},
        {"num": 6, "icon": "🎨", "label": ui["general_remedies"], "text": f"<strong>Health:</strong> {remedies['general_health']} • <strong>Wealth:</strong> {remedies['general_wealth']}"}
    ]
    remedies_html = ""
    for r in remedy_items:
        remedies_html += f"""
        <div class="remedy-card">
            <div class="remedy-num">{r['num']}</div>
            <div class="remedy-content">
                <div class="remedy-label"><span style="margin-right:3px;">{r['icon']}</span>{r['label']}</div>
                <div class="remedy-text">{r['text']}</div>
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
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

@page {{
    size: A4 portrait;
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
    font-size: 9.6px;
    line-height: 1.42;
}}

.page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    padding: 10mm 13mm 9mm 13mm;
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
    top: 4.5mm;
    left: 4.5mm;
    right: 4.5mm;
    bottom: 4.5mm;
    border: 1.2px solid #d4af37;
    pointer-events: none;
    z-index: 1;
}}
.page-border-inner {{
    position: absolute;
    top: 6mm;
    left: 6mm;
    right: 6mm;
    bottom: 6mm;
    border: 0.5px solid #e2c275;
    pointer-events: none;
    z-index: 1;
}}
.corner-ornament {{
    position: absolute;
    width: 12px;
    height: 12px;
    border-color: #b38728;
    z-index: 2;
}}
.corner-tl {{ top: 4.2mm; left: 4.2mm; border-top: 2.5px solid #b38728; border-left: 2.5px solid #b38728; }}
.corner-tr {{ top: 4.2mm; right: 4.2mm; border-top: 2.5px solid #b38728; border-right: 2.5px solid #b38728; }}
.corner-bl {{ bottom: 4.2mm; left: 4.2mm; border-bottom: 2.5px solid #b38728; border-left: 2.5px solid #b38728; }}
.corner-br {{ bottom: 4.2mm; right: 4.2mm; border-bottom: 2.5px solid #b38728; border-right: 2.5px solid #b38728; }}

.page-content {{
    position: relative;
    z-index: 5;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

/* Step Navigation Bar */
.step-banner {{
    background: linear-gradient(135deg, #091124 0%, #172554 100%);
    border: 1px solid #d4af37;
    border-radius: 6px;
    padding: 5px 9px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 7px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}}
.step-banner-left {{
    display: flex;
    align-items: center;
    gap: 7px;
}}
.step-badge-pill {{
    background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);
    color: #0f172a;
    font-size: 8px;
    font-weight: 800;
    text-transform: uppercase;
    padding: 2px 7px;
    border-radius: 12px;
    letter-spacing: 0.5px;
    box-shadow: 0 1px 3px rgba(245,158,11,0.3);
}}
.step-banner-sub {{
    font-size: 8.8px;
    font-weight: 600;
    color: #fef08a;
    letter-spacing: 0.3px;
}}
.step-banner-consultant {{
    font-size: 7.8px;
    color: #93c5fd;
    font-weight: 500;
}}

/* Main Header on Page 1 */
.report-main-header {{
    text-align: center;
    padding-bottom: 5px;
    border-bottom: 1px solid #e8dec9;
    margin-bottom: 7px;
}}
.om-symbol {{
    font-size: 13px;
    color: #b38728;
    font-weight: 700;
    letter-spacing: 2px;
}}
.main-title {{
    font-family: 'Cinzel', serif;
    font-size: 17px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin: 1px 0;
}}
.sub-title {{
    font-size: 8.8px;
    color: #854d0e;
    letter-spacing: 0.4px;
    font-weight: 600;
}}

/* Section Titles */
.section-title {{
    font-family: 'Cinzel', serif;
    font-size: 11px;
    font-weight: 700;
    color: #0f172a;
    border-left: 3px solid #b38728;
    padding-left: 6px;
    margin-bottom: 5px;
    margin-top: 4px;
    display: flex;
    align-items: center;
    letter-spacing: 0.4px;
}}

/* Profile Hero Card */
.profile-card {{
    background: linear-gradient(135deg, #fdfbf7 0%, #f7f3e8 100%);
    border: 1.2px solid #d4af37;
    border-radius: 6px;
    padding: 7px 10px;
    margin-bottom: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}}
.client-data-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 4px 6px;
    margin-bottom: 6px;
}}
.data-pill {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 3px 6px;
}}
.data-pill.highlight {{
    background: #fffbeb;
    border-color: #f59e0b;
}}
.data-pill .label {{
    font-size: 7.2px;
    text-transform: uppercase;
    color: #64748b;
    font-weight: 700;
}}
.data-pill .value {{
    font-size: 9.4px;
    font-weight: 700;
    color: #0f172a;
}}
.data-pill.highlight .value {{
    color: #b45309;
}}

/* Dual Vedic Grids Layout */
.dual-grids-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 5px;
}}
.grid-box-card {{
    background: #ffffff;
    border: 1.2px solid #d4af37;
    border-radius: 5px;
    padding: 4px 6px;
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
    letter-spacing: 0.3px;
    margin-bottom: 1px;
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
    border-radius: 3px;
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
}}
.vedic-cell.natal-cell.active {{
    background: #fef3c7;
    color: #92400e;
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
    font-size: 8px;
}}
.chip {{
    font-size: 8px;
    font-weight: 800;
    padding: 1px 3px;
    border-radius: 2px;
    line-height: 1;
}}
.chip-natal {{ background: #fef3c7; color: #854d0e; border: 1px solid #fde047; }}
.chip-md {{ background: #e0f2fe; color: #0284c7; border: 1px solid #38bdf8; }}
.chip-ad {{ background: #dcfce7; color: #15803d; border: 1px solid #22c55e; }}
.chip-pd {{ background: #f3e8ff; color: #6d28d9; border: 1px solid #7c3aed; }}

.grid-legend-bar {{
    display: flex;
    justify-content: center;
    gap: 8px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 2px 7px;
    margin-bottom: 5px;
    font-size: 7px;
    font-weight: 700;
}}
.legend-pill {{ display: inline-flex; align-items: center; gap: 3px; }}
.legend-dot {{ width: 5.5px; height: 5.5px; border-radius: 50%; display: inline-block; }}
.dot-natal {{ background: #d4af37; }}
.dot-md {{ background: #38bdf8; }}
.dot-ad {{ background: #22c55e; }}
.dot-pd {{ background: #7c3aed; }}

/* Planetary Friendship & Allies Strip */
.allies-box {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #3b82f6;
    border-radius: 5px;
    padding: 5px 8px;
    margin-bottom: 6px;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 4px;
}}
.allies-item {{
    display: flex;
    flex-direction: column;
}}
.allies-label {{
    font-size: 6.8px;
    text-transform: uppercase;
    color: #64748b;
    font-weight: 700;
}}
.allies-val {{
    font-size: 9px;
    font-weight: 700;
    color: #0f172a;
}}
.allies-val.green {{ color: #166534; }}
.allies-val.orange {{ color: #b45309; }}
.allies-val.red {{ color: #991b1b; }}

.name-harmony-bar {{
    background: #f0fdf4;
    border: 1px solid #86efac;
    border-radius: 4px;
    padding: 3.5px 7px;
    font-size: 8.4px;
    color: #166534;
    margin-bottom: 6px;
    line-height: 1.35;
}}

/* 2-Column Traits & Precautions */
.traits-duo-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-bottom: 5px;
}}
.traits-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 5px 7px;
}}
.traits-card.strengths {{
    border-left: 3px solid #16a34a;
    background: #fcfdfc;
}}
.traits-card.precautions {{
    border-left: 3px solid #f59e0b;
    background: #fefdfa;
}}
.traits-card-header {{
    font-size: 8.4px;
    font-weight: 800;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 4px;
}}
.traits-card.strengths .traits-card-header {{ color: #166534; }}
.traits-card.precautions .traits-card-header {{ color: #b45309; }}

.quality-list-clean, .precaution-list-clean {{
    list-style: none;
    padding-left: 0;
}}
.quality-item-clean, .precaution-item-clean {{
    font-size: 8.3px;
    color: #334155;
    line-height: 1.32;
    margin-bottom: 2.5px;
    display: flex;
    align-items: flex-start;
    gap: 4px;
}}
.bullet-icon {{ color: #16a34a; font-size: 8px; font-weight: bold; flex-shrink: 0; }}
.precaution-icon {{ color: #ea580c; font-size: 8px; font-weight: bold; flex-shrink: 0; }}

/* Curiosity Teaser Hook Box */
.curiosity-hook-card {{
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    border: 1.2px solid #f59e0b;
    border-radius: 5px;
    padding: 4px 8px;
    display: flex;
    align-items: center;
    gap: 7px;
    margin-top: auto;
    margin-bottom: 4px;
    box-shadow: 0 1px 3px rgba(245,158,11,0.15);
}}
.curiosity-icon {{
    font-size: 15px;
    flex-shrink: 0;
}}
.curiosity-content {{
    flex: 1;
}}
.curiosity-text {{
    font-size: 7.8px;
    font-weight: 600;
    color: #78350f;
    line-height: 1.32;
}}
.curiosity-hook-card.action-card {{
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border-color: #22c55e;
}}
.curiosity-hook-card.action-card .curiosity-text {{
    color: #14532d;
}}

/* Page 2: 3-Tier Time Horizons */
.intro-lead-pill {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 3px 7px;
    font-size: 8px;
    color: #475569;
    font-weight: 600;
    margin-bottom: 5px;
}}
.tier-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 5px 8px;
    margin-bottom: 5px;
}}
.tier-card.tier-md {{ border-left: 3.5px solid #0284c7; background: #fbfdff; }}
.tier-card.tier-ad {{ border-left: 3.5px solid #16a34a; background: #fbfdfc; }}
.tier-card.tier-pd {{ border-left: 3.5px solid #7c3aed; background: #fbfaff; }}

.tier-header-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2.5px;
    border-bottom: 1px dashed #e2e8f0;
    padding-bottom: 2px;
}}
.tier-badge {{
    font-size: 7.2px;
    font-weight: 800;
    text-transform: uppercase;
    padding: 1.5px 5px;
    border-radius: 3px;
}}
.badge-md {{ background: #e0f2fe; color: #0284c7; border: 1px solid #7dd3fc; }}
.badge-ad {{ background: #dcfce7; color: #16a34a; border: 1px solid #86efac; }}
.badge-pd {{ background: #ffedd5; color: #ea580c; border: 1px solid #fdba74; }}

.tier-title-main {{ font-size: 9.2px; font-weight: 800; color: #0f172a; }}
.tier-date-span {{ font-size: 7.5px; font-weight: 700; color: #475569; }}
.tier-text-content {{ font-size: 8.3px; color: #1e293b; line-height: 1.34; margin-bottom: 2px; }}
.tier-note-bar {{ font-size: 7.6px; color: #0369a1; background: #f0f9ff; padding: 2px 5px; border-radius: 3px; margin-top: 2px; }}
.tier-subgrid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px;
    margin-top: 2.5px;
    font-size: 7.8px;
    color: #334155;
}}
.tier-dos-donts-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
    margin-top: 2px;
}}
.do-box, .dont-box {{
    border-radius: 4px;
    padding: 3px 5px;
    font-size: 7.6px;
}}
.do-box {{ background: #f0fdf4; border: 1px solid #bbf7d0; }}
.dont-box {{ background: #fef2f2; border: 1px solid #fecaca; }}
.do-title {{ font-weight: 800; color: #166534; margin-bottom: 1.5px; }}
.dont-title {{ font-weight: 800; color: #991b1b; margin-bottom: 1.5px; }}
.do-box ul, .dont-box ul {{ list-style: none; padding-left: 0; }}
.do-box li, .dont-box li {{ padding-left: 7px; position: relative; margin-bottom: 1.5px; line-height: 1.25; }}
.do-box li::before {{ content: "✔"; position: absolute; left: 0; font-size: 6.5px; color: #16a34a; }}
.dont-box li::before {{ content: "✖"; position: absolute; left: 0; font-size: 6.5px; color: #dc2626; }}

/* Roadmap Calendar Table */
.roadmap-table-wrap {{
    margin-top: 4px;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 5px;
}}
.roadmap-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.3px;
}}
.roadmap-table th {{
    background: #f8fafc;
    color: #475569;
    font-weight: 800;
    padding: 2.5px 5px;
    border-bottom: 1px solid #e2e8f0;
    text-transform: uppercase;
}}
.roadmap-table td {{
    padding: 2px 5px;
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
    font-size: 6.6px;
    font-weight: 800;
    padding: 1px 3.5px;
    border-radius: 2px;
    display: inline-block;
    background: #f1f5f9;
    color: #475569;
}}
.status-chip.active {{ background: #fef08a; color: #854d0e; border: 1px solid #facc15; }}

/* Page 3: Yogas & Vibrations */
.yogas-grid-clean {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
    margin-bottom: 5px;
}}
.yoga-card-clean {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 4px 6px;
}}
.yoga-card-clean.auspicious {{
    border-left: 3px solid #16a34a;
    background: #fbfdfc;
}}
.yoga-card-clean.inauspicious {{
    border-left: 3px solid #e11d48;
    background: #fffafa;
}}
.yoga-card-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2px;
    padding-bottom: 1.5px;
    border-bottom: 1px dashed #e2e8f0;
}}
.yoga-title {{
    font-size: 9.2px;
    font-weight: 700;
    color: #0f172a;
}}
.yoga-pill {{
    font-size: 7.2px;
    font-weight: 700;
    padding: 1px 4px;
    border-radius: 3px;
}}
.yoga-pill.gold {{ background: #fef3c7; color: #92400e; border: 1px solid #fde047; }}
.yoga-pill.ruby {{ background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }}
.yoga-desc {{
    font-size: 8px;
    color: #334155;
    line-height: 1.3;
}}
.yoga-remedy-strip {{
    font-size: 7.2px;
    color: #991b1b;
    margin-top: 2px;
    padding-top: 2px;
    border-top: 1px dashed #fecdd3;
    line-height: 1.25;
}}

/* Vibrations Grid */
.vibrations-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4.5px;
    margin-bottom: 4px;
}}
.vibe-card {{
    border-radius: 4px;
    padding: 3.5px 6px;
}}
.vibe-card.badge-pos {{ background: #f0fdf4; border: 1px solid #86efac; }}
.vibe-card.badge-neg {{ background: #fef2f2; border: 1px solid #fecaca; }}
.vibe-header {{
    display: flex;
    justify-content: space-between;
    font-weight: 700;
    margin-bottom: 1px;
}}
.badge-pos .vibe-num {{ color: #166534; font-size: 8.5px; }}
.badge-neg .vibe-num {{ color: #991b1b; font-size: 8.5px; }}
.vibe-type-badge {{ font-size: 7.2px; font-weight: 700; }}
.badge-pos .vibe-type-badge {{ color: #166534; }}
.badge-neg .vibe-type-badge {{ color: #991b1b; }}
.vibe-shift-tag {{ font-size: 7px; font-weight: 700; margin-bottom: 1px; }}
.vibe-body {{ font-size: 7.8px; color: #334155; line-height: 1.26; }}

/* Page 4: Predictions 2x4 Grid */
.preds-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 6px;
    margin-bottom: 5px;
}}
.pred-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 4px 6px;
}}
.pred-header {{
    display: flex;
    align-items: center;
    gap: 4px;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 1.5px;
    margin-bottom: 2px;
}}
.pred-icon {{ font-size: 9px; }}
.pred-title {{ font-size: 8.8px; font-weight: 700; color: #0f172a; }}
.pred-body {{ font-size: 8px; color: #334155; line-height: 1.28; }}

/* Remedies 2x3 Grid */
.remedies-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 6px;
    margin-bottom: 5px;
}}
.remedy-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 3.5px 6px;
    display: flex;
    gap: 5px;
    align-items: center;
}}
.remedy-num {{
    width: 16px;
    height: 16px;
    min-width: 16px;
    border-radius: 50%;
    background: #fef3c7;
    color: #92400e;
    border: 1px solid #d4af37;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 8px;
    font-weight: 800;
}}
.remedy-content {{ flex: 1; }}
.remedy-label {{ font-size: 7.6px; font-weight: 700; color: #854d0e; text-transform: uppercase; }}
.remedy-text {{ font-size: 8px; color: #334155; line-height: 1.24; }}

/* Deluxe Master Certification Seal */
.cert-stamp-card-deluxe {{
    background: linear-gradient(135deg, #091124 0%, #1e293b 100%);
    border: 1.2px solid #d4af37;
    border-radius: 6px;
    padding: 7px 11px;
    color: #f8fafc;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
    margin-bottom: 3px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.12);
}}
.cert-title {{
    font-family: 'Cinzel', serif;
    font-size: 10px;
    color: #fbbf24;
    font-weight: 700;
    letter-spacing: 0.6px;
    margin-bottom: 1.5px;
}}
.cert-desc {{
    font-size: 7.8px;
    color: #cbd5e1;
    line-height: 1.3;
    max-width: 460px;
}}
.cert-contact-bar {{
    display: flex;
    gap: 10px;
    margin-top: 3px;
    font-size: 8px;
    color: #fde047;
    font-weight: 600;
}}
.cert-seal-deluxe {{
    border: 1.5px dashed #d4af37;
    border-radius: 50%;
    width: 48px;
    height: 48px;
    min-width: 48px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 6.5px;
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
    padding-top: 3px;
    border-top: 1px solid #e2c275;
    font-size: 7.8px;
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
            <!-- Step Navigation Banner -->
            <div class="step-banner">
                <div class="step-banner-left">
                    <span class="step-badge-pill">{ui.get('step_1_badge', 'STEP 1 OF 4: YOUR COSMIC SOUL CODE')}</span>
                    <span class="step-banner-sub">{ui.get('step_1_title', 'Core Inborn Personality, Dual Vedic Grids & Planetary Allies')}</span>
                </div>
                <div class="step-banner-consultant">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <!-- Header -->
            <div class="report-main-header">
                <div class="om-symbol">॥ श्री गणेशाय नमः ॥</div>
                <h1 class="main-title">{ui['report_title']}</h1>
                <div class="sub-title">Prepared by: <strong>{consultant['name']}</strong> ({consultant['title']}) • 📞 {consultant['phone']} • ✉ {consultant['email']}</div>
            </div>

            <!-- Profile Hero Card -->
            <div class="profile-card">
                <div class="client-data-grid">
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
                        <div class="grid-caption dasha">🪐 {ui['dasha_grid_title']}</div>
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

            <!-- Planetary Allies & Harmony Strip -->
            <div class="allies-box">
                <div class="allies-item">
                    <span class="allies-label">{ui['friendly_numbers']}</span>
                    <span class="allies-val green">{compass.get('friendly_nums', '1, 5, 6')}</span>
                </div>
                <div class="allies-item">
                    <span class="allies-label">{ui['neutral_numbers']}</span>
                    <span class="allies-val orange">{compass.get('neutral_nums', '3, 7')}</span>
                </div>
                <div class="allies-item">
                    <span class="allies-label">{ui['enemy_numbers']}</span>
                    <span class="allies-val red">{compass.get('enemy_nums', '8, 9')}</span>
                </div>
                <div class="allies-item">
                    <span class="allies-label">{ui['auspicious_direction']}</span>
                    <span class="allies-val">{compass.get('direction', 'North')}</span>
                </div>
                <div class="allies-item">
                    <span class="allies-label">{ui['auspicious_metal']}</span>
                    <span class="allies-val">{compass.get('metal', 'Silver')}</span>
                </div>
                <div class="allies-item">
                    <span class="allies-label">{ui['gemstone']}</span>
                    <span class="allies-val">{core['gemstone']}</span>
                </div>
            </div>

            {f'<div class="name-harmony-bar"><strong>{ui["name_harmony"]}:</strong> {name_harmony_text}</div>' if name_harmony_text else ''}

            <!-- Inborn Traits & Precautions 2-Column Split -->
            <div class="traits-duo-grid">
                <div class="traits-card strengths">
                    <div class="traits-card-header">✦ {ui['moolank_qualities']} (No. {core['bn']})</div>
                    <ul class="quality-list-clean">
                        {m_qual_html}
                    </ul>
                </div>
                <div class="traits-card precautions">
                    <div class="traits-card-header">⚠ {ui['moolank_precautions']} (No. {core['bn']})</div>
                    <ul class="precaution-list-clean">
                        {m_prec_html}
                    </ul>
                </div>
            </div>
        </div>

        <!-- Curiosity Preview Hook Box for Step 2 -->
        <div class="curiosity-hook-card">
            <div class="curiosity-icon">🔮</div>
            <div class="curiosity-content">
                <div class="curiosity-text">{ui.get('curiosity_hook_1', 'Next Step: Turn to Page 2 to discover your active 9-Year Mahadasha, your current Annual Focus, and your exact Month-by-Month Timing Matrix...')}</div>
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
            <!-- Step Navigation Banner -->
            <div class="step-banner">
                <div class="step-banner-left">
                    <span class="step-badge-pill">{ui.get('step_2_badge', 'STEP 2 OF 4: YOUR COSMIC TIMELINE & DASHA ROADMAP')}</span>
                    <span class="step-banner-sub">{ui.get('step_2_title', '3-Tier Macro Cycles & 12-Month Action Timing Matrix')}</span>
                </div>
                <div class="step-banner-consultant">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <div class="intro-lead-pill">
                ✦ <strong>Vedic Timing Principles:</strong> Your destiny unfolds in 3 synchronized concentric cycles: <strong>Mahadasha</strong> (Macro Era), <strong>Antardasha</strong> (Annual 1-Year Focus), and <strong>Pratyantar Dasha</strong> (Monthly Sub-Phase).
            </div>

            <!-- Tier 1: Mahadasha (Macro Multi-Year Cycle) -->
            <div class="section-title">🪐 {ui['tier_mahadasha_title']}</div>
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

        <!-- Curiosity Preview Hook Box for Step 3 -->
        <div class="curiosity-hook-card">
            <div class="curiosity-icon">⚡</div>
            <div class="curiosity-content">
                <div class="curiosity-text">{ui.get('curiosity_hook_2', 'Next Step: Turn to Page 3 to explore your Destiny Path, active Divine Yogas, and dynamic planetary vibrations...')}</div>
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
            <!-- Step Navigation Banner -->
            <div class="step-banner">
                <div class="step-banner-left">
                    <span class="step-badge-pill">{ui.get('step_3_badge', 'STEP 3 OF 4: DESTINY PATH, RARE YOGAS & PLANETARY VIBRATIONS')}</span>
                    <span class="step-banner-sub">{ui.get('step_3_title', 'Life Purpose, Special Planetary Combinations & Energetic Shifts')}</span>
                </div>
                <div class="step-banner-consultant">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <!-- Destiny Path 2-Column Split -->
            <div class="section-title">🌟 {ui['bhagyank_qualities']} (No. {core['dn']} - {core['dn_planet']})</div>
            <div class="traits-duo-grid">
                <div class="traits-card strengths">
                    <div class="traits-card-header">✦ Soul Calling & Destiny Gifts</div>
                    <ul class="quality-list-clean">
                        {b_qual_html}
                    </ul>
                </div>
                <div class="traits-card precautions">
                    <div class="traits-card-header">⚠ Essential Growth Guidelines</div>
                    <ul class="precaution-list-clean">
                        {b_prec_html}
                    </ul>
                </div>
            </div>

            <!-- Auspicious Yogas -->
            <div class="section-title">✨ {ui.get('auspicious_yogas_title', ui['active_yogas'])}</div>
            <div class="yogas-grid-clean">
                {auspicious_yogas_html}
            </div>

            <!-- Challenging Doshas -->
            <div class="section-title">⚠ {ui.get('inauspicious_yogas_title', 'Challenging Planetary Yogas & Doshas')}</div>
            <div class="yogas-grid-clean">
                {inauspicious_doshas_html}
            </div>

            <!-- Planetary Vibrations -->
            <div class="section-title">📊 {ui['active_vibrations']}</div>
            <div class="vibrations-grid">
                {vibe_badges_html}
            </div>
            <div style="font-size: 7.2px; color: #475569; font-style: italic; margin-top: 2px; border-top: 0.5px solid #e2e8f0; padding-top: 2px;">
                {ui.get('vibrations_disclaimer', 'Dynamic Vedic Principle: Unlike permanent inborn traits, planetary vibrations dynamically fluctuate under active Mahadasha, Antardasha, and Pratyantar Dasha cycles.')}
            </div>
        </div>

        <!-- Curiosity Preview Hook Box for Step 4 -->
        <div class="curiosity-hook-card">
            <div class="curiosity-icon">🔮</div>
            <div class="curiosity-content">
                <div class="curiosity-text">{ui.get('curiosity_hook_3', 'Next Step: Turn to Page 4 to reveal your 8-Pillar Life Predictions and your personalized Vedic Remedial Protocol...')}</div>
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
            <!-- Step Navigation Banner -->
            <div class="step-banner">
                <div class="step-banner-left">
                    <span class="step-badge-pill">{ui.get('step_4_badge', 'STEP 4 OF 4: 8-PILLAR LIFE PREDICTIONS & SACRED REMEDIES')}</span>
                    <span class="step-banner-sub">{ui.get('step_4_title', 'Personalized Future Guidance & Certified Remedial Protocol')}</span>
                </div>
                <div class="step-banner-consultant">Consultant: {consultant['name']} | 📞 {consultant['phone']}</div>
            </div>

            <!-- Predictions 2x4 Grid -->
            <div class="section-title">🔮 {ui['predictions_title']}</div>
            <div class="preds-grid">
                {preds_html}
            </div>

            <!-- Remedies 2x3 Grid -->
            <div class="section-title">🌿 {ui['remedies_title']}</div>
            <div class="remedies-grid">
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
                    <div style="font-size:7px;color:#94a3b8;margin-top:2px;">{consultant['copyright']}</div>
                </div>
                <div class="cert-seal-deluxe">
                    <span>VEDIC</span>
                    <span>CERTIFIED</span>
                    <span>JIGAR T.</span>
                    <span>✦ 2026 ✦</span>
                </div>
            </div>
        </div>

        <!-- Empowered Action / Success Note -->
        <div class="curiosity-hook-card action-card">
            <div class="curiosity-icon">✨</div>
            <div class="curiosity-content">
                <div class="curiosity-text">{ui.get('curiosity_hook_4', 'Your Empowered Transformation: Apply these sacred remedies with faith and consistency. For personalized 1-on-1 consultations or Vastu audits, contact Jigar Thakkar directly.')}</div>
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
