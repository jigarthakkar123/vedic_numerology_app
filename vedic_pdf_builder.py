# -*- coding: utf-8 -*-
"""
Vedic Numerology PDF Report Generator - Luxury 10-Chapter Master Life Manual Edition
Authored & Certified by: Jigar Thakkar, Certified Numerologist & Vastu Consultant (+91 9377614772 | jigar93776@gmail.com)
Generates user-friendly, progressive 10-page PDF reports in English, Hindi, and Gujarati.
Structured in 10 distinct, dedicated chapters (1 topic per page) with high curiosity hooks,
clean visual breathing room, luxury gold-trimmed styling, and complete responsive rendering.
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
    Constructs a complete HTML document for the luxury 10-page Vedic Numerology Report.
    Features progressive 10-chapter narrative flow (1 topic per page), curiosity hooks,
    and crisp luxury typography.
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
    vibrations = data.get("vibrations", [])
    m_qualities = data.get("moolank_qualities", [])
    m_precautions = data.get("moolank_precautions", [])
    b_qualities = data.get("bhagyank_qualities", [])
    b_precautions = data.get("bhagyank_precautions", [])
    dasha = data.get("dasha", {})
    yogas = data.get("yogas", [])
    preds = data.get("predictions", {})
    remedies = data.get("remedies", {})
    ui = data.get("ui", {})
    lang = client.get("lang", "en")
    tier = str(data.get("tier", client.get("tier", "complete_499"))).lower().strip()
    include_remedies = (tier != "essential_299")
    is_vip = (tier == "vip_1199")

    # Fonts definition based on language
    font_family = "'Plus Jakarta Sans', -apple-system, sans-serif"
    if lang == "hi":
        font_family = "'Plus Jakarta Sans', 'Noto Sans Devanagari', 'Mangal', -apple-system, sans-serif"
    elif lang == "gu":
        font_family = "'Plus Jakarta Sans', 'Shruti', 'Noto Sans Gujarati', -apple-system, sans-serif"

    # Dual Vedic Grids HTML
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

    # Moolank Qualities List HTML (expanded for dedicated page)
    m_qual_html = "".join([f'<li class="quality-item-clean"><span class="bullet-icon">✦</span><span>{q}</span></li>\n' for q in m_qualities[:6]])

    # Moolank Precautions Grid HTML
    m_prec_html = "".join([f'<li class="precaution-item-clean"><span class="precaution-icon">⚠</span><span>{p}</span></li>\n' for p in m_precautions[:6]])

    # Bhagyank Qualities List HTML (expanded for dedicated page)
    b_qual_html = "".join([f'<li class="quality-item-clean"><span class="bullet-icon">✦</span><span>{q}</span></li>\n' for q in b_qualities[:6]])

    # Bhagyank Precautions Grid HTML
    b_prec_html = "".join([f'<li class="precaution-item-clean"><span class="precaution-icon">⚠</span><span>{p}</span></li>\n' for p in b_precautions[:6]])

    # 3-Tier Forecast HTML
    md_data = three_tier.get("mahadasha", {})
    ad_data = three_tier.get("antardasha", {})
    pd_data = three_tier.get("pratyantar_dasha", {})
    roadmap_data = three_tier.get("pd_roadmap", [])

    # Roadmap table rows (Full 9-Phase for dedicated roadmap page)
    roadmap_rows_html = ""
    for r in roadmap_data:
        active_cls = "active-phase" if r.get("is_active") else ""
        badge_txt = "★ ACTIVE" if r.get("is_active") else r.get("tone", "")
        roadmap_rows_html += f"""
        <tr class="{active_cls}">
            <td style="font-weight:700; text-align:center;">Phase {r['phase']}</td>
            <td><strong>{r['planet']}</strong></td>
            <td style="text-align:center;"><strong>No. {r['number']}</strong></td>
            <td style="text-align:center;">{r['duration_days']} Days</td>
            <td style="text-align:center;">{r['start_str']}</td>
            <td style="text-align:center;">{r['end_str']}</td>
            <td style="text-align:center;"><span class="status-chip {'active' if r.get('is_active') else ''}">{badge_txt}</span></td>
        </tr>
        """

    # Yogas Cards HTML (Page 9) - Auspicious & Inauspicious Doshas
    auspicious_list = data.get("auspicious_yogas", [])
    if not auspicious_list:
        auspicious_list = [y for y in yogas if y.get("category") != "inauspicious"]
    inauspicious_list = data.get("inauspicious_yogas", [])
    if not inauspicious_list:
        inauspicious_list = [y for y in yogas if y.get("category") == "inauspicious"]

    # Auspicious HTML (Top 3-4)
    auspicious_yogas_html = ""
    for y in auspicious_list[:4]:
        auspicious_yogas_html += f"""
        <div class="yoga-card-clean auspicious">
            <div class="yoga-card-header">
                <div class="yoga-title">{y['name']}</div>
                <span class="yoga-pill gold">{y['tag']}</span>
            </div>
            <div class="yoga-desc">{y['desc']}</div>
        </div>
        """

    # Inauspicious Doshas HTML
    inauspicious_doshas_html = ""
    if inauspicious_list:
        for y in inauspicious_list[:3]:
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
        inauspicious_doshas_html = f'<div style="font-size: 9.5px; color: #15803d; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 10px 14px; font-weight: 600;">✔ {no_dosha_text}</div>'

    # Vibration badges for Page 9 (All 9 planets spectrum)
    vibe_badges_html = ""
    for v in vibrations[:9]:
        badge_cls = "badge-pos" if v["type"] == "+" else "badge-neg"
        shift_tag = ""
        if v.get("shifted") and v.get("shift_label"):
            shift_color = "#15803d" if v["type"] == "+" else "#b45309"
            shift_tag = f'<div class="vibe-shift-tag" style="color: {shift_color}; font-size: 7.8px; font-weight: 700;">★ {v["shift_label"]}</div>'
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

    # Predictions Cards HTML (Page 10) - 8 Pillars
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

    pd_dos_html = "".join([f"<li>✔ {d}</li>" for d in pd_data.get("dos", [])[:4]])
    pd_donts_html = "".join([f"<li>⚠ {d}</li>" for d in pd_data.get("donts", [])[:4]])

    # Remedies Section HTML (Page 10) - Full in Complete/VIP, Locked in Essential
    remedies_html = ""
    if include_remedies:
        remedy_items = [
            {"num": 1, "icon": "💎", "label": ui.get("gemstone_remedy", "Gemstone"), "text": f"{remedies.get('moolank_gem', '')} (Crystal: {remedies.get('moolank_crystal', '')})"},
            {"num": 2, "icon": "📿", "label": ui.get("mantra_remedy", "Vedic Mantra"), "text": remedies.get("moolank_mantra", "")},
            {"num": 3, "icon": "🌾", "label": ui.get("fasting_remedy", "Fasting Discipline"), "text": remedies.get("moolank_fasting", "")},
            {"num": 4, "icon": "🤝", "label": ui.get("donation_remedy", "Charity & Daan"), "text": remedies.get("moolank_donation", "")},
            {"num": 5, "icon": "🕊️", "label": ui.get("seva_remedy", "Seva & Karma"), "text": remedies.get("moolank_seva", "")},
            {"num": 6, "icon": "🎨", "label": ui.get("general_remedies", "General Remedies"), "text": f"<strong>Health:</strong> {remedies.get('general_health', '')} • <strong>Wealth:</strong> {remedies.get('general_wealth', '')}"}
        ]
        remedies_items_html = ""
        for r in remedy_items:
            remedies_items_html += f"""
            <div class="remedy-card">
                <div class="remedy-num">{r['num']}</div>
                <div class="remedy-content">
                    <div class="remedy-label"><span style="margin-right:4px;">{r['icon']}</span>{r['label']}</div>
                    <div class="remedy-text">{r['text']}</div>
                </div>
            </div>
            """
        remedies_html = f'<div class="remedies-grid">{remedies_items_html}</div>'
    else:
        locked_title = {
            "en": "🔒 Master 6-Pillar Vedic Remedies (Locked in Essential Tier)",
            "hi": "🔒 ६-सूत्रीय वैदिक महा-उपाय (मूल संस्करण में सुरक्षित / लॉक)",
            "gu": "🔒 ૬-સ્તંભ વૈદિક મહા-ઉપાયો (મૂળ આવૃત્તિમાં લોક કરેલ છે)"
        }.get(lang, "🔒 Master 6-Pillar Vedic Remedies (Locked in Essential Tier)")
        
        locked_desc = {
            "en": "Your birth grid indicates specific planetary remedies required to neutralize karmic hurdles and accelerate wealth. The complete prescription—including your customized Primary Gemstone & Crystal frequency, Vedic Beej Mantra Sadhana, Fasting Day, Daan Directive, and Vastu directional keys—is included in the Complete Life Manual & VIP Consultation.",
            "hi": "आपकी जन्म कुंडली एवं दशा चक्र जीवन में ग्रह संतुलन एवं धन-समृद्धि हेतु विशिष्ट वैदिक उपायों की आवश्यकता दर्शाते हैं। आपका व्यक्तिगत भाग्यशाली रत्न, गुप्त वैदिक बीज मंत्र साधना, व्रत अनुशासन, दान निर्देश एवं वास्तु सुधार 'सम्पूर्ण वैदिक लाइफ मैन्युअल' एवं 'VIP परामर्श' में उपलब्ध हैं।",
            "gu": "તમારી જન્મ કુંડળી અને દશા ચક્ર ગ્રહ સંતુલન અને ધન પ્રવાહ વધારવા માટે સચોટ વૈદિક ઉપાયો સૂચવે છે. તમારું લકી રત્ન, વૈદિક બીજ મંત્ર સાધના, વ્રત દિવસ, દાન નિર્દેશ અને વાસ્તુ ઊર્જા સુધારણા 'સંપૂર્ણ વૈદિક લાઇફ મેન્યુઅલ' અને 'VIP કન્સલ્ટેશન' માં ઉપલબ્ધ છે."
        }.get(lang, "Your birth grid indicates specific remedies available in the Complete Life Manual.")

        upgrade_cta = {
            "en": "✦ To unlock your personalized remedies or upgrade your consultation, message Jigar Thakkar on WhatsApp: +91 9377614772",
            "hi": "✦ अपने व्यक्तिगत वैदिक उपाय अनलॉक करने हेतु जिगर ठक्कर से सीधे व्हाट्सएप पर संपर्क करें: +91 9377614772",
            "gu": "✦ તમારા વ્યક્તિગત વૈદિક ઉપાયો અનલોક કરવા માટે જીગર ઠક્કર સાથે સીધા વોટ્સએપ પર સંપર્ક કરો: +91 9377614772"
        }.get(lang, "Contact Jigar Thakkar on WhatsApp: +91 9377614772")

        remedies_html = f"""
        <div style="background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border: 1.5px dashed #d97706; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px; text-align: center;">
            <div style="font-family: 'Cinzel', serif; font-size: 10px; font-weight: 800; color: #92400e; margin-bottom: 4px;">
                {locked_title}
            </div>
            <div style="font-size: 8px; color: #78350f; line-height: 1.4; max-width: 94%; margin: 0 auto 6px;">
                {locked_desc}
            </div>
            <div style="font-size: 7.8px; font-weight: 700; color: #b45309; background: #ffffff; border: 1px solid #fde68a; border-radius: 5px; padding: 4px 8px; display: inline-block;">
                {upgrade_cta}
            </div>
        </div>
        """

    vip_badge_html = ""
    if is_vip:
        vip_badge_html = f"""
        <div style="background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); border: 1.5px solid #d4af37; border-radius: 8px; padding: 7px 12px; margin-bottom: 7px; display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 16px;">👑</span>
                <div>
                    <div style="font-family: 'Cinzel', serif; font-size: 9.5px; font-weight: 800; color: #fbbf24;">VIP 1-ON-1 CONSULTATION CONFIRMED</div>
                    <div style="font-size: 7.6px; color: #cbd5e1;">Your personalized online video/voice consultation with Jigar Thakkar is confirmed. WhatsApp scheduling: +91 9377614772</div>
                </div>
            </div>
            <span style="background: #fbbf24; color: #000; font-size: 7.2px; font-weight: 800; padding: 2px 7px; border-radius: 10px; white-space: nowrap;">MEETING INCLUDED</span>
        </div>
        """

    # Consultant Notes Block HTML
    consultant_notes_html = ""
    if client.get("consultant_notes"):
        consultant_notes_html = f"""
        <div class="consultant-notes-box">
            <div class="consultant-notes-header">✍ {ui.get('consultant_notes', 'Consultant Notes')}</div>
            <div class="consultant-notes-body">{client['consultant_notes']}</div>
        </div>
        """

    name_harmony_text = client.get("name_harmony", {}).get("text", "")

    # Master Table of Contents Items (Index for Page 1)
    toc_html = ""
    for ch_idx in range(1, 10):
        badge = ui.get(f"chap_{ch_idx}_badge", f"CHAPTER {ch_idx}")
        title = ui.get(f"chap_{ch_idx}_title", f"Life Chapter {ch_idx}")
        page_num = ch_idx + 1
        toc_html += f"""
        <div class="toc-item">
            <div class="toc-page-badge">Pg {page_num}</div>
            <div class="toc-text">
                <div class="toc-ch-badge">{badge}</div>
                <div class="toc-ch-title">{title}</div>
            </div>
            <div class="toc-check">✔</div>
        </div>
        """

    def render_curiosity_box(hook_text: str) -> str:
        if not hook_text:
            return ""
        return f"""
        <div class="curiosity-box">
            <div class="curiosity-pill">NEXT CHAPTER</div>
            <div class="curiosity-text">{hook_text}</div>
        </div>
        """

    def render_chapter_banner(ch_num: int) -> str:
        badge = ui.get(f"chap_{ch_num}_badge", f"CHAPTER {ch_num} OF 9")
        title = ui.get(f"chap_{ch_num}_title", "")
        return f"""
        <div class="chap-banner">
            <div class="chap-banner-left">
                <span class="chap-badge-pill">{badge}</span>
                <span class="chap-banner-sub">{title}</span>
            </div>
            <div class="chap-banner-consultant">Jigar Thakkar • Vedic Astrologer</div>
        </div>
        """

    def render_footer(page_num: int) -> str:
        return f"""
        <div class="footer">
            <div><strong>{consultant['name']}</strong> • {consultant['title']} • Phone: {consultant['phone']}</div>
            <div>{ui.get('page', 'Page')} {page_num} of 10</div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{ui.get('report_title', 'Vedic Numerology Report')} - {client['name']}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;600;700&family=Noto+Sans+Gujarati:wght@400;600;700&display=swap');

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
    font-size: 11px;
    line-height: 1.5;
}}

.page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    padding: 8mm 12mm 7mm 12mm;
    background: #ffffff;
    position: relative;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
}}

/* Ornamental Borders */
.page-border {{
    position: absolute;
    top: 3.8mm;
    left: 3.8mm;
    right: 3.8mm;
    bottom: 3.8mm;
    border: 1.2px solid #d4af37;
    pointer-events: none;
    z-index: 1;
}}
.page-border-inner {{
    position: absolute;
    top: 5.2mm;
    left: 5.2mm;
    right: 5.2mm;
    bottom: 5.2mm;
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
.corner-tl {{ top: 3.5mm; left: 3.5mm; border-top: 2.5px solid #b38728; border-left: 2.5px solid #b38728; }}
.corner-tr {{ top: 3.5mm; right: 3.5mm; border-top: 2.5px solid #b38728; border-right: 2.5px solid #b38728; }}
.corner-bl {{ bottom: 3.5mm; left: 3.5mm; border-bottom: 2.5px solid #b38728; border-left: 2.5px solid #b38728; }}
.corner-br {{ bottom: 3.5mm; right: 3.5mm; border-bottom: 2.5px solid #b38728; border-right: 2.5px solid #b38728; }}

.page-content {{
    position: relative;
    z-index: 5;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

/* Chapter Navigation Banner */
.chap-banner {{
    background: linear-gradient(135deg, #091124 0%, #172554 100%);
    border: 1px solid #d4af37;
    border-radius: 6px;
    padding: 5px 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
}}
.chap-banner-left {{
    display: flex;
    align-items: center;
    gap: 8px;
    overflow: hidden;
}}
.chap-badge-pill {{
    background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);
    color: #0f172a;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 12px;
    letter-spacing: 0.5px;
    white-space: nowrap;
}}
.chap-banner-sub {{
    font-size: 11px;
    font-weight: 600;
    color: #fef08a;
    letter-spacing: 0.3px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}}
.chap-banner-consultant {{
    font-size: 9.5px;
    color: #93c5fd;
    font-weight: 500;
    white-space: nowrap;
}}

/* Main Header on Cover Page */
.report-main-header {{
    text-align: center;
    padding-bottom: 6px;
    border-bottom: 1.5px solid #d4af37;
    margin-bottom: 8px;
}}
.om-symbol {{
    font-size: 20px;
    color: #b38728;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 2px;
}}
.main-title {{
    font-family: 'Cinzel', serif;
    font-size: 23px;
    font-weight: 900;
    color: #0f172a;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    margin: 2px 0;
}}
.sub-title {{
    font-size: 11.5px;
    color: #854d0e;
    letter-spacing: 0.5px;
    font-weight: 600;
}}

/* Section Titles */
.section-title {{
    font-family: 'Cinzel', serif;
    font-size: 14px;
    font-weight: 700;
    color: #0f172a;
    border-left: 4px solid #b38728;
    padding-left: 7px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    letter-spacing: 0.4px;
}}

/* Profile Hero Card */
.profile-card {{
    background: linear-gradient(135deg, #fdfbf7 0%, #f7f3e8 100%);
    border: 1.2px solid #d4af37;
    border-radius: 8px;
    padding: 9px 12px;
    margin-bottom: 8px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.03);
}}
.client-data-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 5px 8px;
    margin-bottom: 8px;
}}
.data-pill {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 4px 7px;
}}
.data-pill.highlight {{
    background: #fffbeb;
    border-color: #fcd34d;
}}
.data-pill .label {{
    font-size: 9.5px;
    color: #64748b;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.3px;
}}
.data-pill .value {{
    font-size: 13px;
    color: #0f172a;
    font-weight: 700;
}}
.data-pill.highlight .value {{
    color: #b45309;
    font-size: 14px;
}}

/* Table of Contents Index (Page 1) */
.toc-container {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 6px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}}
.toc-title {{
    font-family: 'Cinzel', serif;
    font-size: 15px;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 1.5px solid #d4af37;
    padding-bottom: 4px;
    margin-bottom: 6px;
    text-align: center;
    letter-spacing: 0.8px;
}}
.toc-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 12px;
}}
.toc-item {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 4px 6px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
}}
.toc-page-badge {{
    background: #172554;
    color: #fbbf24;
    font-size: 10px;
    font-weight: 800;
    padding: 3px 7px;
    border-radius: 4px;
    white-space: nowrap;
}}
.toc-text {{
    flex: 1;
    overflow: hidden;
}}
.toc-ch-badge {{
    font-size: 9px;
    font-weight: 700;
    color: #854d0e;
    text-transform: uppercase;
}}
.toc-ch-title {{
    font-size: 11px;
    font-weight: 600;
    color: #0f172a;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}}
.toc-check {{
    color: #16a34a;
    font-weight: 800;
    font-size: 9px;
}}

/* Dual Grids Row (Page 2) */
.dual-grids-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 10px;
}}
.grid-box-card {{
    background: #ffffff;
    border: 1.5px solid #d4af37;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.03);
}}
.grid-box-card.dasha {{
    border-color: #f59e0b;
    background: #fffdfa;
}}
.grid-caption {{
    font-family: 'Cinzel', serif;
    font-size: 13px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px;
}}
.vedic-grid-table {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 5px;
    max-width: 205px;
    margin: 0 auto;
}}
.vedic-cell {{
    aspect-ratio: 1;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 2px;
    border-radius: 5px;
    font-weight: 800;
    padding: 2px;
    font-size: 15px;
}}
.vedic-cell.natal-cell.active {{
    background: #d97706;
    color: #ffffff;
    box-shadow: 0 1px 3px rgba(217,119,6,0.35);
}}
.vedic-cell.natal-cell.empty {{
    background: #f8fafc;
    color: #cbd5e1;
    border: 1px dashed #cbd5e1;
}}
.vedic-cell.dasha-cell.active {{
    background: #faf5ff;
    border: 1px solid #d8b4fe;
}}
.vedic-cell.dasha-cell.empty {{
    background: #f8fafc;
    color: #cbd5e1;
    border: 1px dashed #cbd5e1;
}}
.chip {{
    font-size: 12px;
    font-weight: 800;
    padding: 2.5px 6px;
    border-radius: 3px;
    display: inline-block;
    line-height: 1.1;
    margin: 1px;
}}
.chip-natal {{
    background: #d97706;
    color: #ffffff;
}}
.chip-md, .chip-mahadasha {{
    background: #0284c7;
    color: #ffffff;
}}
.chip-ad, .chip-antardasha {{
    background: #16a34a;
    color: #ffffff;
}}
.chip-pd, .chip-pratyantar {{
    background: #7c3aed;
    color: #ffffff;
}}

/* Color Legend Bar */
.color-legend-bar {{
    display: flex;
    justify-content: space-around;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 5px 8px;
    margin-bottom: 10px;
}}
.legend-chip {{
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 10px;
    font-weight: 600;
    color: #334155;
}}
.legend-dot {{
    width: 12px;
    height: 12px;
    border-radius: 2px;
}}

/* Plane Cards */
.planes-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-bottom: 8px;
}}
.plane-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 7px 9px;
}}
.plane-header {{
    font-family: 'Cinzel', serif;
    font-size: 12.5px;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 3px;
    margin-bottom: 4px;
}}
.plane-desc {{
    font-size: 10.5px;
    color: #475569;
    line-height: 1.4;
}}

/* Harmony Compass (Page 3) */
.compass-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-bottom: 10px;
}}
.compass-box {{
    border-radius: 8px;
    padding: 10px;
    border: 1px solid;
    text-align: center;
}}
.compass-box.friendly {{
    background: #f0fdf4;
    border-color: #86efac;
}}
.compass-box.neutral {{
    background: #f8fafc;
    border-color: #cbd5e1;
}}
.compass-box.enemy {{
    background: #fef2f2;
    border-color: #fca5a5;
}}
.compass-label {{
    font-family: 'Cinzel', serif;
    font-size: 10px;
    font-weight: 800;
    margin-bottom: 5px;
}}
.compass-box.friendly .compass-label {{ color: #15803d; }}
.compass-box.neutral .compass-label {{ color: #475569; }}
.compass-box.enemy .compass-label {{ color: #b91c1c; }}
.compass-nums {{
    font-size: 18px;
    font-weight: 900;
    letter-spacing: 1px;
}}
.compass-box.friendly .compass-nums {{ color: #166534; }}
.compass-box.neutral .compass-nums {{ color: #1e293b; }}
.compass-box.enemy .compass-nums {{ color: #991b1b; }}
.compass-sub {{
    font-size: 10.5px;
    color: #64748b;
    margin-top: 4px;
}}

/* Alignments 4-Grid */
.align-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 10px;
}}
.align-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 7px 10px;
}}
.align-header {{
    font-size: 10.5px;
    font-weight: 700;
    color: #854d0e;
    text-transform: uppercase;
    margin-bottom: 2px;
}}
.align-val {{
    font-size: 10.5px;
    font-weight: 800;
    color: #0f172a;
}}

/* Name Harmony Card */
.name-card {{
    background: linear-gradient(135deg, #fdfbf7 0%, #fef3c7 100%);
    border: 1.2px solid #d4af37;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 8px;
}}
.name-header {{
    font-family: 'Cinzel', serif;
    font-size: 11px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.name-score-pill {{
    background: #15803d;
    color: #ffffff;
    font-size: 10.5px;
    font-weight: 800;
    padding: 2px 7px;
    border-radius: 10px;
}}
.name-body {{
    font-size: 11px;
    color: #334155;
    line-height: 1.45;
}}

/* Qualities & Precautions (Pages 4 & 5) */
.hero-box {{
    background: linear-gradient(135deg, #091124 0%, #1e293b 100%);
    border: 1.5px solid #d4af37;
    border-radius: 8px;
    padding: 12px 16px;
    color: #ffffff;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.hero-left {{
    flex: 1;
}}
.hero-num-badge {{
    font-size: 10px;
    font-weight: 800;
    color: #fbbf24;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}
.hero-title {{
    font-family: 'Cinzel', serif;
    font-size: 16px;
    font-weight: 800;
    color: #ffffff;
    margin: 2px 0;
}}
.hero-sub {{
    font-size: 11.5px;
    color: #94a3b8;
    line-height: 1.35;
}}
.hero-right-circle {{
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    font-weight: 900;
    color: #0f172a;
    box-shadow: 0 2px 8px rgba(245,158,11,0.4);
}}

.two-col-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
}}
.col-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 12px;
}}
.col-card.precautions {{
    border-color: #fed7aa;
    background: #fffbf5;
}}
.col-title {{
    font-family: 'Cinzel', serif;
    font-size: 13.5px;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 5px;
}}
.quality-item-clean, .precaution-item-clean {{
    list-style: none;
    font-size: 11px;
    margin-bottom: 6px;
    display: flex;
    align-items: flex-start;
    gap: 6px;
    line-height: 1.4;
}}
.bullet-icon {{
    color: #b45309;
    font-weight: 800;
    font-size: 10px;
    flex-shrink: 0;
}}
.precaution-icon {{
    color: #ea580c;
    font-weight: 800;
    font-size: 10px;
    flex-shrink: 0;
}}

.career-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 8px;
}}
.career-title {{
    font-family: 'Cinzel', serif;
    font-size: 10px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 4px;
}}
.career-text {{
    font-size: 11px;
    color: #334155;
    line-height: 1.45;
}}

/* Mahadasha / Forecast (Pages 6 & 7) */
.tier-dash-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 12px;
}}
.tier-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
}}
.tier-card.active-card {{
    border: 1.5px solid #d4af37;
    background: #fffdf8;
    box-shadow: 0 2px 6px rgba(212,175,55,0.15);
}}
.tier-badge {{
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    padding: 2px 6px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 6px;
}}
.tier-badge.gold {{ background: #fef3c7; color: #92400e; }}
.tier-badge.blue {{ background: #dbeafe; color: #1e40af; }}
.tier-badge.purple {{ background: #f3e8ff; color: #6b21a8; }}
.tier-lord {{
    font-size: 12px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 2px;
}}
.tier-dates {{
    font-size: 11px;
    color: #64748b;
    margin-bottom: 6px;
}}
.tier-desc {{
    font-size: 11px;
    color: #334155;
    line-height: 1.35;
    text-align: left;
}}

.tactical-box {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 10px;
}}
.tactical-card {{
    border-radius: 8px;
    padding: 10px 12px;
    border: 1px solid;
}}
.tactical-card.dos {{
    background: #f0fdf4;
    border-color: #86efac;
}}
.tactical-card.donts {{
    background: #fef2f2;
    border-color: #fca5a5;
}}
.tactical-title {{
    font-family: 'Cinzel', serif;
    font-size: 10px;
    font-weight: 800;
    margin-bottom: 6px;
}}
.tactical-card.dos .tactical-title {{ color: #15803d; }}
.tactical-card.donts .tactical-title {{ color: #b91c1c; }}
.tactical-list {{
    list-style: none;
    font-size: 11px;
    line-height: 1.45;
}}
.tactical-card.dos .tactical-list {{ color: #166534; }}
.tactical-card.donts .tactical-list {{ color: #991b1b; }}
.tactical-list li {{ margin-bottom: 4px; }}

/* Roadmap Table (Page 8) */
.roadmap-container {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
}}
.roadmap-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11px;
}}
.roadmap-table th {{
    background: #0f172a;
    color: #f8fafc;
    font-weight: 700;
    padding: 6px 8px;
    text-transform: uppercase;
    font-size: 10.2px;
    letter-spacing: 0.5px;
}}
.roadmap-table td {{
    padding: 5px 8px;
    border-bottom: 1px solid #e2e8f0;
}}
.roadmap-table tr.active-phase {{
    background: #fffbeb !important;
    font-weight: 700;
}}
.roadmap-table tr.active-phase td {{
    border-top: 1.5px solid #f59e0b;
    border-bottom: 1.5px solid #f59e0b;
}}
.status-chip {{
    font-size: 10px;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 10px;
    display: inline-block;
    background: #f1f5f9;
    color: #475569;
}}
.status-chip.active {{
    background: #f59e0b;
    color: #ffffff;
    box-shadow: 0 1px 3px rgba(245,158,11,0.4);
}}

/* Yogas & Vibrations (Page 9) */
.yoga-card-clean {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 7px;
}}
.yoga-card-clean.auspicious {{
    border-left: 3.5px solid #16a34a;
    background: #f0fdf4;
}}
.yoga-card-clean.inauspicious {{
    border-left: 3.5px solid #dc2626;
    background: #fef2f2;
}}
.yoga-card-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 3px;
}}
.yoga-title {{
    font-family: 'Cinzel', serif;
    font-size: 10px;
    font-weight: 800;
    color: #0f172a;
}}
.yoga-pill {{
    font-size: 9.5px;
    font-weight: 800;
    padding: 3px 7px;
    border-radius: 8px;
    text-transform: uppercase;
}}
.yoga-pill.gold {{ background: #fef3c7; color: #92400e; }}
.yoga-pill.ruby {{ background: #fee2e2; color: #991b1b; }}
.yoga-desc {{
    font-size: 10.5px;
    color: #475569;
    line-height: 1.4;
}}
.yoga-remedy-strip {{
    margin-top: 4px;
    padding: 4px 7px;
    background: #ffffff;
    border-radius: 4px;
    font-size: 10.5px;
    color: #991b1b;
    border: 1px dashed #fca5a5;
}}

.vibes-dashboard-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    margin-bottom: 8px;
}}
.vibe-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 6px 8px;
}}
.vibe-card.badge-pos {{ border-left: 3px solid #16a34a; }}
.vibe-card.badge-neg {{ border-left: 3px solid #f59e0b; }}
.vibe-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2px;
}}
.vibe-num {{
    font-size: 9px;
    font-weight: 800;
    color: #0f172a;
}}
.vibe-type-badge {{
    font-size: 9px;
    font-weight: 700;
    padding: 2px 5px;
    border-radius: 4px;
}}
.vibe-card.badge-pos .vibe-type-badge {{ background: #dcfce7; color: #15803d; }}
.vibe-card.badge-neg .vibe-type-badge {{ background: #fef3c7; color: #b45309; }}
.vibe-body {{
    font-size: 10.2px;
    color: #475569;
    line-height: 1.35;
}}

/* Predictions & Remedies (Page 10) */
.preds-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
    margin-bottom: 8px;
}}
.pred-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 6px 8px;
}}
.pred-header {{
    display: flex;
    align-items: center;
    gap: 4px;
    margin-bottom: 3px;
}}
.pred-icon {{
    font-size: 11px;
}}
.pred-title {{
    font-family: 'Cinzel', serif;
    font-size: 11.5px;
    font-weight: 800;
    color: #0f172a;
}}
.pred-body {{
    font-size: 10.2px;
    color: #334155;
    line-height: 1.4;
}}

.remedies-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    margin-bottom: 8px;
}}
.remedy-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 6px 8px;
    display: flex;
    gap: 6px;
}}
.remedy-num {{
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #172554;
    color: #fbbf24;
    font-size: 11px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}}
.remedy-content {{
    flex: 1;
}}
.remedy-label {{
    font-family: 'Cinzel', serif;
    font-size: 11px;
    font-weight: 800;
    color: #854d0e;
    margin-bottom: 1px;
}}
.remedy-text {{
    font-size: 10.5px;
    color: #334155;
    line-height: 1.3;
}}

/* Astrological Seal Card */
.seal-card {{
    background: linear-gradient(135deg, #091124 0%, #172554 100%);
    border: 1.5px solid #d4af37;
    border-radius: 8px;
    padding: 8px 14px;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 4px;
}}
.seal-symbol {{
    font-size: 34px;
    color: #fbbf24;
    line-height: 1;
}}
.seal-content {{
    flex: 1;
}}
.seal-title {{
    font-family: 'Cinzel', serif;
    font-size: 14px;
    font-weight: 800;
    color: #fbbf24;
    letter-spacing: 0.8px;
    margin-bottom: 2px;
}}
.seal-text {{
    font-size: 10.5px;
    color: #cbd5e1;
    line-height: 1.4;
}}
.seal-blessing {{
    font-size: 10.5px;
    color: #fef08a;
    font-weight: 600;
    margin-top: 3px;
}}

/* Curiosity Preview Hook */
.curiosity-box {{
    background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    border: 1px dashed #d97706;
    border-radius: 6px;
    padding: 4px 8px;
    margin-top: 4px;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 8px;
}}
.curiosity-pill {{
    background: #d97706;
    color: #ffffff;
    font-size: 9.5px;
    font-weight: 800;
    padding: 3px 7px;
    border-radius: 10px;
    white-space: nowrap;
    text-transform: uppercase;
}}
.curiosity-text {{
    font-size: 10.5px;
    color: #78350f;
    font-weight: 600;
    line-height: 1.35;
}}

/* Footer */
.footer {{
    border-top: 1px solid #e2e8f0;
    padding-top: 4px;
    font-size: 9.5px;
    color: #64748b;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2px;
}}
</style>
</head>
<body>

<!-- ==================== PAGE 1: ROYAL COVER & SOUL CERTIFICATE ==================== -->
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
                <div class="om-symbol">ॐ • श्री गणेशाय नमः • ॐ</div>
                <h1 class="main-title">{ui.get('report_title', 'Personal Vedic Numerology Blueprint')}</h1>
                <p class="sub-title">Authentic Sankhya Shastra Analysis & 10-Year Dasha Roadmap</p>
            </div>

            <!-- Profile Hero Certificate Card -->
            <div class="profile-card">
                <div class="client-data-grid">
                    <div class="data-pill">
                        <div class="label">{ui.get('full_name', 'Client Name')}</div>
                        <div class="value">{client['name']}</div>
                    </div>
                    <div class="data-pill">
                        <div class="label">{ui.get('dob', 'Date of Birth')}</div>
                        <div class="value">{client['dob']} ({client.get('weekday', '')})</div>
                    </div>
                    <div class="data-pill">
                        <div class="label">{ui.get('gender', 'Gender')}</div>
                        <div class="value">{str(client.get('gender', 'Male')).capitalize()}</div>
                    </div>
                    <div class="data-pill highlight">
                        <div class="label">{ui.get('basic_number', 'Moolank (Soul Number)')}</div>
                        <div class="value">{core['bn']} — {core['bn_planet']}</div>
                    </div>
                    <div class="data-pill highlight">
                        <div class="label">{ui.get('destiny_number', 'Bhagyank (Destiny Path)')}</div>
                        <div class="value">{core['dn']} — {core['dn_planet']}</div>
                    </div>
                    <div class="data-pill highlight">
                        <div class="label">{ui.get('name_number', 'Namank (Name Number)')}</div>
                        <div class="value">{core['namank']} ({client.get('name_harmony', {}).get('status', 'Balanced').title()})</div>
                    </div>
                </div>
            </div>

            <!-- Master Table of Contents Index -->
            <div class="toc-container">
                <div class="toc-title">📜 {ui.get('toc_title', '10-Chapter Master Life Index')}</div>
                <div class="toc-grid">
                    {toc_html}
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_1', ''))}
            {render_footer(1)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 2: CHAPTER 1 - DUAL VEDIC SACRED GRIDS ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(1)}
            <div class="section-title">🕉️ {ui.get('chap_1_title', 'Dual Vedic Grids: Lifetime Natal Blueprint & Active Dasha Activation')}</div>

            <!-- Dual Grids Side-by-Side -->
            <div class="dual-grids-row">
                <div class="grid-box-card">
                    <div class="grid-caption">
                        <span>🌟</span>
                        <span>{ui.get('natal_grid_title', 'Natal Birth Grid')}</span>
                    </div>
                    <div class="vedic-grid-table">
                        {natal_grid_html}
                    </div>
                    <div style="font-size: 8px; color: #64748b; margin-top: 6px;">
                        Fixed cosmic imprint cast at moment of birth.
                    </div>
                </div>

                <div class="grid-box-card dasha">
                    <div class="grid-caption" style="color: #b45309;">
                        <span>🪐</span>
                        <span>{ui.get('dasha_grid_title', 'Dasha Activation Grid')}</span>
                    </div>
                    <div class="vedic-grid-table">
                        {dasha_grid_html}
                    </div>
                    <div style="font-size: 8px; color: #b45309; margin-top: 6px; font-weight: 600;">
                        Active energies activated by {three_tier.get('mahadasha', {}).get('planet', 'Mahadasha')}.
                    </div>
                </div>
            </div>

            <!-- Color Legend Bar -->
            <div class="color-legend-bar">
                <div class="legend-chip"><span class="legend-dot" style="background: #d97706;"></span><span>{ui.get('legend_natal', 'Natal Inborn (Gold)')}</span></div>
                <div class="legend-chip"><span class="legend-dot" style="background: #0284c7;"></span><span>{ui.get('legend_md', 'Mahadasha • Multi-Year (Sky Blue)')}</span></div>
                <div class="legend-chip"><span class="legend-dot" style="background: #16a34a;"></span><span>{ui.get('legend_ad', 'Antardasha • Yearly (Emerald Green)')}</span></div>
                <div class="legend-chip"><span class="legend-dot" style="background: #ffffff; border: 1.5px dashed #94a3b8;"></span><span>{ui.get('legend_missing', 'Missing Void')}</span></div>
            </div>

            <!-- Grid Planes Analysis Cards -->
            <div class="planes-grid">
                <div class="plane-card">
                    <div class="plane-header">Mental Plane (4-9-2)</div>
                    <div class="plane-desc">Governs intellectual capacity, analytical strategy, memory, and visionary execution. Shows mental focus and long-term foresight.</div>
                </div>
                <div class="plane-card">
                    <div class="plane-header">Emotional Plane (3-5-7)</div>
                    <div class="plane-desc">Governs spiritual intuition, empathy, heart connection, and determination. Reflects willpower and emotional stability.</div>
                </div>
                <div class="plane-card">
                    <div class="plane-header">Practical Plane (8-1-6)</div>
                    <div class="plane-desc">Governs material manifestation, business acumen, hard work, and wealth accumulation. Directs physical action.</div>
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_2', ''))}
            {render_footer(2)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 3: CHAPTER 2 - COSMIC ALLIES & HARMONY COMPASS ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(2)}
            <div class="section-title">🧭 {ui.get('chap_2_title', 'Cosmic Allies, Auspicious Vastu Orientations & Name Frequency Alignment')}</div>

            <!-- Harmony Compass 3 Cards -->
            <div class="compass-grid">
                <div class="compass-box friendly">
                    <div class="compass-label">✦ {ui.get('friendly_numbers', 'Friendly Numbers')}</div>
                    <div class="compass-nums">{compass.get('friendly_nums', core['favourable_nums'])}</div>
                    <div class="compass-sub">Best for partnerships, bank accounts, vehicle plates, contracts</div>
                </div>
                <div class="compass-box neutral">
                    <div class="compass-label">☯ {ui.get('neutral_numbers', 'Neutral Numbers')}</div>
                    <div class="compass-nums">{compass.get('neutral_nums', '1, 4, 7')}</div>
                    <div class="compass-sub">Harmonious and peaceful interactions without friction</div>
                </div>
                <div class="compass-box enemy">
                    <div class="compass-label">⚠ {ui.get('enemy_numbers', 'Unfriendly / Avoid Numbers')}</div>
                    <div class="compass-nums">{compass.get('enemy_nums', 'None')}</div>
                    <div class="compass-sub">Avoid for critical life signatures, agreements, and major deals</div>
                </div>
            </div>

            <!-- Auspicious Alignments 4-Grid -->
            <div class="align-grid">
                <div class="align-card">
                    <div class="align-header">📅 {ui.get('favourable_days', 'Favourable Days')}</div>
                    <div class="align-val">{core['favourable_days']}</div>
                </div>
                <div class="align-card">
                    <div class="align-header">🎨 {ui.get('favourable_colors', 'Favourable Colors')}</div>
                    <div class="align-val">{core['favourable_colors']}</div>
                </div>
                <div class="align-card">
                    <div class="align-header">🧭 {ui.get('auspicious_direction', 'Auspicious Vastu Direction')}</div>
                    <div class="align-val">{compass.get('direction', 'North-East (Ishanya)')}</div>
                </div>
                <div class="align-card">
                    <div class="align-header">💎 {ui.get('gemstone_remedy', 'Recommended Gemstone')} & Metal</div>
                    <div class="align-val">{core['gemstone']} • {compass.get('metal', 'Gold / Silver')}</div>
                </div>
            </div>

            <!-- Chaldean Name Frequency Alignment -->
            <div class="name-card">
                <div class="name-header">
                    <span>🔤 Chaldean Name Numerology: {client['name']}</span>
                    <span class="name-score-pill">Namank {core['namank']} • {client.get('name_harmony', {}).get('status', 'Balanced').title()}</span>
                </div>
                <div class="name-body">
                    {name_harmony_text}
                    <div style="margin-top: 6px; font-size: 8.5px; color: #854d0e; font-weight: 600;">
                        💡 <strong>Vedic Advice:</strong> Align your professional signature and email handle with your favorable compound numbers to attract effortless abundance.
                    </div>
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_3', ''))}
            {render_footer(3)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 4: CHAPTER 3 - INBORN SOUL MATRIX (MOOLANK) ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(3)}
            <div class="section-title">🌟 {ui.get('chap_3_title', 'Core Personality, Inborn Superpowers & Mindful Guardrails (Moolank)')}</div>

            <!-- Moolank Hero Box -->
            <div class="hero-box">
                <div class="hero-left">
                    <div class="hero-num-badge">Root Archetype • Soul Vibration</div>
                    <div class="hero-title">{core['bn_planet']} (Moolank {core['bn']})</div>
                    <div class="hero-sub">The radical energy frequency determined by your birth date, shaping your intrinsic psychology, instincts, and raw natural gifts.</div>
                </div>
                <div class="hero-right-circle">{core['bn']}</div>
            </div>

            <!-- 2-Column Split: Superpowers vs Mindful Guardrails -->
            <div class="two-col-grid">
                <div class="col-card">
                    <div class="col-title" style="color: #15803d;">
                        <span>✦</span>
                        <span>{ui.get('moolank_qualities', 'Inborn Core Talents & Superpowers')}</span>
                    </div>
                    <ul style="padding-left: 0;">
                        {m_qual_html}
                    </ul>
                </div>

                <div class="col-card precautions">
                    <div class="col-title" style="color: #c2410c;">
                        <span>⚠</span>
                        <span>{ui.get('moolank_precautions', 'Mindful Guardrails & Pitfalls')}</span>
                    </div>
                    <ul style="padding-left: 0;">
                        {m_prec_html}
                    </ul>
                </div>
            </div>

            <!-- Career Inclinations Box -->
            <div class="career-box">
                <div class="career-title">💼 Career & Wealth Pathways for Moolank {core['bn']}</div>
                <div class="career-text">
                    Naturally thrives in leadership, visionary advisory, independent enterprise, and fields demanding intellectual discernment. Creates maximum wealth when maintaining emotional detachment and upholding ethical integrity.
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_4', ''))}
            {render_footer(4)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 5: CHAPTER 4 - DESTINY BLUEPRINT (BHAGYANK) ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(4)}
            <div class="section-title">🎯 {ui.get('chap_4_title', 'Karmic Calling, Higher Life Mission & Soul Purpose (Bhagyank)')}</div>

            <!-- Bhagyank Hero Box -->
            <div class="hero-box" style="background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);">
                <div class="hero-left">
                    <div class="hero-num-badge" style="color: #a78bfa;">Life Path • Karmic Mission</div>
                    <div class="hero-title">{core['dn_planet']} (Bhagyank {core['dn']})</div>
                    <div class="hero-sub">The aggregate cosmic frequency calculated from your full birth date, representing what the universe demands you master and achieve.</div>
                </div>
                <div class="hero-right-circle" style="background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 100%); color: #ffffff;">{core['dn']}</div>
            </div>

            <!-- 2-Column Split: Destiny Calling vs Karmic Lessons -->
            <div class="two-col-grid">
                <div class="col-card">
                    <div class="col-title" style="color: #6d28d9;">
                        <span>✦</span>
                        <span>{ui.get('bhagyank_qualities', 'Destiny Calling & Life Mission')}</span>
                    </div>
                    <ul style="padding-left: 0;">
                        {b_qual_html}
                    </ul>
                </div>

                <div class="col-card precautions">
                    <div class="col-title" style="color: #b91c1c;">
                        <span>⚠</span>
                        <span>{ui.get('bhagyank_precautions', 'Karmic Lessons & Growth Catalysts')}</span>
                    </div>
                    <ul style="padding-left: 0;">
                        {b_prec_html}
                    </ul>
                </div>
            </div>

            <!-- The Sacred Bridge Box -->
            <div class="career-box" style="border-left: 3.5px solid #d4af37; background: #fffdf8;">
                <div class="career-title" style="color: #854d0e;">🌉 The Sacred Bridge: Harmonizing Moolank {core['bn']} with Bhagyank {core['dn']}</div>
                <div class="career-text">
                    Your Moolank dictates your internal desires and comfort zone, while your Bhagyank represents the external arena of your life's greatest victories. When you align your daily actions with your Bhagyank frequency, worldly obstacles dissolve into stepping stones.
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_5', ''))}
            {render_footer(5)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 6: CHAPTER 5 - MACRO TIME WHEEL (MAHADASHA) ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(5)}
            <div class="section-title">🪐 {ui.get('chap_5_title', 'Mahadasha: 9-Year Macro Planetary Life Cycle & Wealth Directives')}</div>

            <!-- Mahadasha Hero Dashboard -->
            <div class="hero-box" style="background: linear-gradient(135deg, #451a03 0%, #1c1917 100%); border-color: #f59e0b;">
                <div class="hero-left">
                    <div class="hero-num-badge" style="color: #fde047;">Macro Time Phase • 9-Year Reign</div>
                    <div class="hero-title">{md_data.get('planet', 'Mahadasha')} (No. {md_data.get('number', '')})</div>
                    <div class="hero-sub">Duration: {md_data.get('duration_years', 9)} Years • Operating Window: {md_data.get('start_year', '')} — {md_data.get('end_year', '')}</div>
                </div>
                <div class="hero-right-circle" style="background: linear-gradient(135deg, #fbbf24 0%, #b45309 100%);">{md_data.get('number', '')}</div>
            </div>

            <!-- Macro Opportunities 4-Pillar Grid -->
            <div class="align-grid" style="margin-bottom: 12px;">
                <div class="align-card">
                    <div class="align-header">💰 Wealth & Capital Expansion</div>
                    <div class="career-text">High-leverage investment cycles peak under this macro ruler. Prioritize tangible asset creation over speculative risks.</div>
                </div>
                <div class="align-card">
                    <div class="align-header">🏢 Professional Elevation</div>
                    <div class="career-text">Expansion of authority and reputation. Strategic networking opens access to influential decision makers.</div>
                </div>
                <div class="align-card">
                    <div class="align-header">🏠 Real Estate & Property</div>
                    <div class="career-text">Favorable periods for property deeds, home revitalization, and establishing stable familial roots.</div>
                </div>
                <div class="align-card">
                    <div class="align-header">🧘 Spiritual Consciousness</div>
                    <div class="career-text">Intensified intuitive depth and karmic clearing. Alignment with higher purpose yields peace and fulfillment.</div>
                </div>
            </div>

            <!-- In-Depth Macro Interpretation -->
            <div class="career-box" style="border-left: 3.5px solid #d97706;">
                <div class="career-title" style="color: #9a3412;">📜 Macro Directive for Active Mahadasha</div>
                <div class="career-text">
                    {md_data.get('desc', 'This active Mahadasha cycle marks a transformative epoch where foundational life decisions bear exponential fruit. Maintain consistent discipline and align your goals with the planetary frequency of ' + md_data.get('planet', 'your ruling planet') + '.')}
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_6', ''))}
            {render_footer(6)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 7: CHAPTER 6 - ANNUAL & MONTHLY TIMING ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(6)}
            <div class="section-title">📅 {ui.get('chap_6_title', 'Antardasha (Annual 1-Year Forecast) & Active Pratyantar Action Window')}</div>

            <!-- Tier 2 & Tier 3 Split Cards -->
            <div class="two-col-grid" style="margin-bottom: 12px;">
                <div class="col-card" style="border-top: 3.5px solid #2563eb;">
                    <div class="col-title" style="color: #1e40af;">
                        <span>📅</span>
                        <span>{ui.get('tier_antardasha_title', 'Annual Antardasha (1-Year Focus)')}</span>
                    </div>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin-bottom: 3px;">
                        {ad_data.get('planet', 'Antardasha')} (No. {ad_data.get('number', '')})
                    </div>
                    <div style="font-size: 8.2px; color: #64748b; margin-bottom: 6px;">
                        Timeline: {ad_data.get('start_str', '')} to {ad_data.get('end_str', '')}
                    </div>
                    <div class="career-text">
                        {ad_data.get('desc', 'Year of targeted consolidation and strategic action.')}
                    </div>
                </div>

                <div class="col-card" style="border-top: 3.5px solid #7c3aed;">
                    <div class="col-title" style="color: #6d28d9;">
                        <span>🌙</span>
                        <span>{ui.get('tier_pratyantar_title', 'Active Pratyantar Dasha (30-Day Window)')}</span>
                    </div>
                    <div style="font-size: 11px; font-weight: 800; color: #0f172a; margin-bottom: 3px;">
                        {pd_data.get('planet', 'Pratyantar')} (No. {pd_data.get('number', '')})
                    </div>
                    <div style="font-size: 8.2px; color: #64748b; margin-bottom: 6px;">
                        Active Window: {pd_data.get('start_str', '')} to {pd_data.get('end_str', '')} ({pd_data.get('duration_days', 30)} Days)
                    </div>
                    <div class="career-text">
                        {pd_data.get('desc', 'Current monthly sub-period operating with heightened sensitivity.')}
                    </div>
                </div>
            </div>

            <!-- Tactical Guide: Do's and Don'ts -->
            <div class="tactical-box">
                <div class="tactical-card dos">
                    <div class="tactical-title">✔ {ui.get('monthly_dos', 'Actions Blessed with Cosmic Momentum (Do This)')}</div>
                    <ul class="tactical-list">
                        {pd_dos_html}
                    </ul>
                </div>

                <div class="tactical-card donts">
                    <div class="tactical-title">⚠ {ui.get('monthly_donts', 'Friction Points to Avoid (Caution)')}</div>
                    <ul class="tactical-list">
                        {pd_donts_html}
                    </ul>
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_7', ''))}
            {render_footer(7)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 8: CHAPTER 7 - 12-MONTH CALENDAR ROADMAP ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(7)}
            <div class="section-title">🗓️ {ui.get('chap_7_title', 'Annual 9-Phase Pratyantar Dasha Timeline & Golden Timing Windows')}</div>

            <!-- 9-Phase Comprehensive Table -->
            <div class="roadmap-container">
                <table class="roadmap-table">
                    <thead>
                        <tr>
                            <th>Phase</th>
                            <th>Sub-Lord</th>
                            <th style="text-align:center;">Vibration</th>
                            <th style="text-align:center;">Duration</th>
                            <th style="text-align:center;">Start Date</th>
                            <th style="text-align:center;">End Date</th>
                            <th style="text-align:center;">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {roadmap_rows_html}
                    </tbody>
                </table>
            </div>

            <!-- Golden Timing Directives -->
            <div class="career-box" style="border-left: 3.5px solid #16a34a; background: #f0fdf4;">
                <div class="career-title" style="color: #15803d;">💡 How to Navigate Your 12-Month Calendar Roadmap</div>
                <div class="career-text">
                    The highlighted <strong>★ ACTIVE</strong> row represents your immediate universal atmospheric energy. When transitioning into phases governed by your friendly numbers ({compass.get('friendly_nums', core['favourable_nums'])}), execute major contracts, property deals, and launches. During neutral or enemy phases, protect capital and focus on planning.
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_8', ''))}
            {render_footer(8)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 9: CHAPTER 8 - PLANETARY YOGAS & VIBRATIONS ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(8)}
            <div class="section-title">✨ {ui.get('chap_8_title', 'Rare Planetary Yogas, Karmic Afflictions & Dynamic Vibrational Polarities')}</div>

            <!-- Auspicious Yogas -->
            <div style="margin-bottom: 8px;">
                <div style="font-size: 9px; font-weight: 800; color: #166534; text-transform: uppercase; margin-bottom: 4px;">
                    👑 {ui.get('auspicious_yogas_title', 'Auspicious Planetary Yogas (Divine Alignments)')}
                </div>
                {auspicious_yogas_html}
            </div>

            <!-- Inauspicious Doshas -->
            <div style="margin-bottom: 8px;">
                <div style="font-size: 9px; font-weight: 800; color: #991b1b; text-transform: uppercase; margin-bottom: 4px;">
                    ⚠ {ui.get('inauspicious_yogas_title', 'Challenging Planetary Yogas & Doshas (Karmic Hurdles)')}
                </div>
                {inauspicious_doshas_html}
            </div>

            <!-- Planetary Vibrations Spectrum (9 Planets) -->
            <div>
                <div style="font-size: 9px; font-weight: 800; color: #0f172a; text-transform: uppercase; margin-bottom: 4px;">
                    📊 {ui.get('active_vibrations', 'Planetary Vibrations Analysis')} (Planetary Spectrum 1-9)
                </div>
                <div class="vibes-dashboard-grid">
                    {vibe_badges_html}
                </div>
            </div>
        </div>

        <div>
            {render_curiosity_box(ui.get('curiosity_hook_9', ''))}
            {render_footer(9)}
        </div>
    </div>
</div>

<!-- ==================== PAGE 10: CHAPTER 9 - PREDICTIONS, REMEDIES & SEAL ==================== -->
<div class="page">
    <div class="page-border"></div>
    <div class="page-border-inner"></div>
    <div class="corner-ornament corner-tl"></div>
    <div class="corner-ornament corner-tr"></div>
    <div class="corner-ornament corner-bl"></div>
    <div class="corner-ornament corner-br"></div>

    <div class="page-content">
        <div>
            {render_chapter_banner(9)}
            <div class="section-title">🔮 {ui.get('chap_9_title', '8-Pillar Life Predictions, Sacred Vedic Remedies & Official Certification')}</div>

            <!-- 8-Pillar Predictions 2x4 Grid -->
            <div class="preds-grid">
                {preds_html}
            </div>

            <!-- Master 6-Pillar Vedic Remedies -->
            {remedies_html}

            {vip_badge_html}

            {consultant_notes_html}

            <!-- Astrological Seal & Official Verification Card -->
            <div class="seal-card">
                <div class="seal-symbol">🕉️</div>
                <div class="seal-content">
                    <div class="seal-title">{ui.get('certified_box_title', 'Certified Astrological Verification & Seal')}</div>
                    <div class="seal-text">
                        {ui.get('certified_box_text', 'This report is prepared and mathematically certified by Jigar Thakkar, Certified Numerologist & Vastu Consultant.')}
                    </div>
                    <div class="seal-blessing">
                        ✦ {ui.get('empowerment_blessing', 'Planets indicate tendencies; consciousness and righteous action command destiny.')}
                    </div>
                </div>
            </div>
        </div>

        <div>
            {render_footer(10)}
        </div>
    </div>
</div>

</body>
</html>"""
    return html

def render_pdf_from_html(html_content_or_path: str, output_pdf_path: str) -> bool:
    """
    Renders an HTML string or file to PDF using headless Chrome/Edge.
    Configured for exact A4 portrait printing without default browser headers/footers.
    """
    abs_pdf_path = os.path.abspath(output_pdf_path)
    os.makedirs(os.path.dirname(abs_pdf_path), exist_ok=True)
    
    if os.path.exists(html_content_or_path) and os.path.isfile(html_content_or_path):
        abs_html_path = os.path.abspath(html_content_or_path)
    else:
        abs_html_path = abs_pdf_path.replace(".pdf", ".html")
        with open(abs_html_path, "w", encoding="utf-8") as f:
            f.write(html_content_or_path)

    browser_bin = get_browser_binary()
    if not browser_bin or not os.path.exists(browser_bin):
        browser_bin = shutil.which("chromium") or shutil.which("google-chrome") or shutil.which("msedge")
        if not browser_bin:
            raise RuntimeError("No headless browser binary found for PDF rendering.")

    cmd = [
        browser_bin,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf_path}",
        abs_html_path
    ]

    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
        return os.path.exists(abs_pdf_path) and os.path.getsize(abs_pdf_path) > 1000
    except Exception as e:
        print(f"PDF Rendering Error: {e}")
        return False
