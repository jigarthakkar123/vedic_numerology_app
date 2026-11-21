# -*- coding: utf-8 -*-
"""
Vedic Numerology Calculation & Prediction Engine
Implements authentic mathematical formulas, Dasha cycles (MD, AD, PD),
Natal Grid generation, Yogas detection, Positive/Negative vibrations,
and domain-specific predictions (Finance, Property, Vehicle, Education, Travel, Litigation, Health).
"""

from datetime import date, datetime, timedelta
from typing import Dict, List, Any, Tuple
from vedic_translations import (
    UI_TEXT, PLANET_INFO, NUMBER_QUALITIES, NUMBER_PRECAUTIONS,
    VIBRATION_DETAILS, YOGA_DEFINITIONS, PROFESSIONS_INFO,
    NUMBER_REMEDIES, GENERAL_REMEDIES, CONSULTANT_INFO
)

# Chaldean / Cheiro Letter Vibration Values for Name Numerology
CHALDEAN_MAP = {
    'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
    'B': 2, 'K': 2, 'R': 2,
    'C': 3, 'G': 3, 'L': 3, 'S': 3,
    'D': 4, 'M': 4, 'T': 4,
    'E': 5, 'H': 5, 'N': 5, 'X': 5,
    'U': 6, 'V': 6, 'W': 6,
    'O': 7, 'Z': 7,
    'F': 8, 'P': 8
}

def calculate_name_number(name: str) -> int:
    """Calculates Name Number (Namank) using classical Chaldean reduction."""
    cleaned = "".join(c.upper() for c in name if c.isalpha())
    if not cleaned:
        return 1
    total = sum(CHALDEAN_MAP.get(c, 0) for c in cleaned)
    return reduce_to_single_digit(total)

def evaluate_name_harmony(namank: int, bn: int, dn: int, lang: str) -> Dict[str, str]:
    """Evaluates whether the client's current name spelling vibrates in harmony with BN and DN."""
    p_info = PLANET_INFO[bn]["en"]
    friendly = [int(x.strip()) for x in p_info["friendly_nums"].split(",")]
    enemy = [int(x.strip()) for x in p_info["enemy_nums"].split(",")]
    
    if namank in friendly or namank == dn:
        status = "harmonious"
        text = {
            "en": f"Name Number {namank} is highly harmonious with Root Number {bn} and Destiny Number {dn}. Attracts luck and natural goodwill.",
            "hi": f"नामांक {namank} आपके मूलांक {bn} व भाग्यांक {dn} के साथ पूर्ण सामंजस्य में है। यह नाम सौभाग्य और प्रतिष्ठा को आकर्षित करता है।",
            "gu": f"નામાંક {namank} આપના મૂળાંક {bn} અને ભાગ્યાંક {dn} સાથે ઉત્તમ સુમેળમાં છે. આ નામ કુદરતી પ્રગતિ અને ભાગ્યોદય લાવે છે."
        }
    elif namank in enemy:
        status = "conflict"
        text = {
            "en": f"Name Number {namank} presents mild friction with Root Number {bn}. Harmonizing name spelling to a friendly vibration (such as 1, 5, or 6) is recommended.",
            "hi": f"नामांक {namank} आपके मूलांक {bn} के साथ थोड़ा विरोधाभासी है। नाम की स्पेलिंग में आंशिक सुधार (1, 5 या 6 पर) करने की सलाह दी जाती है।",
            "gu": f"નામાંક {namank} આપના મૂળાંક {bn} સાથે સામાન્ય ઘર્ષણ દર્શાવે છે. નામના સ્પેલિંગમાં સામાન્ય ફેરફાર કરી શુભ અંક પર સેટ કરવાની સલાહ છે."
        }
    else:
        status = "neutral"
        text = {
            "en": f"Name Number {namank} maintains a steady, neutral vibration with your planetary chart. Stable and supportive.",
            "hi": f"नामांक {namank} आपके ग्रहीय चक्र के साथ स्थिर व तटस्थ स्पंदन बनाए रखता है। यह संतुलित प्रगति प्रदान करता है।",
            "gu": f"નામાંક {namank} આપના ગ્રહીય ચક્ર સાથે સંતુલિત અને તટસ્થ સ્પંદન જાળવે છે. સ્થિર પરિણામો આપે છે."
        }
        
    return {
        "status": status,
        "text": text.get(lang, text["en"])
    }

def reduce_to_single_digit(n: int) -> int:
    """Reduces any positive integer to a single digit 1-9 by summing digits."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def calculate_basic_number(day: int) -> int:
    """Basic Number (Moolank / Root Number): sum of digits of the birth day."""
    return reduce_to_single_digit(day)

def calculate_destiny_number(day: int, month: int, year: int) -> int:
    """Destiny Number (Bhagyank / Life Path): sum of all digits of DD + MM + YYYY."""
    total = sum(int(d) for d in f"{day:02d}{month:02d}{year:04d}")
    return reduce_to_single_digit(total)

def get_day_number(weekday_idx: int) -> int:
    """
    Vedic weekday code for Antardasha:
    Monday=0 -> Mon=2
    Tuesday=1 -> Tue=9
    Wednesday=2 -> Wed=5
    Thursday=3 -> Thu=3
    Friday=4 -> Fri=6
    Saturday=5 -> Sat=8
    Sunday=6 -> Sun=1
    """
    mapping = {
        0: 2,  # Monday
        1: 9,  # Tuesday
        2: 5,  # Wednesday
        3: 3,  # Thursday
        4: 6,  # Friday
        5: 8,  # Saturday
        6: 1   # Sunday
    }
    return mapping.get(weekday_idx, 1)

def calculate_vedic_grid(day: int, month: int, year: int) -> Dict[str, Any]:
    """
    Computes the 3x3 Vedic Birth Grid (Natal Grid).
    Standard Vedic placement rules from Course Level 1 & 2:
    1. Day: If single digit (1-9) or 10,20,30 -> count single digit (1-9).
            If compound (11-29 except 20, or 31) -> count both digits.
    2. Month: 1-9 count once; 10 count '1'; 11 count '1','1'; 12 count '1','2'.
    3. Year: Century excluded! Only last two digits counted (e.g. 1982 -> 8, 2).
    4. Basic Number: If compound day, BN is added to grid.
    5. Destiny Number: ALWAYS added to grid.
    """
    digits: List[int] = []
    
    # 1. Day of birth
    if day in [10, 20, 30]:
        digits.append(day // 10)
    elif day < 10:
        digits.append(day)
    else:
        # Compound day: enter both digits
        digits.extend([int(d) for d in str(day)])
        
    # 2. Month of birth
    for d in str(month):
        val = int(d)
        if val > 0:
            digits.append(val)
            
    # 3. Year of birth (Exclude century: take last 2 digits)
    yr_str = f"{year:04d}"[-2:]
    for d in yr_str:
        val = int(d)
        if val > 0:
            digits.append(val)
            
    # 4. Basic Number (if compound day, add BN to grid)
    bn = calculate_basic_number(day)
    if day not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]:
        digits.append(bn)
        
    # 5. Destiny Number (always added)
    dn = calculate_destiny_number(day, month, year)
    digits.append(dn)
    
    # Count occurrences of 1 through 9
    counts = {i: digits.count(i) for i in range(1, 10)}
    
    # Vedic 3x3 Grid Layout:
    # [ 3 ] [ 1 ] [ 9 ]
    # [ 6 ] [ 7 ] [ 5 ]
    # [ 2 ] [ 8 ] [ 4 ]
    grid_cells = [
        {"num": 3, "count": counts[3], "str": "3" * counts[3] if counts[3] > 0 else "-"},
        {"num": 1, "count": counts[1], "str": "1" * counts[1] if counts[1] > 0 else "-"},
        {"num": 9, "count": counts[9], "str": "9" * counts[9] if counts[9] > 0 else "-"},
        {"num": 6, "count": counts[6], "str": "6" * counts[6] if counts[6] > 0 else "-"},
        {"num": 7, "count": counts[7], "str": "7" * counts[7] if counts[7] > 0 else "-"},
        {"num": 5, "count": counts[5], "str": "5" * counts[5] if counts[5] > 0 else "-"},
        {"num": 2, "count": counts[2], "str": "2" * counts[2] if counts[2] > 0 else "-"},
        {"num": 8, "count": counts[8], "str": "8" * counts[8] if counts[8] > 0 else "-"},
        {"num": 4, "count": counts[4], "str": "4" * counts[4] if counts[4] > 0 else "-"},
    ]
    
    return {
        "digits": digits,
        "counts": counts,
        "cells": grid_cells,
        "bn": bn,
        "dn": dn
    }

def evaluate_vibrations(counts: Dict[int, int], dn: int) -> Dict[int, str]:
    """
    Evaluates Positive (+) or Negative (-) vibration for each number 1-9.
    Rules from Advanced Vedic Numerology Level 2:
    - 1: Single 1 or multiple 1 with DN1 = +1; multiple 1 without DN1 = -1.
    - 2: Single 2 = +2; 22 = -2; 222+ = extreme -2.
    - 3: Single 3 = +3; multiple 3 = -3.
    - 4: Even 4s (44, 4444) = +4; odd 4s (4, 444) = -4.
    - 5: Single 5 = +5; multiple 5 = -5.
    - 6: Single 6 or multiple with DN6 = +6; multiple without DN6 = -6.
    - 7: Single 7 = +7; multiple 7 = -7.
    - 8: Even 8s (88, 8888) = +8; odd 8s (8, 888) = -8.
    - 9: Single 9 = +9; multiple 9 = -9.
    """
    vibrations = {}
    for num in range(1, 10):
        c = counts.get(num, 0)
        if c == 0:
            vibrations[num] = "absent"
            continue
            
        if num == 1:
            if c == 1 or dn == 1:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 2:
            if c == 1:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 3:
            if c == 1:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 4:
            if c % 2 == 0:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 5:
            if c == 1:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 6:
            if c == 1 or dn == 6:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 7:
            if c == 1:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 8:
            if c % 2 == 0:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
        elif num == 9:
            if c == 1:
                vibrations[num] = "+"
            else:
                vibrations[num] = "-"
                
    return vibrations

def calculate_mahadasha_timeline(bn: int, dob: date, target_date: date) -> Dict[str, Any]:
    """
    Calculates the Mahadasha timeline starting from DOB with BN.
    Duration of MD = number itself (1=1yr, 2=2yrs ... 9=9yrs). Total cycle = 45 years.
    Sequence: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 (cyclic).
    """
    periods = []
    curr_start = dob
    curr_num = bn
    
    # Generate MD periods for 90 years (2 complete 45-year cycles)
    for _ in range(18):
        duration_years = curr_num
        try:
            curr_end = date(curr_start.year + duration_years, curr_start.month, curr_start.day)
        except ValueError:
            # Handle Feb 29
            curr_end = date(curr_start.year + duration_years, curr_start.month, curr_start.day - 1)
            
        periods.append({
            "number": curr_num,
            "duration": duration_years,
            "start": curr_start,
            "end": curr_end,
            "start_str": curr_start.strftime("%d/%m/%Y"),
            "end_str": curr_end.strftime("%d/%m/%Y"),
            "is_active": curr_start <= target_date < curr_end
        })
        curr_start = curr_end
        curr_num = (curr_num % 9) + 1

    active_md = next((p for p in periods if p["is_active"]), periods[0])
    return {
        "periods": periods[:10],
        "active_md": active_md
    }

def calculate_antardasha(dob: date, target_date: date) -> Dict[str, Any]:
    """
    Antardasha (AD): 1-year period from last birthday to next birthday.
    Formula: reduce(Date + Month + Last2DigitsOfLastBirthdayYear + DayNumber)
    """
    # Find most recent birthday on or before target_date
    candidate_bday_year = target_date.year
    try:
        candidate_bday = date(candidate_bday_year, dob.month, dob.day)
    except ValueError:
        candidate_bday = date(candidate_bday_year, dob.month, dob.day - 1)
        
    if candidate_bday > target_date:
        last_bday_year = candidate_bday_year - 1
        try:
            last_bday = date(last_bday_year, dob.month, dob.day)
        except ValueError:
            last_bday = date(last_bday_year, dob.month, dob.day - 1)
    else:
        last_bday_year = candidate_bday_year
        last_bday = candidate_bday
        
    try:
        next_bday = date(last_bday_year + 1, dob.month, dob.day)
    except ValueError:
        next_bday = date(last_bday_year + 1, dob.month, dob.day - 1)
        
    weekday_code = get_day_number(last_bday.weekday())
    yr_2digits = last_bday_year % 100
    
    ad_sum = dob.day + dob.month + yr_2digits + weekday_code
    ad_number = reduce_to_single_digit(ad_sum)
    
    return {
        "ad_number": ad_number,
        "start": last_bday,
        "end": next_bday,
        "start_str": last_bday.strftime("%d/%m/%Y"),
        "end_str": next_bday.strftime("%d/%m/%Y"),
        "last_bday_year": last_bday_year,
        "weekday_code": weekday_code
    }

def calculate_pratyantar_dasha(ad_number: int, ad_start: date, target_date: date) -> Dict[str, Any]:
    """
    Pratyantar Dasha (PD):
    Year has 9 sub-periods starting from AD number.
    Duration of each sub-period = Root Number * 8 days.
    (Sum of 1*8 + 2*8 + ... + 9*8 = 360 days).
    """
    pd_periods = []
    curr_start = ad_start
    curr_num = ad_number
    
    for _ in range(9):
        span_days = curr_num * 8
        curr_end = curr_start + timedelta(days=span_days)
        is_active = curr_start <= target_date < curr_end
        pd_periods.append({
            "number": curr_num,
            "duration_days": span_days,
            "start": curr_start,
            "end": curr_end,
            "start_str": curr_start.strftime("%d/%m/%Y"),
            "end_str": curr_end.strftime("%d/%m/%Y"),
            "is_active": is_active
        })
        curr_start = curr_end
        curr_num = (curr_num % 9) + 1
        
    active_pd = next((p for p in pd_periods if p["is_active"]), pd_periods[0])
    return {
        "periods": pd_periods,
        "active_pd": active_pd
    }

def detect_active_yogas(counts: Dict[int, int], vibrations: Dict[int, str], lang: str) -> List[Dict[str, Any]]:
    """Identifies all active planes, verticals, combinations, and special yogas."""
    active_yogas = []
    
    for yoga_id, yoga in YOGA_DEFINITIONS.items():
        req_numbers = yoga["numbers"]
        # Check if all numbers required are present in grid (count > 0)
        is_present = all(counts.get(n, 0) > 0 for n in req_numbers)
        if is_present:
            # Check tone or tags
            tags = [yoga["tag"].get(lang, yoga["tag"]["en"])]
            
            # Check vibrations of constituent numbers
            constituent_vibes = [vibrations.get(n, "+") for n in req_numbers]
            if all(v == "+" for v in constituent_vibes):
                tags.append("Superior (+) / श्रेष्ठ" if lang != "en" else "Superior (+)")
            elif any(v == "-" for v in constituent_vibes):
                tags.append("Mixed / मिश्रित" if lang != "en" else "Mixed Vibrations")
                
            active_yogas.append({
                "id": yoga_id,
                "name": yoga["name"].get(lang, yoga["name"]["en"]),
                "tag": " • ".join(tags),
                "desc": yoga["desc"].get(lang, yoga["desc"]["en"]),
                "numbers": req_numbers
            })
            
    # Raj Yog Check: 3-1-9 present OR 1-7-8 present OR 6-5 present
    has_319 = all(counts.get(n, 0) > 0 for n in [3, 1, 9])
    has_178 = all(counts.get(n, 0) > 0 for n in [1, 7, 8])
    has_65 = all(counts.get(n, 0) > 0 for n in [6, 5])
    
    if (has_319 or has_178 or has_65) and not any(y["id"] == "raj_yog" for y in active_yogas):
        name_map = {
            "en": "Special Imperial Raj Yog (Supreme Auspiciousness)",
            "hi": "विशेष राजयोग (सर्वोच्च ग्रहीय कृपा)",
            "gu": "વિશેષ રાજયોગ (સર્વોચ્ચ ગ્રહીય કૃપા)"
        }
        desc_map = {
            "en": "Strong Raj Yog alignment in the birth chart grants elevated social prestige, magnetic authority, and effortless luxury during favorable Dasha periods.",
            "hi": "जन्म चक्र में राजयोग का निर्माण जातक को समाज में उच्च मान-प्रतिष्ठा, प्रशासनिक अधिकार और अनुकूल दशाओं में असीम ऐश्वर्य प्रदान करता है।",
            "gu": "જન્મ કુંડળીમાં રાજયોગનું નિર્માણ જાતકને સમાજમાં ઉચ્ચ માન-પ્રતિષ્ઠા, અધિકાર અને સાનુકૂળ દશાઓમાં ભવ્ય ઐશ્વર્ય પ્રદાન કરે છે."
        }
        active_yogas.insert(0, {
            "id": "raj_yog",
            "name": name_map.get(lang, name_map["en"]),
            "tag": "Imperial Alignment / राजयोग",
            "desc": desc_map.get(lang, desc_map["en"]),
            "numbers": [1, 8] if has_178 else ([3, 1, 9] if has_319 else [6, 5])
        })
        
    return active_yogas

def generate_life_predictions(
    bn: int, dn: int, counts: Dict[int, int], vibrations: Dict[int, str],
    active_yogas: List[Dict[str, Any]], active_md: int, active_ad: int, lang: str
) -> Dict[str, Dict[str, Any]]:
    """
    Generates domain-specific predictions for:
    1. Finance & Wealth
    2. Property & Real Estate
    3. Vehicles
    4. Education & Intellectual Strengths
    5. Travel & Foreign Settlement
    6. Litigation, Disputes & Court Cases
    7. Marriage, Harmony & Relationships
    8. Health & Physical Well-being
    """
    preds = {}
    
    # ---------------- 1. Finance & Wealth ----------------
    # Standard of living (+1, +5, +8, DN 6)
    sol_score = 0
    if vibrations.get(1) == "+": sol_score += 1
    if vibrations.get(5) == "+": sol_score += 1
    if vibrations.get(8) == "+": sol_score += 1
    if dn == 6: sol_score += 1
    
    # MD/AD beneficial check: +3, +5, +6, +8
    is_beneficial_dasha = active_md in [3, 5, 6, 8] or active_ad in [3, 5, 6, 8]
    is_challenging_dasha = active_md in [4, 8, 9] and vibrations.get(active_md) == "-"
    
    if lang == "hi":
        fin_tier = "उत्कृष्ट (उच्चतम जीवन स्तर)" if sol_score >= 2 else ("मध्यम एवं प्रगतिशील" if sol_score == 1 else "परिश्रम साध्य एवं संतुलित")
        fin_desc = f"आपके वैदिक चक्र में मानक जीवन स्तर का स्तर {fin_tier} है। "
        if is_beneficial_dasha:
            fin_desc += f"वर्तमान में सक्रिय दशा चक्र (महादशा {active_md} एवं अंतर्दशा {active_ad}) धन संचय, नए व्यापारिक अनुबंध और वित्तीय स्थिरता के लिए अत्यंत अनुकूल है। "
        else:
            fin_desc += f"वर्तमान समय में वित्तीय निवेशों में सतर्कता बरतें; अचानक किए गए सट्टेबाजी या जोखिम भरे निवेश से बचें। "
        if counts.get(8, 0) >= 2 and vibrations.get(8) == "+":
            fin_desc += "अंक 8 की दोहरी उपस्थिति (88) अचल संपत्ति, दीर्घकालिक निवेश और विशाल वित्तीय साम्राज्य निर्माण का सशक्त संकेत देती है।"
        elif counts.get(2, 0) >= 1:
            fin_desc += "अंक 2 की उपस्थिति के कारण तरल धन के प्रवाह में उतार-चढ़ाव संभव है; नियमित बचत की आदत बनाए रखें।"
    elif lang == "gu":
        fin_tier = "ઉત્કૃષ્ટ (ઉચ્ચ જીવનધોરણ)" if sol_score >= 2 else ("મધ્યમ અને પ્રગતિશીલ" if sol_score == 1 else "પરિશ્રમ આધારિત અને સંતુલિત")
        fin_desc = f"આપના વૈદિક ચક્ર મુજબ જીવનધોરણનું સ્તર {fin_tier} છે. "
        if is_beneficial_dasha:
            fin_desc += f"હાલમાં સક્રિય દશા ચક્ર (મહાદશા {active_md} અને અંતર્દશા {active_ad}) નાણાકીય બચત, વેપાર વૃદ્ધિ અને આર્થિક મજબૂતી માટે ખૂબ શુભ છે. "
        else:
            fin_desc += f"હાલના સમયમાં નાણાકીય રોકાણોમાં સાવચેતી રાખવી; સટ્ટાકીય કે ઉતાવળા જોખમી રોકાણોથી દૂર રહેવું. "
        if counts.get(8, 0) >= 2 and vibrations.get(8) == "+":
            fin_desc += "અંક 8 ની બેવડી હાજરી (88) સ્થાવર મિલકતો, દીર્ઘકાલીન રોકાણ અને વિરાટ આર્થિક સામ્રાજ્ય નિર્માણની મજબૂત સંભાવના દર્શાવે છે."
        elif counts.get(2, 0) >= 1:
            fin_desc += "અંક 2 ની હાજરીને કારણે રોકડ નાણાંના પ્રવાહમાં વધ-ઘટ થઈ શકે છે; નિયમિત બચત કરવાની ટેવ પાડવી."
    else:
        fin_tier = "High (Affluent Standard of Living)" if sol_score >= 2 else ("Moderate & Progressive" if sol_score == 1 else "Labor-Driven & Balanced")
        fin_desc = f"Your Vedic chart reflects a financial lifestyle baseline of: {fin_tier}. "
        if is_beneficial_dasha:
            fin_desc += f"Currently active Dasha periods (MD {active_md} and AD {active_ad}) strongly favor wealth creation, lucrative business expansion, and liquidity. "
        else:
            fin_desc += f"Exercise disciplined prudence in capital investments during the current phase; avoid uncalculated speculations. "
        if counts.get(8, 0) >= 2 and vibrations.get(8) == "+":
            fin_desc += "The double activation of Number 8 (88) creates tremendous potential for immovable assets, industrial growth, and generational wealth."
        elif counts.get(2, 0) >= 1:
            fin_desc += "Presence of Number 2 indicates fluctuating cash liquidity; maintaining automated conservative savings is highly advised."

    preds["finance"] = {
        "title": UI_TEXT[lang]["pred_finance"],
        "tier": fin_tier,
        "desc": fin_desc
    }
    
    # ---------------- 2. Property & Real Estate ----------------
    has_pos_1 = vibrations.get(1) == "+"
    has_pos_8 = vibrations.get(8) == "+"
    has_neg_1 = vibrations.get(1) == "-"
    prop_favorable_now = (active_md in [1, 5, 6, 8] or active_ad in [1, 5, 4, 8])
    
    if lang == "hi":
        prop_status = "अत्यधिक प्रबल (भूमि-भवन सुख)" if (has_pos_1 or has_pos_8) else "परिश्रम उपरांत मध्यम योग"
        prop_desc = f"संपत्ति अर्जन का योग: {prop_status}। "
        if has_pos_8:
            prop_desc += "अंक 8 की शुभ ऊर्जा आपको स्वतंत्र भूखंड, मकान अथवा व्यावसायिक संपत्ति का स्थायी स्वामित्व प्रदान करती है। "
        if has_neg_1:
            prop_desc += "चार्ट में -1 स्पंदन होने के कारण संपत्ति क्रय करते समय जीवनसाथी या माता के संयुक्त नाम पर रजिस्ट्री कराना अति शुभ व निर्विवाद रहेगा। "
        if prop_favorable_now:
            prop_desc += f"वर्तमान दशा चक्र (MD {active_md} / AD {active_ad}) नई संपत्ति के क्रय अथवा निर्माण कार्य प्रारंभ करने हेतु अत्यंत अनुकूल समय है।"
    elif lang == "gu":
        prop_status = "અત્યંત પ્રબળ (જમીન-મકાન સુખ)" if (has_pos_1 or has_pos_8) else "પરિશ્રમ બાદ મધ્યમ યોગ"
        prop_desc = f"મિલકત પ્રાપ્તિનો યોગ: {prop_status}. "
        if has_pos_8:
            prop_desc += "અંક 8 ની શુભ ઊર્જા આપને સ્વતંત્ર પ્લોટ, મકાન કે કોમર્શિયલ મિલકતનું કાયમી માલિકીપણું આપે છે. "
        if has_neg_1:
            prop_desc += "કુંડળીમાં -1 સ્પંદન હોવાથી મિલકત ખરીદતી વખતે પત્ની કે માતાના સંયુક્ત નામે દસ્તાવેજ કરવો જેથી કૌટુંબિક વિવાદો ટળે. "
        if prop_favorable_now:
            prop_desc += f"હાલનું દશા ચક્ર (MD {active_md} / AD {active_ad}) નવું મકાન ખરીદવા કે બાંધકામ શરૂ કરવા માટે ઉત્તમ તક પૂરી પાડે છે."
    else:
        prop_status = "Highly Favorable (Strong Real Estate Potential)" if (has_pos_1 or has_pos_8) else "Moderate (Requires Sustained Effort)"
        prop_desc = f"Real Estate Acquisition Potential: {prop_status}. "
        if has_pos_8:
            prop_desc += "Auspicious activation of Number 8 grants enduring mastery over land, commercial spaces, and residential assets. "
        if has_neg_1:
            prop_desc += "Due to -1 vibration, purchasing properties in joint ownership with your spouse or mother is recommended to avoid unnecessary disputes. "
        if prop_favorable_now:
            prop_desc += f"The currently active Dasha cycle (MD {active_md} / AD {active_ad}) marks a prime window for acquiring property or initiating construction."

    preds["property"] = {
        "title": UI_TEXT[lang]["pred_property"],
        "status": prop_status,
        "desc": prop_desc
    }
    
    # ---------------- 3. Vehicle Acquisition ----------------
    has_6 = counts.get(6, 0) > 0
    has_4 = counts.get(4, 0) > 0
    veh_active_now = active_md in [6, 4, 5] or active_ad in [6, 4, 5]
    
    if lang == "hi":
        veh_desc = "शुक्र (6) और राहु (4) वाहन सुख के प्रमुख कारक हैं। "
        if veh_active_now:
            veh_desc += f"वर्तमान दशा चक्र (MD {active_md} / AD {active_ad}) नए वाहन के क्रय और उन्नयन (अपग्रेड) के लिए बहुत शुभ है। "
        else:
            veh_desc += "वाहन क्रय करते समय अपनी शुभ संख्या (5, 6 या 1) के कुल योग वाली वाहन नंबर प्लेट का चयन करें। "
        veh_desc += "वाहन चलाते समय गति नियंत्रण रखें और गति में अचानक ब्रेक या उतावलेपन से बचें।"
    elif lang == "gu":
        veh_desc = "શુક્ર (6) અને રાહુ (4) વાહન સુખના મુખ્ય કારક છે. "
        if veh_active_now:
            veh_desc += f"હાલનું દશા ચક્ર (MD {active_md} / AD {active_ad}) નવું વાહન ખરીદવા અને અપગ્રેડ કરવા માટે ખૂબ અનુકૂળ સમય છે. "
        else:
            veh_desc += "વાહન ખરીદતી વખતે આપના અનુકૂળ અંકો (5, 6 અથવા 1) ના સરવાળાવાળી નંબર પ્લેટ પસંદ કરવી હિતાવહ છે. "
        veh_desc += "વાહન ચલાવતી વખતે અતિ-ઝડપ ટાળવી અને ટ્રાફિક નિયમોનું ચુસ્ત પાલન કરવું."
    else:
        veh_desc = "Venus (6) and Rahu (4) are prime catalysts for automobile acquisition. "
        if veh_active_now:
            veh_desc += f"The current Dasha period (MD {active_md} / AD {active_ad}) represents an auspicious window for purchasing or upgrading personal vehicles. "
        else:
            veh_desc += "When registering a new vehicle, choose a license plate number whose digits sum to your friendly numbers (5, 6, or 1). "
        veh_desc += "Maintain defensive driving discipline and avoid aggressive speeding."

    preds["vehicle"] = {
        "title": UI_TEXT[lang]["pred_vehicle"],
        "desc": veh_desc
    }
    
    # ---------------- 4. Education & Intellect ----------------
    edu_prof = PROFESSIONS_INFO[bn][lang]
    if lang == "hi":
        edu_desc = f"आपकी बौद्धिक संरचना में मूलांक {bn} का गहरा प्रभाव है। आप गहन चिंतन, तकनीकी विश्लेषण और रणनीतिक कार्यों में असाधारण दक्षता रखते हैं। आपके लिए सर्वाधिक अनुकूल शैक्षणिक एवं व्यावसायिक क्षेत्र हैं: {edu_prof}"
    elif lang == "gu":
        edu_desc = f"આપની બૌદ્ધિક ક્ષમતા પર મૂળાંક {bn} નો વિશેષ પ્રભાવ છે. આપ ઊંડું ચિંતન, ટેકનિકલ વિશ્લેષણ અને આયોજનબદ્ધ કાર્યોમાં કુદરતી નિપુણતા ધરાવો છો. આપના માટે સૌથી યોગ્ય અભ્યાસ અને કાર્યક્ષેત્રો: {edu_prof}"
    else:
        edu_desc = f"Your intellectual framework is strongly shaped by Root Number {bn}. You possess a sharp analytical mindset suited for structured, deep problem solving. Best aligned fields of study and profession: {edu_prof}"

    preds["education"] = {
        "title": UI_TEXT[lang]["pred_education"],
        "desc": edu_desc
    }
    
    # ---------------- 5. Travel & Foreign Settlement ----------------
    has_7 = counts.get(7, 0) > 0
    is_dn_7 = dn == 7
    travel_active_now = active_md in [7, 4, 5] or active_ad in [7, 4, 5]
    
    if lang == "hi":
        if is_dn_7:
            travel_desc = "भाग्यांक 7 होने के कारण आपका जीवन विदेश गमन, विदेशी व्यापार अथवा सुदूर स्थानों पर स्थायी निवास (पीआर/नागरिकता) के लिए अत्यधिक प्रबल है।"
        elif has_7:
            travel_desc = "अंक 7 की उपस्थिति विकसित देशों की आरामदायक व आध्यात्मिक विदेश यात्राओं का सशक्त योग बनाती है।"
        elif counts.get(4, 0) > 0:
            travel_desc = "अंक 4 की उपस्थिति व्यावसायिक व तकनीकी कारणों से विदेश या अन्य राज्यों में यात्राओं का योग बनाती है (प्रारंभ में कागजी अड़चनों के उपरांत सफलता)।"
        else:
            travel_desc = "सामान्य यात्राओं का योग है। विदेश यात्रा हेतु अनुकूल दशा (7, 4 या 5) के सक्रिय होने की प्रतीक्षा करें।"
        if travel_active_now:
            travel_desc += f" वर्तमान दशा चक्र (MD {active_md} / AD {active_ad}) लंबी दूरी की यात्राओं एवं स्थानांतरण के लिए सक्रिय है।"
    elif lang == "gu":
        if is_dn_7:
            travel_desc = "ભાગ્યાંક 7 હોવાના કારણે આપના જીવનમાં વિદેશ ગમન, વિદેશી વેપાર અથવા કાયમી વિદેશ વસવાટ (PR) ના ઉત્તમ યોગ છે."
        elif has_7:
            travel_desc = "અંક 7 ની હાજરી વિકસિત દેશોની આરામદાયક, ધંધાકીય કે આધ્યાત્મિક વિદેશ યાત્રાઓના પ્રબળ યોગ બનાવે છે."
        elif counts.get(4, 0) > 0:
            travel_desc = "અંક 4 ની હાજરી ટેકનિકલ અને વ્યવસાયિક કારણોસર વિદેશ પ્રવાસના યોગ દર્શાવે છે (શરૂઆતમાં કાગળિયાની સામાન્ય અડચણો બાદ સફળતા)."
        else:
            travel_desc = "સામાન્ય મુસાફરીના યોગ છે. વિશેષ વિદેશ ગમન માટે સાનુકૂળ દશા (7, 4 અથવા 5) ની સક્રિયતા આવશ્યક છે."
        if travel_active_now:
            travel_desc += f" હાલનું દશા ચક્ર (MD {active_md} / AD {active_ad}) લાંબા અંતરના પ્રવાસ અને સ્થળાંતર માટે સક્રિય છે."
    else:
        if is_dn_7:
            travel_desc = "Destiny Number 7 creates exceptionally strong prospects for international relocation, foreign PR/citizenship, and cross-border commercial success."
        elif has_7:
            travel_desc = "Presence of Number 7 indicates luxury journeys to developed countries, cultural research, and restorative spiritual travels."
        elif counts.get(4, 0) > 0:
            travel_desc = "Number 4 stimulates technical and business-driven overseas travel (achieved smoothly after initial documentation perseverance)."
        else:
            travel_desc = "Standard domestic and professional travel indicated. Long-distance global travel activates during periods of 7, 4, or 5."
        if travel_active_now:
            travel_desc += f" Currently active Dasha periods (MD {active_md} / AD {active_ad}) actively stimulate travel, relocations, or foreign linkages."

    preds["travel"] = {
        "title": UI_TEXT[lang]["pred_travel"],
        "desc": travel_desc
    }
    
    # ---------------- 6. Litigation, Disputes & Court Cases ----------------
    has_9_4 = counts.get(9, 0) > 0 and counts.get(4, 0) > 0
    has_5_4 = counts.get(5, 0) > 0 and counts.get(4, 0) > 0
    has_neg_6 = vibrations.get(6) == "-"
    has_stabilizer = vibrations.get(7) == "+" or vibrations.get(8) == "+"
    
    is_litigation_risk = (has_9_4 or has_5_4 or has_neg_6)
    
    if lang == "hi":
        if is_litigation_risk:
            lit_desc = "चार्ट में 9 और 4 अथवा 5 और 4 की उपस्थिति विवादों व कानूनी कागजी कार्यवाहियों में विशेष सावधानी का संकेत देती है। वैदिक नियम के अनुसार, जब यह संयोजन लगातार 2 वर्ष या अधिक समय तक दशा में सक्रिय रहता है, तभी न्यायालयीन विवाद उत्पन्न होता है। "
            if has_stabilizer:
                lit_desc += "सौभाग्य से, आपके चक्र में स्थिरक ग्रह प्रभाव (7/8) उपस्थित हैं जो अंततः कूटनीतिक समझौतों या निष्पक्ष न्याय के माध्यम से विजय दिलाते हैं।"
            else:
                lit_desc += "अस्पष्ट अनुबंधों पर हस्ताक्षर करने से बचें और किसी की जमानत देने से पूर्णतः दूर रहें।"
        else:
            lit_desc = "जन्म चक्र कानूनी मामलों में सुरक्षित व संतुलित है। किसी गंभीर अदालती विवाद की संभावना नगण्य है। अनुबंधों में पारदर्शिता बनाए रखें।"
    elif lang == "gu":
        if is_litigation_risk:
            lit_desc = "કુંડળીમાં 9 અને 4 અથવા 5 અને 4 ની હાજરી કાનૂની દસ્તાવેજો અને વિવાદોમાં સાવચેત રહેવાનો સંકેત આપે છે. વૈદિક નિયમ મુજબ જો આ યોગ સતત 2 કે વધુ વર્ષ સુધી દશામાં સક્રિય રહે તો જ કોર્ટ-કચેરીના વિવાદ બને છે. "
            if has_stabilizer:
                lit_desc += "સદનસીબે આપની કુંડળીમાં સ્થિરક અંકો (7/8) હાજર હોવાથી મધ્યસ્થી કે ધીરજપૂર્વક ન્યાય દ્વારા મામલો આપની તરફેણમાં થાળે પડે છે."
            else:
                lit_desc += "અસ્પષ્ટ કરારો પર સહી કરવાનું ટાળવું અને કોઈના જામીન બનવાથી દૂર રહેવું."
        else:
            lit_desc = "જન્મ ચક્ર કાનૂની બાબતોમાં સુરક્ષિત અને શાંતિપૂર્ણ છે. કોઈ ગંભીર કોર્ટ કેસ કે દાવાની શક્યતા નથી. પારદર્શક વ્યવહારો જાળવવા."
    else:
        if is_litigation_risk:
            lit_desc = "Presence of combinations like (9 & 4) or (5 & 4) counsels vigilance regarding legal agreements and partnership documentation. Per Vedic numerology, these trigger court proceedings only when active for 2+ consecutive years in Dasha cycles. "
            if has_stabilizer:
                lit_desc += "Fortunately, stabilizing numbers (+7 / +8) in your matrix act as anchors, facilitating out-of-court settlements or judicial exoneration."
            else:
                lit_desc += "Avoid signing ambiguously worded contracts and strictly refrain from standing surety or guarantor for third parties."
        else:
            lit_desc = "The birth grid is well-shielded against legal controversies. No persistent litigation indicators are observed. Maintain customary contractual transparency."

    preds["litigation"] = {
        "title": UI_TEXT[lang]["pred_litigation"],
        "desc": lit_desc
    }
    
    # ---------------- 7. Marriage, Harmony & Relationships ----------------
    if lang == "hi":
        rel_desc = "दांपत्य जीवन में सुख और सामंजस्य बनाए रखने हेतु खुले व पारदर्शी संवाद की आवश्यकता है। अहंकार (-1) या अत्यधिक कार्यव्यस्तता (-8) को वैवाहिक जीवन के आड़े न आने दें। जीवनसाथी की भावनाओं का सम्मान करने और शुक्रवार को उपहार देने से दांपत्य में मधुरता बनी रहेगी।"
    elif lang == "gu":
        rel_desc = "દામ્પત્ય જીવનમાં સુખ અને સંવાદિતા જાળવવા માટે ખુલ્લા અને પારદર્શક સંવાદની જરૂર છે. અહંકાર (-1) કે વધુ પડતા કામના બોજ (-8) ને લગ્નજીવન વચ્ચે ન આવવા દો. જીવનસાથીની લાગણીઓનું સન્માન કરવાથી અને શુક્રવારે ભેટ આપવાથી સંબંધોમાં મધુરતા જળવાશે."
    else:
        rel_desc = "Domestic harmony thrives when ego assertions (-1) and excessive workaholism (-8) are consciously set aside at home. Cultivating open communication, appreciating your spouse's emotional perspective, and honoring Venus (6) safeguards mutual love and marital longevity."

    preds["relationship"] = {
        "title": UI_TEXT[lang]["pred_relationship"],
        "desc": rel_desc
    }
    
    # ---------------- 8. Health & Vitality ----------------
    health_organs = {
        1: {"en": "Heart, eyes, blood pressure, vitality, headaches, spinal vertebrae.", "hi": "हृदय, नेत्र ज्योति, रक्तचाप, जीवन शक्ति, सिरदर्द एवं रीढ़ की हड्डी।", "gu": "હૃદય, આંખોનું તેજ, બ્લડ પ્રેશર, જીવનશક્તિ, માથાનો દુખાવો, કરોડરજ્જુ."},
        2: {"en": "Stomach, digestive tracts, water retention, insomnia, mental anxiety.", "hi": "आमाशय (पेट), पाचन क्रिया, जल संतुलन, अनिद्रा, मानसिक चिंता व अवसाद।", "gu": "હોજરી, પાચનક્રિયા, જળ સંતુલન, અનિદ્રા, માનસિક ચિંતા અને મૂડ સ્વિંગ્સ."},
        3: {"en": "Liver, gallbladder, arterial blood circulation, diabetes, cholesterol.", "hi": "यकृत (लिवर), पित्ताशय, धमनियों का रक्त प्रवाह, मधुमेह एवं कोलेस्ट्रॉल।", "gu": "લીવર, પિત્તાશય, લોહીનું ભ્રમણ, ડાયાબિટીસ અને કોલેસ્ટ્રોલ."},
        4: {"en": "Sudden ailments, respiratory organs, knees, nervous tension, unexplained fatigue.", "hi": "अचानक होने वाले रोग, श्वसन तंत्र, घुटने, स्नायु तनाव व रहस्यमयी कमजोरी।", "gu": "અચાનક થતા રોગો, શ્વસનતંત્ર, ઢીંચણ, સ્નાયુબદ્ધ તણાવ અને અજાણી નબળાઈ."},
        5: {"en": "Nervous system, speech organs, skin allergies, mental restlessness, stammering.", "hi": "तंत्रिका तंत्र, वाक् इंद्रियां, त्वचा संबंधी संवेदनशीलता, मानसिक चंचलता।", "gu": "ચેતાતંત્ર (નર્વસ સિસ્ટમ), વાણીના અંગો, ચામડીની એલર્જી, અજંપો."},
        6: {"en": "Kidneys, urinary tract, reproductive vitality, throat, throat vocal cords, diabetes.", "hi": "वृक्क (किडनी), मूत्र मार्ग, प्रजनन प्रणाली, गला, स्वर तंत्र एवं मधुमेह।", "gu": "કિડની, મૂત્રાશય, પ્રજનન તંત્ર, ગળું, વોકલ કોર્ડ્સ અને ડાયાબિટીસ."},
        7: {"en": "Skin allergies, psychic sensitivity, lymphatic circulation, unexplained fevers.", "hi": "त्वचा विकार, मानसिक संवेदनशीलता, लसिका तंत्र (लिम्फैटिक), अकारण थकान।", "gu": "ચામડીની તકલીફો, માનસિક સંવેદનશીલતા, લસિકા તંત્ર, અકારણ થાક."},
        8: {"en": "Joints, knees, bones, teeth, chronic rheumatism, back stiffness, paralysis risk.", "hi": "जोड़, घुटने, अस्थि तंत्र (हड्डियां), दांत, वात रोग, पीठ दर्द एवं जकड़न।", "gu": "સાંધા, ઢીંચણ, હાડકાં, દાંત, વાયુ (સંધિવા), કમરનો દુખાવો અને જકડન."},
        9: {"en": "Blood purity, high blood pressure, cuts, burns, surgeries, piles, inflammations.", "hi": "रक्त विकार, उच्च रक्तचाप, चोट, जलन, शल्य चिकित्सा (सर्जरी), बवासीर व सूजन।", "gu": "લોહીની અશુદ્ધિ, હાઇ બ્લડ પ્રેશર, કાપા-ઈજા, દાઝવું, સર્જરીનો યોગ, બવાસીર."}
    }
    
    has_neg_9 = vibrations.get(9) == "-"
    has_neg_2 = vibrations.get(2) == "-"
    
    if lang == "hi":
        hlth_desc = f"मूलांक {bn} के अनुसार शरीर के संवेदनशील अंग हैं: {health_organs[bn]['hi']} "
        if has_neg_9:
            hlth_desc += "चार्ट में -9 स्पंदन होने के कारण रक्तचाप, आकस्मिक चोटों अथवा शल्य चिकित्सा (सर्जरी) से बचाव हेतु सुरक्षात्मक आचरण अपनाएं। "
        if has_neg_2:
            hlth_desc += "मानसिक शांति, तनाव मुक्ति और अनिद्रा से बचने के लिए नियमित प्राणायाम व ध्यान आवश्यक है। "
        hlth_desc += "प्रातःकाल तांबे के बर्तन में रखा जल पिएं और गरिष्ठ तैलीय भोजन से बचें।"
    elif lang == "gu":
        hlth_desc = f"મૂળાંક {bn} મુજબ શરીરના સંવેદનશીલ અંગો છે: {health_organs[bn]['gu']} "
        if has_neg_9:
            hlth_desc += "કુંડળીમાં -9 સ્પંદન હોવાથી બ્લડ પ્રેશર, અચાનક ઇજા કે સર્જરીથી બચવા માટે શાંતિ અને સાવચેતીભર્યું વર્તન રાખવું. "
        if has_neg_2:
            hlth_desc += "માનસિક શાંતિ અને અનિદ્રાથી બચવા માટે રોજેરોજ પ્રાણાયામ અને ધ્યાન કરવાની ખાસ ભલામણ છે. "
        hlth_desc += "સવારે તાંબાના વાસણમાં રાખેલું પાણી પીવું અને વધુ પડતો તેલ-મસાલાવાળો ખોરાક ટાળવો."
    else:
        hlth_desc = f"Per Root Number {bn}, prime anatomical zones of physiological sensitivity include: {health_organs[bn]['en']} "
        if has_neg_9:
            hlth_desc += "Presence of -9 vibration advises vigilance against blood pressure spikes, lacerations, or surgical intervention; practice calming routines. "
        if has_neg_2:
            hlth_desc += "To counter psychosomatic stress and insomnia, daily pranayama (breathwork) and meditation are strongly recommended. "
        hlth_desc += "Consume morning water stored in a copper vessel and avoid excessively rich, greasy diets."

    preds["health"] = {
        "title": UI_TEXT[lang]["pred_health"],
        "desc": hlth_desc
    }
    
    return preds

def compile_full_numerology_profile(
    name: str, dob_str: str, gender: str = "Male",
    target_date_str: str = None, lang: str = "en",
    consultant_notes: str = ""
) -> Dict[str, Any]:
    """
    Main entry point for generating the complete Vedic Numerology Profile.
    Accepts DOB string (YYYY-MM-DD or DD/MM/YYYY) and returns a complete analytical payload.
    """
    # Parse DOB
    if "-" in dob_str:
        parts = [int(p) for p in dob_str.split("-")]
        if parts[0] > 1000: # YYYY-MM-DD
            birth_date = date(parts[0], parts[1], parts[2])
        else: # DD-MM-YYYY
            birth_date = date(parts[2], parts[1], parts[0])
    elif "/" in dob_str:
        parts = [int(p) for p in dob_str.split("/")]
        if parts[0] > 1000: # YYYY/MM/DD
            birth_date = date(parts[0], parts[1], parts[2])
        else: # DD/MM/YYYY
            birth_date = date(parts[2], parts[1], parts[0])
    else:
        raise ValueError("Invalid DOB format. Use YYYY-MM-DD or DD/MM/YYYY.")
        
    # Target date for Dasha forecast (defaults to today)
    if target_date_str:
        if "-" in target_date_str:
            tp = [int(p) for p in target_date_str.split("-")]
            target_date = date(tp[0], tp[1], tp[2]) if tp[0] > 1000 else date(tp[2], tp[1], tp[0])
        else:
            tp = [int(p) for p in target_date_str.split("/")]
            target_date = date(tp[0], tp[1], tp[2]) if tp[0] > 1000 else date(tp[2], tp[1], tp[0])
    else:
        target_date = date.today()
        
    # Calculations
    day, month, year = birth_date.day, birth_date.month, birth_date.year
    bn = calculate_basic_number(day)
    dn = calculate_destiny_number(day, month, year)
    grid_info = calculate_vedic_grid(day, month, year)
    vibrations = evaluate_vibrations(grid_info["counts"], dn)
    
    # Dasha calculations
    md_info = calculate_mahadasha_timeline(bn, birth_date, target_date)
    ad_info = calculate_antardasha(birth_date, target_date)
    pd_info = calculate_pratyantar_dasha(ad_info["ad_number"], ad_info["start"], target_date)
    
    # Active Yogas
    active_yogas = detect_active_yogas(grid_info["counts"], vibrations, lang)
    
    # Life Predictions
    predictions = generate_life_predictions(
        bn, dn, grid_info["counts"], vibrations, active_yogas,
        md_info["active_md"]["number"], ad_info["ad_number"], lang
    )
    
    # Remedies Assembly
    moolank_remedy = NUMBER_REMEDIES[bn]
    bhagyank_remedy = NUMBER_REMEDIES[dn]
    
    # Weekday Name Localization
    weekdays_map = {
        0: {"en": "Monday", "hi": "सोमवार", "gu": "સોમવાર"},
        1: {"en": "Tuesday", "hi": "मंगलवार", "gu": "મંગળવાર"},
        2: {"en": "Wednesday", "hi": "बुधवार", "gu": "બુધવાર"},
        3: {"en": "Thursday", "hi": "गुरुवार", "gu": "ગુરુવાર"},
        4: {"en": "Friday", "hi": "शुक्रवार", "gu": "શુક્રવાર"},
        5: {"en": "Saturday", "hi": "शनिवार", "gu": "શનિવાર"},
        6: {"en": "Sunday", "hi": "रविवार", "gu": "રવિવાર"}
    }
    weekday_name = weekdays_map[birth_date.weekday()][lang]
    
    # Build Vibration Descriptions
    vibration_list = []
    for num in range(1, 10):
        c = grid_info["counts"].get(num, 0)
        if c > 0:
            vibe_type = vibrations.get(num, "+")
            desc_key = "pos" if vibe_type == "+" else "neg"
            desc_text = VIBRATION_DETAILS[num][desc_key][lang]
            vibration_list.append({
                "number": num,
                "count": c,
                "type": vibe_type,
                "type_label": UI_TEXT[lang]["positive"] if vibe_type == "+" else UI_TEXT[lang]["negative"],
                "text": desc_text
            })

    # Name Numerology (Namank)
    namank = calculate_name_number(name)
    name_harmony = evaluate_name_harmony(namank, bn, dn, lang)
    
    # Auspicious Compass & Friendship Matrix
    compass = {
        "friendly_nums": PLANET_INFO[bn][lang]["friendly_nums"],
        "neutral_nums": PLANET_INFO[bn][lang]["neutral_nums"],
        "enemy_nums": PLANET_INFO[bn][lang]["enemy_nums"],
        "direction": PLANET_INFO[bn][lang]["direction"],
        "metal": PLANET_INFO[bn][lang]["metal"],
    }

    # Consolidated Result Payload
    return {
        "consultant": {
            "name": CONSULTANT_INFO["name"],
            "phone": CONSULTANT_INFO["phone"],
            "phone_raw": CONSULTANT_INFO["phone_raw"],
            "email": CONSULTANT_INFO["email"],
            "title": CONSULTANT_INFO["title"][lang],
            "copyright": CONSULTANT_INFO["copyright"][lang]
        },
        "client": {
            "name": name,
            "dob": birth_date.strftime("%d/%m/%Y"),
            "dob_iso": birth_date.isoformat(),
            "weekday": weekday_name,
            "gender": gender,
            "target_date": target_date.strftime("%d/%m/%Y"),
            "target_year": target_date.year,
            "lang": lang,
            "consultant_notes": consultant_notes,
            "namank": namank,
            "name_harmony": name_harmony
        },
        "core_numbers": {
            "bn": bn,
            "dn": dn,
            "namank": namank,
            "bn_planet": PLANET_INFO[bn][lang]["planet"],
            "dn_planet": PLANET_INFO[dn][lang]["planet"],
            "favourable_nums": PLANET_INFO[bn][lang]["favourable_nums"],
            "favourable_days": PLANET_INFO[bn][lang]["days"],
            "favourable_colors": PLANET_INFO[bn][lang]["colors"],
            "gemstone": PLANET_INFO[bn][lang]["gem"]
        },
        "compass": compass,
        "grid": grid_info,
        "vibrations": vibration_list,
        "moolank_qualities": NUMBER_QUALITIES[bn][lang],
        "moolank_precautions": NUMBER_PRECAUTIONS[bn][lang],
        "bhagyank_qualities": NUMBER_QUALITIES[dn][lang],
        "bhagyank_precautions": NUMBER_PRECAUTIONS[dn][lang],
        "dasha": {
            "active_md": md_info["active_md"],
            "active_ad": ad_info,
            "active_pd": pd_info["active_pd"],
            "md_timeline": md_info["periods"]
        },
        "yogas": active_yogas,
        "predictions": predictions,
        "remedies": {
            "moolank_gem": moolank_remedy["gem"][lang],
            "moolank_crystal": moolank_remedy["crystal"][lang],
            "moolank_mantra": moolank_remedy["mantra"][lang],
            "moolank_fasting": moolank_remedy["fasting"][lang],
            "moolank_donation": moolank_remedy["donation"][lang],
            "moolank_seva": moolank_remedy["seva"][lang],
            "bhagyank_gem": bhagyank_remedy["gem"][lang],
            "general_health": GENERAL_REMEDIES["health"]["desc"][lang],
            "general_wealth": GENERAL_REMEDIES["wealth"]["desc"][lang],
            "general_harmony": GENERAL_REMEDIES["harmony"]["desc"][lang]
        },
        "ui": UI_TEXT[lang]
    }
