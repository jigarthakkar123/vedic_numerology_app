# -*- coding: utf-8 -*-
"""
Vedic Numerology PDF Report Generator - Editorial Professional Edition
Authored & Certified by: Jigar Thakkar, Certified Numerologist & Vastu Consultant
Generates clean, white, editorial-grade multi-page PDF reports in English, Hindi, and Gujarati.
Cross-platform: Supports Microsoft Edge on Windows and Chromium/Chrome on Linux cloud deployments.
"""

import os
import subprocess
import shutil
from typing import Dict, Any, List


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


# Planet color palette for badges & timeline bars (numbers 1-9)
NUM_COLORS = {
    1: "#f59e0b",  # Sun - Amber
    2: "#06b6d4",  # Moon - Cyan
    3: "#ca8a04",  # Jupiter - Gold
    4: "#15803d",  # Rahu - Forest
    5: "#10b981",  # Mercury - Emerald
    6: "#ec4899",  # Venus - Pink
    7: "#8b5cf6",  # Ketu - Violet
    8: "#312e81",  # Saturn - Indigo
    9: "#dc2626",  # Mars - Crimson
}

# Localized labels for the editorial report layout
REPORT_LABELS = {
    "en": {
        "report_kicker": "Vedic Numerology ·",
        "report_title": "Personal Analysis Report",
        "caution_banner": "This report should be read in consultation with an experienced numerologist.",
        "prepared_for": "Prepared for",
        "born": "Born",
        "as_on": "As on",
        "basic_number": "Basic Number",
        "destiny_number": "Destiny Number",
        "mahadasha": "Mahadasha",
        "antardasha": "Antardasha",
        "pratyantar": "Pratyantar",
        "pratyantar_dasha": "Pratyantar Dasha",
        "birth_grid": "Birth grid",
        "nums_in_grid": "Numbers in the grid:",
        "missing_nums": "Missing numbers:",
        "pos_and_neg": "Positive and negative:",
        "personality": "Personality",
        "year_grids": "Year grids",
        "year_grids_sub": "Birth grid with each year's Mahadasha and Antardasha. The running year is in the centre.",
        "running": "Running",
        "birth": "Birth",
        "age": "Age",
        "age_lower": "age",
        "cycle": "Cycle",
        "md": "MD",
        "ad": "AD",
        "pd": "PD",
        "start": "Start",
        "end": "End",
        "from": "From",
        "to": "To",
        "planet": "Planet",
        "days": "Days",
        "now": "now",
        "adjustment": "adjustment",
        "ad_formula": "From each birthday: day + month + last two digits of the year + the day's planet number.",
        "pd_formula": "Within Antardasha {ad}, {start} to {end}. Each period lasts its number × 8 days.",
        "pd_adj_note": "The last period is shorter: it adjusts to the end of the Antardasha year.",
        "prof_report": "Professional report",
        "life_path": "Life Path",
        "basic_pct": "Basic 30%",
        "destiny_pct": "Destiny 40%",
        "other_pct": "Other numbers 30%",
        "life_path_dn": "Life Path · Destiny Number · Bhagyank",
        "personality_bn": "Personality · Basic Number · Moolank",
        "friendly": "Friendly",
        "neutral": "Neutral",
        "enemy": "Enemy",
        "compat_friendly": "Personality and life path reinforce each other naturally, creating smooth momentum and confidence.",
        "compat_neutral": "Personality and life path neither help nor hinder each other. Progress follows effort and awareness.",
        "compat_enemy": "Personality and life path pull in different directions, creating inner tension that rewards conscious balance.",
        "other_together": "Other numbers together (30%):",
        "lucky_dates": "Lucky dates",
        "fav_days": "Favourable days",
        "lucky_colors": "Lucky colours",
        "gemstone": "Gemstone",
        "professions_title": "Professions suited to Basic Number {bn}",
        "grid_analysis": "Grid analysis",
        "once": "once",
        "times": "times",
        "yogas_title": "Yogas in the birth grid",
        "predictions": "Predictions",
        "from_birth_grid": "From the birth grid",
        "this_year": "This year",
        "nine_year_outlook": "Nine-year outlook",
        "year": "Year",
        "money": "Money",
        "assets": "Assets",
        "travel": "Travel",
        "disputes": "Disputes",
        "health": "Health",
        "remedies": "Remedies",
        "remedies_intro": "A number that appears two or more times is in affliction — its energy is too strong. Remedies balance it, reduce its negative expression and strengthen its positive side.",
        "appears_grid": "appears {n} times in the birth grid",
        "active_period_neg": "active in affliction during current period",
        "mantras_practices": "Mantras and practices",
        "service_seva": "Service (seva)",
        "donations": "Donations",
        "colours": "Colours",
        "fasting": "Fasting",
        "supporting_crystals": "Supporting crystals",
        "prepared_by": "Prepared by",
        "disclaimer": "Numerology offers guidance and reflection, not certainty. It is not medical, legal or financial advice.",
    },
    "hi": {
        "report_kicker": "वैदिक अंकशास्त्र ·",
        "report_title": "व्यक्तिगत विश्लेषण रिपोर्ट",
        "caution_banner": "यह रिपोर्ट किसी अनुभवी अंकशास्त्री के परामर्श के साथ पढ़ी जानी चाहिए।",
        "prepared_for": "के लिए तैयार",
        "born": "जन्म",
        "as_on": "दिनांक",
        "basic_number": "मूलांक (Basic Number)",
        "destiny_number": "भाग्यांक (Destiny Number)",
        "mahadasha": "महादशा",
        "antardasha": "अंतर्दशा",
        "pratyantar": "प्रत्यंतर दशा",
        "pratyantar_dasha": "प्रत्यंतर दशा",
        "birth_grid": "जन्म कुंडली (Birth Grid)",
        "nums_in_grid": "ग्रिड में अंक:",
        "missing_nums": "अनुपस्थित अंक:",
        "pos_and_neg": "सकारात्मक और नकारात्मक:",
        "personality": "व्यक्तित्व",
        "year_grids": "वार्षिक ग्रिड (Year Grids)",
        "year_grids_sub": "प्रत्येक वर्ष की महादशा और अंतर्दशा के साथ जन्म ग्रिड। वर्तमान वर्ष केंद्र में है।",
        "running": "वर्तमान",
        "birth": "जन्म",
        "age": "आयु",
        "age_lower": "आयु",
        "cycle": "चक्र",
        "md": "महादशा",
        "ad": "अंतर्दशा",
        "pd": "प्रत्यंतर",
        "start": "प्रारंभ",
        "end": "समाप्त",
        "from": "से",
        "to": "तक",
        "planet": "ग्रह",
        "days": "दिन",
        "now": "वर्तमान",
        "adjustment": "समायोजन",
        "ad_formula": "प्रत्येक जन्मदिन से: दिन + माह + वर्ष के अंतिम दो अंक + उस दिन का ग्रह अंक।",
        "pd_formula": "अंतर्दशा {ad} के अंतर्गत, {start} से {end}। प्रत्येक अवधि अपने अंक × 8 दिन की होती है।",
        "pd_adj_note": "अंतिम अवधि छोटी होती है: यह अंतर्दशा वर्ष के अंत तक समायोजित होती है।",
        "prof_report": "व्यावसायिक रिपोर्ट",
        "life_path": "जीवन पथ (Life Path)",
        "basic_pct": "मूलांक 30%",
        "destiny_pct": "भाग्यांक 40%",
        "other_pct": "अन्य अंक 30%",
        "life_path_dn": "जीवन पथ · भाग्यांक (Destiny Number)",
        "personality_bn": "व्यक्तित्व · मूलांक (Basic Number)",
        "friendly": "मित्रवत",
        "neutral": "तटस्थ",
        "enemy": "शत्रुवत",
        "compat_friendly": "व्यक्तित्व और जीवन पथ स्वाभाविक रूप से एक-दूसरे का समर्थन करते हैं, जिससे सहज गति और आत्मविश्वास मिलता है।",
        "compat_neutral": "व्यक्तित्व और जीवन पथ न तो सहायता करते हैं और न ही बाधा डालते हैं। प्रगति प्रयास और जागरूकता से होती है।",
        "compat_enemy": "व्यक्तित्व और जीवन पथ अलग दिशाओं में खींचते हैं, जिसे सचेत संतुलन द्वारा साधा जा सकता है।",
        "other_together": "अन्य अंक एक साथ (30%):",
        "lucky_dates": "शुभ तिथियाँ",
        "fav_days": "अनुकूल दिन",
        "lucky_colors": "शुभ रंग",
        "gemstone": "रत्न",
        "professions_title": "मूलांक {bn} के लिए उपयुक्त व्यवसाय",
        "grid_analysis": "ग्रिड विश्लेषण",
        "once": "एक बार",
        "times": "बार",
        "yogas_title": "जन्म ग्रिड में योग",
        "predictions": "भविष्यफल",
        "from_birth_grid": "जन्म ग्रिड से",
        "this_year": "इस वर्ष",
        "nine_year_outlook": "नौ वर्षीय दृष्टिकोण",
        "year": "वर्ष",
        "money": "धन",
        "assets": "संपत्ति",
        "travel": "यात्रा",
        "disputes": "विवाद",
        "health": "स्वास्थ्य",
        "remedies": "उपाय",
        "remedies_intro": "जो अंक दो या अधिक बार आता है वह पीड़ा में होता है — उसकी ऊर्जा बहुत प्रबल होती है। उपाय उसे संतुलित करते हैं और सकारात्मक पक्ष को बढ़ाते हैं।",
        "appears_grid": "जन्म ग्रिड में {n} बार आया है",
        "active_period_neg": "वर्तमान अवधि में नकारात्मक प्रभाव में सक्रिय",
        "mantras_practices": "मंत्र और साधना",
        "service_seva": "सेवा",
        "donations": "दान",
        "colours": "रंग",
        "fasting": "व्रत",
        "supporting_crystals": "सहायक क्रिस्टल",
        "prepared_by": "द्वारा तैयार",
        "disclaimer": "अंकशास्त्र मार्गदर्शन और चिंतन प्रदान करता है, निश्चितता नहीं। यह चिकित्सा, कानूनी या वित्तीय सलाह नहीं है।",
    },
    "gu": {
        "report_kicker": "વૈદિક અંકશાસ્ત્ર ·",
        "report_title": "વ્યક્તિગત વિશ્લેષણ રિપોર્ટ",
        "caution_banner": "આ રિપોર્ટ અનુભવી અંકશાસ્ત્રીના માર્ગદર્શન સાથે વાંચવો જોઈએ.",
        "prepared_for": "માટે તૈયાર",
        "born": "જન્મ",
        "as_on": "તારીખ",
        "basic_number": "મૂળાંક (Basic Number)",
        "destiny_number": "ભાગ્યાંક (Destiny Number)",
        "mahadasha": "મહાદશા",
        "antardasha": "અંતર્દશા",
        "pratyantar": "પ્રત્યંતર દશા",
        "pratyantar_dasha": "પ્રત્યંતર દશા",
        "birth_grid": "જન્મ કુંડળી (Birth Grid)",
        "nums_in_grid": "ગ્રીડમાં અંકો:",
        "missing_nums": "ખૂટતા અંકો:",
        "pos_and_neg": "સકારાત્મક અને નકારાત્મક:",
        "personality": "વ્યક્તિત્વ",
        "year_grids": "વાર્ષિક ગ્રીડ (Year Grids)",
        "year_grids_sub": "દરેક વર્ષની મહાદશા અને અંતર્દશા સાથે જન્મ ગ્રીડ. ચાલુ વર્ષ કેન્દ્રમાં છે.",
        "running": "ચાલુ",
        "birth": "જન્મ",
        "age": "ઉંમર",
        "age_lower": "ઉંમર",
        "cycle": "ચક્ર",
        "md": "મહાદશા",
        "ad": "અંતર્દશા",
        "pd": "પ્રત્યંતર",
        "start": "શરૂઆત",
        "end": "અંત",
        "from": "થી",
        "to": "સુધી",
        "planet": "ગ્રહ",
        "days": "દિવસ",
        "now": "હાલ",
        "adjustment": "સમાયોજન",
        "ad_formula": "દરેક જન્મદિવસથી: દિવસ + મહિનો + વર્ષના છેલ્લા બે અંક + તે દિવસનો ગ્રહ અંક.",
        "pd_formula": "અંતર્દશા {ad} હેઠળ, {start} થી {end}. દરેક સમયગાળો તેના અંક × 8 દિવસનો હોય છે.",
        "pd_adj_note": "છેલ્લો સમયગાળો ટૂંકો હોય છે: તે અંતર્દશા વર્ષના અંત સુધી સમાયોજિત થાય છે.",
        "prof_report": "વ્યાવસાયિક રિપોર્ટ",
        "life_path": "જીવન પથ (Life Path)",
        "basic_pct": "મૂળાંક 30%",
        "destiny_pct": "ભાગ્યાંક 40%",
        "other_pct": "અન્ય અંકો 30%",
        "life_path_dn": "જીવન પથ · ભાગ્યાંક (Destiny Number)",
        "personality_bn": "વ્યક્તિત્વ · મૂળાંક (Basic Number)",
        "friendly": "મિત્ર",
        "neutral": "તટસ્થ",
        "enemy": "શત્રુ",
        "compat_friendly": "વ્યક્તિત્વ અને જીવન પથ કુદરતી રીતે એકબીજાને ટેકો આપે છે, જેનાથી સરળ પ્રગતિ અને આત્મવિશ્વાસ મળે છે.",
        "compat_neutral": "વ્યક્તિત્વ અને જીવન પથ ન તો મદદ કરે છે કે ન તો અવરોધે છે. પ્રગતિ પ્રયત્ન અને જાગૃતિથી થાય છે.",
        "compat_enemy": "વ્યક્તિત્વ અને જીવન પથ અલગ દિશામાં ખેંચે છે, જેને સભાન સંતુલનથી સાધી શકાય છે.",
        "other_together": "અન્ય અંકો સાથે (30%):",
        "lucky_dates": "શુભ તારીખો",
        "fav_days": "અનુકૂળ દિવસો",
        "lucky_colors": "શુભ રંગો",
        "gemstone": "રત્ન",
        "professions_title": "મૂળાંક {bn} માટે યોગ્ય વ્યવસાયો",
        "grid_analysis": "ગ્રીડ વિશ્લેષણ",
        "once": "એક વાર",
        "times": "વાર",
        "yogas_title": "જન્મ ગ્રીડમાં યોગ",
        "predictions": "ભવિષ્યફળ",
        "from_birth_grid": "જન્મ ગ્રીડ પરથી",
        "this_year": "આ વર્ષ",
        "nine_year_outlook": "નવ વર્ષીય દૃષ્ટિકોણ",
        "year": "વર્ષ",
        "money": "ધન",
        "assets": "સંપત્તિ",
        "travel": "પ્રવાસ",
        "disputes": "વિવાદ",
        "health": "સ્વાસ્થ્ય",
        "remedies": "ઉપાયો",
        "remedies_intro": "જે અંક બે કે તેથી વધુ વખત આવે છે તે પીડામાં હોય છે — તેની ઊર્જા ખૂબ પ્રબળ હોય છે. ઉપાયો તેને સંતુલિત કરે છે અને સકારાત્મક પાસાંને મજબૂત બનાવે છે.",
        "appears_grid": "જન્મ ગ્રીડમાં {n} વખત આવે છે",
        "active_period_neg": "ચાલુ સમયગાળામાં નકારાત્મક અસરમાં સક્રિય",
        "mantras_practices": "મંત્ર અને સાધના",
        "service_seva": "સેવા",
        "donations": "દાન",
        "colours": "રંગો",
        "fasting": "ઉપવાસ",
        "supporting_crystals": "સહાયક ક્રિસ્ટલ્સ",
        "prepared_by": "દ્વારા તૈયાર",
        "disclaimer": "અંકશાસ્ત્ર માર્ગદર્શન અને ચિંતન આપે છે, નિશ્ચિતતા નહીં. તે તબીબી, કાનૂની કે નાણાકીય સલાહ નથી.",
    }
}

ARCHETYPES_EN = {
    1: ("The Radiant Leader", ["Leadership", "Drive", "Clarity"], "Number 1 is the energy of self. It carries leadership, confidence and a clear sense of identity. These are the people who take initiative, step forward when everyone else hesitates, and pull others along through sheer drive and clarity."),
    2: ("The Intuitive Harmoniser", ["Intuition", "Empathy", "Diplomacy"], "Number 2 is the energy of sensitivity and partnership. Ruled by the Moon, it brings emotional depth, imagination, diplomacy and a natural gift for reading people and building harmony."),
    3: ("The Wise Communicator", ["Wisdom", "Creativity", "Expression"], "Number 3 is the energy of expansion and expression. Ruled by Jupiter, it carries optimism, teaching ability, creative intelligence and a natural flair for inspiring others."),
    4: ("The Grounded Architect", ["Discipline", "Structure", "Innovation"], "Number 4 is the energy of practical execution. Ruled by Rahu, it brings unconventional thinking, relentless work ethic, system-building and resilience under pressure."),
    5: ("The Dynamic Strategist", ["Adaptability", "Wit", "Commerce"], "Number 5 is the energy of movement and intellect. Ruled by Mercury, it confers sharp communication, commercial instinct, versatility and magnetic social energy."),
    6: ("The Nurturing Art Lover", ["Love", "Beauty", "Harmony"], "Number 6 is the energy of beauty. Ruled by Venus, it carries care, creativity, harmony and responsibility. These people are magnetic without effort — they draw others in and elevate every space they occupy."),
    7: ("The Mystic Seeker", ["Insight", "Research", "Spirituality"], "Number 7 is the energy of depth and introspection. Ruled by Ketu, it brings analytical brilliance, spiritual curiosity, keen observation and a search for deeper truth."),
    8: ("The Karma Builder", ["Ambition", "Endurance", "Justice"], "Number 8 is the energy of material mastery and justice. Ruled by Saturn, it brings patience, organizational power, resilience through tests and enduring long-term success."),
    9: ("The Courageous Humanitarian", ["Courage", "Passion", "Service"], "Number 9 is the energy of completion and valor. Ruled by Mars, it carries fierce determination, protective strength, idealism and a desire to champion meaningful causes."),
}

PROFESSIONS_BY_BN = {
    1: [("Leadership", "Founder, CEO, Startup Leader, Project Lead, Creative Director, Command-level Officer"),
        ("Power", "IAS / IPS, Senior Corporate Executive, Real Estate Developer, Hospital Administrator, Media Head"),
        ("Individuality", "Solopreneur, Independent Consultant, Signature-Style Artist, Author, Innovator"),
        ("Authority", "Judge, Senior Lawyer, Police / Defence Officer, Aviation or Ship Captain, Sports Coach"),
        ("Ambition", "Investment Banker, Private Equity, High-Growth Tech, Sales Leadership, Politics")],
    2: [("Counsel", "Psychologist, Life Coach, HR Director, Mediator, Relationship Counsellor"),
        ("Creative", "Writer, Poet, Musician, Interior Designer, Film & Storytelling"),
        ("Care", "Healthcare, Nursing, Hospitality, Wellness Retreat Founder, Nutrition"),
        ("Diplomacy", "Public Relations, Client Success, International Relations, Brand Communications")],
    3: [("Knowledge", "Professor, Educator, Mentor, Corporate Trainer, Educational Entrepreneur"),
        ("Advisory", "Management Consultant, Legal Advisor, Financial Planner, Astrologer / Numerologist"),
        ("Media", "Public Speaker, Journalist, Podcaster, Publishing, Content Strategist"),
        ("Leadership", "Institution Builder, Non-Profit Director, Cultural & Event Producer")],
    4: [("Engineering", "Software Architect, Systems Engineer, Civil / Structural Engineer, Data Scientist"),
        ("Operations", "Supply Chain Head, Manufacturing Director, Quality & Compliance Lead, Project Manager"),
        ("Research", "Forensic Analyst, Cybersecurity, Investigative Journalism, Technical Auditor"),
        ("Enterprise", "Logistics, Infrastructure, Precision Trades, Contrarian Investing")],
    5: [("Commerce", "Entrepreneur, Trader, E-Commerce Founder, Business Development, Venture Partner"),
        ("Communication", "Marketing Director, Sales Strategist, Copywriter, PR & Media Anchor"),
        ("Travel & Tech", "Aviation, Tourism, SaaS Product Manager, Digital Growth Lead"),
        ("Finance", "Stock Market Analyst, Wealth Advisor, FinTech, Brokerage")],
    6: [("Design", "Fashion Designer, Luxury Brand Founder, Interior Architect, UI/UX Director"),
        ("Hospitality", "Fine Dining, Boutique Hotelier, Event Curation, Lifestyle Concierge"),
        ("Arts & Media", "Actor, Film Producer, Musician, Beauty & Cosmetics, Art Curator"),
        ("Harmony", "Family Business Leadership, Real Estate Staging, Wellness & Aesthetics")],
    7: [("Research", "Scientist, AI / ML Researcher, Philosopher, Think-Tank Analyst, Historian"),
        ("Healing", "Spiritual Guide, Holistic Healer, Psychotherapist, Yoga & Meditation Teacher"),
        ("Strategy", "Intelligence Analyst, Risk Strategist, Patent Specialist, Niche Consultant"),
        ("Writing", "Investigative Author, Scriptwriter, Technical Writer, Documentary Maker")],
    8: [("Industry", "Industrialist, Real Estate Baron, Infrastructure, Mining & Energy, Manufacturing"),
        ("Finance", "CFO, Banking Executive, Private Equity, Chartered Accountant, Tax Strategist"),
        ("Law & Governance", "Judiciary, Corporate Law, Regulatory Affairs, Public Administration"),
        ("Scale", "Operations Executive, Turnaround Specialist, Institutional Asset Management")],
    9: [("Action", "Defence Services, Fire & Rescue, Athletics, Martial Arts, Adventure Leadership"),
        ("Impact", "Social Entrepreneur, NGO Founder, Humanitarian Aid, Public Policy"),
        ("Medicine", "Surgeon, Emergency Medicine, Sports Physiotherapy, Trauma Care"),
        ("Command", "Operations Commander, Security Director, Crisis Management, Politics")],
}

SUPPORTING_CRYSTALS = [
    ("Clear Quartz", "Stone of Power — amplifies energy and intention; cleanses and aligns all chakras"),
    ("Citrine", "Attracts wealth, status and knowledge; motivation and confidence"),
    ("Pyrite", "Protection; attracts wealth and financial stability; strengthens willpower"),
    ("Amethyst", "Calm and intuition — relieves stress, irritability, anger, fear and anxiety"),
    ("Aventurine", "Balances the nervous system; reduces stress and irritation"),
    ("Tiger's Eye", "Courage and action — releases fear, strengthens willpower and decision-making"),
]

ARCHETYPES_HI = {
    1: ("तेजस्वी नेतृत्वकर्ता", ["नेतृत्व", "ऊर्जा", "स्पष्टता"], "अंक 1 आत्मबल और सूर्य की ऊर्जा का प्रतीक है। यह नेतृत्व, आत्मविश्वास और स्पष्ट पहचान प्रदान करता है। ऐसे व्यक्ति पहल करने वाले, निडर और अपने संकल्प से दूसरों का मार्गदर्शन करने वाले होते हैं।"),
    2: ("संवेदनशील समन्वयक", ["अंतर्ज्ञान", "सहानुभूति", "कूटनीति"], "अंक 2 संवेदनशीलता और साझेदारी की ऊर्जा है। चंद्रमा के प्रभाव से यह भावनात्मक गहराई, कल्पनाशक्ति, मधुर व्यवहार और लोगों के बीच सामंजस्य स्थापित करने की स्वाभाविक क्षमता देता है।"),
    3: ("ज्ञानी संवादक", ["ज्ञान", "रचनात्मकता", "अभिव्यक्ति"], "अंक 3 विस्तार और अभिव्यक्ति की ऊर्जा है। गुरु (बृहस्पति) के प्रभाव से यह आशावाद, शिक्षण क्षमता, रचनात्मक बुद्धिमत्ता और दूसरों को प्रेरित करने का गुण प्रदान करता है।"),
    4: ("व्यवस्थित निर्माता", ["अनुशासन", "संरचना", "नवाचार"], "अंक 4 व्यावहारिक निष्पादन की ऊर्जा है। राहु के प्रभाव से यह अनूठी सोच, अथक परिश्रम, सुव्यवस्थित प्रणाली निर्माण और दबाव में भी अडिग रहने की क्षमता देता है।"),
    5: ("गतिशील रणनीतिकार", ["अनुकूलनशीलता", "चातुर्य", "व्यापार"], "अंक 5 गति और बुद्धि की ऊर्जा है। बुध के प्रभाव से यह तीव्र संवाद कला, व्यावसायिक सूझबूझ, बहुमुखी प्रतिभा और आकर्षक व्यक्तित्व प्रदान करता है।"),
    6: ("सौंदर्य एवं स्नेह के पोषक", ["प्रेम", "सौंदर्य", "सामंजस्य"], "अंक 6 सौंदर्य और सद्भाव की ऊर्जा है। शुक्र के प्रभाव से यह देखभाल, कलात्मकता, पारिवारिक जिम्मेदारी और सहज आकर्षण प्रदान करता है।"),
    7: ("आध्यात्मिक अन्वेषक", ["अंतर्दृष्टि", "शोध", "आध्यात्मिकता"], "अंक 7 गहराई और आत्मचिंतन की ऊर्जा है। केतु के प्रभाव से यह विश्लेषणात्मक प्रतिभा, आध्यात्मिक जिज्ञासा, सूक्ष्म अवलोकन और सत्य की खोज की प्रवृत्ति देता है।"),
    8: ("कर्मयोगी निर्माता", ["महत्वाकांक्षा", "धैर्य", "न्याय"], "अंक 8 कर्म, व्यवस्था और न्याय की ऊर्जा है। शनि के प्रभाव से यह धैर्य, संगठनात्मक शक्ति, परीक्षाओं में स्थिरता और दीर्घकालिक स्थायी सफलता प्रदान करता है।"),
    9: ("साहसी लोकसेवक", ["साहस", "उत्साह", "सेवा"], "अंक 9 पूर्णता और पराक्रम की ऊर्जा है। मंगल के प्रभाव से यह दृढ़ संकल्प, रक्षक स्वभाव, उच्च आदर्श और सार्थक कार्यों के लिए समर्पण देता है।"),
}

ARCHETYPES_GU = {
    1: ("તેજસ્વી નેતૃત્વકર્તા", ["નેતૃત્વ", "ઉત્સાહ", "સ્પષ્ટતા"], "અંક 1 આત્મબળ અને સૂર્યની ઊર્જાનું પ્રતીક છે. તે નેતૃત્વ, આત્મવિશ્વાસ અને સ્પષ્ટ ઓળખ આપે છે. આવા વ્યક્તિઓ પહેલ કરનાર, નિર્ભય અને પોતાના સંકલ્પથી અન્યોને માર્ગદર્શન આપનાર હોય છે."),
    2: ("સંવેદનશીલ સમન્વયક", ["અંતઃસ્ફુરણા", "સહાનુભૂતિ", "કૂટનીતિ"], "અંક 2 સંવેદનશીલતા અને ભાગીદારીની ઊર્જા છે. ચંદ્રના પ્રભાવથી તે ભાવનાત્મક ઊંડાણ, કલ્પનાશક્તિ, મધુર વ્યવહાર અને લોકો વચ્ચે સુમેળ સાધવાની કુદરતી ક્ષમતા આપે છે."),
    3: ("જ્ઞાની સંવાદક", ["જ્ઞાન", "સર્જનાત્મકતા", "અભિવ્યક્તિ"], "અંક 3 વિસ્તાર અને અભિવ્યક્તિની ઊર્જા છે. ગુરુના પ્રભાવથી તે આશાવાદ, શિક્ષણ ક્ષમતા, સર્જનાત્મક બુદ્ધિ અને અન્યોને પ્રેરણા આપવાનો ગુણ આપે છે."),
    4: ("વ્યવસ્થિત નિર્માતા", ["શિસ્ત", "વ્યવસ્થા", "નવીનતા"], "અંક 4 વ્યવહારિક કાર્યદક્ષતાની ઊર્જા છે. રાહુના પ્રભાવથી તે અનોખી વિચારસરણી, અથાગ પરિશ્રમ, સુવ્યવસ્થિત કાર્યપદ્ધતિ અને મુશ્કેલ પરિસ્થિતિમાં સ્થિરતા આપે છે."),
    5: ("ગતિશીલ વ્યૂહરચનાકાર", ["અનુકૂલનશીલતા", "ચાતુર્ય", "વ્યાપાર"], "અંક 5 ગતિ અને બુદ્ધિની ઊર્જા છે. બુધના પ્રભાવથી તે તીવ્ર સંવાદ કલા, વ્યાપારિક સૂઝબૂઝ, બહુમુખી પ્રતિભા અને આકર્ષક વ્યક્તિત્વ આપે છે."),
    6: ("સૌંદર્ય અને સ્નેહના પોષક", ["પ્રેમ", "સૌંદર્ય", "સુમેળ"], "અંક 6 સૌંદર્ય અને સદભાવની ઊર્જા છે. શુક્રના પ્રભાવથી તે સંભાળ, કલાત્મકતા, પારિવારિક જવાબદારી અને સહજ આકર્ષણ આપે છે."),
    7: ("આધ્યાત્મિક અન્વેષક", ["અંતર્દૃષ્ટિ", "સંશોધન", "આધ્યાત્મિકતા"], "અંક 7 ઊંડાણ અને આત્મચિંતનની ઊર્જા છે. કેતુના પ્રભાવથી તે વિશ્લેષણાત્મક પ્રતિભા, આધ્યાત્મિક જિજ્ઞાસા, સૂક્ષ્મ અવલોકન અને સત્યની શોધની વૃત્તિ આપે છે."),
    8: ("કર્મયોગી નિર્માતા", ["મહત્વાકાંક્ષા", "ધૈર્ય", "ન્યાય"], "અંક 8 કર્મ, વ્યવસ્થા અને ન્યાયની ઊર્જા છે. શનિના પ્રભાવથી તે ધીરજ, સંગઠનાત્મક શક્તિ, કસોટીમાં સ્થિરતા અને લાંબા ગાળાની સ્થાયી સફળતા આપે છે."),
    9: ("સાહસી લોકસેવક", ["સાહસ", "જુસ્સો", "સેવા"], "અંક 9 પૂર્ણતા અને પરાક્રમની ઊર્જા છે. મંગળના પ્રભાવથી તે દૃઢ સંકલ્પ, રક્ષક સ્વભાવ, ઉચ્ચ આદર્શો અને સાર્થક કાર્યો માટે સમર્પણ આપે છે."),
}

ARCHETYPES_BY_LANG = {"en": ARCHETYPES_EN, "hi": ARCHETYPES_HI, "gu": ARCHETYPES_GU}

PROFESSIONS_BY_BN_HI = {
    1: [("नेतृत्व", "संस्थापक, सीईओ, स्टार्टअप लीडर, प्रोजेक्ट लीड, क्रिएटिव डायरेक्टर"),
        ("प्रशासन एवं अधिकार", "आईएएस / आईपीएस, वरिष्ठ कॉर्पोरेट अधिकारी, रियल एस्टेट डेवलपर, मीडिया प्रमुख"),
        ("स्वतंत्र पहचान", "स्वतंत्र सलाहकार, सोलोप्रेन्योर, लेखक, नवप्रवर्तक"),
        ("न्याय एवं सुरक्षा", "न्यायाधीश, वरिष्ठ अधिवक्ता, पुलिस / रक्षा अधिकारी, खेल प्रशिक्षक")],
    2: [("परामर्श", "मनोवैज्ञानिक, लाइफ कोच, एचआर डायरेक्टर, मध्यस्थ, रिलेशनशिप काउंसलर"),
        ("सृजन एवं कला", "लेखक, कवि, संगीतकार, इंटीरियर डिजाइनर, फिल्म एवं स्टोरीटेलिंग"),
        ("सेवा एवं स्वास्थ्य", "स्वास्थ्य सेवा, नर्सिंग, हॉस्पिटैलिटी, वेलनेस रिट्रीट, पोषण विशेषज्ञ"),
        ("कूटनीति एवं जनसंपर्क", "जनसंपर्क (PR), क्लाइंट सक्सेस, अंतरराष्ट्रीय संबंध, ब्रांड संचार")],
    3: [("ज्ञान एवं शिक्षा", "प्रोफेसर, शिक्षक, मेंटर, कॉर्पोरेट ट्रेनर, शैक्षणिक उद्यमी"),
        ("सलाहकार क्षेत्र", "मैनेजमेंट कंसल्टेंट, कानूनी सलाहकार, वित्तीय योजनाकार, ज्योतिषी / अंकशास्त्री"),
        ("मीडिया एवं प्रकाशन", "वक्ता, पत्रकार, पॉडकास्टर, प्रकाशन, कंटेंट रणनीतिकार"),
        ("संस्था निर्माण", "संस्था प्रमुख, एनजीओ निदेशक, सांस्कृतिक एवं इवेंट निर्माता")],
    4: [("इंजीनियरिंग एवं तकनीक", "सॉफ्टवेयर आर्किटेक्ट, सिस्टम इंजीनियर, सिविल इंजीनियर, डेटा साइंटिस्ट"),
        ("संचालन एवं गुणवत्ता", "सप्लाई चेन प्रमुख, मैन्युफैक्चरिंग डायरेक्टर, प्रोजेक्ट मैनेजर"),
        ("शोध एवं विश्लेषण", "फॉरेंसिक विश्लेषक, साइबर सुरक्षा, खोजी पत्रकारिता, तकनीकी ऑडिटर"),
        ("उद्योग एवं निर्माण", "लॉजिस्टिक्स, इन्फ्रास्ट्रक्चर, सटीक तकनीकी कार्य")],
    5: [("व्यापार एवं वाणिज्य", "उद्यमी, ट्रेडर, ई-कॉमर्स संस्थापक, बिजनेस डेवलपमेंट"),
        ("संचार एवं विपणन", "मार्केटिंग डायरेक्टर, सेल्स रणनीतिकार, कॉपीराइटर, मीडिया एंकर"),
        ("यात्रा एवं तकनीक", "एविएशन, पर्यटन, SaaS प्रोडक्ट मैनेजर, डिजिटल ग्रोथ लीड"),
        ("वित्त एवं बाजार", "शेयर बाजार विश्लेषक, वेल्थ एडवाइजर, फिनटेक")],
    6: [("डिजाइन एवं विलासिता", "फैशन डिजाइनर, लग्जरी ब्रांड संस्थापक, इंटीरियर आर्किटेक्ट, UI/UX डायरेक्टर"),
        ("आतिथ्य सत्कार", "फाइन डाइनिंग, बुटीक होटल, इवेंट क्यूरेशन, लाइफस्टाइल सेवाएं"),
        ("कला एवं मीडिया", "अभिनय, फिल्म निर्माण, संगीत, सौंदर्य एवं कॉस्मेटिक्स, कला संग्रह"),
        ("संतुलन एवं कल्याण", "पारिवारिक व्यवसाय नेतृत्व, रियल एस्टेट, वेलनेस एवं सौंदर्यशास्त्र")],
    7: [("शोध एवं विज्ञान", "वैज्ञानिक, AI / ML शोधकर्ता, दार्शनिक, थिंक-टैंक विश्लेषक, इतिहासकार"),
        ("आध्यात्मिक एवं चिकित्सा", "आध्यात्मिक मार्गदर्शक, होलिस्टिक हीलर, मनोचिकित्सक, योग एवं ध्यान शिक्षक"),
        ("रणनीति एवं विश्लेषण", "इंटेलिजेंस विश्लेषक, रिस्क रणनीतिकार, पेटेंट विशेषज्ञ, विशिष्ट सलाहकार"),
        ("लेखन एवं दस्तावेजीकरण", "खोजी लेखक, स्क्रिप्टराइटर, तकनीकी लेखक, डॉक्यूमेंट्री निर्माता")],
    8: [("उद्योग एवं निर्माण", "उद्योगपति, रियल एस्टेट, इन्फ्रास्ट्रक्चर, ऊर्जा एवं विनिर्माण"),
        ("वित्त एवं लेखा", "सीएफओ, बैंकिंग अधिकारी, चार्टर्ड अकाउंटेंट, कर रणनीतिकार"),
        ("कानून एवं प्रशासन", "न्यायपालिका, कॉर्पोरेट लॉ, नियामक मामले, लोक प्रशासन"),
        ("प्रबंधन एवं विस्तार", "ऑपरेशंस एग्जीक्यूटिव, टर्नअराउंड विशेषज्ञ, संपत्ति प्रबंधन")],
    9: [("रक्षा एवं साहस", "रक्षा सेवाएं, अग्निशमन एवं बचाव, खेलकूद, मार्शल आर्ट, साहसिक नेतृत्व"),
        ("सामाजिक प्रभाव", "सामाजिक उद्यमी, एनजीओ संस्थापक, मानवीय सहायता, लोक नीति"),
        ("चिकित्सा एवं उपचार", "सर्जन, आपातकालीन चिकित्सा, स्पोर्ट्स फिजियोथेरेपी, ट्रॉमा केयर"),
        ("कमान एवं संकट प्रबंधन", "ऑपरेशंस कमांडर, सुरक्षा निदेशक, संकट प्रबंधन, राजनीति")],
}

PROFESSIONS_BY_BN_GU = {
    1: [("નેતૃત્વ", "સ્થાપક, સીઈઓ, સ્ટાર્ટઅપ લીડર, પ્રોજેક્ટ લીડ, ક્રિએટિવ ડિરેક્ટર"),
        ("વહીવટ અને સત્તા", "આઈએએસ / આઈપીએસ, વરિષ્ઠ કોર્પોરેટ અધિકારી, રિયલ એસ્ટેટ ડેવલપર, મીડિયા વડા"),
        ("સ્વતંત્ર ઓળખ", "સ્વતંત્ર સલાહકાર, સોલોપ્રેન્યોર, લેખક, નવપ્રવર્તક"),
        ("ન્યાય અને સુરક્ષા", "ન્યાયાધીશ, વરિષ્ઠ વકીલ, પોલીસ / સંરક્ષણ અધિકારી, સ્પોર્ટ્સ કોચ")],
    2: [("પરામર્શ", "મનોવૈજ્ઞાનિક, લાઇફ કોચ, એચઆર ડિરેક્ટર, મધ્યસ્થ, રિલેશનશિપ કાઉન્સેલર"),
        ("સર્જન અને કલા", "લેખક, કવિ, સંગીતકાર, ઇન્ટિરિયર ડિઝાઇનર, ફિલ્મ અને સ્ટોરીટેલિંગ"),
        ("સેવા અને આરોગ્ય", "આરોગ્ય સેવા, નર્સિંગ, હોસ્પિટાલિટી, વેલનેસ રિટ્રીટ, ન્યુટ્રિશન"),
        ("કૂટનીતિ અને જનસંપર્ક", "જનસંપર્ક (PR), ક્લાયન્ટ સક્સેસ, આંતરરાષ્ટ્રીય સંબંધો, બ્રાન્ડ કોમ્યુનિકેશન")],
    3: [("જ્ઞાન અને શિક્ષણ", "પ્રોફેસર, શિક્ષક, મેન્ટર, કોર્પોરેટ ટ્રેનર, શૈક્ષણિક ઉદ્યોગસાહસિક"),
        ("સલાહકાર ક્ષેત્ર", "મેનેજમેન્ટ કન્સલ્ટન્ટ, કાનૂની સલાહકાર, નાણાકીય આયોજક, જ્યોતિષી / અંકશાસ્ત્રી"),
        ("મીડિયા અને પ્રકાશન", "વક્તા, પત્રકાર, પોડકાસ્ટર, પ્રકાશન, કન્ટેન્ટ સ્ટ્રેટેજિસ્ટ"),
        ("સંસ્થા નિર્માણ", "સંસ્થા વડા, એનજીઓ ડિરેક્ટર, સાંસ્કૃતિક અને ઇવેન્ટ નિર્માતા")],
    4: [("એન્જિનિયરિંગ અને ટેક", "સોફ્ટવેર આર્કિટેક્ટ, સિસ્ટમ એન્જિનિયર, સિવિલ એન્જિનિયર, ડેટા સાયન્ટિસ્ટ"),
        ("સંચાલન અને ગુણવત્તા", "સપ્લાય ચેઇન હેડ, મેન્યુફેક્ચરિંગ ડિરેક્ટર, પ્રોજેક્ટ મેનેજર"),
        ("સંશોધન અને વિશ્લેષણ", "ફોરેન્સિક એનાલિસ્ટ, સાયબર સુરક્ષા, ઇન્વેસ્ટિગેટિવ જર્નાલિઝમ, ટેકનિકલ ઓડિટર"),
        ("ઉદ્યોગ અને બાંધકામ", "લોજિસ્ટિક્સ, ઇન્ફ્રાસ્ટ્રક્ચર, ચોકસાઈપૂર્ણ તકનીકી કાર્યો")],
    5: [("વ્યાપાર અને વાણિજ્ય", "ઉદ્યોગસાહસિક, ટ્રેડર, ઈ-કોમર્સ સ્થાપક, બિઝનેસ ડેવલપમેન્ટ"),
        ("સંચાર અને માર્કેટિંગ", "માર્કેટિંગ ડિરેક્ટર, સેલ્સ સ્ટ્રેટેજિસ્ટ, કોપીરાઇટર, મીડિયા એન્કર"),
        ("પ્રવાસ અને ટેકનોલોજી", "એવિએશન, ટુરિઝમ, SaaS પ્રોડક્ટ મેનેજર, ડિજિટલ ગ્રોથ લીડ"),
        ("નાણાં અને બજાર", "શેરબજાર વિશ્લેષક, વેલ્થ એડવાઇઝર, ફિનટેક")],
    6: [("ડિઝાઇન અને વૈભવ", "ફેશન ડિઝાઇનર, લક્ઝરી બ્રાન્ડ સ્થાપક, ઇન્ટિરિયર આર્કિટેક્ટ, UI/UX ડિરેક્ટર"),
        ("આતિથ્ય સત્કાર", "ફાઇન ડાઇનિંગ, બુટિક હોટેલ, ઇવેન્ટ ક્યુરેશન, લાઇફસ્ટાઇલ સેવાઓ"),
        ("કલા અને મીડિયા", "અભિનય, ફિલ્મ નિર્માણ, સંગીત, સૌંદર્ય અને કોસ્મેટિક્સ, કલા સંગ્રહ"),
        ("સંતુલન અને કલ્યાણ", "પારિવારિક વ્યવસાય નેતૃત્વ, રિયલ એસ્ટેટ, વેલનેસ અને સૌંદર્યશાસ્ત્ર")],
    7: [("સંશોધન અને વિજ્ઞાન", "વૈજ્ઞાનિક, AI / ML સંશોધક, ફિલોસોફર, થિંક-ટેન્ક એનાલિસ્ટ, ઇતિહાસકાર"),
        ("આધ્યાત્મિક અને ઉપચાર", "આધ્યાત્મિક માર્ગદર્શક, હોલિસ્ટિક હીલર, સાયકોથેરાપિસ્ટ, યોગ અને ધ્યાન શિક્ષક"),
        ("વ્યૂહરચના અને વિશ્લેષણ", "ઇન્ટેલિજન્સ એનાલિસ્ટ, રિસ્ક સ્ટ્રેટેજિસ્ટ, પેટન્ટ નિષ્ણાત, વિશિષ્ટ સલાહકાર"),
        ("લેખન અને દસ્તાવેજીકરણ", "સંશોધનાત્મક લેખક, સ્ક્રિપ્ટરાઇટર, ટેકનિકલ લેખક, ડોક્યુમેન્ટરી નિર્માતા")],
    8: [("ઉદ્યોગ અને નિર્માણ", "ઉદ્યોગપતિ, રિયલ એસ્ટેટ, ઇન્ફ્રાસ્ટ્રક્ચર, ઊર્જા અને ઉત્પાદન"),
        ("નાણાં અને હિસાબ", "સીએફઓ, બેંકિંગ અધિકારી, ચાર્ટર્ડ એકાઉન્ટન્ટ, ટેક્સ સ્ટ્રેટેજિસ્ટ"),
        ("કાયદો અને વહીવટ", "ન્યાયતંત્ર, કોર્પોરેટ લો, નિયમનકારી બાબતો, જાહેર વહીવટ"),
        ("વ્યવસ્થાપન અને વિસ્તરણ", "ઓપરેશન્સ એક્ઝિક્યુટિવ, ટર્નઅરાઉન્ડ નિષ્ણાત, એસેટ મેનેજમેન્ટ")],
    9: [("સંરક્ષણ અને સાહસ", "સંરક્ષણ સેવાઓ, ફાયર અને રેસ્ક્યુ, રમતગમત, માર્શલ આર્ટ્સ, સાહસિક નેતૃત્વ"),
        ("સામાજિક પ્રભાવ", "સામાજિક ઉદ્યોગસાહસિક, એનજીઓ સ્થાપક, માનવતાવાદી સહાય, જાહેર નીતિ"),
        ("તબીબી અને સારવાર", "સર્જન, ઇમરજન્સી મેડિસિન, સ્પોર્ટ્સ ફિઝિયોથેરાપી, ટ્રોમા કેર"),
        ("કમાન્ડ અને કટોકટી વ્યવસ્થાપન", "ઓપરેશન્સ કમાન્ડર, સિક્યુરિટી ડિરેક્ટર, ક્રાઇસિસ મેનેજમેન્ટ, રાજકારણ")],
}

PROFESSIONS_BY_LANG = {"en": PROFESSIONS_BY_BN, "hi": PROFESSIONS_BY_BN_HI, "gu": PROFESSIONS_BY_BN_GU}

SUPPORTING_CRYSTALS_HI = [
    ("Clear Quartz (स्फटिक)", "शक्ति का रत्न — ऊर्जा और संकल्प को बढ़ाता है; सभी चक्रों को शुद्ध और संतुलित करता है"),
    ("Citrine (सुनैला)", "धन, सम्मान और ज्ञान को आकर्षित करता है; प्रेरणा और आत्मविश्वास बढ़ाता है"),
    ("Pyrite (पायराइट)", "सुरक्षा कवच; धन और आर्थिक स्थिरता को आकर्षित करता है; इच्छाशक्ति को मजबूत करता है"),
    ("Amethyst (जामुनिया)", "शांति और अंतर्ज्ञान — तनाव, चिड़चिड़ापन, क्रोध, भय और चिंता को दूर करता है"),
    ("Aventurine (एवेंट्यूरिन)", "तंत्रिका तंत्र को संतुलित करता है; मानसिक तनाव और बेचैनी कम करता है"),
    ("Tiger's Eye (टाइगर आई)", "साहस और कर्म — भय को दूर करता है, इच्छाशक्ति और निर्णय क्षमता को सशक्त बनाता है"),
]

SUPPORTING_CRYSTALS_GU = [
    ("Clear Quartz (સ્ફટિક)", "શક્તિનું રત્ન — ઊર્જા અને સંકલ્પને વધારે છે; તમામ ચક્રોને શુદ્ધ અને સંતુલિત કરે છે"),
    ("Citrine (સુનૈલા)", "ધન, પ્રતિષ્ઠા અને જ્ઞાનને આકર્ષે છે; પ્રેરણા અને આત્મવિશ્વાસ વધારે છે"),
    ("Pyrite (પાયરાઇટ)", "સુરક્ષા કવચ; ધન અને આર્થિક સ્થિરતા આકર્ષે છે; ઇચ્છાશક્તિ મજબૂત કરે છે"),
    ("Amethyst (જાંબુડિયો)", "શાંતિ અને અંતઃસ્ફુરણા — તણાવ, ચીડિયાપણું, ક્રોધ, ભય અને ચિંતા દૂર કરે છે"),
    ("Aventurine (એવેન્ટ્યુરિન)", "નર્વસ સિસ્ટમને સંતુલિત કરે છે; માનસિક તણાવ અને અશાંતિ ઘટાડે છે"),
    ("Tiger's Eye (ટાઇગર આઈ)", "સાહસ અને કર્મ — ભય દૂર કરે છે, ઇચ્છાશક્તિ અને નિર્ણયશક્તિ મજબૂત કરે છે"),
]

SUPPORTING_CRYSTALS_BY_LANG = {"en": SUPPORTING_CRYSTALS, "hi": SUPPORTING_CRYSTALS_HI, "gu": SUPPORTING_CRYSTALS_GU}

GRID_PLANETS_EN = {
    3: "Jupiter", 1: "Sun", 9: "Mars",
    6: "Venus", 7: "Ketu", 5: "Mercury",
    2: "Moon", 8: "Saturn", 4: "Rahu",
}


def _fmt_dash(date_str: str) -> str:
    return str(date_str or "").replace("/", "-")


def _lucky_dates(bn: int) -> str:
    dates = [bn]
    d = bn + 9
    while d <= 31:
        dates.append(d)
        d += 9
    return " · ".join(str(x) for x in dates)


def build_report_html(data: Dict[str, Any]) -> str:
    """
    Constructs the clean, white, editorial-grade Vedic Numerology HTML report
    matching the 12-page professional layout across English, Hindi, and Gujarati.
    """
    client = data["client"]
    consultant = data.get("consultant", {
        "name": "Jigar Thakkar",
        "phone": "+91 9377614772",
        "email": "jigar93776@gmail.com",
        "title": "Certified Vedic Numerologist & Vastu Consultant",
        "copyright": "© 2026 Jigar Thakkar. All Rights Reserved.",
    })
    core = data["core_numbers"]
    compass = data.get("compass", {})
    natal_grid = data.get("natal_grid", data["grid"])
    dasha = data.get("dasha", {})
    vibrations = data.get("vibrations", [])
    m_qualities = data.get("moolank_qualities", [])
    b_qualities = data.get("bhagyank_qualities", [])
    yogas = data.get("yogas", [])
    preds = data.get("predictions", {})
    remedies_by_num = data.get("remedies_by_number", [])
    ui = data.get("ui", {})

    lang = client.get("lang", "en")
    if lang not in REPORT_LABELS:
        lang = "en"
    L = REPORT_LABELS[lang]

    tier = str(data.get("tier", client.get("tier", "complete_499"))).lower().strip()
    include_remedies = (tier != "essential_299")

    bn = int(core["bn"])
    dn = int(core["dn"])
    bn_planet = core["bn_planet"]
    dn_planet = core["dn_planet"]

    # Fonts
    if lang == "hi":
        body_font = "'Source Sans 3', 'Noto Sans Devanagari', 'Mangal', sans-serif"
        serif_font = "'Libre Baskerville', 'Noto Serif Devanagari', 'Noto Sans Devanagari', serif"
        google_fonts = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Noto+Sans+Devanagari:wght@400;600;700&family=Source+Sans+3:wght@400;600;700&display=swap"
    elif lang == "gu":
        body_font = "'Source Sans 3', 'Noto Sans Gujarati', 'Shruti', sans-serif"
        serif_font = "'Libre Baskerville', 'Noto Serif Gujarati', 'Noto Sans Gujarati', serif"
        google_fonts = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Noto+Sans+Gujarati:wght@400;600;700&family=Source+Sans+3:wght@400;600;700&display=swap"
    else:
        body_font = "'Source Sans 3', -apple-system, BlinkMacSystemFont, sans-serif"
        serif_font = "'Libre Baskerville', Georgia, serif"
        google_fonts = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap"

    # Active dashas
    active_md = dasha.get("active_md", {})
    active_ad = dasha.get("active_ad", {})
    active_pd = dasha.get("active_pd", {})
    md_num = int(active_md.get("number", bn))
    ad_num = int(active_ad.get("ad_number", bn))
    pd_num = int(active_pd.get("number", ad_num))

    all_md = dasha.get("all_md_timeline", dasha.get("md_timeline", []))
    lifetime_ad = dasha.get("lifetime_ad", [])
    nine_year_grids = dasha.get("nine_year_grids", [])
    pratyantar_full = dasha.get("pratyantar_full", [])

    # Active age
    active_ad_row = next((r for r in lifetime_ad if r.get("is_active")), None)
    current_age = active_ad_row["age"] if active_ad_row else ""

    # Planet names lookup helper
    def planet_name(n: int) -> str:
        from vedic_translations import PLANET_INFO
        return PLANET_INFO.get(int(n), PLANET_INFO[1])[lang]["planet"]

    # Natal grid numbers & missing numbers
    grid_digits_str = ", ".join(str(d) for d in natal_grid.get("digits", []))
    counts = natal_grid.get("counts", {})
    missing_nums = [str(n) for n in range(1, 10) if counts.get(n, 0) == 0]
    missing_str = ", ".join(missing_nums) if missing_nums else "–"

    # Positive & Negative pills from natal vibrations
    natal_vibs = data.get("natal_vibrations", vibrations)
    pos_neg_pills = ""
    for v in natal_vibs:
        sign = "+" if v["type"] == "+" else "−"
        cls = "pill-pos" if v["type"] == "+" else "pill-neg"
        pos_neg_pills += f'<span class="vpill {cls}">{sign}{v["number"]}</span>'

    # Archetypes
    arch_map = ARCHETYPES_BY_LANG.get(lang, ARCHETYPES_EN)
    bn_arch_title, bn_arch_tags, bn_arch_desc = arch_map.get(bn, arch_map[1])
    dn_arch_title, dn_arch_tags, dn_arch_desc = arch_map.get(dn, arch_map[1])

    # Compatibility between BN and DN
    def _parse_num_list(val) -> List[int]:
        if isinstance(val, list):
            return [int(x) for x in val if str(x).strip().isdigit()]
        if isinstance(val, str):
            return [int(x.strip()) for x in val.replace("·", ",").split(",") if x.strip().isdigit()]
        return []

    friendly_nums = _parse_num_list(compass.get("friendly_nums", []))
    enemy_nums = _parse_num_list(compass.get("enemy_nums", []))
    if dn in friendly_nums or dn == bn:
        compat_label = L["friendly"]
        compat_desc = L["compat_friendly"]
    elif dn in enemy_nums:
        compat_label = L["enemy"]
        compat_desc = L["compat_enemy"]
    else:
        compat_label = L["neutral"]
        compat_desc = L["compat_neutral"]

    # Other numbers in natal grid besides BN and DN
    other_nums = sorted({int(n) for n, c in counts.items() if c > 0 and int(n) not in (bn, dn)})
    other_parts = []
    for onum in other_nums:
        _, otags, _ = arch_map.get(onum, arch_map[1])
        other_parts.append(f"<strong>{onum}</strong> — {', '.join(t.lower() for t in otags)}")
    other_summary_html = " · ".join(other_parts) if other_parts else "–"

    # Helper to render 3x3 Birth Grid
    def render_birth_grid_html(cells: List[Dict[str, Any]], mini: bool = False) -> str:
        html_cells = ""
        for c in cells:
            num = c["num"]
            p_lbl = GRID_PLANETS_EN.get(num, "")
            if mini:
                nat_s = c.get("natal_str", "")
                tr_s = c.get("transit_str", "")
                val_html = f'<span class="mg-nat">{nat_s}</span><span class="mg-tr">{tr_s}</span>'
            else:
                val_html = f'<span class="bg-val">{c["str"]}</span>' if c.get("count", 0) > 0 else ""
            html_cells += (
                f'<div class="vg-cell">'
                f'<div class="vg-planet">{p_lbl}</div>'
                f'<div class="vg-num">{val_html}</div>'
                f'</div>'
            )
        cls = "vg-grid vg-mini" if mini else "vg-grid"
        return f'<div class="{cls}">{html_cells}</div>'

    # Lotus SVG emblem
    lotus_svg = """<svg class="brand-logo" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="32" cy="32" r="28" stroke="#a855f7" stroke-width="1.5" stroke-opacity="0.35"/>
      <path d="M32 10C37 18 39 26 32 34C25 26 27 18 32 10Z" stroke="#9333ea" stroke-width="1.6" fill="#f3e8ff"/>
      <path d="M18 18C26 21 31 27 32 36C22 33 17 27 18 18Z" stroke="#a855f7" stroke-width="1.5" fill="#faf5ff"/>
      <path d="M46 18C38 21 33 27 32 36C42 33 47 27 46 18Z" stroke="#a855f7" stroke-width="1.5" fill="#faf5ff"/>
      <path d="M12 32C20 30 27 33 32 41C22 42 15 39 12 32Z" stroke="#c084fc" stroke-width="1.4" fill="#faf5ff"/>
      <path d="M52 32C44 30 37 33 32 41C42 42 49 39 52 32Z" stroke="#c084fc" stroke-width="1.4" fill="#faf5ff"/>
      <circle cx="32" cy="35" r="7" fill="#ffffff" stroke="#9333ea" stroke-width="1.6"/>
      <text x="32" y="38.5" text-anchor="middle" font-family="Georgia, serif" font-size="10" font-weight="700" fill="#7e22ce">ॐ</text>
    </svg>"""

    # ---------------- PAGE 2: Year Grids ----------------
    year_grids_html = ""
    for yg in nine_year_grids:
        is_run = yg.get("is_active", False)
        card_cls = "yg-card yg-running" if is_run else "yg-card"
        badge_html = f'<span class="running-badge">{L["running"]}</span>' if is_run else ""
        grid_inner = render_birth_grid_html(yg["cells"], mini=True)
        year_grids_html += f"""
        <div class="{card_cls}">
            <div class="yg-year">{yg["year"]} {badge_html}</div>
            <div class="yg-dates">{yg["from_str"]} – {yg["to_str"]}</div>
            <div class="yg-dasha"><span class="md-txt">{L["md"]} {yg["md"]}</span> <span class="ad-txt">{L["ad"]} {yg["ad"]}</span></div>
            {grid_inner}
        </div>"""

    # ---------------- PAGE 3: Mahadasha 90-Year Bar & 2 Cycles ----------------
    md_bar_html = ""
    for p in all_md[:18]:
        pct = (p["duration"] / 90.0) * 100.0
        col = NUM_COLORS.get(p["number"], "#6366f1")
        md_bar_html += f'<div class="md-seg" style="width:{pct:.2f}%;background:{col};">{p["number"]}</div>'

    def render_md_cycle_table(periods_slice: List[Dict[str, Any]], cycle_num: int) -> str:
        rows = ""
        for p in periods_slice:
            act_cls = ' class="row-active"' if p.get("is_active") else ""
            s_str = p.get("start_dash", _fmt_dash(p["start_str"]))
            e_str = p.get("end_dash", _fmt_dash(p["end_str"]))
            age_str = f'{p.get("start_age", "")}–{p.get("end_age", "")}'
            p_name = planet_name(p["number"])
            rows += f'<tr{act_cls}><td class="num-col">{p["number"]}</td><td>{p_name}</td><td>{s_str}</td><td>{e_str}</td><td>{age_str}</td></tr>'
        return f"""
        <div class="cycle-col">
            <div class="cycle-title">{L["cycle"]} {cycle_num}</div>
            <table class="clean-tbl">
                <thead><tr><th>{L["md"]}</th><th></th><th>{L["start"]}</th><th>{L["end"]}</th><th>{L["age"]}</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
        </div>"""

    md_cycle1_html = render_md_cycle_table(all_md[:9], 1)
    md_cycle2_html = render_md_cycle_table(all_md[9:18], 2)

    # ---------------- PAGE 4: Antardasha 90-Year 3-Column Table ----------------
    def render_ad_col(rows_slice: List[Dict[str, Any]]) -> str:
        trs = ""
        for r in rows_slice:
            act_cls = ' class="row-active"' if r.get("is_active") else ""
            trs += f'<tr{act_cls}><td>{r["age"]}</td><td>{r["from_str"]}</td><td>{r["to_str"]}</td><td class="bold-col">{r["md"]}</td><td class="bold-col">{r["ad"]}</td></tr>'
        return f"""
        <div class="ad-col">
            <table class="clean-tbl compact-tbl">
                <thead><tr><th>{L["age"]}</th><th>{L["from"]}</th><th>{L["to"]}</th><th>{L["md"]}</th><th>{L["ad"]}</th></tr></thead>
                <tbody>{trs}</tbody>
            </table>
        </div>"""

    ad_col1 = render_ad_col(lifetime_ad[0:30])
    ad_col2 = render_ad_col(lifetime_ad[30:60])
    ad_col3 = render_ad_col(lifetime_ad[60:90])

    # ---------------- PAGE 5: Pratyantar Dasha Table ----------------
    pd_rows_html = ""
    for p in pratyantar_full:
        act_cls = ' class="row-active-pd"' if p.get("is_active") else ""
        now_badge = f' <span class="now-pill">{L["now"]}</span>' if p.get("is_active") else ""
        days_lbl = f'{p["duration_days"]} ({L["adjustment"]})' if p.get("is_adjustment") else f'{p["duration_days"]}'
        s_str = p.get("start_dash", _fmt_dash(p["start_str"]))
        e_str = p.get("end_dash", _fmt_dash(p["end_str"]))
        p_name = planet_name(p["number"])
        pd_rows_html += f"""
        <tr{act_cls}>
            <td class="pd-num-col">{p["number"]}</td>
            <td>{p_name}</td>
            <td>{days_lbl}</td>
            <td>{s_str}</td>
            <td>{e_str}{now_badge}</td>
        </tr>"""

    # ---------------- PAGES 6 & 7: Life Path & Professions ----------------
    bn_qual_lis = "".join(f"<li>{q}</li>" for q in m_qualities)
    dn_tag_pills = "".join(f'<span class="kw-pill">{t}</span>' for t in dn_arch_tags)
    prof_rows_html = ""
    prof_map = PROFESSIONS_BY_LANG.get(lang, PROFESSIONS_BY_BN)
    for cat_title, cat_items in prof_map.get(bn, prof_map[1]):
        prof_rows_html += f"""
        <div class="prof-row">
            <div class="prof-cat">{cat_title}</div>
            <div class="prof-items">{cat_items}</div>
        </div>"""

    # ---------------- PAGES 8 & 9: Grid Analysis & Yogas ----------------
    vibe_cards_html = ""
    for v in vibrations:
        is_pos = (v["type"] == "+")
        card_cls = "ga-card ga-pos" if is_pos else "ga-card ga-neg"
        sign = "+" if is_pos else "−"
        cnt = v.get("count", 1)
        cnt_lbl = L["once"] if cnt == 1 else f'{cnt} {L["times"]}'
        v_planet = planet_name(v["number"])
        vibe_cards_html += f"""
        <div class="{card_cls}">
            <div class="ga-head">
                <span class="ga-num">{sign}{v["number"]}</span>
                <span class="ga-meta">{v_planet} · {cnt_lbl}</span>
            </div>
            <div class="ga-body">{v.get("text", "")}</div>
        </div>"""

    yogas_cards_html = ""
    for y in yogas:
        pts_html = "".join(f"<li>{pt}</li>" for pt in y.get("points", []))
        y_tag = y.get("tag", "")
        yogas_cards_html += f"""
        <div class="yoga-box">
            <div class="yoga-title">{y["name"]} <span class="yoga-tag">{y_tag}</span></div>
            {f'<ul class="yoga-pts">{pts_html}</ul>' if pts_html else ''}
        </div>"""

    # ---------------- PAGE 10: Predictions & Nine-Year Outlook ----------------
    pred_rows_natal = [
        (ui.get("pred_finance", L["money"]), preds.get("finance", "")),
        (ui.get("pred_property", L["assets"]), preds.get("property", "")),
        (ui.get("pred_health", L["health"]), preds.get("health", "")),
    ]
    pred_rows_year = [
        (ui.get("pred_vehicle", "Vehicles"), preds.get("vehicle", "")),
        (ui.get("pred_education", "Growth"), preds.get("education", "")),
        (ui.get("pred_travel", L["travel"]), preds.get("travel", "")),
        (ui.get("pred_litigation", L["disputes"]), preds.get("litigation", "")),
        (ui.get("pred_relationship", "Relations"), preds.get("relationship", "")),
    ]

    def render_pred_rows(rows: list) -> str:
        out = ""
        for lbl, txt in rows:
            timing_html = ""
            if isinstance(txt, dict):
                tw = txt.get("timing_windows")
                if tw:
                    def _pills(items):
                        return "".join(
                            f'<span style="display:inline-block;background:#fff;border:1px solid #fde68a;border-radius:4px;padding:1px 6px;margin:1px 4px 1px 0;font-size:8.6px;color:#0f172a;">{it}</span>'
                            for it in items
                        )
                    note_badge = f' <span style="color:#b91c1c;font-weight:700;">({tw["note"]})</span>' if tw.get("note") else ""
                    timing_html = f"""
                    <div style="margin-top:5px;padding:6px 9px;background:#fefce8;border-left:3px solid #eab308;border-radius:0 6px 6px 0;font-size:8.8px;line-height:1.45;">
                        <div style="margin-bottom:2px;"><strong style="color:#854d0e;">{tw["pd_label"]}{note_badge}:</strong> {_pills(tw.get("pratyantar", []))}</div>
                        <div style="margin-bottom:2px;"><strong style="color:#854d0e;">{tw["ad_label"]}:</strong> {_pills(tw.get("antardasha_years", []))}</div>
                        <div><strong style="color:#854d0e;">{tw["md_label"]}:</strong> {_pills(tw.get("mahadasha", []))}</div>
                    </div>"""
                elif txt.get("timing"):
                    timing_html = f'<div style="margin-top:4px;padding:4px 8px;background:#fefce8;border-left:3px solid #eab308;font-size:9px;color:#713f12;">{txt.get("timing")}</div>'
                txt = txt.get("desc", "")
            if txt:
                out += f'<div class="pred-row"><div class="pred-lbl">{lbl}</div><div class="pred-txt">{txt}{timing_html}</div></div>'
        return out

    outlook_rows_html = ""
    for yg in nine_year_grids:
        act_cls = ' class="row-active-pd"' if yg.get("is_active") else ""
        def pill(tup):
            code, txt = tup
            if code == "none":
                return f'<span class="ol-dash">{txt}</span>'
            return f'<span class="ol-pill ol-{code}">{txt}</span>'

        outlook_rows_html += f"""
        <tr{act_cls}>
            <td class="bold-col">{yg["year"]}</td>
            <td>{yg["age"]}</td>
            <td>{yg["md"]}</td>
            <td>{yg["ad"]}</td>
            <td>{pill(yg["money"])}</td>
            <td>{pill(yg["assets"])}</td>
            <td>{pill(yg["travel"])}</td>
            <td>{pill(yg["disputes"])}</td>
            <td>{pill(yg["health"])}</td>
        </tr>"""

    # ---------------- PAGES 11 & 12: Remedies & Crystals ----------------
    remedies_section_html = ""
    if include_remedies:
        rem_cards_list = []
        for r in remedies_by_num:
            nc = r.get("natal_count", 0)
            sub_line = L["appears_grid"].format(n=nc) if nc >= 2 else L["active_period_neg"]
            rem_cards_list.append(f"""
            <div class="rem-card">
                <div class="rem-head">
                    <span class="rem-circle">{r["number"]}</span>
                    <div>
                        <div class="rem-title">Number {r["number"]} · {r["planet"]}</div>
                        <div class="rem-sub">{sub_line}</div>
                    </div>
                </div>
                <div class="rem-sec-lbl">{L["mantras_practices"]}</div>
                <p class="rem-p">{r["mantra"]}</p>
                <div class="rem-sec-lbl">{L["service_seva"]}</div>
                <p class="rem-p">{r["seva"]}</p>
                <div class="rem-sec-lbl">{L["donations"]}</div>
                <p class="rem-p">{r["donation"]}</p>
                <div class="rem-sec-lbl">{L["colours"]}</div>
                <p class="rem-p">{r["colors"]}</p>
                <div class="rem-sec-lbl">{L["fasting"]}</div>
                <p class="rem-p">{r["fasting"]}</p>
            </div>""")

        crystals_list = SUPPORTING_CRYSTALS_BY_LANG.get(lang, SUPPORTING_CRYSTALS)
        crystals_html = "".join(
            f'<div class="crystal-row"><div class="crystal-name">{cname}</div><div class="crystal-desc">{cdesc}</div></div>'
            for cname, cdesc in crystals_list
        )

        # Paginate remedies cleanly (max 4 cards per page; crystals on separate page if > 2 remedies)
        remedies_section_html = ""
        for idx in range(0, len(rem_cards_list), 4):
            chunk = "".join(rem_cards_list[idx:idx + 4])
            intro_p = f'<p class="lead-note">{L["remedies_intro"]}</p>' if idx == 0 else ""
            crystals_inline = (
                f'<h3 class="sec-h3">{L["supporting_crystals"]}</h3><div class="crystal-list">{crystals_html}</div>'
                if (idx == 0 and len(rem_cards_list) <= 2) else ""
            )
            remedies_section_html += f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{L["prof_report"]}</div>
            <h2 class="sec-h2">{L["remedies"]}</h2>
            {intro_p}
            <div class="rem-grid">
                {chunk}
            </div>
            {crystals_inline}
        </div>"""

        if len(rem_cards_list) > 2:
            remedies_section_html += f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{L["prof_report"]}</div>
            <h2 class="sec-h2">{L["supporting_crystals"]}</h2>
            <div class="crystal-list">
                {crystals_html}
            </div>
        </div>"""

    # Complete HTML
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{consultant["name"]} - {L["report_title"]} - {client["name"]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{google_fonts}" rel="stylesheet">
<style>
@page {{
    size: A4 portrait;
    margin: 12mm;
}}
* {{
    box-sizing: border-box;
}}
body {{
    margin: 0;
    padding: 0;
    background: #ffffff;
    color: #1e293b;
    font-family: {body_font};
    font-size: 11px;
    line-height: 1.48;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}
.page-break {{
    page-break-before: always;
    break-before: page;
}}
.sheet {{
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px 22px;
    background: #ffffff;
    margin-bottom: 12px;
}}
/* Header */
.brand-row {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid #e2e8f0;
}}
.brand-logo {{
    width: 44px;
    height: 44px;
    flex-shrink: 0;
}}
.brand-name {{
    font-family: {serif_font};
    font-size: 18px;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.2;
}}
.brand-meta {{
    font-size: 10.5px;
    color: #64748b;
    margin-top: 2px;
}}
.report-sub-bar {{
    padding: 10px 0;
    font-size: 12px;
    color: #475569;
}}
.report-sub-bar strong {{
    font-family: {serif_font};
    color: #1e293b;
    font-size: 13.5px;
    margin-left: 6px;
}}
.caution-bar {{
    background: #fefce8;
    border-left: 4px solid #eab308;
    padding: 9px 14px;
    font-size: 11px;
    font-weight: 600;
    color: #713f12;
    border-radius: 0 6px 6px 0;
    margin-bottom: 14px;
}}
/* Client Hero */
.kicker {{
    font-family: {serif_font};
    font-style: italic;
    font-size: 11px;
    color: #7c3aed;
    margin-bottom: 2px;
}}
.client-name {{
    font-family: {serif_font};
    font-size: 24px;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 3px 0;
}}
.client-meta {{
    font-size: 11px;
    color: #64748b;
    margin-bottom: 14px;
}}
/* Summary 5-card grid */
.summary-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}}
.sum-card {{
    background: #f8f7ff;
    border: 1px solid #ede9fe;
    border-radius: 10px;
    padding: 10px 14px;
}}
.sum-card.full-span {{
    grid-column: span 2;
}}
.sum-lbl {{
    font-size: 10px;
    color: #64748b;
    font-weight: 600;
}}
.sum-val {{
    font-family: {serif_font};
    font-size: 20px;
    font-weight: 700;
    margin: 2px 0;
}}
.sum-sub {{
    font-size: 10px;
    color: #475569;
}}
/* Birth Grid */
.sec-h2 {{
    font-family: {serif_font};
    font-size: 18px;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 10px 0;
}}
.sec-h3 {{
    font-family: {serif_font};
    font-size: 14px;
    font-weight: 700;
    color: #0f172a;
    margin: 14px 0 8px 0;
}}
.birth-grid-wrap {{
    display: flex;
    gap: 18px;
    align-items: flex-start;
}}
.vg-grid {{
    display: grid;
    grid-template-columns: repeat(3, 62px);
    grid-template-rows: repeat(3, 46px);
    border: 1.5px solid #c9a96e;
    border-radius: 4px;
    background: #ffffff;
    flex-shrink: 0;
}}
.vg-grid.vg-mini {{
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 34px);
    width: 100%;
    margin-top: 6px;
}}
.vg-cell {{
    border: 0.5px solid #e2d1a8;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 2px;
}}
.vg-planet {{
    font-size: 7.5px;
    color: #b48a3e;
    line-height: 1.1;
}}
.vg-mini .vg-planet {{
    font-size: 6.5px;
}}
.vg-num {{
    font-family: {serif_font};
    font-size: 14px;
    font-weight: 700;
    color: #0f172a;
    margin-top: 3px;
}}
.vg-mini .vg-num {{
    font-size: 11px;
    margin-top: 1px;
}}
.mg-nat {{ color: #0f172a; }}
.mg-tr {{ color: #d97706; }}
.grid-facts {{
    flex: 1;
}}
.fact-line {{
    font-size: 11px;
    margin-bottom: 6px;
    color: #334155;
}}
.vpill {{
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    padding: 1px 7px;
    border-radius: 999px;
    margin-right: 4px;
}}
.pill-pos {{ background: #dcfce7; color: #166534; }}
.pill-neg {{ background: #fee2e2; color: #991b1b; }}
.pers-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 12px;
    margin-top: 10px;
}}
.pers-title {{
    font-family: {serif_font};
    font-size: 12.5px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 4px;
}}
.pers-desc {{
    font-size: 10.5px;
    color: #475569;
}}
/* Page 2: Year Grids */
.lead-note {{
    font-size: 10.8px;
    color: #64748b;
    margin: 0 0 12px 0;
}}
.yg-matrix {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}}
.yg-card {{
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 8px 10px;
    text-align: center;
    background: #ffffff;
}}
.yg-card.yg-running {{
    border: 2px solid #7c3aed;
    background: #fdfcff;
}}
.yg-year {{
    font-family: {serif_font};
    font-size: 13px;
    font-weight: 700;
    color: #0f172a;
}}
.running-badge {{
    background: #7c3aed;
    color: #ffffff;
    font-family: {body_font};
    font-size: 8.5px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 999px;
    vertical-align: middle;
    margin-left: 4px;
}}
.yg-dates {{
    font-size: 8.8px;
    color: #64748b;
    margin: 2px 0;
}}
.yg-dasha {{
    font-size: 9.5px;
    font-weight: 700;
}}
.md-txt {{ color: #0f766e; }}
.ad-txt {{ color: #b45309; margin-left: 4px; }}
/* Page 3, 4, 5: Dasha Headings & Tables */
.dasha-head {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}}
.d-circle {{
    width: 28px;
    height: 28px;
    border-radius: 50%;
    color: #ffffff;
    font-family: {serif_font};
    font-size: 13px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}}
.d-sub {{
    font-size: 11px;
    color: #475569;
}}
.md-bar {{
    display: flex;
    height: 20px;
    border-radius: 999px;
    overflow: hidden;
    margin: 8px 0 4px 0;
}}
.md-seg {{
    color: #ffffff;
    font-size: 9px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
}}
.md-bar-labels {{
    display: flex;
    justify-content: space-between;
    font-size: 9.5px;
    color: #64748b;
    margin-bottom: 14px;
}}
.cycles-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
}}
.cycle-title {{
    font-size: 11.5px;
    font-weight: 700;
    color: #334155;
    margin-bottom: 6px;
}}
.clean-tbl {{
    width: 100%;
    border-collapse: collapse;
    font-size: 10px;
}}
.clean-tbl th {{
    text-align: left;
    font-weight: 600;
    color: #64748b;
    border-bottom: 1px solid #cbd5e1;
    padding: 5px 4px;
}}
.clean-tbl td {{
    padding: 5px 4px;
    border-bottom: 1px solid #f1f5f9;
    color: #334155;
}}
.clean-tbl.compact-tbl th,
.clean-tbl.compact-tbl td {{
    padding: 3px 3px;
    font-size: 8.8px;
}}
.num-col, .bold-col, .pd-num-col {{
    font-weight: 700;
    color: #0f172a;
}}
.pd-num-col {{
    color: #7c3aed;
}}
.row-active td {{
    background: #f5f3ff;
    font-weight: 700;
    color: #0f172a;
}}
.row-active-pd td {{
    background: #f3e8ff;
    font-weight: 700;
    color: #0f172a;
}}
.ad-3col {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}}
.now-pill {{
    background: #7c3aed;
    color: #ffffff;
    font-size: 8px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 999px;
    margin-left: 5px;
}}
/* Page 6 & 7: Life Path */
.prop-bar {{
    display: flex;
    height: 22px;
    border-radius: 6px;
    overflow: hidden;
    font-size: 10px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
}}
.prop-b {{ width: 30%; background: #7c3aed; display: flex; align-items: center; padding-left: 10px; }}
.prop-d {{ width: 40%; background: #2563eb; display: flex; align-items: center; padding-left: 10px; }}
.prop-o {{ width: 30%; background: #db2777; display: flex; align-items: center; padding-left: 10px; }}
.lp-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
}}
.lp-card {{
    background: #f8f7ff;
    border: 1px solid #ede9fe;
    border-radius: 10px;
    padding: 12px 14px;
}}
.lp-hero {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 6px 0 8px 0;
}}
.lp-big-num {{
    font-family: {serif_font};
    font-size: 26px;
    font-weight: 700;
    color: #7c3aed;
}}
.lp-arch {{
    font-family: {serif_font};
    font-size: 13px;
    font-weight: 700;
    color: #0f172a;
}}
.lp-planet {{
    font-size: 10px;
    color: #64748b;
}}
.kw-pill {{
    display: inline-block;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 999px;
    padding: 2px 8px;
    font-size: 9.5px;
    font-weight: 600;
    margin-right: 4px;
    margin-top: 6px;
}}
.qual-ul {{
    margin: 6px 0 0 16px;
    padding: 0;
    font-size: 10px;
    color: #334155;
}}
.qual-ul li {{ margin-bottom: 4px; }}
.compat-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 10px;
}}
.compat-title {{
    font-family: {serif_font};
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
    margin: 2px 0 4px 0;
}}
.mini4-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 8px;
}}
.mini4-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 8px 10px;
}}
.mini4-lbl {{ font-size: 9.5px; color: #64748b; }}
.mini4-val {{ font-size: 10.5px; font-weight: 700; color: #0f172a; margin-top: 2px; }}
.prof-row {{
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 6px;
}}
.prof-cat {{
    font-family: {serif_font};
    font-size: 11.5px;
    font-weight: 700;
    color: #0f172a;
}}
.prof-items {{ font-size: 10px; color: #475569; margin-top: 2px; }}
/* Page 8 & 9: Grid Analysis & Yogas */
.ga-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 14px;
}}
.ga-card {{
    border-radius: 8px;
    padding: 10px 12px;
    border-left: 3.5px solid;
}}
.ga-pos {{ background: #f0fdf4; border-left-color: #16a34a; }}
.ga-neg {{ background: #fef2f2; border-left-color: #b91c1c; }}
.ga-head {{ margin-bottom: 4px; }}
.ga-num {{ font-family: {serif_font}; font-size: 13px; font-weight: 700; color: #0f172a; }}
.ga-meta {{ font-size: 10px; color: #475569; margin-left: 4px; }}
.ga-body {{ font-size: 10px; color: #334155; }}
.yoga-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}}
.yoga-box {{
    border: 1px solid #e5d5a7;
    background: #fffdf7;
    border-radius: 8px;
    padding: 10px 12px;
    break-inside: avoid;
}}
.yoga-title {{
    font-family: {serif_font};
    font-size: 12px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 4px;
}}
.yoga-tag {{
    font-family: {body_font};
    font-size: 9.5px;
    font-weight: 600;
    color: #a16207;
}}
.yoga-pts {{
    margin: 4px 0 0 15px;
    padding: 0;
    font-size: 9.8px;
    color: #334155;
}}
/* Page 10: Predictions & Outlook */
.pred-row {{
    display: flex;
    gap: 12px;
    padding: 6px 0;
    border-bottom: 1px solid #f1f5f9;
    break-inside: avoid;
    page-break-inside: avoid;
}}
.pred-lbl {{
    width: 80px;
    flex-shrink: 0;
    font-weight: 700;
    font-size: 10.5px;
    color: #15803d;
}}
.pred-txt {{ font-size: 10.3px; color: #334155; flex: 1; }}
.ol-pill {{
    display: inline-block;
    font-size: 9px;
    font-weight: 700;
    padding: 1px 7px;
    border-radius: 999px;
}}
.ol-mixed {{ background: #fef3c7; color: #92400e; }}
.ol-tight {{ background: #fee2e2; color: #991b1b; }}
.ol-up {{ background: #dcfce7; color: #166534; }}
.ol-likely {{ background: #dcfce7; color: #166534; }}
.ol-friction {{ background: #fee2e2; color: #991b1b; }}
.ol-body_mind, .ol-mind, .ol-body {{ background: #fee2e2; color: #991b1b; }}
.ol-dash {{ color: #94a3b8; }}
/* Page 11 & 12: Remedies & Crystals */
.rem-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 10px;
}}
.rem-card {{
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 8px 10px;
    break-inside: avoid;
}}
.rem-head {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 4px;
}}
.rem-circle {{
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #f5f3ff;
    color: #7c3aed;
    font-weight: 700;
    font-size: 10.5px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}}
.rem-title {{ font-family: {serif_font}; font-size: 11.8px; font-weight: 700; color: #0f172a; }}
.rem-sub {{ font-size: 9px; color: #64748b; }}
.rem-sec-lbl {{ font-size: 9.5px; font-weight: 700; color: #7c3aed; margin-top: 4px; }}
.rem-p {{ font-size: 9.3px; color: #334155; margin: 1px 0; line-height: 1.35; }}
.crystal-row {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 5px 10px;
    margin-bottom: 4px;
    break-inside: avoid;
}}
.crystal-name {{ font-family: {serif_font}; font-size: 10.5px; font-weight: 700; color: #0f172a; }}
.crystal-desc {{ font-size: 9.3px; color: #475569; }}
.report-footer {{
    text-align: center;
    padding: 12px 0 4px 0;
    font-size: 10px;
    color: #64748b;
}}
</style>
</head>
<body>

<!-- PAGE 1: COVER + SUMMARY + BIRTH GRID -->
<div class="sheet">
    <div class="brand-row">
        {lotus_svg}
        <div>
            <div class="brand-name">{L["prepared_by"]}: {consultant["name"]}</div>
            <div class="brand-meta">{consultant.get("title", "")} · {consultant["phone"]} · {consultant["email"]}</div>
        </div>
    </div>
    <div class="report-sub-bar">{L["report_kicker"]} <strong>{L["report_title"]}</strong></div>
    <div class="caution-bar">{L["caution_banner"]}</div>

    <div class="kicker">{L["prepared_for"]}</div>
    <h1 class="client-name">{client["name"]}</h1>
    <div class="client-meta">{L["born"]} {_fmt_dash(client["dob"])} · {client["weekday"]} · {L["as_on"]} {_fmt_dash(client["target_date"])}</div>

    <div class="summary-grid">
        <div class="sum-card">
            <div class="sum-lbl">{L["basic_number"]}</div>
            <div class="sum-val" style="color:#92400e;">{bn}</div>
            <div class="sum-sub">{bn_planet}</div>
        </div>
        <div class="sum-card">
            <div class="sum-lbl">{L["destiny_number"]}</div>
            <div class="sum-val" style="color:#312e81;">{dn}</div>
            <div class="sum-sub">{dn_planet}</div>
        </div>
        <div class="sum-card">
            <div class="sum-lbl">{L["mahadasha"]}</div>
            <div class="sum-val" style="color:#0f766e;">{md_num}</div>
            <div class="sum-sub">{_fmt_dash(active_md.get("start_str", ""))} – {_fmt_dash(active_md.get("end_str", ""))}</div>
        </div>
        <div class="sum-card">
            <div class="sum-lbl">{L["antardasha"]}</div>
            <div class="sum-val" style="color:#c2410c;">{ad_num}</div>
            <div class="sum-sub">{_fmt_dash(active_ad.get("start_str", ""))} – {_fmt_dash(active_ad.get("end_str", ""))}</div>
        </div>
        <div class="sum-card full-span">
            <div class="sum-lbl">{L["pratyantar"]}</div>
            <div class="sum-val" style="color:#be185d;">{pd_num}</div>
            <div class="sum-sub">{_fmt_dash(active_pd.get("start_str", ""))} – {_fmt_dash(active_pd.get("end_str", ""))}</div>
        </div>
    </div>
</div>

<div class="sheet">
    <h2 class="sec-h2">{L["birth_grid"]}</h2>
    <div class="birth-grid-wrap">
        {render_birth_grid_html(natal_grid["cells"], mini=False)}
        <div class="grid-facts">
            <div class="fact-line"><strong>{L["nums_in_grid"]}</strong> {grid_digits_str}</div>
            <div class="fact-line"><strong>{L["missing_nums"]}</strong> {missing_str}</div>
            <div class="fact-line"><strong>{L["pos_and_neg"]}</strong> {pos_neg_pills}</div>
            <div class="pers-box">
                <div class="pers-title">{L["personality"]} · {L["basic_number"]} {bn} · {bn_arch_title}</div>
                <div class="pers-desc">{bn_arch_desc}</div>
            </div>
        </div>
    </div>
</div>

<!-- PAGE 2: YEAR GRIDS -->
<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">{L["year_grids"]}</h2>
    <p class="lead-note">{L["year_grids_sub"]}</p>
    <div class="yg-matrix">
        {year_grids_html}
    </div>
</div>

<!-- PAGE 3: MAHADASHA -->
<div class="page-break"></div>
<div class="sheet">
    <div class="dasha-head">
        <h2 class="sec-h2" style="margin:0;">{L["mahadasha"]}</h2>
        <span class="d-circle" style="background:{NUM_COLORS.get(md_num, '#dc2626')};">{md_num}</span>
        <span class="d-sub">{planet_name(md_num)} {_fmt_dash(active_md.get("start_str", ""))} – {_fmt_dash(active_md.get("end_str", ""))} · {L["age_lower"]} {active_md.get("start_age", "")}–{active_md.get("end_age", "")}</span>
    </div>
    <div class="md-bar">{md_bar_html}</div>
    <div class="md-bar-labels"><span>{L["birth"]}</span><span>{L["age"]} 45</span><span>{L["age"]} 90</span></div>
    <div class="cycles-grid">
        {md_cycle1_html}
        {md_cycle2_html}
    </div>
</div>

<!-- PAGE 4: ANTARDASHA (90 YEARS) -->
<div class="page-break"></div>
<div class="sheet">
    <div class="dasha-head">
        <h2 class="sec-h2" style="margin:0;">{L["antardasha"]}</h2>
        <span class="d-circle" style="background:{NUM_COLORS.get(ad_num, '#4f46e5')};">{ad_num}</span>
        <span class="d-sub">{planet_name(ad_num)} {_fmt_dash(active_ad.get("start_str", ""))} – {_fmt_dash(active_ad.get("end_str", ""))} · {L["age_lower"]} {current_age}</span>
    </div>
    <p class="lead-note">{L["ad_formula"]}</p>
    <div class="ad-3col">
        {ad_col1}
        {ad_col2}
        {ad_col3}
    </div>
</div>

<!-- PAGE 5: PRATYANTAR DASHA -->
<div class="page-break"></div>
<div class="sheet">
    <div class="dasha-head">
        <h2 class="sec-h2" style="margin:0;">{L["pratyantar_dasha"]}</h2>
        <span class="d-circle" style="background:{NUM_COLORS.get(pd_num, '#8b5cf6')};">{pd_num}</span>
        <span class="d-sub">{planet_name(pd_num)} {_fmt_dash(active_pd.get("start_str", ""))} – {_fmt_dash(active_pd.get("end_str", ""))} · {active_pd.get("duration_days", 0)} {L["days"].lower()}</span>
    </div>
    <p class="lead-note">{L["pd_formula"].format(ad=ad_num, start=_fmt_dash(active_ad.get("start_str", "")), end=_fmt_dash(active_ad.get("end_str", "")))}</p>
    <table class="clean-tbl">
        <thead><tr><th>{L["pd"]}</th><th>{L["planet"]}</th><th>{L["days"]}</th><th>{L["start"]}</th><th>{L["end"]}</th></tr></thead>
        <tbody>{pd_rows_html}</tbody>
    </table>
    <p class="lead-note" style="margin-top:10px;">{L["pd_adj_note"]}</p>
</div>

<!-- PAGES 6 & 7: LIFE PATH & PROFESSIONS -->
<div class="page-break"></div>
<div class="sheet">
    <div class="kicker">{L["prof_report"]}</div>
    <h2 class="sec-h2">{L["life_path"]}</h2>
    <div class="prop-bar">
        <div class="prop-b">{L["basic_pct"]}</div>
        <div class="prop-d">{L["destiny_pct"]}</div>
        <div class="prop-o">{L["other_pct"]}</div>
    </div>

    <div class="lp-grid">
        <div class="lp-card">
            <div class="kicker">{L["life_path_dn"]}</div>
            <div class="lp-hero">
                <div class="lp-big-num">{dn}</div>
                <div>
                    <div class="lp-arch">{dn_arch_title}</div>
                    <div class="lp-planet">{dn_planet}</div>
                </div>
            </div>
            <div class="pers-desc">{dn_arch_desc}</div>
            <div>{dn_tag_pills}</div>
        </div>
        <div class="lp-card">
            <div class="kicker">{L["personality_bn"]}</div>
            <div class="lp-hero">
                <div class="lp-big-num">{bn}</div>
                <div>
                    <div class="lp-arch">{bn_arch_title}</div>
                    <div class="lp-planet">{bn_planet}</div>
                </div>
            </div>
            <ul class="qual-ul">{bn_qual_lis}</ul>
        </div>
    </div>

    <div class="compat-card">
        <div class="kicker">{L["basic_number"]} {bn} × {L["destiny_number"]} {dn}</div>
        <div class="compat-title">{compat_label}</div>
        <div class="pers-desc">{compat_desc}</div>
    </div>

    <div class="fact-line"><strong>{L["other_together"]}</strong> {other_summary_html}</div>

    <div class="mini4-grid">
        <div class="mini4-card"><div class="mini4-lbl">{L["lucky_dates"]}</div><div class="mini4-val">{_lucky_dates(bn)}</div></div>
        <div class="mini4-card"><div class="mini4-lbl">{L["fav_days"]}</div><div class="mini4-val">{core.get("favourable_days", "")}</div></div>
        <div class="mini4-card"><div class="mini4-lbl">{L["lucky_colors"]}</div><div class="mini4-val">{core.get("favourable_colors", "")}</div></div>
        <div class="mini4-card"><div class="mini4-lbl">{L["gemstone"]}</div><div class="mini4-val">{core.get("gemstone", "")}</div></div>
    </div>

    <h3 class="sec-h3">{L["professions_title"].format(bn=bn)}</h3>
    {prof_rows_html}
</div>

<!-- PAGES 8 & 9: GRID ANALYSIS & YOGAS -->
<div class="page-break"></div>
<div class="sheet">
    <div class="kicker">{L["prof_report"]}</div>
    <h2 class="sec-h2">{L["grid_analysis"]}</h2>
    <div class="ga-grid">
        {vibe_cards_html}
    </div>
    <h3 class="sec-h3">{L["yogas_title"]}</h3>
    <div class="yoga-grid">
        {yogas_cards_html}
    </div>
</div>

<!-- PAGE 10A: PREDICTIONS (BIRTH GRID) -->
<div class="page-break"></div>
<div class="sheet">
    <div class="kicker">{L["prof_report"]}</div>
    <h2 class="sec-h2">{L["predictions"]}</h2>
    <h3 class="sec-h3">{L["from_birth_grid"]}</h3>
    {render_pred_rows(pred_rows_natal)}
</div>

<!-- PAGE 10B: PREDICTIONS (THIS YEAR & UPCOMING) -->
<div class="page-break"></div>
<div class="sheet">
    <div class="kicker">{L["prof_report"]}</div>
    <h2 class="sec-h2">{L["predictions"]}</h2>
    <h3 class="sec-h3">{L["this_year"]} · {L["md"]} {md_num} · {L["ad"]} {ad_num} · {_fmt_dash(active_ad.get("start_str", ""))} – {_fmt_dash(active_ad.get("end_str", ""))}</h3>
    {render_pred_rows(pred_rows_year)}
</div>

<!-- PAGE 11: NINE-YEAR OUTLOOK -->
<div class="page-break"></div>
<div class="sheet">
    <div class="kicker">{L["prof_report"]}</div>
    <h2 class="sec-h2">{L["nine_year_outlook"]}</h2>
    <table class="clean-tbl">
        <thead>
            <tr>
                <th>{L["year"]}</th><th>{L["age"]}</th><th>{L["md"]}</th><th>{L["ad"]}</th>
                <th>{L["money"]}</th><th>{L["assets"]}</th><th>{L["travel"]}</th><th>{L["disputes"]}</th><th>{L["health"]}</th>
            </tr>
        </thead>
        <tbody>{outlook_rows_html}</tbody>
    </table>
</div>

{remedies_section_html}

<div class="report-footer">
    <div>{L["prepared_by"]} {consultant["name"]} · {consultant["phone"]}</div>
    <div style="margin-top:3px;">{L["disclaimer"]}</div>
</div>

</body>
</html>"""
    return html


def build_matchmaking_html(m: Dict[str, Any]) -> str:
    """
    Constructs the clean, white, editorial-grade 5-Pillar Match Making Report HTML
    for Boy (Groom) and Girl (Bride) in English, Hindi, or Gujarati, ready for Chromium PDF export.
    """
    lang = m.get("lang", "en")
    if lang not in ("en", "hi", "gu"):
        lang = "en"

    MM_STRINGS = {
        "en": {
            "report_sub": "Match Making Report",
            "kicker_top": "Vedic Numerology",
            "prepared_by": "Prepared by",
            "prepared_for": "Prepared for",
            "sub_pillars": "Five pillars of 20 points each · Vedic Compatibility Method",
            "the_two_grids": "The two grids",
            "boy_role": "Boy · Groom",
            "girl_role": "Girl · Bride",
            "born": "Born",
            "age": "age",
            "basic": "Basic",
            "destiny": "Destiny",
            "yogas_lbl": "Yogas:",
            "none": "None",
            "five_pillars": "The five pillars",
            "rules_title": "Basic matching & rejection rules",
            "matching_rules_title": "Basic Matching Rules (Compatibility & Support)",
            "rejection_rules_title": "Basic Rejection Rules & Red-Flag Checks",
            "why_important_lbl": "Why Important:",
            "couple_effect_lbl": "Effect on Couple:",
            "status_ok": "Matched",
            "status_warn": "Caution",
            "status_reject": "Rejected",
            "lit_title": "5-Year Litigation Check:",
            "lit_ok": "No 2+ year litigation activation detected in the next 5 years for either grid.",
            "lit_warn_pre": "Litigation trigger active — ",
            "lit_warn_post": ". Consult carefully before proceeding.",
            "running": "Running",
            "grids_title": "9-Year Forward Transit Grids (Current to Next 8 Years)",
            "grids_sub": "Birth grid overlaid with each upcoming year's Mahadasha (MD) and Antardasha (AD), starting from the current running year.",
            "dasha_title": "Mahadasha & Active Periods",
            "cycle": "Cycle",
            "birth": "Birth",
            "age45": "Age 45",
            "age90": "Age 90",
            "analysis_title": "Grid Analysis & Yogas",
            "active_yogas": "Active Yogas in Birth Grid (Positive / Negative & Impact)",
            "yoga_pos": "Positive · Auspicious",
            "yoga_neg": "Negative · Challenging",
            "yoga_mix": "Mixed Energy",
            "no_yogas": "No major yogas triggered.",
            "outlook_kicker": "Joint Timeline Comparison (Current to Next 8 Years)",
            "outlook_title": "9-Year Couple Outlook (Year-by-Year)",
            "outlook_sub": "Side-by-side comparison of Mahadasha, Antardasha, financial flow, and dispute/litigation windows for both partners.",
            "outlook_detail_title": "Detailed Year-by-Year Couple Guidance",
            "outlook_detail_sub": "Clear plain-language guidance for finance, relationship harmony, and health for each upcoming year.",
            "year": "Year",
            "money": "Money",
            "disputes": "Disputes",
            "rem_kicker": "Marriage-Saving Number Remedies (3 · 7 · 8)",
            "rem_title": "Focused Marriage-Saving Remedies",
            "rem_intro": "In match making, remedies focus strictly on missing or afflicted marriage-saving numbers (3, 7, and 8). General individual number remedies belong in each person's standalone birthdate report.",
            "who_do": "Who Should Perform This Remedy:",
            "both_partners": "Both {boy} & {girl}",
            "only_partner": "{name} Only",
            "reason_lbl": "Reason:",
            "neg_lbl": "Negative (-{n})",
            "miss_lbl": "Missing ({n})",
            "rem_none": "All marriage-saving numbers (3, 7, 8) are positively balanced in both natal grids — no targeted marriage-saving remedies are required.",
            "mantras": "Mantras & Practices",
            "seva": "Service (Seva)",
            "donations": "Donations",
            "colours_fasting": "Colours, Fasting & Crystal",
            "final_title": "Final recommendation & Supporting Crystals",
            "what_next": "What to do next",
            "next_1": "Review both partners' forward 9-year transit grids, Mahadasha cycles, and detailed couple outlook included in this report.",
            "next_2": "Discuss any weaker pillars or red/amber matching rules openly before finalizing the match.",
            "next_3": "Follow the assigned marriage-saving remedies (3, 7, 8) clearly marked for each partner and use the supporting crystals below.",
            "crystals_title": "Supporting Crystals for Couple Harmony",
            "disclaimer": "Disclaimer: Prepared using Vedic numerology for guidance. Report generated on",
        },
        "hi": {
            "report_sub": "विवाह मिलान रिपोर्ट (Match Making)",
            "kicker_top": "वैदिक अंकशास्त्र",
            "prepared_by": "द्वारा तैयार:",
            "prepared_for": "के लिए तैयार",
            "sub_pillars": "प्रत्येक 20 अंकों के पांच स्तंभ · वैदिक मिलान पद्धति",
            "the_two_grids": "दोनों जन्म कुंडली (Grids)",
            "boy_role": "वर · Boy",
            "girl_role": "वधू · Girl",
            "born": "जन्म",
            "age": "आयु",
            "basic": "मूलांक",
            "destiny": "भाग्यांक",
            "yogas_lbl": "योग:",
            "none": "कोई नहीं",
            "five_pillars": "पांच मुख्य स्तंभ (Five Pillars)",
            "rules_title": "मुख्य मिलान एवं अस्वीकृति नियम (Rules 1–8)",
            "matching_rules_title": "मुख्य मिलान नियम (अनुकूलता एवं सहयोग)",
            "rejection_rules_title": "मुख्य अस्वीकृति नियम एवं चेतावनी जांच",
            "why_important_lbl": "यह नियम क्यों महत्वपूर्ण है:",
            "couple_effect_lbl": "दंपति पर प्रभाव:",
            "status_ok": "अनुकूल / पास",
            "status_warn": "सावधानी",
            "status_reject": "अस्वीकृत / प्रतिकूल",
            "lit_title": "5-वर्षीय विवाद/मुकदमा जांच:",
            "lit_ok": "आगामी 5 वर्षों में किसी भी कुंडली में 2+ वर्ष का कानूनी विवाद योग सक्रिय नहीं है।",
            "lit_warn_pre": "विवाद योग सक्रिय — ",
            "lit_warn_post": "। निर्णय लेने से पहले सावधानीपूर्वक परामर्श करें।",
            "running": "वर्तमान",
            "grids_title": "आगामी 9-वर्षीय गोचर ग्रिड (वर्तमान से अगले 8 वर्ष)",
            "grids_sub": "वर्तमान वर्ष से शुरू होकर आगामी 9 वर्षों की महादशा (MD) और अंतर्दशा (AD) के साथ जन्म ग्रिड।",
            "dasha_title": "महादशा एवं सक्रिय अवधि",
            "cycle": "चक्र",
            "birth": "जन्म",
            "age45": "आयु 45",
            "age90": "आयु 90",
            "analysis_title": "ग्रिड विश्लेषण एवं योग",
            "active_yogas": "जन्म ग्रिड में सक्रिय योग (सकारात्मक / नकारात्मक और प्रभाव)",
            "yoga_pos": "सकारात्मक · शुभ",
            "yoga_neg": "नकारात्मक · चुनौतीपूर्ण",
            "yoga_mix": "मिश्रित ऊर्जा",
            "no_yogas": "कोई प्रमुख योग सक्रिय नहीं है।",
            "outlook_kicker": "संयुक्त समय तुलना (वर्तमान से अगले 8 वर्ष)",
            "outlook_title": "9-वर्षीय युगल भविष्यफल (वर्ष-वार)",
            "outlook_sub": "दोनों जीवनसाथी की महादशा, अंतर्दशा, आर्थिक स्थिति और विवाद की संभावनाओं की वर्ष-वार तुलना।",
            "outlook_detail_title": "विस्तृत वर्ष-वार युगल मार्गदर्शन",
            "outlook_detail_sub": "प्रत्येक आगामी वर्ष के लिए धन, दांपत्य सामंजस्य और स्वास्थ्य का स्पष्ट मार्गदर्शन।",
            "year": "वर्ष",
            "money": "धन",
            "disputes": "विवाद",
            "rem_kicker": "विवाह-रक्षक अंक उपाय (3 · 7 · 8)",
            "rem_title": "लक्षित विवाह-रक्षक उपाय",
            "rem_intro": "विवाह मिलान में केवल अनुपस्थित या पीड़ित विवाह-रक्षक अंकों (3, 7, 8) के उपाय दिए जाते हैं। अन्य व्यक्तिगत अंकों के उपाय व्यक्ति की अलग जन्मतिथि रिपोर्ट में होते हैं।",
            "who_do": "यह उपाय किसे करना है:",
            "both_partners": "{boy} और {girl} दोनों को",
            "only_partner": "केवल {name} को",
            "reason_lbl": "कारण:",
            "neg_lbl": "नकारात्मक (-{n})",
            "miss_lbl": "अनुपस्थित ({n})",
            "rem_none": "दोनों कुंडलियों में विवाह-रक्षक अंक (3, 7, 8) सकारात्मक रूप से संतुलित हैं — किसी विशेष उपाय की आवश्यकता नहीं है।",
            "mantras": "मंत्र एवं साधना",
            "seva": "सेवा",
            "donations": "दान",
            "colours_fasting": "रंग, उपवास एवं क्रिस्टल",
            "final_title": "अंतिम अनुशंसा एवं सहायक क्रिस्टल",
            "what_next": "आगे क्या करें",
            "next_1": "इस रिपोर्ट में दिए गए आगामी 9-वर्षीय गोचर ग्रिड, महादशा चक्र और विस्तृत युगल भविष्यफल की समीक्षा करें।",
            "next_2": "विवाह तय करने से पहले कमजोर स्तंभों या लाल/पीले नियमों पर खुलकर चर्चा करें।",
            "next_3": "प्रत्येक साथी के लिए स्पष्ट रूप से बताए गए विवाह-रक्षक उपाय (3, 7, 8) और सहायक क्रिस्टल अपनाएं।",
            "crystals_title": "दांपत्य सामंजस्य के लिए सहायक क्रिस्टल",
            "disclaimer": "अस्वीकरण: वैदिक अंकशास्त्र मार्गदर्शन के लिए है। रिपोर्ट तिथि:",
        },
        "gu": {
            "report_sub": "લગ્ન મિલાન રિપોર્ટ (Match Making)",
            "kicker_top": "વૈદિક અંકશાસ્ત્ર",
            "prepared_by": "દ્વારા તૈયાર:",
            "prepared_for": "માટે તૈયાર",
            "sub_pillars": "દરેક 20 ગુણના પાંચ સ્તંભ · વૈદિક મિલાન પદ્ધતિ",
            "the_two_grids": "બંને જન્મ કુંડળી (Grids)",
            "boy_role": "વર · Boy",
            "girl_role": "કન્યા · Girl",
            "born": "જન્મ",
            "age": "ઉંમર",
            "basic": "મૂળાંક",
            "destiny": "ભાગ્યાંક",
            "yogas_lbl": "યોગ:",
            "none": "કોઈ નહીં",
            "five_pillars": "પાંચ મુખ્ય સ્તંભ (Five Pillars)",
            "rules_title": "મુખ્ય મિલાન અને અસ્વીકૃતિ નિયમો (Rules 1–8)",
            "matching_rules_title": "મુખ્ય મિલાન નિયમો (અનુકૂળતા અને સહયોગ)",
            "rejection_rules_title": "મુખ્ય અસ્વીકૃતિ નિયમો અને ચેતવણી તપાસ",
            "why_important_lbl": "આ નિયમ કેમ મહત્વપૂર્ણ છે:",
            "couple_effect_lbl": "યુગલ પર અસર:",
            "status_ok": "અનુકૂળ / પાસ",
            "status_warn": "સાવચેતી",
            "status_reject": "અસ્વીકૃત / પ્રતિકૂળ",
            "lit_title": "5-વર્ષીય વિવાદ/કોર્ટ-કચેરી તપાસ:",
            "lit_ok": "આગામી 5 વર્ષમાં બંનેમાંથી કોઈની કુંડળીમાં 2+ વર્ષનો કાનૂની વિવાદ યોગ સક્રિય નથી.",
            "lit_warn_pre": "વિવાદ યોગ સક્રિય — ",
            "lit_warn_post": ". નિર્ણય લેતા પહેલા સાવચેતીપૂર્વક સલાહ લો.",
            "running": "ચાલુ",
            "grids_title": "આગામી 9-વર્ષીય ગોચર ગ્રીડ (વર્તમાનથી આવતા 8 વર્ષ)",
            "grids_sub": "ચાલુ વર્ષથી શરૂ થઈને આગામી 9 વર્ષની મહાદશા (MD) અને અંતર્દશા (AD) સાથે જન્મ ગ્રીડ.",
            "dasha_title": "મહાદશા અને સક્રિય સમયગાળો",
            "cycle": "ચક્ર",
            "birth": "જન્મ",
            "age45": "ઉંમર 45",
            "age90": "ઉંમર 90",
            "analysis_title": "ગ્રીડ વિશ્લેષણ અને યોગ",
            "active_yogas": "જન્મ ગ્રીડમાં સક્રિય યોગ (સકારાત્મક / નકારાત્મક અને અસર)",
            "yoga_pos": "સકારાત્મક · શુભ",
            "yoga_neg": "નકારાત્મક · પડકારજનક",
            "yoga_mix": "મિશ્ર ઊર્જા",
            "no_yogas": "કોઈ મુખ્ય યોગ સક્રિય નથી.",
            "outlook_kicker": "સંયુક્ત સમય તુલના (વર્તમાનથી આવતા 8 વર્ષ)",
            "outlook_title": "9-વર્ષીય યુગલ ભવિષ્યફળ (વર્ષ મુજબ)",
            "outlook_sub": "બંને જીવનસાથીની મહાદશા, અંતર્દશા, નાણાકીય પ્રવાહ અને વિવાદની શક્યતાઓની વર્ષ-વાર તુલના.",
            "outlook_detail_title": "વિગતવાર વર્ષ-વાર યુગલ માર્ગદર્શન",
            "outlook_detail_sub": "દરેક આગામી વર્ષ માટે ધન, દાંપત્ય સુમેળ અને સ્વાસ્થ્યનું સ્પષ્ટ માર્ગદર્શન.",
            "year": "વર્ષ",
            "money": "ધન",
            "disputes": "વિવાદ",
            "rem_kicker": "લગ્ન-રક્ષક અંક ઉપાયો (3 · 7 · 8)",
            "rem_title": "લક્ષિત લગ્ન-રક્ષક ઉપાયો",
            "rem_intro": "લગ્ન મિલાનમાં માત્ર ખૂટતા કે પીડિત લગ્ન-રક્ષક અંકો (3, 7, 8) ના જ ઉપાયો આપવામાં આવે છે. અન્ય વ્યક્તિગત અંકોના ઉપાયો દરેકની અલગ જન્મતારીખ રિપોર્ટમાં હોય છે.",
            "who_do": "આ ઉપાય કોણે કરવાનો છે:",
            "both_partners": "{boy} અને {girl} બંનેએ",
            "only_partner": "માત્ર {name} એ",
            "reason_lbl": "કારણ:",
            "neg_lbl": "નકારાત્મક (-{n})",
            "miss_lbl": "ખૂટતો ({n})",
            "rem_none": "બંને કુંડળીમાં લગ્ન-રક્ષક અંકો (3, 7, 8) સકારાત્મક રીતે સંતુલિત છે — કોઈ ખાસ ઉપાયની જરૂર નથી.",
            "mantras": "મંત્ર અને સાધના",
            "seva": "સેવા",
            "donations": "દાન",
            "colours_fasting": "રંગો, ઉપવાસ અને ક્રિસ્ટલ",
            "final_title": "અંતિમ ભલામણ અને સહાયક ક્રિસ્ટલ્સ",
            "what_next": "આગળ શું કરવું",
            "next_1": "આ રિપોર્ટમાં આપેલ આગામી 9-વર્ષીય ગોચર ગ્રીડ, મહાદશા ચક્ર અને વિગતવાર યુગલ ભવિષ્યફળ તપાસો.",
            "next_2": "લગ્ન નક્કી કરતા પહેલા નબળા સ્તંભો કે લાલ/પીળા નિયમો વિશે ખુલ્લી ચર્ચા કરો.",
            "next_3": "દરેક જીવનસાથી માટે સ્પષ્ટ દર્શાવેલા લગ્ન-રક્ષક ઉપાયો (3, 7, 8) અને સહાયક ક્રિસ્ટલ્સ અપનાવો.",
            "crystals_title": "દાંપત્ય સુમેળ માટે સહાયક ક્રિસ્ટલ્સ",
            "disclaimer": "અસ્વીકરણ: વૈદિક અંકશાસ્ત્ર માર્ગદર્શન માટે છે. રિપોર્ટ તારીખ:",
        },
    }
    ML = MM_STRINGS[lang]

    google_fonts = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap"
    if lang == "hi":
        google_fonts += "&family=Noto+Sans+Devanagari:wght@400;600;700"
        body_font = "'Noto Sans Devanagari', 'Source Sans 3', sans-serif"
        serif_font = "'Noto Sans Devanagari', 'Libre Baskerville', serif"
    elif lang == "gu":
        google_fonts += "&family=Noto+Sans+Gujarati:wght@400;600;700"
        body_font = "'Noto Sans Gujarati', 'Source Sans 3', sans-serif"
        serif_font = "'Noto Sans Gujarati', 'Libre Baskerville', serif"
    else:
        body_font = "'Source Sans 3', sans-serif"
        serif_font = "'Libre Baskerville', serif"

    arch_map = ARCHETYPES_BY_LANG.get(lang, ARCHETYPES_EN)
    crystals_list = SUPPORTING_CRYSTALS_BY_LANG.get(lang, SUPPORTING_CRYSTALS)

    consultant = m["consultant"]
    boy = m["boy"]
    girl = m["girl"]
    score = m["total_score"]
    verdict = m["verdict"]
    verdict_sub = m["verdict_sub"]
    level = m["verdict_level"]

    if lang == "hi":
        verdict = {"good": "उत्तम मिलान", "moderate": "विचारणीय मिलान", "low": "अनुशंसित नहीं"}.get(level, verdict)
        verdict_sub = {
            "good": "70% से अधिक — पांचों स्तंभों में मजबूत और शुभ सामंजस्य।",
            "moderate": "50–70% — संवाद और उपायों के साथ संतुलित एवं कार्यशील मिलान।",
            "low": "50% से कम — अंकशास्त्र के अनुसार यह मिलान उपयुक्त नहीं है।",
        }.get(level, verdict_sub)
    elif lang == "gu":
        verdict = {"good": "ઉત્તમ મિલાન", "moderate": "વિચારણીય મિલાન", "low": "ભલામણ કરેલ નથી"}.get(level, verdict)
        verdict_sub = {
            "good": "70% થી વધુ — પાંચેય સ્તંભોમાં મજબૂત અને શુભ સુમેળ.",
            "moderate": "50–70% — સભાન સંવાદ અને ઉપાયો સાથે ચાલી શકે તેવું મિલાન.",
            "low": "50% થી ઓછું — અંકશાસ્ત્ર મુજબ આ મિલાન યોગ્ય નથી.",
        }.get(level, verdict_sub)

    banner_bg = (
        "linear-gradient(90deg, #059669, #10b981)" if level == "good"
        else ("linear-gradient(90deg, #d97706, #f59e0b)" if level == "moderate"
              else "linear-gradient(90deg, #991b1b, #db2777)")
    )

    def _person_card(p: Dict[str, Any], role_lbl: str) -> str:
        cells_html = ""
        for c in p["grid"]["cells"]:
            val = c["str"] if c.get("count", 0) > 0 else ""
            cells_html += f'<div class="vg-cell"><div class="vg-planet">{GRID_PLANETS_EN.get(c["num"], "")}</div><div class="vg-num">{val}</div></div>'
        pills = ""
        for v in p["vibrations"]:
            sign = "+" if v["type"] == "+" else "−"
            cls = "pill-pos" if v["type"] == "+" else "pill-neg"
            pills += f'<span class="vpill {cls}">{sign}{v["number"]}</span>'
        y_names = ", ".join(y["name"].split("(")[0].strip() for y in p.get("yogas", [])[:3]) or ML["none"]
        bn_arch = arch_map.get(p["bn"], arch_map[1])[0]
        dn_arch = arch_map.get(p["dn"], arch_map[1])[0]
        return f"""
        <div class="mm-person">
            <div class="kicker">{role_lbl}</div>
            <div class="mm-pname">{p["name"]}</div>
            <div class="mm-pdob">{ML["born"]} {p["dob"]} · {ML["age"]} {p["age"]}</div>
            <div class="mm-grid-row">
                <div class="vg-grid vg-sm">{cells_html}</div>
                <div class="mm-stats">
                    <div><strong>{ML["basic"]} {p["bn"]}</strong> · {p["bn_planet"].split("(")[0].strip()}</div>
                    <div class="mm-arch">{bn_arch}</div>
                    <div style="margin-top:6px;"><strong>{ML["destiny"]} {p["dn"]}</strong> · {p["dn_planet"].split("(")[0].strip()}</div>
                    <div class="mm-arch">{dn_arch}</div>
                    <div style="margin-top:6px;">{pills}</div>
                </div>
            </div>
            <div class="mm-yogas"><strong>{ML["yogas_lbl"]}</strong> {y_names}</div>
        </div>"""

    pillars_html = ""
    pillar_title_tr = {
        "hi": {"emotional": "भावनात्मक सामंजस्य (Emotional Quotient)", "practical": "व्यावहारिक तालमेल (Practical Quotient)", "money": "आर्थिक अनुकूलता (Money Compatibility)", "root_destiny": "मूलांक एवं भाग्यांक मिलान", "marriage_saving": "विवाह-रक्षक अंक (+3, +7, +8)"},
        "gu": {"emotional": "ભાવનાત્મક સુમેળ (Emotional Quotient)", "practical": "વ્યવહારિક તાલમેલ (Practical Quotient)", "money": "આર્થિક સુસંગતતા (Money Compatibility)", "root_destiny": "મૂળાંક અને ભાગ્યાંક મિલાન", "marriage_saving": "લગ્ન-રક્ષક અંકો (+3, +7, +8)"},
    }
    for p in m["pillars"]:
        pct = int((p["score"] / p["max"]) * 100)
        bar_col = "#15803d" if p["score"] >= 15 else ("#d97706" if p["score"] >= 10 else "#cbd5e1")
        p_title = pillar_title_tr.get(lang, {}).get(p.get("key", ""), p["title"])
        pillars_html += f"""
        <div class="pillar-card">
            <div class="pillar-top">
                <div class="pillar-title">{p_title}</div>
                <div class="pillar-score">{p["score"]}<span class="pillar-max">/{p["max"]}</span></div>
            </div>
            <div class="pillar-bar-bg"><div class="pillar-bar-fill" style="width:{pct}%;background:{bar_col};"></div></div>
            <div class="pillar-desc">{p["desc"]}</div>
        </div>"""

    matching_rules_html = ""
    rejection_rules_html = ""
    for rc in m.get("rules_checks", []):
        st = rc["status"]
        cat = rc.get("category", "matching")
        is_rej = (cat == "rejection")
        icon = "✓" if st == "ok" else ("✕" if st == "reject" else "!")
        cls = ("rule-reject" if is_rej else ("rule-ok" if st == "ok" else ("rule-reject" if st == "reject" else "rule-warn")))
        box_cls = ("rule-box-reject" if is_rej else ("rule-box-ok" if st == "ok" else ("rule-box-reject" if st == "reject" else "rule-box-warn")))
        st_lbl = (
            (ML["status_reject"] if st == "reject" else ML["status_ok"])
            if is_rej else
            (ML["status_ok"] if st == "ok" else (ML["status_reject"] if st == "reject" else ML["status_warn"]))
        )
        why_html = f'<div style="font-size:9.6px;color:#334155;margin-top:4px;"><strong>{ML["why_important_lbl"]}</strong> {rc["why_important"]}</div>' if rc.get("why_important") else ""
        eff_html = f'<div style="font-size:9.6px;color:#0f172a;margin-top:2px;"><strong>{ML["couple_effect_lbl"]}</strong> {rc["couple_effect"]}</div>' if rc.get("couple_effect") else ""
        card_html = f"""
        <div class="rule-row {box_cls}" style="align-items:flex-start;break-inside:avoid;">
            <div class="rule-badge {cls}" style="margin-top:2px;">{icon}</div>
            <div style="flex:1;">
                <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;">
                    <strong>{rc["rule"]} · {rc["title"]}</strong>
                    <span class="rule-pill {box_cls}-pill">{st_lbl}</span>
                </div>
                <div class="sub-muted" style="margin-top:2px;">{rc["detail"]}</div>
                {why_html}
                {eff_html}
            </div>
        </div>"""
        if cat == "rejection":
            rejection_rules_html += card_html
        else:
            matching_rules_html += card_html

    lit = m.get("litigation_check", {})
    b_lit = lit.get("boy", {})
    g_lit = lit.get("girl", {})
    lit_items = []
    if b_lit.get("risk"):
        lit_items.append(f"{b_lit['name']}: {', '.join(b_lit['years'])}")
    if g_lit.get("risk"):
        lit_items.append(f"{g_lit['name']}: {', '.join(g_lit['years'])}")
    lit_html = (
        f'<div class="lit-warn"><strong>{ML["lit_title"]}</strong> {ML["lit_warn_pre"]}{"; ".join(lit_items)}{ML["lit_warn_post"]}</div>'
        if lit_items else
        f'<div class="lit-ok"><strong>{ML["lit_title"]}</strong> {ML["lit_ok"]}</div>'
    )

    rec_bg = "#f0fdf4" if level == "good" else ("#fffbeb" if level == "moderate" else "#fef2f2")
    rec_bd = "#bbf7d0" if level == "good" else ("#fde68a" if level == "moderate" else "#fecaca")
    rec_title = verdict

    boy_full = m.get("boy_full", {})
    girl_full = m.get("girl_full", {})
    boy_fwd = m.get("boy_forward_grids") or boy_full.get("dasha", {}).get("nine_year_grids", [])
    girl_fwd = m.get("girl_forward_grids") or girl_full.get("dasha", {}).get("nine_year_grids", [])

    def _year_grids_page(prof: Dict[str, Any], nyg: List[Dict[str, Any]], label: str) -> str:
        cards = ""
        for yg in nyg:
            is_run = yg.get("is_active", False)
            cls = "yg-card yg-running" if is_run else "yg-card"
            badge = f'<span class="running-badge">{ML["running"]}</span>' if is_run else ""
            c_html = ""
            for c in yg["cells"]:
                p_lbl = GRID_PLANETS_EN.get(c["num"], "")
                val = f'<span class="mg-nat">{c.get("natal_str", "")}</span><span class="mg-tr">{c.get("transit_str", "")}</span>'
                c_html += f'<div class="vg-cell"><div class="vg-planet">{p_lbl}</div><div class="vg-num">{val}</div></div>'
            cards += f"""
            <div class="{cls}">
                <div class="yg-year">{yg["year"]} {badge}</div>
                <div class="yg-dates">{yg["from_str"]} – {yg["to_str"]}</div>
                <div class="yg-dasha"><span class="md-txt">MD {yg["md"]}</span> <span class="ad-txt">AD {yg["ad"]}</span></div>
                <div class="vg-grid vg-mini">{c_html}</div>
            </div>"""
        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{label}</div>
            <h2 class="sec-h2">{prof["client"]["name"]} · {ML["grids_title"]}</h2>
            <p class="sub-muted" style="margin-bottom:10px;">{ML["grids_sub"]}</p>
            <div class="yg-matrix">{cards}</div>
        </div>"""

    def _dasha_page(prof: Dict[str, Any], label: str) -> str:
        d = prof.get("dasha", {})
        all_md = d.get("all_md_timeline", [])
        act_md = d.get("active_md", {})
        act_ad = d.get("active_ad", {})
        act_pd = d.get("active_pd", {})
        bar_html = "".join(
            f'<div class="md-seg" style="width:{(p["duration"]/90.0)*100:.2f}%;background:{NUM_COLORS.get(p["number"], "#6366f1")};">{p["number"]}</div>'
            for p in all_md[:18]
        )
        def _cycle_tbl(sl, cno):
            trs = ""
            for p in sl:
                ac = ' class="row-active"' if p.get("is_active") else ""
                trs += f'<tr{ac}><td class="bold-col">{p["number"]}</td><td>{p.get("start_dash", _fmt_dash(p["start_str"]))}</td><td>{p.get("end_dash", _fmt_dash(p["end_str"]))}</td><td>{p.get("start_age","")}–{p.get("end_age","")}</td></tr>'
            return f'<div><div class="cycle-title">{ML["cycle"]} {cno}</div><table class="clean-tbl"><thead><tr><th>MD</th><th>Start</th><th>End</th><th>Age</th></tr></thead><tbody>{trs}</tbody></table></div>'

        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{label}</div>
            <h2 class="sec-h2">{prof["client"]["name"]} · {ML["dasha_title"]}</h2>
            <div class="dasha-sum-row">
                <div class="ds-box"><span>Mahadasha</span><strong>{act_md.get("number","")}</strong><small>{_fmt_dash(act_md.get("start_str",""))} – {_fmt_dash(act_md.get("end_str",""))}</small></div>
                <div class="ds-box"><span>Antardasha</span><strong>{act_ad.get("ad_number","")}</strong><small>{_fmt_dash(act_ad.get("start_str",""))} – {_fmt_dash(act_ad.get("end_str",""))}</small></div>
                <div class="ds-box"><span>Pratyantar</span><strong>{act_pd.get("number","")}</strong><small>{_fmt_dash(act_pd.get("start_str",""))} – {_fmt_dash(act_pd.get("end_str",""))}</small></div>
            </div>
            <div class="md-bar">{bar_html}</div>
            <div class="md-bar-labels"><span>{ML["birth"]}</span><span>{ML["age45"]}</span><span>{ML["age90"]}</span></div>
            <div class="cycles-grid">{_cycle_tbl(all_md[:9], 1)}{_cycle_tbl(all_md[9:18], 2)}</div>
        </div>"""

    def _analysis_yogas_page(prof: Dict[str, Any], label: str) -> str:
        v_cards = ""
        for v in prof.get("vibrations", []):
            is_pos = (v["type"] == "+")
            cls = "ga-card ga-pos" if is_pos else "ga-card ga-neg"
            sign = "+" if is_pos else "−"
            cnt = v.get("count", 1)
            v_cards += f'<div class="{cls}"><div class="ga-head"><strong>{sign}{v["number"]}</strong> <span class="sub-muted">· {cnt}x</span></div><div class="ga-body">{v.get("text","")}</div></div>'
        y_cards = ""
        for y in prof.get("yogas", []):
            cat = y.get("category", "auspicious")
            if cat == "challenging":
                y_cls = "yoga-box yoga-neg"
                y_pill = f'<span class="ypill ypill-neg">{ML["yoga_neg"]}</span>'
            elif cat in ("mixed", "neutral"):
                y_cls = "yoga-box yoga-mix"
                y_pill = f'<span class="ypill ypill-mix">{ML["yoga_mix"]}</span>'
            else:
                y_cls = "yoga-box yoga-pos"
                y_pill = f'<span class="ypill ypill-pos">{ML["yoga_pos"]}</span>'
            desc_txt = f'<div class="yoga-desc">{y["desc"]}</div>' if y.get("desc") else ""
            pts = "".join(f"<li>{pt}</li>" for pt in y.get("points", [])[:4])
            y_cards += f'<div class="{y_cls}"><div class="yoga-hdr"><span class="yoga-title">{y["name"]}</span>{y_pill}</div>{desc_txt}{f"<ul class=yoga-pts>{pts}</ul>" if pts else ""}</div>'
        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{label}</div>
            <h2 class="sec-h2">{prof["client"]["name"]} · {ML["analysis_title"]}</h2>
            <div class="ga-grid">{v_cards}</div>
            <h3 class="sec-h3">{ML["active_yogas"]}</h3>
            <div class="yoga-grid">{y_cards or f"<div class=sub-muted>{ML['no_yogas']}</div>"}</div>
        </div>"""

    def _joint_outlook_pages() -> str:
        g_by_yr = {x["year"]: x for x in girl_fwd}
        rows = ""
        detail_cards = []
        for bx in boy_fwd:
            yr = bx["year"]
            gx = g_by_yr.get(yr, {})
            is_act = bx.get("is_active", False)
            ac = ' class="row-active"' if is_act else ""
            b_m_k, b_m_v = bx["money"]
            b_d_k, b_d_v = bx["disputes"]
            b_h_k, b_h_v = bx["health"]
            g_m_k, g_m_v = gx.get("money", ("", "–"))
            g_d_k, g_d_v = gx.get("disputes", ("", "–"))
            g_h_k, g_h_v = gx.get("health", ("", "–"))
            rows += f"""
            <tr{ac}>
                <td class="bold-col">{yr}</td>
                <td>MD {bx["md"]} / AD {bx["ad"]}</td>
                <td>{b_m_v}</td>
                <td>{b_d_v}</td>
                <td>MD {gx.get("md","–")} / AD {gx.get("ad","–")}</td>
                <td>{g_m_v}</td>
                <td>{g_d_v}</td>
            </tr>"""

            if lang == "hi":
                fin_note = (
                    "दोनों के लिए आर्थिक उन्नति और बचत का उत्तम वर्ष — बड़े निवेश व संयुक्त लक्ष्यों के लिए अनुकूल।"
                    if (b_m_k == "up" and g_m_k == "up") else
                    ("खर्च और बजट पर नियंत्रण रखें; जोखिम भरे निवेश से बचें।" if ("tight" in (b_m_k, g_m_k)) else "संतुलित आर्थिक वर्ष — नियमित बचत बनाए रखें।")
                )
                disp_note = (
                    "संवाद में धैर्य और पारदर्शिता रखें; अहंकार या कानूनी विवाद से बचें।"
                    if (b_d_k == "friction" or g_d_k == "friction") else
                    "रिश्ते में सहज सामंजस्य और शांतिपूर्ण तालमेल रहेगा।"
                )
                hlth_note = f"{boy['name']}: {b_h_v if b_h_v != '–' else 'सामान्य'} · {girl['name']}: {g_h_v if g_h_v != '–' else 'सामान्य'}"
                fin_lbl, rel_lbl, hlth_lbl = "आर्थिक स्थिति:", "दांपत्य एवं संवाद:", "स्वास्थ्य एवं ध्यान:"
            elif lang == "gu":
                fin_note = (
                    "બંને માટે આર્થિક પ્રગતિ અને બચતનું ઉત્તમ વર્ષ — મોટા રોકાણ અને સંયુક્ત લક્ષ્યો માટે શુભ."
                    if (b_m_k == "up" and g_m_k == "up") else
                    ("ખર્ચ અને બજેટ પર કાબૂ રાખવો; જોખમી રોકાણ ટાળવું." if ("tight" in (b_m_k, g_m_k)) else "સંતુલિત આર્થિક વર્ષ — નિયમિત બચત જાળવી રાખવી.")
                )
                disp_note = (
                    "સંવાદમાં ધીરજ અને પારદર્શિતા રાખવી; અહંકાર કે કાનૂની મતભેદથી દૂર રહેવું."
                    if (b_d_k == "friction" or g_d_k == "friction") else
                    "સંબંધમાં સહજ સુમેળ અને શાંતિપૂર્ણ તાલમેલ જળવાશે."
                )
                hlth_note = f"{boy['name']}: {b_h_v if b_h_v != '–' else 'સામાન્ય'} · {girl['name']}: {g_h_v if g_h_v != '–' else 'સામાન્ય'}"
                fin_lbl, rel_lbl, hlth_lbl = "આર્થિક સ્થિતિ:", "દાંપત્ય અને સંવાદ:", "સ્વાસ્થ્ય અને કાળજી:"
            else:
                fin_note = (
                    "Strong joint financial growth year — favourable for savings, career expansion, and shared investments."
                    if (b_m_k == "up" and g_m_k == "up") else
                    ("Keep a disciplined budget and avoid speculative or high-risk investments this year." if ("tight" in (b_m_k, g_m_k)) else "Steady, balanced financial year — maintain consistent savings.")
                )
                disp_note = (
                    "Practice extra patience and transparent communication; avoid ego clashes or unclear commitments."
                    if (b_d_k == "friction" or g_d_k == "friction") else
                    "Smooth relational harmony with low risk of disputes or friction."
                )
                hlth_note = f"{boy['name']}: {b_h_v if b_h_v != '–' else 'Stable'} · {girl['name']}: {g_h_v if g_h_v != '–' else 'Stable'}"
                fin_lbl, rel_lbl, hlth_lbl = "Finance & Growth:", "Relationship & Harmony:", "Health & Care:"

            run_pill = f' <span class="running-badge">{ML["running"]}</span>' if is_act else ""
            detail_cards.append(f"""
            <div class="outlook-card {'outlook-act' if is_act else ''}">
                <div class="oc-hdr">
                    <strong>{yr}{run_pill}</strong>
                    <span class="sub-muted">{boy["name"]}: MD {bx["md"]}/AD {bx["ad"]} · {girl["name"]}: MD {gx.get("md","–")}/AD {gx.get("ad","–")}</span>
                </div>
                <div class="oc-line"><strong>{fin_lbl}</strong> {fin_note}</div>
                <div class="oc-line"><strong>{rel_lbl}</strong> {disp_note}</div>
                <div class="oc-line"><strong>{hlth_lbl}</strong> {hlth_note}</div>
            </div>""")

        p1_cards = "".join(detail_cards[:3])
        p2_cards = "".join(detail_cards[3:])
        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{ML["outlook_kicker"]}</div>
            <h2 class="sec-h2">{ML["outlook_title"]}</h2>
            <p class="sub-muted" style="margin-bottom:8px;">{ML["outlook_sub"]}</p>
            <table class="clean-tbl">
                <thead>
                    <tr>
                        <th>{ML["year"]}</th>
                        <th>{boy["name"]} (MD/AD)</th><th>{ML["money"]}</th><th>{ML["disputes"]}</th>
                        <th>{girl["name"]} (MD/AD)</th><th>{ML["money"]}</th><th>{ML["disputes"]}</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
            <h3 class="sec-h3" style="margin-top:12px;">{ML["outlook_detail_title"]}</h3>
            <p class="sub-muted" style="margin-bottom:8px;">{ML["outlook_detail_sub"]}</p>
            {p1_cards}
        </div>
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{ML["outlook_kicker"]}</div>
            <h2 class="sec-h2">{ML["outlook_detail_title"]} (cont.)</h2>
            {p2_cards}
        </div>"""

    def _marriage_saving_remedies_page() -> str:
        from vedic_translations import NUMBER_REMEDIES, PLANET_INFO

        ms_roles = {
            "en": {
                3: "Communication Harmony, Wisdom & Family Peace",
                7: "Spiritual Bonding, Trust & Emotional Depth",
                8: "Discipline, Patience & Long-Term Commitment",
            },
            "hi": {
                3: "संवाद सामंजस्य, ज्ञान एवं पारिवारिक शांति",
                7: "आध्यात्मिक जुड़ाव, विश्वास एवं भावनात्मक गहराई",
                8: "अनुशासन, धैर्य एवं दीर्घकालिक समर्पण",
            },
            "gu": {
                3: "સંવાદ સુમેળ, જ્ઞાન અને પારિવારિક શાંતિ",
                7: "આધ્યાત્મિક જોડાણ, વિશ્વાસ અને ભાવનાત્મક ઊંડાણ",
                8: "શિસ્ત, ધીરજ અને લાંબા ગાળાનું સમર્પણ",
            },
        }[lang]
        b_vibs = {f'{v["type"]}{v["number"]}' for v in boy.get("vibrations", [])}
        g_vibs = {f'{v["type"]}{v["number"]}' for v in girl.get("vibrations", [])}

        def _status_for(vibs: set, num: int) -> str:
            if f"-{num}" in vibs:
                return ML["neg_lbl"].format(n=num)
            if f"+{num}" not in vibs:
                return ML["miss_lbl"].format(n=num)
            return ""

        cards = ""
        for num in (3, 7, 8):
            b_issue = _status_for(b_vibs, num)
            g_issue = _status_for(g_vibs, num)
            if not b_issue and not g_issue:
                continue

            if b_issue and g_issue:
                who_str = ML["both_partners"].format(boy=boy["name"], girl=girl["name"])
            elif b_issue:
                who_str = ML["only_partner"].format(name=boy["name"])
            else:
                who_str = ML["only_partner"].format(name=girl["name"])

            reasons = []
            if b_issue:
                reasons.append(f"{boy['name']}: {b_issue}")
            if g_issue:
                reasons.append(f"{girl['name']}: {g_issue}")
            reason_str = " · ".join(reasons)

            rem = NUMBER_REMEDIES.get(num, {})
            pinfo = PLANET_INFO.get(num, {}).get(lang, PLANET_INFO.get(num, {}).get("en", {}))
            planet_name = pinfo.get("planet", f"Planet {num}")
            colors = pinfo.get("colors", "")
            mantra = rem.get("mantra", {}).get(lang, rem.get("mantra", {}).get("en", ""))
            seva = rem.get("seva", {}).get(lang, rem.get("seva", {}).get("en", ""))
            donation = rem.get("donation", {}).get(lang, rem.get("donation", {}).get("en", ""))
            fasting = rem.get("fasting", {}).get(lang, rem.get("fasting", {}).get("en", ""))
            crystal = rem.get("crystal", {}).get(lang, rem.get("crystal", {}).get("en", ""))

            cards += f"""
            <div class="rem-card">
                <div class="rem-head">
                    <span class="rem-circle">{num}</span>
                    <div>
                        <div class="rem-title">Number {num} · {planet_name} <span style="font-weight:400;color:#64748b;">({ms_roles[num]})</span></div>
                    </div>
                </div>
                <div class="who-box">
                    <strong>{ML["who_do"]} {who_str}</strong><br>
                    <span class="sub-muted">{ML["reason_lbl"]} {reason_str}</span>
                </div>
                <div class="rem-sec-lbl">{ML["mantras"]}</div><p class="rem-p">{mantra}</p>
                <div class="rem-sec-lbl">{ML["seva"]}</div><p class="rem-p">{seva}</p>
                <div class="rem-sec-lbl">{ML["donations"]}</div><p class="rem-p">{donation}</p>
                <div class="rem-sec-lbl">{ML["colours_fasting"]}</div><p class="rem-p">{colors} · {fasting} · Crystal: {crystal}</p>
            </div>"""

        if not cards:
            cards = f'<div class="sub-muted">{ML["rem_none"]}</div>'

        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{ML["rem_kicker"]}</div>
            <h2 class="sec-h2">{boy["name"]} &amp; {girl["name"]} · {ML["rem_title"]}</h2>
            <p class="sub-muted" style="margin-bottom:10px;">{ML["rem_intro"]}</p>
            <div class="rem-grid">{cards}</div>
        </div>"""

    crystals_html = "".join(
        f'<div class="crystal-row"><strong>{cn}</strong> — <span class="sub-muted">{cd}</span></div>'
        for cn, cd in crystals_list
    )

    extra_pages_html = ""
    if boy_full and girl_full:
        extra_pages_html = (
            _year_grids_page(boy_full, boy_fwd, ML["boy_role"])
            + _year_grids_page(girl_full, girl_fwd, ML["girl_role"])
            + _dasha_page(boy_full, ML["boy_role"])
            + _dasha_page(girl_full, ML["girl_role"])
            + _analysis_yogas_page(boy_full, ML["boy_role"])
            + _analysis_yogas_page(girl_full, ML["girl_role"])
            + _joint_outlook_pages()
            + _marriage_saving_remedies_page()
        )

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{consultant["name"]} - {ML["report_sub"]} - {boy["name"]} &amp; {girl["name"]}</title>
<link href="{google_fonts}" rel="stylesheet">
<style>
@page {{ size: A4 portrait; margin: 12mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: {body_font}; color: #1e293b; font-size: 11px; line-height: 1.45; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.sheet {{ border: 1px solid #e2e8f0; border-radius: 14px; padding: 18px 20px; margin-bottom: 12px; background: #fff; }}
.page-break {{ page-break-before: always; break-before: page; }}
.mm-head {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px; border-bottom: 2px solid; border-image: linear-gradient(90deg, #7c3aed, #f59e0b) 1; margin-bottom: 12px; }}
.mm-brand {{ font-family: {serif_font}; font-size: 15px; font-weight: 700; color: #0f172a; }}
.mm-rtitle {{ text-align: right; font-size: 10px; color: #64748b; }}
.mm-rtitle strong {{ display: block; font-family: {serif_font}; font-size: 13px; color: #0f172a; }}
.kicker {{ font-family: {serif_font}; font-style: italic; font-size: 10.5px; color: #7c3aed; }}
.couple-name {{ font-family: {serif_font}; font-size: 22px; font-weight: 700; color: #0f172a; margin: 2px 0; }}
.sub-muted {{ font-size: 10.5px; color: #64748b; }}
.score-banner {{ background: {banner_bg}; color: #fff; border-radius: 12px; padding: 14px 18px; display: flex; align-items: center; gap: 18px; margin-bottom: 12px; }}
.score-big {{ font-family: {serif_font}; font-size: 28px; font-weight: 700; line-height: 1; }}
.score-big span {{ font-size: 14px; opacity: 0.85; }}
.score-verdict {{ font-family: {serif_font}; font-size: 16px; font-weight: 700; }}
.score-sub {{ font-size: 10.5px; opacity: 0.92; }}
.sec-h2 {{ font-family: {serif_font}; font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 10px 0; }}
.mm-two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
.mm-person {{ background: #f8f7ff; border: 1px solid #ede9fe; border-radius: 10px; padding: 12px; }}
.mm-pname {{ font-family: {serif_font}; font-size: 15px; font-weight: 700; color: #0f172a; }}
.mm-pdob {{ font-size: 10px; color: #64748b; margin-bottom: 8px; }}
.mm-grid-row {{ display: flex; gap: 10px; align-items: flex-start; }}
.vg-grid.vg-sm {{ display: grid; grid-template-columns: repeat(3, 44px); grid-template-rows: repeat(3, 36px); border: 1.5px solid #c9a96e; background: #fff; flex-shrink: 0; }}
.vg-cell {{ border: 0.5px solid #e2d1a8; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 1px; }}
.vg-planet {{ font-size: 6.5px; color: #b48a3e; }}
.vg-num {{ font-family: {serif_font}; font-size: 11px; font-weight: 700; color: #0f172a; }}
.mm-stats {{ font-size: 10px; color: #1e293b; flex: 1; }}
.mm-arch {{ font-size: 9.5px; color: #64748b; }}
.mm-yogas {{ font-size: 9.5px; color: #334155; margin-top: 8px; }}
.vpill {{ display: inline-block; font-size: 9px; font-weight: 700; padding: 1px 6px; border-radius: 999px; margin-right: 3px; }}
.pill-pos {{ background: #dcfce7; color: #166534; }}
.pill-neg {{ background: #fee2e2; color: #991b1b; }}
.pillar-card {{ border: 1px solid #e2e8f0; border-radius: 8px; padding: 9px 12px; margin-bottom: 8px; }}
.pillar-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }}
.pillar-title {{ font-family: {serif_font}; font-size: 12px; font-weight: 700; color: #0f172a; }}
.pillar-score {{ font-family: {serif_font}; font-size: 13px; font-weight: 700; color: #15803d; }}
.pillar-max {{ font-size: 10px; color: #64748b; }}
.pillar-bar-bg {{ height: 5px; background: #e2e8f0; border-radius: 999px; overflow: hidden; margin-bottom: 5px; }}
.pillar-bar-fill {{ height: 100%; border-radius: 999px; }}
.pillar-desc {{ font-size: 10px; color: #475569; }}
.rule-row {{ display: flex; gap: 10px; align-items: center; padding: 7px 10px; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 6px; }}
.rule-box-ok {{ background: #f0fdf4; border-color: #bbf7d0; }}
.rule-box-warn {{ background: #fffbeb; border-color: #fde68a; }}
.rule-box-reject {{ background: #fef2f2; border-color: #fecaca; }}
.rule-pill {{ font-size: 8.5px; font-weight: 700; padding: 1px 7px; border-radius: 999px; flex-shrink: 0; }}
.rule-box-ok-pill {{ background: #dcfce7; color: #166534; }}
.rule-box-warn-pill {{ background: #fef3c7; color: #92400e; }}
.rule-box-reject-pill {{ background: #fee2e2; color: #991b1b; }}
.rule-badge {{ width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 11px; color: #fff; flex-shrink: 0; }}
.rule-ok {{ background: #15803d; }}
.rule-warn {{ background: #d97706; }}
.rule-reject {{ background: #b91c1c; }}
.lit-ok {{ background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 8px 12px; font-size: 10px; color: #166534; margin-top: 8px; }}
.lit-warn {{ background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 8px 12px; font-size: 10px; color: #991b1b; margin-top: 8px; }}
.yg-matrix {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
.yg-card {{ border: 1px solid #e2e8f0; border-radius: 10px; padding: 8px 10px; text-align: center; background: #fff; }}
.yg-card.yg-running {{ border: 2px solid #7c3aed; background: #fdfcff; }}
.yg-year {{ font-family: {serif_font}; font-size: 13px; font-weight: 700; color: #0f172a; }}
.running-badge {{ background: #7c3aed; color: #fff; font-size: 8.5px; font-weight: 700; padding: 1px 6px; border-radius: 999px; margin-left: 4px; }}
.yg-dates {{ font-size: 8.8px; color: #64748b; margin: 2px 0; }}
.yg-dasha {{ font-size: 9.5px; font-weight: 700; }}
.md-txt {{ color: #0f766e; }}
.ad-txt {{ color: #b45309; margin-left: 4px; }}
.vg-grid.vg-mini {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(3, 34px); border: 1.5px solid #c9a96e; background: #fff; margin-top: 6px; }}
.mg-nat {{ color: #0f172a; }}
.mg-tr {{ color: #d97706; }}
.dasha-sum-row {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; }}
.ds-box {{ background: #f8f7ff; border: 1px solid #ede9fe; border-radius: 8px; padding: 8px 12px; }}
.ds-box span {{ display: block; font-size: 9.5px; color: #64748b; }}
.ds-box strong {{ display: block; font-family: {serif_font}; font-size: 18px; color: #7c3aed; }}
.ds-box small {{ font-size: 9.5px; color: #475569; }}
.md-bar {{ display: flex; height: 18px; border-radius: 999px; overflow: hidden; margin: 8px 0 4px 0; }}
.md-seg {{ color: #fff; font-size: 8.5px; font-weight: 700; display: flex; align-items: center; justify-content: center; }}
.md-bar-labels {{ display: flex; justify-content: space-between; font-size: 9.5px; color: #64748b; margin-bottom: 12px; }}
.cycles-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }}
.cycle-title {{ font-size: 11px; font-weight: 700; margin-bottom: 4px; }}
.clean-tbl {{ width: 100%; border-collapse: collapse; font-size: 9.5px; }}
.clean-tbl th {{ text-align: left; color: #64748b; border-bottom: 1px solid #cbd5e1; padding: 4px; }}
.clean-tbl td {{ padding: 4px; border-bottom: 1px solid #f1f5f9; }}
.bold-col {{ font-weight: 700; color: #0f172a; }}
.row-active td {{ background: #f5f3ff; font-weight: 700; }}
.ga-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px; }}
.ga-card {{ border-radius: 8px; padding: 8px 10px; border-left: 3.5px solid; }}
.ga-pos {{ background: #f0fdf4; border-left-color: #16a34a; }}
.ga-neg {{ background: #fef2f2; border-left-color: #b91c1c; }}
.ga-body {{ font-size: 9.5px; color: #334155; }}
.yoga-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.yoga-box {{ border: 1px solid #e5d5a7; background: #fffdf7; border-radius: 8px; padding: 8px 10px; break-inside: avoid; }}
.yoga-box.yoga-pos {{ border-color: #86efac; background: #f0fdf4; }}
.yoga-box.yoga-neg {{ border-color: #fca5a5; background: #fef2f2; }}
.yoga-box.yoga-mix {{ border-color: #fcd34d; background: #fffbeb; }}
.yoga-hdr {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 6px; margin-bottom: 4px; }}
.yoga-title {{ font-family: {serif_font}; font-size: 10.8px; font-weight: 700; color: #0f172a; }}
.ypill {{ font-size: 8px; font-weight: 700; padding: 1px 6px; border-radius: 999px; white-space: nowrap; flex-shrink: 0; }}
.ypill-pos {{ background: #dcfce7; color: #166534; }}
.ypill-neg {{ background: #fee2e2; color: #991b1b; }}
.ypill-mix {{ background: #fef3c7; color: #92400e; }}
.yoga-desc {{ font-size: 9.3px; color: #334155; line-height: 1.38; margin-bottom: 3px; }}
.yoga-pts {{ margin: 3px 0 0 14px; padding: 0; font-size: 9.1px; color: #334155; }}
.outlook-card {{ border: 1px solid #e2e8f0; border-radius: 8px; padding: 8px 11px; margin-bottom: 7px; background: #fff; break-inside: avoid; }}
.outlook-card.outlook-act {{ border: 1.5px solid #7c3aed; background: #faf8ff; }}
.oc-hdr {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; font-size: 11px; }}
.oc-line {{ font-size: 9.8px; color: #334155; margin-bottom: 2px; line-height: 1.38; }}
.rem-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.rem-card {{ border: 1px solid #e2e8f0; border-radius: 10px; padding: 9px 11px; break-inside: avoid; }}
.rem-head {{ display: flex; align-items: center; gap: 8px; margin-bottom: 5px; }}
.rem-circle {{ width: 22px; height: 22px; border-radius: 50%; background: #f5f3ff; color: #7c3aed; font-weight: 700; font-size: 10.5px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; }}
.rem-title {{ font-family: {serif_font}; font-size: 11.2px; font-weight: 700; }}
.who-box {{ background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 5px 8px; margin-bottom: 6px; font-size: 9.8px; color: #991b1b; }}
.rem-sec-lbl {{ font-size: 9.5px; font-weight: 700; color: #7c3aed; margin-top: 4px; }}
.rem-p {{ font-size: 9.3px; color: #334155; margin: 1px 0; }}
.crystal-row {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 6px 10px; margin-bottom: 5px; font-size: 10px; }}
.sec-h3 {{ font-family: {serif_font}; font-size: 13.5px; font-weight: 700; margin: 12px 0 8px 0; }}
.rec-box {{ background: {rec_bg}; border: 1px solid {rec_bd}; border-radius: 10px; padding: 12px 14px; margin-bottom: 10px; }}
.rec-title {{ font-family: {serif_font}; font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px; }}
.next-box {{ border: 1px solid #e2e8f0; border-radius: 10px; padding: 10px 14px; }}
.next-box ol {{ margin: 6px 0 0 16px; padding: 0; font-size: 10.5px; color: #334155; }}
.next-box li {{ margin-bottom: 3px; }}
.mm-foot {{ text-align: center; font-size: 9.5px; color: #64748b; margin-top: 10px; }}
</style>
</head>
<body>
<div class="sheet">
    <div class="mm-head">
        <div>
            <div class="mm-brand">{ML["prepared_by"]} {consultant["name"]}</div>
            <div class="sub-muted">{consultant.get("title", "")} · {consultant["phone"]} · {consultant["email"]}</div>
        </div>
        <div class="mm-rtitle">{ML["kicker_top"]} <strong>{ML["report_sub"]}</strong></div>
    </div>
    <div class="kicker">{ML["prepared_for"]}</div>
    <div class="couple-name">{boy["name"]} &amp; {girl["name"]}</div>
    <div class="sub-muted">{ML["sub_pillars"]}</div>
</div>

<div class="score-banner">
    <div class="score-big">{score}<span>/100</span></div>
    <div>
        <div class="score-verdict">{verdict}</div>
        <div class="score-sub">{verdict_sub}</div>
    </div>
</div>

<div class="sheet">
    <h2 class="sec-h2">{ML["the_two_grids"]}</h2>
    <div class="mm-two">
        {_person_card(boy, ML["boy_role"])}
        {_person_card(girl, ML["girl_role"])}
    </div>
</div>

<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">{ML["five_pillars"]}</h2>
    {pillars_html}
</div>

<div class="page-break"></div>
<div class="sheet" style="border-color:#bbf7d0;">
    <h2 class="sec-h2" style="color:#15803d;">✓ {ML["matching_rules_title"]}</h2>
    {matching_rules_html}
</div>

<div class="sheet" style="border-color:#fecaca;">
    <h2 class="sec-h2" style="color:#b91c1c;">⛔ {ML["rejection_rules_title"]}</h2>
    {rejection_rules_html}
    {lit_html}
</div>

{extra_pages_html}

<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">{ML["final_title"]}</h2>
    <div class="rec-box">
        <div class="rec-title">{rec_title}</div>
        <div><strong>{boy["name"]}</strong> &amp; <strong>{girl["name"]}</strong> — <strong>{score}/100</strong>.</div>
    </div>
    <div class="next-box">
        <strong>{ML["what_next"]}</strong>
        <ol>
            <li>{ML["next_1"]}</li>
            <li>{ML["next_2"]}</li>
            <li>{ML["next_3"]}</li>
        </ol>
    </div>
    <h3 class="sec-h3">{ML["crystals_title"]}</h3>
    {crystals_html}
    <div class="mm-foot">
        <div>{ML["disclaimer"]} {m["generated_on"]}.</div>
        <div style="margin-top:3px;">{ML["prepared_by"]} {consultant["name"]} · {consultant["phone"]} · {consultant["email"]}</div>
    </div>
</div>
</body>
</html>"""


def build_business_partnership_html(b: Dict[str, Any]) -> str:
    """
    Constructs a clean, white, editorial-grade Business Partnership Numerology Report
    for 1, 2, 3, or N partners in English, Hindi, or Gujarati.
    """
    lang = b.get("lang", "en")
    if lang not in ("en", "hi", "gu"):
        lang = "en"

    BL = {
        "en": {
            "kicker_top": "Vedic Business Numerology",
            "report_sub": "Business Partnership Report",
            "prepared_by": "Prepared by",
            "prepared_for": "Prepared for",
            "partners_lbl": "Partners Evaluated:",
            "anchor_title": "Strongest Anchor Partner & Business Leadership Recommendation",
            "team_cov": "Collective Team Grid Coverage",
            "covered": "Present Positive Numbers:",
            "missing": "Shared Missing Numbers (Blind Spots):",
            "none": "None",
            "partner_cards": "Partner Charts, Dashas & Assigned Business Roles",
            "born": "Born",
            "basic": "Basic",
            "destiny": "Destiny",
            "strength": "Business Strength",
            "role": "Recommended Role:",
            "dasha": "Active Dasha:",
            "yogas": "Active Yogas:",
            "pairwise_title": "Pairwise Partner Compatibility Matrix",
            "pair_strong": "Strong Synergy",
            "pair_mod": "Balanced / Role Split",
            "pair_fric": "Requires Structure",
            "biz_title": "Common Recommended Businesses & Professions Together",
            "biz_sub": "Industries where your combined planetary strengths, Yogas, and active Dashas generate the highest growth together.",
            "backed_by": "Supported by:",
            "namank_title": "Best Business Name Numbers (Namank) & Firm Audit",
            "best_namank": "Most Auspicious Business Name Numbers:",
            "firm_audit": "Evaluated Business Name:",
            "ausp": "Auspicious for Team",
            "adj": "Consider Spelling Adjustment",
            "outlook_title": "5-Year Joint Business & Dasha Outlook (Current to +4 Years)",
            "year": "Year",
            "running": "Running",
            "rem_title": "Focused Business Growth Remedies (For Shared Blind Spots)",
            "rem_none": "Your combined team covers all core business numbers (1, 3, 5, 6, 8) — no shared business-number remedies needed.",
            "crystals": "Supporting Crystals for Business Prosperity",
            "disclaimer": "Disclaimer: Prepared using Vedic numerology for business guidance. Report generated on",
        },
        "hi": {
            "kicker_top": "वैदिक व्यापार अंकशास्त्र",
            "report_sub": "बिजनेस पार्टनरशिप रिपोर्ट",
            "prepared_by": "द्वारा तैयार:",
            "prepared_for": "के लिए तैयार",
            "partners_lbl": "कुल साझेदार:",
            "anchor_title": "सबसे मजबूत एंकर पार्टनर एवं नेतृत्व अनुशंसा",
            "team_cov": "सामूहिक टीम ग्रिड विश्लेषण",
            "covered": "टीम में सकारात्मक अंक:",
            "missing": "साझा अनुपस्थित अंक (कमजोरियाँ):",
            "none": "कोई नहीं",
            "partner_cards": "साझेदारों के चार्ट, दशा और व्यापारिक भूमिकाएँ",
            "born": "जन्म",
            "basic": "मूलांक",
            "destiny": "भाग्यांक",
            "strength": "व्यापारिक शक्ति",
            "role": "उपयुक्त भूमिका:",
            "dasha": "सक्रिय दशा:",
            "yogas": "सक्रिय योग:",
            "pairwise_title": "परस्पर साझेदार अनुकूलता मैट्रिक्स",
            "pair_strong": "मजबूत तालमेल",
            "pair_mod": "संतुलित / स्पष्ट भूमिका",
            "pair_fric": "सावधानी एवं अनुबंध",
            "biz_title": "एक साथ करने योग्य सर्वोत्तम व्यवसाय एवं उद्योग",
            "biz_sub": "वे क्षेत्र जहाँ आपकी संयुक्त ग्रह शक्ति, योग और सक्रिय दशाएँ सर्वाधिक लाभ देती हैं।",
            "backed_by": "सहायक साझेदार:",
            "namank_title": "सर्वोत्तम व्यवसाय नामांक (Namank) एवं फर्म जांच",
            "best_namank": "शुभ व्यवसाय नामांक:",
            "firm_audit": "प्रस्तावित फर्म नाम:",
            "ausp": "टीम के लिए शुभ",
            "adj": "स्पेलिंग सुधार पर विचार करें",
            "outlook_title": "आगामी 5-वर्षीय संयुक्त व्यापारिक दृष्टिकोण",
            "year": "वर्ष",
            "running": "वर्तमान",
            "rem_title": "व्यापारिक वृद्धि उपाय (साझा अनुपस्थित अंकों के लिए)",
            "rem_none": "आपकी टीम में सभी प्रमुख व्यापारिक अंक (1, 3, 5, 6, 8) मौजूद हैं — अतिरिक्त उपाय की आवश्यकता नहीं।",
            "crystals": "व्यापारिक समृद्धि के लिए सहायक क्रिस्टल",
            "disclaimer": "अस्वीकरण: वैदिक अंकशास्त्र व्यापारिक मार्गदर्शन के लिए है। रिपोर्ट तिथि:",
        },
        "gu": {
            "kicker_top": "વૈદિક વ્યાપાર અંકશાસ્ત્ર",
            "report_sub": "બિઝનેસ પાર્ટનરશિપ રિપોર્ટ",
            "prepared_by": "દ્વારા તૈયાર:",
            "prepared_for": "માટે તૈયાર",
            "partners_lbl": "કુલ ભાગીદારો:",
            "anchor_title": "સૌથી મજબૂત એન્કર પાર્ટનર અને નેતૃત્વ ભલામણ",
            "team_cov": "સામૂહિક ટીમ ગ્રીડ વિશ્લેષણ",
            "covered": "ટીમમાં સકારાત્મક અંકો:",
            "missing": "સામૂહિક ખૂટતા અંકો (નબળાઈ):",
            "none": "કોઈ નહીં",
            "partner_cards": "ભાગીદારોના ચાર્ટ, દશા અને વ્યાપારિક ભૂમિકા",
            "born": "જન્મ",
            "basic": "મૂળાંક",
            "destiny": "ભાગ્યાંક",
            "strength": "વ્યાપારિક શક્તિ",
            "role": "યોગ્ય ભૂમિકા:",
            "dasha": "સક્રિય દશા:",
            "yogas": "સક્રિય યોગ:",
            "pairwise_title": "પરસ્પર ભાગીદાર સુસંગતતા મેટ્રિક્સ",
            "pair_strong": "મજબૂત તાલમેલ",
            "pair_mod": "સંતુલિત / સ્પષ્ટ ભૂમિકા",
            "pair_fric": "સાવચેતી અને કરાર જરૂરી",
            "biz_title": "સાથે મળીને કરવા યોગ્ય શ્રેષ્ઠ વ્યવસાયો અને ઉદ્યોગો",
            "biz_sub": "એવા ક્ષેત્રો જ્યાં તમારી સંયુક્ત ગ્રહ શક્તિ, યોગ અને સક્રિય દશાઓ સૌથી વધુ પ્રગતિ આપે છે.",
            "backed_by": "સહાયક ભાગીદારો:",
            "namank_title": "શ્રેષ્ઠ બિઝનેસ નામાંક (Namank) અને ફર્મ તપાસ",
            "best_namank": "શુભ બિઝનેસ નામાંક:",
            "firm_audit": "તપાસેલ ફર્મનું નામ:",
            "ausp": "ટીમ માટે શુભ",
            "adj": "સ્પેલિંગ સુધારવા વિચારવું",
            "outlook_title": "આગામી 5-વર્ષીય સંયુક્ત વ્યાપારિક દૃષ્ટિકોણ",
            "year": "વર્ષ",
            "running": "ચાલુ",
            "rem_title": "વ્યાપારિક વૃદ્ધિ ઉપાયો (સામૂહિક ખૂટતા અંકો માટે)",
            "rem_none": "તમારી ટીમમાં તમામ મુખ્ય વ્યાપારિક અંકો (1, 3, 5, 6, 8) હાજર છે — વધારાના ઉપાયની જરૂર નથી.",
            "crystals": "વ્યાપારિક સમૃદ્ધિ માટે સહાયક ક્રિસ્ટલ્સ",
            "disclaimer": "અસ્વીકરણ: વૈદિક અંકશાસ્ત્ર વ્યાપારિક માર્ગદર્શન માટે છે. રિપોર્ટ તારીખ:",
        },
    }[lang]

    google_fonts = "https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap"
    if lang == "hi":
        google_fonts += "&family=Noto+Sans+Devanagari:wght@400;600;700"
        body_font = "'Noto Sans Devanagari', 'Source Sans 3', sans-serif"
        serif_font = "'Noto Sans Devanagari', 'Libre Baskerville', serif"
    elif lang == "gu":
        google_fonts += "&family=Noto+Sans+Gujarati:wght@400;600;700"
        body_font = "'Noto Sans Gujarati', 'Source Sans 3', sans-serif"
        serif_font = "'Noto Sans Gujarati', 'Libre Baskerville', serif"
    else:
        body_font = "'Source Sans 3', sans-serif"
        serif_font = "'Libre Baskerville', serif"

    consultant = b["consultant"]
    partners = b["partners"]
    strongest = b["strongest_partner"]
    level = b["verdict_level"]
    banner_bg = (
        "linear-gradient(90deg, #059669, #10b981)" if level == "good"
        else ("linear-gradient(90deg, #d97706, #f59e0b)" if level == "moderate"
              else "linear-gradient(90deg, #991b1b, #db2777)")
    )
    partner_names_title = " · ".join(p["name"] for p in partners)

    partner_cards_html = ""
    for p in partners:
        cells_html = ""
        for c in p["grid"]["cells"]:
            val = c["str"] if c.get("count", 0) > 0 else ""
            cells_html += f'<div class="vg-cell"><div class="vg-planet">{GRID_PLANETS_EN.get(c["num"], "")}</div><div class="vg-num">{val}</div></div>'
        y_names = ", ".join(y["name"].split("(")[0].strip() for y in p.get("yogas", [])[:3]) or BL["none"]
        is_anc = (p["name"] == strongest["name"])
        anc_cls = "pcard pcard-anchor" if is_anc else "pcard"
        partner_cards_html += f"""
        <div class="{anc_cls}">
            <div class="pcard-hdr">
                <div>
                    <div class="pname">{p["name"]} {'★' if is_anc else ''}</div>
                    <div class="sub-muted">{BL["born"]} {p["dob"]}</div>
                </div>
                <div class="p-score">{p["strength_score"]}/100</div>
            </div>
            <div class="pcard-body">
                <div class="vg-grid vg-sm">{cells_html}</div>
                <div class="pstats">
                    <div><strong>{BL["basic"]} {p["bn"]}</strong> · {p["bn_planet"].split("(")[0].strip()}</div>
                    <div><strong>{BL["destiny"]} {p["dn"]}</strong> · {p["dn_planet"].split("(")[0].strip()}</div>
                    <div style="margin-top:4px;"><strong>{BL["dasha"]}</strong> MD {p["active_md"]} / AD {p["active_ad"]}</div>
                    <div><strong>{BL["role"]}</strong> {p["role"]}</div>
                </div>
            </div>
            <div class="pyogas"><strong>{BL["yogas"]}</strong> {y_names}</div>
        </div>"""

    pairwise_html = ""
    if b.get("pairwise_matrix"):
        prows = ""
        for pm in b["pairwise_matrix"]:
            st = pm["status"]
            st_lbl = BL["pair_strong"] if st == "strong" else (BL["pair_mod"] if st == "moderate" else BL["pair_fric"])
            st_cls = "pill-pos" if st == "strong" else ("pill-warn" if st == "moderate" else "pill-neg")
            prows += f"""
            <div class="pair-row">
                <div class="pair-top">
                    <strong>{pm["partner_a"]} × {pm["partner_b"]}</strong>
                    <span><span class="vpill {st_cls}">{st_lbl}</span> <strong>{pm["score"]}/100</strong></span>
                </div>
                <div class="sub-muted">{pm["note"]}</div>
            </div>"""
        pairwise_html = f'<div class="sheet"><h2 class="sec-h2">{BL["pairwise_title"]}</h2>{prows}</div>'

    biz_cards = ""
    for rb in b["recommended_businesses"]:
        biz_cards += f"""
        <div class="biz-card">
            <div class="biz-top"><strong>Number {rb["number"]} · {rb["planet"]} — {rb["title"]}</strong></div>
            <div class="biz-sec">{rb["sectors"]}</div>
            <div class="sub-muted">{BL["backed_by"]} {", ".join(rb["supporters"])}</div>
        </div>"""

    firm_eval_html = ""
    if b.get("business_name_eval"):
        fe = b["business_name_eval"]
        is_ausp = fe.get("is_auspicious", False)
        f_pill = f'<span class="vpill {"pill-pos" if is_ausp else "pill-warn"}">{BL["ausp"] if is_ausp else BL["adj"]}</span>'
        firm_eval_html = f'<div style="margin-top:6px;"><strong>{BL["firm_audit"]}</strong> {fe["name"]} (Compound {fe["compound"]} → Namank {fe["namank"]}) {f_pill}</div>'

    outlook_rows = ""
    for yr_row in b["joint_5yr"]:
        run_tag = f' <span class="run-pill">{BL["running"]}</span>' if yr_row.get("is_active") else ""
        p_cells = "".join(
            f'<div><strong>{pr["name"]}:</strong> MD {pr["md"]}/AD {pr["ad"]} · {pr["money"]} · {pr["disputes"]}</div>'
            for pr in yr_row["partners"]
        )
        outlook_rows += f'<tr><td class="bold-col">{yr_row["year"]}{run_tag}</td><td>{p_cells}</td></tr>'

    from vedic_translations import NUMBER_REMEDIES, PLANET_INFO
    rem_cards = ""
    for num in b.get("key_biz_missing", []):
        rem = NUMBER_REMEDIES.get(num, {})
        pinfo = PLANET_INFO.get(num, {}).get(lang, PLANET_INFO.get(num, {}).get("en", {}))
        rem_cards += f"""
        <div class="rem-card">
            <div class="rem-title">Number {num} · {pinfo.get("planet", num)}</div>
            <div class="rem-p"><strong>Mantra:</strong> {rem.get("mantra", {}).get(lang, rem.get("mantra", {}).get("en", ""))}</div>
            <div class="rem-p"><strong>Seva/Donation:</strong> {rem.get("seva", {}).get(lang, "")} · {rem.get("donation", {}).get(lang, "")}</div>
        </div>"""
    if not rem_cards:
        rem_cards = f'<div class="sub-muted">{BL["rem_none"]}</div>'

    crystals_list = SUPPORTING_CRYSTALS_BY_LANG.get(lang, SUPPORTING_CRYSTALS)
    crystals_html = "".join(f'<div class="crystal-row"><strong>{cn}</strong> — <span class="sub-muted">{cd}</span></div>' for cn, cd in crystals_list)

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{consultant["name"]} - {BL["report_sub"]} - {partner_names_title}</title>
<link href="{google_fonts}" rel="stylesheet">
<style>
@page {{ size: A4 portrait; margin: 12mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: {body_font}; color: #1e293b; font-size: 11px; line-height: 1.45; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.sheet {{ border: 1px solid #e2e8f0; border-radius: 14px; padding: 16px 18px; margin-bottom: 12px; background: #fff; }}
.page-break {{ page-break-before: always; break-before: page; }}
.mm-head {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px; border-bottom: 2px solid; border-image: linear-gradient(90deg, #7c3aed, #f59e0b) 1; margin-bottom: 10px; }}
.mm-brand {{ font-family: {serif_font}; font-size: 15px; font-weight: 700; color: #0f172a; }}
.mm-rtitle {{ text-align: right; font-size: 10px; color: #64748b; }}
.mm-rtitle strong {{ display: block; font-family: {serif_font}; font-size: 13px; color: #0f172a; }}
.kicker {{ font-family: {serif_font}; font-style: italic; font-size: 10.5px; color: #7c3aed; }}
.couple-name {{ font-family: {serif_font}; font-size: 19px; font-weight: 700; color: #0f172a; margin: 2px 0; }}
.sub-muted {{ font-size: 10px; color: #64748b; }}
.score-banner {{ background: {banner_bg}; color: #fff; border-radius: 12px; padding: 13px 16px; display: flex; align-items: center; gap: 16px; margin-bottom: 12px; }}
.score-big {{ font-family: {serif_font}; font-size: 26px; font-weight: 700; line-height: 1; }}
.score-big span {{ font-size: 13px; opacity: 0.85; }}
.score-verdict {{ font-family: {serif_font}; font-size: 15px; font-weight: 700; }}
.anchor-box {{ background: #fefce8; border: 1.5px solid #eab308; border-radius: 10px; padding: 12px 14px; margin-bottom: 12px; }}
.anchor-title {{ font-family: {serif_font}; font-size: 13px; font-weight: 700; color: #854d0e; margin-bottom: 4px; }}
.sec-h2 {{ font-family: {serif_font}; font-size: 15px; font-weight: 700; color: #0f172a; margin: 0 0 10px 0; }}
.pgrid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
.pcard {{ border: 1px solid #e2e8f0; border-radius: 10px; padding: 10px 12px; background: #fff; break-inside: avoid; }}
.pcard-anchor {{ border: 1.5px solid #eab308; background: #fffdf5; }}
.pcard-hdr {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }}
.pname {{ font-family: {serif_font}; font-size: 14px; font-weight: 700; color: #0f172a; }}
.p-score {{ font-weight: 700; font-size: 12px; color: #15803d; background: #dcfce7; padding: 2px 8px; border-radius: 999px; }}
.pcard-body {{ display: flex; gap: 10px; align-items: flex-start; }}
.vg-grid.vg-sm {{ display: grid; grid-template-columns: repeat(3, 40px); grid-template-rows: repeat(3, 32px); border: 1.5px solid #c9a96e; background: #fff; flex-shrink: 0; }}
.vg-cell {{ border: 0.5px solid #e2d1a8; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 1px; }}
.vg-planet {{ font-size: 6px; color: #b48a3e; }}
.vg-num {{ font-family: {serif_font}; font-size: 10px; font-weight: 700; color: #0f172a; }}
.pstats {{ font-size: 9.5px; color: #1e293b; flex: 1; }}
.pyogas {{ font-size: 9px; color: #475569; margin-top: 6px; }}
.pair-row {{ border: 1px solid #e2e8f0; border-radius: 8px; padding: 8px 10px; margin-bottom: 6px; break-inside: avoid; }}
.pair-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px; }}
.vpill {{ display: inline-block; font-size: 8.5px; font-weight: 700; padding: 1px 6px; border-radius: 999px; }}
.pill-pos {{ background: #dcfce7; color: #166534; }}
.pill-warn {{ background: #fef3c7; color: #92400e; }}
.pill-neg {{ background: #fee2e2; color: #991b1b; }}
.biz-card {{ border: 1px solid #ede9fe; background: #f8f7ff; border-radius: 8px; padding: 9px 12px; margin-bottom: 7px; break-inside: avoid; }}
.biz-top {{ font-size: 11.5px; color: #0f172a; margin-bottom: 2px; }}
.biz-sec {{ font-size: 10px; color: #334155; margin-bottom: 2px; }}
.clean-tbl {{ width: 100%; border-collapse: collapse; font-size: 9.5px; }}
.clean-tbl td, .clean-tbl th {{ padding: 6px; border-bottom: 1px solid #f1f5f9; text-align: left; vertical-align: top; }}
.bold-col {{ font-weight: 700; color: #0f172a; width: 90px; }}
.run-pill {{ background: #7c3aed; color: #fff; font-size: 8px; padding: 1px 5px; border-radius: 999px; }}
.rem-card {{ border: 1px solid #e2e8f0; border-radius: 8px; padding: 8px 10px; margin-bottom: 6px; break-inside: avoid; }}
.rem-title {{ font-weight: 700; font-size: 11px; margin-bottom: 3px; }}
.rem-p {{ font-size: 9.5px; color: #334155; }}
.crystal-row {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 5px 10px; margin-bottom: 4px; font-size: 9.5px; }}
.mm-foot {{ text-align: center; font-size: 9px; color: #64748b; margin-top: 10px; }}
</style>
</head>
<body>
<div class="sheet">
    <div class="mm-head">
        <div>
            <div class="mm-brand">{BL["prepared_by"]} {consultant["name"]}</div>
            <div class="sub-muted">{consultant.get("title", "")} · {consultant["phone"]} · {consultant["email"]}</div>
        </div>
        <div class="mm-rtitle">{BL["kicker_top"]} <strong>{BL["report_sub"]}</strong></div>
    </div>
    <div class="kicker">{BL["prepared_for"]}</div>
    <div class="couple-name">{partner_names_title}</div>
    <div class="sub-muted">{BL["partners_lbl"]} {b["partner_count"]}</div>
</div>

<div class="score-banner">
    <div class="score-big">{b["overall_score"]}<span>/100</span></div>
    <div>
        <div class="score-verdict">{b["verdict"]}</div>
    </div>
</div>

<div class="anchor-box">
    <div class="anchor-title">★ {BL["anchor_title"]}: {strongest["name"]} ({strongest["score"]}/100)</div>
    <div style="font-size:10.3px;color:#422006;">{strongest["reason"]}</div>
</div>

<div class="sheet">
    <h2 class="sec-h2">{BL["team_cov"]}</h2>
    <div><strong>{BL["covered"]}</strong> {", ".join(str(x) for x in b["team_covered"]) or BL["none"]}</div>
    <div style="margin-top:4px;"><strong>{BL["missing"]}</strong> {", ".join(str(x) for x in b["team_missing"]) or BL["none"]}</div>
</div>

<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">{BL["partner_cards"]}</h2>
    <div class="pgrid">{partner_cards_html}</div>
</div>

{pairwise_html}

<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">{BL["biz_title"]}</h2>
    <p class="sub-muted" style="margin-bottom:8px;">{BL["biz_sub"]}</p>
    {biz_cards}
    <h3 style="margin:12px 0 6px 0;font-size:13px;">{BL["namank_title"]}</h3>
    <div><strong>{BL["best_namank"]}</strong> {", ".join(str(x) for x in b["best_biz_namank"])}</div>
    {firm_eval_html}
</div>

<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">{BL["outlook_title"]}</h2>
    <table class="clean-tbl"><tbody>{outlook_rows}</tbody></table>
    <h3 style="margin:12px 0 6px 0;font-size:13px;">{BL["rem_title"]}</h3>
    {rem_cards}
    <h3 style="margin:12px 0 6px 0;font-size:13px;">{BL["crystals"]}</h3>
    {crystals_html}
    <div class="mm-foot">
        <div>{BL["disclaimer"]} {b["generated_on"]}.</div>
        <div style="margin-top:3px;">{BL["prepared_by"]} {consultant["name"]} · {consultant["phone"]} · {consultant["email"]}</div>
    </div>
</div>
</body>
</html>"""


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
