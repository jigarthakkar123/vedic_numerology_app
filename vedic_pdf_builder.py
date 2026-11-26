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
        "report_kicker": "Vedic Numerology",
        "report_title": "Numerology Report",
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
        "report_kicker": "वैदिक अंकशास्त्र",
        "report_title": "अंकशास्त्र रिपोर्ट",
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
        "report_kicker": "વૈદિક અંકશાસ્ત્ર",
        "report_title": "અંકશાસ્ત્ર રિપોર્ટ",
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
    bn_arch_title, bn_arch_tags, bn_arch_desc = ARCHETYPES_EN.get(bn, ARCHETYPES_EN[1])
    dn_arch_title, dn_arch_tags, dn_arch_desc = ARCHETYPES_EN.get(dn, ARCHETYPES_EN[1])

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
        _, otags, _ = ARCHETYPES_EN.get(onum, ARCHETYPES_EN[1])
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
    for cat_title, cat_items in PROFESSIONS_BY_BN.get(bn, PROFESSIONS_BY_BN[1]):
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
        (ui.get("pred_education", "Growth"), preds.get("education", "")),
        (ui.get("pred_travel", L["travel"]), preds.get("travel", "")),
        (ui.get("pred_litigation", L["disputes"]), preds.get("litigation", "")),
        (ui.get("pred_relationship", "Relations"), preds.get("relationship", "")),
    ]

    def render_pred_rows(rows: list) -> str:
        out = ""
        for lbl, txt in rows:
            if isinstance(txt, dict):
                txt = txt.get("desc", "")
            if txt:
                out += f'<div class="pred-row"><div class="pred-lbl">{lbl}</div><div class="pred-txt">{txt}</div></div>'
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
        rem_cards_html = ""
        for r in remedies_by_num:
            nc = r.get("natal_count", 0)
            sub_line = L["appears_grid"].format(n=nc) if nc >= 2 else L["active_period_neg"]
            rem_cards_html += f"""
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
            </div>"""

        crystals_html = "".join(
            f'<div class="crystal-row"><div class="crystal-name">{cname}</div><div class="crystal-desc">{cdesc}</div></div>'
            for cname, cdesc in SUPPORTING_CRYSTALS
        )

        remedies_section_html = f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{L["prof_report"]}</div>
            <h2 class="sec-h2">{L["remedies"]}</h2>
            <p class="lead-note">{L["remedies_intro"]}</p>
            <div class="rem-grid">
                {rem_cards_html}
            </div>
            <h3 class="sec-h3">{L["supporting_crystals"]}</h3>
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
            <div class="brand-name">{consultant["name"]}</div>
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

<!-- PAGE 10: PREDICTIONS & NINE-YEAR OUTLOOK -->
<div class="page-break"></div>
<div class="sheet">
    <div class="kicker">{L["prof_report"]}</div>
    <h2 class="sec-h2">{L["predictions"]}</h2>
    <h3 class="sec-h3">{L["from_birth_grid"]}</h3>
    {render_pred_rows(pred_rows_natal)}

    <h3 class="sec-h3">{L["this_year"]} · {L["md"]} {md_num} · {L["ad"]} {ad_num} · {_fmt_dash(active_ad.get("start_str", ""))} to {_fmt_dash(active_ad.get("end_str", ""))}</h3>
    {render_pred_rows(pred_rows_year)}

    <h3 class="sec-h3">{L["nine_year_outlook"]}</h3>
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
    for Boy (Groom) and Girl (Bride), ready for Chromium PDF export.
    """
    consultant = m["consultant"]
    boy = m["boy"]
    girl = m["girl"]
    score = m["total_score"]
    verdict = m["verdict"]
    verdict_sub = m["verdict_sub"]
    level = m["verdict_level"]

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
        y_names = ", ".join(y["name"].split("(")[0].strip() for y in p.get("yogas", [])[:3]) or "None"
        bn_arch = ARCHETYPES_EN.get(p["bn"], ARCHETYPES_EN[1])[0]
        dn_arch = ARCHETYPES_EN.get(p["dn"], ARCHETYPES_EN[1])[0]
        return f"""
        <div class="mm-person">
            <div class="kicker">{role_lbl}</div>
            <div class="mm-pname">{p["name"]}</div>
            <div class="mm-pdob">Born {p["dob"]} · age {p["age"]}</div>
            <div class="mm-grid-row">
                <div class="vg-grid vg-sm">{cells_html}</div>
                <div class="mm-stats">
                    <div><strong>Basic {p["bn"]}</strong> · {p["bn_planet"].split("(")[0].strip()}</div>
                    <div class="mm-arch">{bn_arch}</div>
                    <div style="margin-top:6px;"><strong>Destiny {p["dn"]}</strong> · {p["dn_planet"].split("(")[0].strip()}</div>
                    <div class="mm-arch">{dn_arch}</div>
                    <div style="margin-top:6px;">{pills}</div>
                </div>
            </div>
            <div class="mm-yogas"><strong>Yogas:</strong> {y_names}</div>
        </div>"""

    pillars_html = ""
    for p in m["pillars"]:
        pct = int((p["score"] / p["max"]) * 100)
        bar_col = "#15803d" if p["score"] >= 15 else ("#d97706" if p["score"] >= 10 else "#e2e8f0")
        pillars_html += f"""
        <div class="pillar-card">
            <div class="pillar-top">
                <div class="pillar-title">{p["title"]}</div>
                <div class="pillar-score">{p["score"]}<span class="pillar-max">/{p["max"]}</span></div>
            </div>
            <div class="pillar-bar-bg"><div class="pillar-bar-fill" style="width:{pct}%;background:{bar_col};"></div></div>
            <div class="pillar-desc">{p["desc"]}</div>
        </div>"""

    rules_html = ""
    for rc in m.get("rules_checks", []):
        st = rc["status"]
        icon = "✓" if st == "ok" else ("✕" if st == "reject" else "!")
        cls = "rule-ok" if st == "ok" else ("rule-reject" if st == "reject" else "rule-warn")
        rules_html += f"""
        <div class="rule-row" style="margin-bottom:7px;">
            <div class="rule-badge {cls}">{icon}</div>
            <div>
                <strong>{rc["rule"]} · {rc["title"]}</strong><br>
                <span class="sub-muted">{rc["detail"]}</span>
            </div>
        </div>"""

    lit = m.get("litigation_check", {})
    b_lit = lit.get("boy", {})
    g_lit = lit.get("girl", {})
    lit_items = []
    if b_lit.get("risk"):
        lit_items.append(f"{b_lit['name']}: litigation trigger active in {', '.join(b_lit['years'])}")
    if g_lit.get("risk"):
        lit_items.append(f"{g_lit['name']}: litigation trigger active in {', '.join(g_lit['years'])}")
    lit_html = (
        f'<div class="lit-warn"><strong>5-Year Litigation Check:</strong> {"; ".join(lit_items)}. Consult carefully before proceeding.</div>'
        if lit_items else
        '<div class="lit-ok"><strong>5-Year Litigation Check:</strong> No 2+ year litigation activation detected in the next 5 years for either grid.</div>'
    )

    rec_bg = "#f0fdf4" if level == "good" else ("#fffbeb" if level == "moderate" else "#fef2f2")
    rec_bd = "#bbf7d0" if level == "good" else ("#fde68a" if level == "moderate" else "#fecaca")
    rec_title = "Good matching" if level == "good" else ("Suggestive matching" if level == "moderate" else "Not recommended")

    boy_full = m.get("boy_full", {})
    girl_full = m.get("girl_full", {})

    def _year_grids_page(prof: Dict[str, Any], label: str) -> str:
        nyg = prof.get("dasha", {}).get("nine_year_grids", [])
        cards = ""
        for yg in nyg:
            is_run = yg.get("is_active", False)
            cls = "yg-card yg-running" if is_run else "yg-card"
            badge = '<span class="running-badge">Running</span>' if is_run else ""
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
            <h2 class="sec-h2">{prof["client"]["name"]} · 9-Year Transit Grids</h2>
            <p class="sub-muted" style="margin-bottom:10px;">Birth grid with each year's Mahadasha (MD) and Antardasha (AD). Running year is highlighted in the centre.</p>
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
            return f'<div><div class="cycle-title">Cycle {cno}</div><table class="clean-tbl"><thead><tr><th>MD</th><th>Start</th><th>End</th><th>Age</th></tr></thead><tbody>{trs}</tbody></table></div>'

        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{label}</div>
            <h2 class="sec-h2">{prof["client"]["name"]} · Mahadasha &amp; Active Periods</h2>
            <div class="dasha-sum-row">
                <div class="ds-box"><span>Mahadasha</span><strong>{act_md.get("number","")}</strong><small>{_fmt_dash(act_md.get("start_str",""))} – {_fmt_dash(act_md.get("end_str",""))}</small></div>
                <div class="ds-box"><span>Antardasha</span><strong>{act_ad.get("ad_number","")}</strong><small>{_fmt_dash(act_ad.get("start_str",""))} – {_fmt_dash(act_ad.get("end_str",""))}</small></div>
                <div class="ds-box"><span>Pratyantar</span><strong>{act_pd.get("number","")}</strong><small>{_fmt_dash(act_pd.get("start_str",""))} – {_fmt_dash(act_pd.get("end_str",""))}</small></div>
            </div>
            <div class="md-bar">{bar_html}</div>
            <div class="md-bar-labels"><span>Birth</span><span>Age 45</span><span>Age 90</span></div>
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
            pts = "".join(f"<li>{pt}</li>" for pt in y.get("points", [])[:4])
            y_cards += f'<div class="yoga-box"><div class="yoga-title">{y["name"]}</div>{f"<ul class=yoga-pts>{pts}</ul>" if pts else ""}</div>'
        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{label}</div>
            <h2 class="sec-h2">{prof["client"]["name"]} · Grid Analysis &amp; Yogas</h2>
            <div class="ga-grid">{v_cards}</div>
            <h3 class="sec-h3">Active Yogas in Birth Grid</h3>
            <div class="yoga-grid">{y_cards or "<div class=sub-muted>No major yogas triggered.</div>"}</div>
        </div>"""

    def _joint_outlook_page() -> str:
        b_nyg = boy_full.get("dasha", {}).get("nine_year_grids", [])
        g_nyg = girl_full.get("dasha", {}).get("nine_year_grids", [])
        g_by_yr = {x["year"]: x for x in g_nyg}
        rows = ""
        for bx in b_nyg:
            yr = bx["year"]
            gx = g_by_yr.get(yr, {})
            ac = ' class="row-active"' if bx.get("is_active") else ""
            rows += f"""
            <tr{ac}>
                <td class="bold-col">{yr}</td>
                <td>MD {bx["md"]} / AD {bx["ad"]}</td>
                <td>{bx["money"][1]}</td>
                <td>{bx["disputes"][1]}</td>
                <td>MD {gx.get("md","–")} / AD {gx.get("ad","–")}</td>
                <td>{gx.get("money", ("","–"))[1]}</td>
                <td>{gx.get("disputes", ("","–"))[1]}</td>
            </tr>"""
        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">Joint Timeline Comparison</div>
            <h2 class="sec-h2">9-Year Couple Outlook (Year-by-Year)</h2>
            <p class="sub-muted" style="margin-bottom:10px;">Side-by-side comparison of Mahadasha, Antardasha, financial flow, and dispute/litigation windows for both partners.</p>
            <table class="clean-tbl">
                <thead>
                    <tr>
                        <th>Year</th>
                        <th>{boy["name"]} (MD/AD)</th><th>Money</th><th>Disputes</th>
                        <th>{girl["name"]} (MD/AD)</th><th>Money</th><th>Disputes</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        </div>"""

    def _remedies_page(prof: Dict[str, Any], label: str) -> str:
        rems = prof.get("remedies_by_number", [])
        cards = ""
        for r in rems:
            cards += f"""
            <div class="rem-card">
                <div class="rem-head"><span class="rem-circle">{r["number"]}</span><div><div class="rem-title">Number {r["number"]} · {r["planet"]}</div></div></div>
                <div class="rem-sec-lbl">Mantras &amp; Practices</div><p class="rem-p">{r["mantra"]}</p>
                <div class="rem-sec-lbl">Service (Seva)</div><p class="rem-p">{r["seva"]}</p>
                <div class="rem-sec-lbl">Donations</div><p class="rem-p">{r["donation"]}</p>
                <div class="rem-sec-lbl">Colours &amp; Fasting</div><p class="rem-p">{r["colors"]} · {r["fasting"]}</p>
            </div>"""
        if not cards:
            cards = '<div class="sub-muted">No severe number afflictions requiring targeted remedies.</div>'
        return f"""
        <div class="page-break"></div>
        <div class="sheet">
            <div class="kicker">{label}</div>
            <h2 class="sec-h2">{prof["client"]["name"]} · Personalized Vedic Remedies</h2>
            <p class="sub-muted" style="margin-bottom:10px;">Targeted balancing remedies for repeated or negative numbers in the natal grid and active dasha period.</p>
            <div class="rem-grid">{cards}</div>
        </div>"""

    crystals_html = "".join(
        f'<div class="crystal-row"><strong>{cn}</strong> — <span class="sub-muted">{cd}</span></div>'
        for cn, cd in SUPPORTING_CRYSTALS
    )

    extra_pages_html = ""
    if boy_full and girl_full:
        extra_pages_html = (
            _year_grids_page(boy_full, "Boy · Groom")
            + _year_grids_page(girl_full, "Girl · Bride")
            + _dasha_page(boy_full, "Boy · Groom")
            + _dasha_page(girl_full, "Girl · Bride")
            + _analysis_yogas_page(boy_full, "Boy · Groom")
            + _analysis_yogas_page(girl_full, "Girl · Bride")
            + _joint_outlook_page()
            + _remedies_page(boy_full, "Boy · Groom")
            + _remedies_page(girl_full, "Girl · Bride")
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{consultant["name"]} - Match Making Report - {boy["name"]} &amp; {girl["name"]}</title>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<style>
@page {{ size: A4 portrait; margin: 12mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'Source Sans 3', sans-serif; color: #1e293b; font-size: 11px; line-height: 1.45; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.sheet {{ border: 1px solid #e2e8f0; border-radius: 14px; padding: 18px 20px; margin-bottom: 12px; background: #fff; break-inside: avoid; }}
.page-break {{ page-break-before: always; break-before: page; }}
.mm-head {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px; border-bottom: 2px solid; border-image: linear-gradient(90deg, #7c3aed, #f59e0b) 1; margin-bottom: 12px; }}
.mm-brand {{ font-family: 'Libre Baskerville', serif; font-size: 15px; font-weight: 700; color: #0f172a; }}
.mm-rtitle {{ text-align: right; font-size: 10px; color: #64748b; }}
.mm-rtitle strong {{ display: block; font-family: 'Libre Baskerville', serif; font-size: 13px; color: #0f172a; }}
.kicker {{ font-family: 'Libre Baskerville', serif; font-style: italic; font-size: 10.5px; color: #7c3aed; }}
.couple-name {{ font-family: 'Libre Baskerville', serif; font-size: 22px; font-weight: 700; color: #0f172a; margin: 2px 0; }}
.sub-muted {{ font-size: 10.5px; color: #64748b; }}
.score-banner {{ background: {banner_bg}; color: #fff; border-radius: 12px; padding: 14px 18px; display: flex; align-items: center; gap: 18px; margin-bottom: 12px; }}
.score-big {{ font-family: 'Libre Baskerville', serif; font-size: 28px; font-weight: 700; line-height: 1; }}
.score-big span {{ font-size: 14px; opacity: 0.85; }}
.score-verdict {{ font-family: 'Libre Baskerville', serif; font-size: 16px; font-weight: 700; }}
.score-sub {{ font-size: 10.5px; opacity: 0.92; }}
.sec-h2 {{ font-family: 'Libre Baskerville', serif; font-size: 16px; font-weight: 700; color: #0f172a; margin: 0 0 10px 0; }}
.mm-two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
.mm-person {{ background: #f8f7ff; border: 1px solid #ede9fe; border-radius: 10px; padding: 12px; }}
.mm-pname {{ font-family: 'Libre Baskerville', serif; font-size: 15px; font-weight: 700; color: #0f172a; }}
.mm-pdob {{ font-size: 10px; color: #64748b; margin-bottom: 8px; }}
.mm-grid-row {{ display: flex; gap: 10px; align-items: flex-start; }}
.vg-grid.vg-sm {{ display: grid; grid-template-columns: repeat(3, 44px); grid-template-rows: repeat(3, 36px); border: 1.5px solid #c9a96e; background: #fff; flex-shrink: 0; }}
.vg-cell {{ border: 0.5px solid #e2d1a8; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: 1px; }}
.vg-planet {{ font-size: 6.5px; color: #b48a3e; }}
.vg-num {{ font-family: 'Libre Baskerville', serif; font-size: 11px; font-weight: 700; color: #0f172a; }}
.mm-stats {{ font-size: 10px; color: #1e293b; flex: 1; }}
.mm-arch {{ font-size: 9.5px; color: #64748b; }}
.mm-yogas {{ font-size: 9.5px; color: #334155; margin-top: 8px; }}
.vpill {{ display: inline-block; font-size: 9px; font-weight: 700; padding: 1px 6px; border-radius: 999px; margin-right: 3px; }}
.pill-pos {{ background: #dcfce7; color: #166534; }}
.pill-neg {{ background: #fee2e2; color: #991b1b; }}
.pillar-card {{ border: 1px solid #e2e8f0; border-radius: 8px; padding: 9px 12px; margin-bottom: 8px; }}
.pillar-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }}
.pillar-title {{ font-family: 'Libre Baskerville', serif; font-size: 12px; font-weight: 700; color: #0f172a; }}
.pillar-score {{ font-family: 'Libre Baskerville', serif; font-size: 13px; font-weight: 700; color: #15803d; }}
.pillar-max {{ font-size: 10px; color: #64748b; }}
.pillar-bar-bg {{ height: 5px; background: #e2e8f0; border-radius: 999px; overflow: hidden; margin-bottom: 5px; }}
.pillar-bar-fill {{ height: 100%; border-radius: 999px; }}
.pillar-desc {{ font-size: 10px; color: #475569; }}
.rule-row {{ display: flex; gap: 10px; align-items: center; }}
.rule-badge {{ width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 11px; color: #fff; flex-shrink: 0; }}
.rule-ok {{ background: #15803d; }}
.rule-warn {{ background: #d97706; }}
.rule-reject {{ background: #b91c1c; }}
.lit-ok {{ background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 8px 12px; font-size: 10px; color: #166534; margin-top: 8px; }}
.lit-warn {{ background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 8px 12px; font-size: 10px; color: #991b1b; margin-top: 8px; }}
.yg-matrix {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
.yg-card {{ border: 1px solid #e2e8f0; border-radius: 10px; padding: 8px 10px; text-align: center; background: #fff; }}
.yg-card.yg-running {{ border: 2px solid #7c3aed; background: #fdfcff; }}
.yg-year {{ font-family: 'Libre Baskerville', serif; font-size: 13px; font-weight: 700; color: #0f172a; }}
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
.ds-box strong {{ display: block; font-family: 'Libre Baskerville', serif; font-size: 18px; color: #7c3aed; }}
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
.yoga-box {{ border: 1px solid #e5d5a7; background: #fffdf7; border-radius: 8px; padding: 8px 10px; }}
.yoga-title {{ font-family: 'Libre Baskerville', serif; font-size: 11px; font-weight: 700; margin-bottom: 3px; }}
.yoga-pts {{ margin: 3px 0 0 14px; padding: 0; font-size: 9.3px; color: #334155; }}
.rem-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.rem-card {{ border: 1px solid #e2e8f0; border-radius: 10px; padding: 8px 10px; }}
.rem-head {{ display: flex; align-items: center; gap: 8px; margin-bottom: 4px; }}
.rem-circle {{ width: 22px; height: 22px; border-radius: 50%; background: #f5f3ff; color: #7c3aed; font-weight: 700; font-size: 10.5px; display: inline-flex; align-items: center; justify-content: center; }}
.rem-title {{ font-family: 'Libre Baskerville', serif; font-size: 11.5px; font-weight: 700; }}
.rem-sec-lbl {{ font-size: 9.5px; font-weight: 700; color: #7c3aed; margin-top: 4px; }}
.rem-p {{ font-size: 9.3px; color: #334155; margin: 1px 0; }}
.crystal-row {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 6px 10px; margin-bottom: 5px; font-size: 10px; }}
.sec-h3 {{ font-family: 'Libre Baskerville', serif; font-size: 13.5px; font-weight: 700; margin: 12px 0 8px 0; }}
.rec-box {{ background: {rec_bg}; border: 1px solid {rec_bd}; border-radius: 10px; padding: 12px 14px; margin-bottom: 10px; }}
.rec-title {{ font-family: 'Libre Baskerville', serif; font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 4px; }}
.next-box {{ border: 1px solid #e2e8f0; border-radius: 10px; padding: 10px 14px; }}
.next-box ol {{ margin: 6px 0 0 16px; padding: 0; font-size: 10.5px; color: #334155; }}
.next-box li {{ margin-bottom: 3px; }}
.mm-foot {{ text-align: center; font-size: 9.5px; color: #64748b; margin-top: 10px; }}
</style>
</head>
<body>
<div class="sheet">
    <div class="mm-head">
        <div class="mm-brand">{consultant["name"]}</div>
        <div class="mm-rtitle">Vedic Numerology <strong>Match Making Report</strong></div>
    </div>
    <div class="kicker">Prepared for</div>
    <div class="couple-name">{boy["name"]} &amp; {girl["name"]}</div>
    <div class="sub-muted">Five pillars of 20 points each · Vedic Compatibility Method</div>
</div>

<div class="score-banner">
    <div class="score-big">{score}<span>/100</span></div>
    <div>
        <div class="score-verdict">{verdict}</div>
        <div class="score-sub">{verdict_sub}</div>
    </div>
</div>

<div class="sheet">
    <h2 class="sec-h2">The two grids</h2>
    <div class="mm-two">
        {_person_card(boy, "Boy · Groom")}
        {_person_card(girl, "Girl · Bride")}
    </div>
</div>

<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">The five pillars</h2>
    {pillars_html}
</div>

<div class="sheet">
    <h2 class="sec-h2">Basic matching &amp; rejection rules</h2>
    {rules_html}
    {lit_html}
</div>

{extra_pages_html}

<div class="page-break"></div>
<div class="sheet">
    <h2 class="sec-h2">Final recommendation &amp; Supporting Crystals</h2>
    <div class="rec-box">
        <div class="rec-title">{rec_title}</div>
        <div><strong>{boy["name"]}</strong> and <strong>{girl["name"]}</strong> score <strong>{score} of 100</strong>. Key areas to review: {m["weak_summary"]}.</div>
        <div class="sub-muted" style="margin-top:4px;">This is a reason for a careful, detailed consultation before any decision — not a judgement on either person.</div>
    </div>
    <div class="next-box" style="margin-bottom:12px;">
        <strong>What to do next</strong>
        <ol>
            <li>Review both partners' full 9-year transit grids, Mahadasha cycles, and 5-year litigation windows included in this report.</li>
            <li>Discuss the weaker pillars ({m["weak_summary"]}) openly before finalizing the match.</li>
            <li>Follow the personalized Vedic remedies for both partners and use the supporting crystals below.</li>
        </ol>
    </div>
    <h3 class="sec-h3">Supporting Crystals for Couple Harmony</h3>
    {crystals_html}
    <div class="mm-foot">
        <strong>Disclaimer:</strong> Prepared using Vedic numerology for guidance. Report generated on {m["generated_on"]}.<br>
        Prepared by {consultant["name"]} · {consultant["phone"]} · {consultant["email"]}
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
