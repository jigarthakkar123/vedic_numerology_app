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
    VIBRATION_DETAILS, AUSPICIOUS_YOGAS_DEFINITIONS, INAUSPICIOUS_YOGAS_DEFINITIONS, YOGA_DEFINITIONS, PROFESSIONS_INFO,
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

def build_vibrations_analysis(
    natal_counts: Dict[int, int],
    dasha_counts: Dict[int, int],
    dn: int,
    lang: str = "en"
) -> Dict[str, Any]:
    """
    Computes both Active Dasha Period Vibrations and Lifetime Natal Baseline Vibrations,
    detecting any dynamic karmic shifts (e.g. 8 turning from - to + via 88, 9 turning from + to - via 99,
    or 7 newly activated via Dasha).
    """
    natal_vib = evaluate_vibrations(natal_counts, dn)
    period_vib = evaluate_vibrations(dasha_counts, dn)
    
    active_period_list = []
    has_shifts = False
    shifts_count = 0
    
    # 1. Build Active Dasha Period List
    for num in range(1, 10):
        dc = dasha_counts.get(num, 0)
        if dc == 0:
            continue
            
        nc = natal_counts.get(num, 0)
        pt = period_vib.get(num, "+")
        nt = natal_vib.get(num, "absent")
        
        # Determine shift status
        if nt == "absent":
            shift_status = "newly_activated"
            shift_badge = UI_TEXT[lang]["shift_newly_activated"]
            has_shifts = True
            shifts_count += 1
        elif nt == "-" and pt == "+":
            shift_status = "neg_to_pos"
            shift_badge = UI_TEXT[lang]["shift_neg_to_pos"]
            has_shifts = True
            shifts_count += 1
        elif nt == "+" and pt == "-":
            shift_status = "pos_to_neg"
            shift_badge = UI_TEXT[lang]["shift_pos_to_neg"]
            has_shifts = True
            shifts_count += 1
        else:
            shift_status = "stable"
            shift_badge = UI_TEXT[lang]["shift_stable"]
            
        # Specific explanatory reasons for common shifts
        shift_reason = ""
        if num == 8 and shift_status == "neg_to_pos":
            shift_reason = {
                "en": "Inborn single 8 is challenging (-8), causing struggles and delays. However, the active Dasha introduces an additional 8, forming an Even 8 (88). Classical Vedic texts confirm that double 8 diminishes negativity, eliminates depression, and strongly triggers massive financial breakthroughs and sharp intuition for this active period.",
                "hi": "जन्म चक्र में एकल 8 कठिन (-8) फलदायी होता है, किंतु वर्तमान दशा प्रभाव से यह सम संख्या (88) बन गया है। वैदिक अंकशास्त्र के अनुसार 88 बनने से शनि का अवसाद व विष समाप्त होता है; यह अवधि विपुल धन लाभ, अचल संपत्ति और अटूट कर्मठता प्रदान करने वाली शुभ (+) बन गई है।",
                "gu": "જન્મ કુંડળીમાં એકલ 8 પડકારરૂપ (-8) હોય છે, પરંતુ વર્તમાન દશાના પ્રભાવથી બેવડો 8 (88) બન્યો છે. વૈદિક નિયમ મુજબ 88 બનવાથી શનિનો વિષાદ શાંત થાય છે; આ સમયગાળો અઢળક આર્થિક પ્રગતિ અને સ્થાવર મિલકત અપાવનારો શુભ (+) બન્યો છે."
            }.get(lang, "")
        elif num == 9 and shift_status == "pos_to_neg":
            shift_reason = {
                "en": "Inborn single 9 is positive (+9). In this active Dasha period, the infusion of another 9 creates Multiple 9s (99). The excessive Martian heat overpowers patience, turning this frequency challenging (-9); native must avoid volcanic temper outbursts, drive cautiously, and maintain disciplined communication during this period.",
                "hi": "जन्म चक्र में एकल 9 सकारात्मक (+9) होता है। वर्तमान दशा प्रभाव से दोहरे 9 (99) की सक्रियता से मंगल की उग्र अग्नि अत्यधिक तीव्र हो गई है, जिससे यह अवधि कठिन (-) हो गई है। जातक को इस वर्ष क्रोध पर नियंत्रण, शांत वाणी और रक्तचाप की सतर्कता रखनी चाहिए।",
                "gu": "જન્મ કુંડળીમાં એકલ 9 સકારાત્મક (+9) હોય છે. વર્તમાન દશાના પ્રભાવથી બેવડો 9 (99) બનવાથી મંગળની અગ્નિ અતિશય વધી ગઈ છે, જેથી આ સમયગાળો પડકારરૂપ (-) બન્યો છે. ક્રોધ પર સંયમ રાખવો અને શાંત વાણી રાખવી હિતાવહ છે."
            }.get(lang, "")
        elif num == 4 and shift_status == "neg_to_pos":
            shift_reason = {
                "en": "Natal odd 4 is volatile (-4). Under this active Dasha, an even number of 4s (44) is established. Classical texts state that double 4 diminishes Bandhan and legal hurdles, enables swift health recovery, and unlocks breakthrough technical innovations.",
                "hi": "जन्म चक्र में एकल 4 अशांत (-4) होता है। वर्तमान दशा में सम संख्या 4 (44) बनने से बंधन, मुकदमेबाजी व कानूनी बाधाएं शिथिल होती हैं तथा स्वास्थ्य लाभ व क्रांतिकारी बौद्धिक नवाचार का मार्ग खुलता है।",
                "gu": "જન્મ કુંડળીમાં એકલ 4 અશાંત (-4) હોય છે. દશાથી બેવડો 4 (44) બનવાથી બંધન કે કાનૂની અડચણો હળવી બને છે અને ઝડપી મુક્તિ તથા ટેકનિકલ સફળતાનો માર્ગ ખુલે છે."
            }.get(lang, "")
        elif num == 5 and shift_status == "pos_to_neg":
            shift_reason = {
                "en": "Inborn single 5 is a balanced merchant (+5). Under active Dasha, multiple 5s (55) hyper-accelerate nervous calculation, causing insomnia and temptation to cut ethical corners (-5); native must practice mindful grounding and honest bookkeeping.",
                "hi": "जन्म चक्र में एकल 5 श्रेष्ठ व्यापारिक बुद्धि देता है। वर्तमान दशा में दोहरे 5 (55) से अत्यधिक मानसिक उद्वेग, अनिद्रा और अति-चतुराई से नुकसान का जोखिम (-5) रहता है; अतः सट्टेबाजी से बचें।",
                "gu": "જન્મ કુંડળીમાં એકલ 5 સારો વેપારી છે. દશામાં 55 બનવાથી માનસિક અતિશય અશાંતિ, અનિદ્રા અને વધુ પડતી ચાલાકીથી નુકસાન થવાની સંભાવના (-5) રહે છે."
            }.get(lang, "")
        elif shift_status == "newly_activated":
            shift_reason = {
                "en": f"Number {num} is absent in the permanent inborn matrix. Under this active Dasha cycle, this planetary frequency is temporarily infused ({dc}x), awakening its distinct qualities for this phase.",
                "hi": f"अंक {num} जन्म चक्र में अनुपस्थित है। वर्तमान दशा चक्र के माध्यम से यह ग्रहीय ऊर्जा तात्कालिक रूप से ({dc} बार) जाग्रत हुई है, जो इस अवधि में अपना विशेष प्रभाव प्रदान करेगी।",
                "gu": f"અંક {num} જન્મ કુંડળીમાં ગેરહાજર છે. વર્તમાન દશા ચક્ર દ્વારા આ ગ્રહીય ઉર્જા તાત્કાલિક રીતે ({dc} વાર) સક્રિય થઈ છે, જે આ સમયગાળા દરમિયાન વિશેષ પ્રભાવ આપશે."
            }.get(lang, "")

        desc_key = "pos" if pt == "+" else "neg"
        desc_text = VIBRATION_DETAILS[num][desc_key][lang]
        
        active_period_list.append({
            "number": num,
            "count": dc,
            "natal_count": nc,
            "type": pt,
            "type_label": UI_TEXT[lang]["positive"] if pt == "+" else UI_TEXT[lang]["negative"],
            "natal_type": nt,
            "natal_type_label": (UI_TEXT[lang]["positive"] if nt == "+" else UI_TEXT[lang]["negative"]) if nt != "absent" else "Absent in Natal",
            "is_transformed": shift_status in ["neg_to_pos", "pos_to_neg", "newly_activated"],
            "shift_status": shift_status,
            "shift_badge": shift_badge,
            "shift_reason": shift_reason,
            "text": desc_text
        })
        
    # 2. Build Inborn Natal Baseline List
    natal_baseline_list = []
    for num in range(1, 10):
        nc = natal_counts.get(num, 0)
        if nc == 0:
            continue
        nt = natal_vib.get(num, "+")
        desc_key = "pos" if nt == "+" else "neg"
        desc_text = VIBRATION_DETAILS[num][desc_key][lang]
        natal_baseline_list.append({
            "number": num,
            "count": nc,
            "type": nt,
            "type_label": UI_TEXT[lang]["positive"] if nt == "+" else UI_TEXT[lang]["negative"],
            "text": desc_text
        })
        
    return {
        "active_period": active_period_list,
        "natal_baseline": natal_baseline_list,
        "has_shifts": has_shifts,
        "shifts_count": shifts_count,
        "disclaimer": UI_TEXT[lang]["vibrations_disclaimer"]
    }

def calculate_mahadasha_timeline(bn: int, dob: date, target_date: date) -> Dict[str, Any]:
    """
    Calculates the Mahadasha timeline starting from DOB with BN.
    Duration of MD = number itself (1=1yr, 2=2yrs ... 9=9yrs). Total cycle = 45 years.
    Sequence: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 (cyclic).
    """
    periods = []
    curr_start = dob
    curr_num = bn
    age_acc = 0
    
    # Generate MD periods for 90 years (2 complete 45-year cycles)
    for idx in range(18):
        duration_years = curr_num
        try:
            curr_end = date(curr_start.year + duration_years, curr_start.month, curr_start.day)
        except ValueError:
            # Handle Feb 29
            curr_end = date(curr_start.year + duration_years, curr_start.month, curr_start.day - 1)
            
        periods.append({
            "cycle": 1 if idx < 9 else 2,
            "number": curr_num,
            "duration": duration_years,
            "start_age": age_acc,
            "end_age": age_acc + duration_years,
            "start": curr_start,
            "end": curr_end,
            "start_str": curr_start.strftime("%d/%m/%Y"),
            "end_str": curr_end.strftime("%d/%m/%Y"),
            "start_dash": curr_start.strftime("%d-%m-%Y"),
            "end_dash": curr_end.strftime("%d-%m-%Y"),
            "is_active": curr_start <= target_date < curr_end
        })
        age_acc += duration_years
        curr_start = curr_end
        curr_num = (curr_num % 9) + 1

    active_md = next((p for p in periods if p["is_active"]), periods[0])
    return {
        "periods": periods[:10],
        "all_periods": periods,
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

def calculate_pratyantar_dasha(ad_number: int, ad_start: date, target_date: date, ad_end: date = None) -> Dict[str, Any]:
    """
    Pratyantar Dasha (PD):
    Year has 9 sub-periods starting from AD number.
    Duration of each sub-period = Root Number * 8 days.
    (Sum of 1*8 + 2*8 + ... + 9*8 = 360 days).
    Plus an adjustment period covering remaining days up to ad_end.
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
            "start_dash": curr_start.strftime("%d-%m-%Y"),
            "end_dash": (curr_end - timedelta(days=1)).strftime("%d-%m-%Y"),
            "is_active": is_active,
            "is_adjustment": False
        })
        curr_start = curr_end
        curr_num = (curr_num % 9) + 1

    full_periods = list(pd_periods)
    if ad_end and curr_start < ad_end:
        adj_days = (ad_end - curr_start).days
        is_active_adj = curr_start <= target_date < ad_end
        full_periods.append({
            "number": ad_number,
            "duration_days": adj_days,
            "start": curr_start,
            "end": ad_end,
            "start_str": curr_start.strftime("%d/%m/%Y"),
            "end_str": ad_end.strftime("%d/%m/%Y"),
            "start_dash": curr_start.strftime("%d-%m-%Y"),
            "end_dash": (ad_end - timedelta(days=1)).strftime("%d-%m-%Y"),
            "is_active": is_active_adj,
            "is_adjustment": True
        })

    active_pd = next((p for p in full_periods if p["is_active"]), pd_periods[0])
    return {
        "periods": pd_periods,
        "full_periods": full_periods,
        "active_pd": active_pd
    }


def calculate_lifetime_antardasha(dob: date, target_date: date, md_all_periods: list) -> list:
    """
    Computes 90 years of Antardasha (Ages 1..90) from each birthday to the day before next birthday.
    """
    rows = []
    for age in range(1, 91):
        yr = dob.year + age - 1
        try:
            bday_start = date(yr, dob.month, dob.day)
        except ValueError:
            bday_start = date(yr, dob.month, dob.day - 1)
        try:
            next_bday = date(yr + 1, dob.month, dob.day)
        except ValueError:
            next_bday = date(yr + 1, dob.month, dob.day - 1)
        bday_end = next_bday - timedelta(days=1)

        weekday_code = get_day_number(bday_start.weekday())
        yr_2digits = yr % 100
        ad_num = reduce_to_single_digit(dob.day + dob.month + yr_2digits + weekday_code)

        # Find MD active at bday_start
        md_num = md_all_periods[0]["number"]
        for p in md_all_periods:
            if p["start"] <= bday_start < p["end"]:
                md_num = p["number"]
                break

        rows.append({
            "age": age,
            "year": yr,
            "from_date": bday_start,
            "to_date": bday_end,
            "from_str": bday_start.strftime("%d-%m-%Y"),
            "to_str": bday_end.strftime("%d-%m-%Y"),
            "md": md_num,
            "ad": ad_num,
            "is_active": bday_start <= target_date < next_bday
        })
    return rows


def calculate_nine_year_grids_and_outlook(
    natal_counts: Dict[int, int], bn: int, dn: int, lifetime_ad: list, lang: str
) -> list:
    """
    Builds 9-year window centered on the running Antardasha year, with overlaid 3x3 Vedic grids
    and outlook tags (Money, Assets, Travel, Disputes, Health).
    """
    active_idx = next((i for i, r in enumerate(lifetime_ad) if r["is_active"]), 0)
    start_idx = max(0, min(len(lifetime_ad) - 9, active_idx - 4))
    window = lifetime_ad[start_idx : start_idx + 9]

    grid_order = [3, 1, 9, 6, 7, 5, 2, 8, 4]
    labels = {
        "en": {"mixed": "Mixed", "tight": "Tight", "up": "Up", "likely": "Likely", "friction": "Friction", "body_mind": "Body, mind", "mind": "Mind", "body": "Body"},
        "hi": {"mixed": "मिश्रित", "tight": "कठिन", "up": "उत्तम", "likely": "संभावित", "friction": "मतभेद", "body_mind": "तन, मन", "mind": "मन", "body": "शरीर"},
        "gu": {"mixed": "મિશ્ર", "tight": "કઠિન", "up": "ઉત્તમ", "likely": "સંભવિત", "friction": "મતભેદ", "body_mind": "તન, મન", "mind": "મન", "body": "શરીર"},
    }[lang]

    result = []
    for row in window:
        md = row["md"]
        ad = row["ad"]
        comb_counts = dict(natal_counts)
        comb_counts[md] = comb_counts.get(md, 0) + 1
        comb_counts[ad] = comb_counts.get(ad, 0) + 1

        cells = []
        for num in grid_order:
            nat_c = natal_counts.get(num, 0)
            add_c = (1 if md == num else 0) + (1 if ad == num else 0)
            cells.append({
                "num": num,
                "natal_str": str(num) * nat_c if nat_c > 0 else "",
                "transit_str": str(num) * add_c if add_c > 0 else "",
            })

        vibes = evaluate_vibrations(comb_counts, dn)
        pos_nums = {n for n, v in vibes.items() if v == "+"}
        neg_nums = {n for n, v in vibes.items() if v == "-"}

        # Outlook heuristics aligned with Vedic grid vibrations
        has_money_pos = any(n in pos_nums for n in (1, 5, 6, 8)) or (md in (1, 5, 6) and md in pos_nums) or (ad in (1, 5, 6) and ad in pos_nums)
        has_money_neg = any(n in (md, ad) and n in neg_nums for n in (1, 5, 8, 9))
        if has_money_pos and has_money_neg:
            money = ("mixed", labels["mixed"])
        elif has_money_pos and not has_money_neg:
            money = ("up", labels["up"])
        elif has_money_neg:
            money = ("tight", labels["tight"])
        else:
            money = ("none", "–")

        assets = ("likely", labels["likely"]) if (8 in pos_nums and (8 in (md, ad) or 6 in (md, ad))) or (6 in pos_nums and 6 in (md, ad)) else ("none", "–")
        travel = ("likely", labels["likely"]) if (4 in (md, ad) or 7 in (md, ad) or 5 in (md, ad)) and (4 in comb_counts and comb_counts[4] > 0) else ("none", "–")
        disputes = ("friction", labels["friction"]) if (4 in (md, ad) and 4 in neg_nums) or (8 in (md, ad) and 9 in (md, ad)) else ("none", "–")

        body_risk = any(n in (md, ad) and n in neg_nums for n in (1, 8, 9))
        mind_risk = any(n in (md, ad) and n in neg_nums for n in (2, 4, 7, 9))
        if body_risk and mind_risk:
            health = ("body_mind", labels["body_mind"])
        elif body_risk:
            health = ("body", labels["body"])
        elif mind_risk:
            health = ("mind", labels["mind"])
        else:
            health = ("none", "–")

        result.append({
            **row,
            "cells": cells,
            "money": money,
            "assets": assets,
            "travel": travel,
            "disputes": disputes,
            "health": health,
        })
    return result

def detect_active_yogas(counts: Dict[int, int], vibrations: Dict[int, str], lang: str) -> Dict[str, Any]:
    """
    Identifies all active Auspicious Yogas (Shubh Yogas) and
    Inauspicious Yogas / Doshas (Ashubh Yogas with remedies) in the chart.
    """
    auspicious = []
    inauspicious = []
    
    # ---------------- 1. Auspicious Yogas Detection ----------------
    # Check 3-1-9, 1-7-8, 6-5 Raj Yog first
    has_319 = all(counts.get(n, 0) > 0 for n in [3, 1, 9])
    has_178 = all(counts.get(n, 0) > 0 for n in [1, 7, 8])
    has_65 = all(counts.get(n, 0) > 0 for n in [6, 5])
    
    if has_319 or has_178 or has_65:
        name_map = {
            "en": "Imperial Raj Yog (Supreme Sovereign Grace)",
            "hi": "साम्राज्य राजयोग (सर्वोच्च ग्रहीय कृपा एवं सत्ता)",
            "gu": "સામ્રાજ્ય રાજયોગ (સર્વોચ્ચ ગ્રહીય કૃપા અને સત્તા)"
        }
        tag_map = {
            "en": "Imperial Sovereignty • Supreme Auspiciousness",
            "hi": "राजयोग संप्रभुता • सर्वोच्च शुभता",
            "gu": "રાજયોગ સાર્વભૌમત્વ • સર્વોચ્ચ શુભતા"
        }
        desc_map = {
            "en": "Rare Imperial Raj Yog alignment grants elevated societal honor, unyielding administrative authority, and immense luxury during favorable Dasha cycles.",
            "hi": "जन्म चक्र में राजयोग का निर्माण जातक को समाज में सर्वोच्च मान-सम्मान, प्रशासनिक अधिकार और अनुकूल दशाओं में असीम ऐश्वर्य व वैभव प्रदान करता है।",
            "gu": "જન્મ કુંડળીમાં રાજયોગનું નિર્માણ જાતકને સમાજમાં ઉચ્ચ મોભો, વહીવટી સત્તા અને સાનુકૂળ દશાઓમાં ભવ્ય ઐશ્વર્ય તથા સંપત્તિ પ્રદાન કરે છે."
        }
        auspicious.append({
            "id": "raj_yog",
            "name": name_map.get(lang, name_map["en"]),
            "tag": tag_map.get(lang, tag_map["en"]),
            "desc": desc_map.get(lang, desc_map["en"]),
            "numbers": [1, 8] if has_178 else ([3, 1, 9] if has_319 else [6, 5]),
            "category": "auspicious"
        })

    # Check all Auspicious Yogas
    for yoga_id, yoga in AUSPICIOUS_YOGAS_DEFINITIONS.items():
        req_numbers = yoga["numbers"]
        is_present = all(counts.get(n, 0) > 0 for n in req_numbers)
        if not is_present:
            continue
            
        # Additional absence conditions for specific pairs based on course texts
        if yoga_id == "combination_1_7" and counts.get(8, 0) > 0:
            continue
        if yoga_id == "combination_3_1" and counts.get(9, 0) > 0:
            continue
        if yoga_id == "combination_1_2" and (counts.get(6, 0) > 0 or counts.get(3, 0) > 0):
            continue
        if yoga_id == "combination_9_5" and counts.get(4, 0) > 0:
            continue
        if yoga_id == "combination_6_7" and counts.get(5, 0) > 0:
            continue
        if yoga_id == "combination_6_2" and counts.get(3, 0) > 0:
            continue
            
        tags = [yoga["tag"].get(lang, yoga["tag"]["en"])]
        constituent_vibes = [vibrations.get(n, "+") for n in req_numbers]
        if all(v == "+" for v in constituent_vibes):
            tags.append("Superior (+)" if lang == "en" else ("श्रेष्ठ (+)" if lang == "hi" else "શ્રેષ્ઠ (+)"))
        elif any(v == "-" for v in constituent_vibes):
            tags.append("Mixed Vibrations" if lang == "en" else ("मिश्रित ऊर्जा" if lang == "hi" else "મિશ્રિત ઉર્જા"))
            
        auspicious.append({
            "id": yoga_id,
            "name": yoga["name"].get(lang, yoga["name"]["en"]),
            "tag": " • ".join(tags),
            "desc": yoga["desc"].get(lang, yoga["desc"]["en"]),
            "numbers": req_numbers,
            "category": "auspicious"
        })

    # ---------------- 2. Inauspicious Yogas (Doshas) Detection ----------------
    # 1. Bandhan Yog (9-4 with missing 5)
    if counts.get(9, 0) > 0 and counts.get(4, 0) > 0 and counts.get(5, 0) == 0:
        c4 = counts.get(4, 0)
        c9 = counts.get(9, 0)
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["bandhan_yog_94"]
        desc = item["desc"].get(lang, item["desc"]["en"])
        if c4 % 2 == 0:
            desc += " [Even 4s active: negative effects diminished; recovery and relief are swift.]" if lang == "en" else (" [सम संख्या में 4 (44) होने से दोष का प्रभाव काफी कम होता है और राहत शीघ्र मिलती है।]" if lang == "hi" else " [બેવડા 4 (44) હોવાથી દોષની અસર ઘટે છે અને મુક્તિ ઝડપથી મળે છે.]")
        elif c9 >= 2:
            desc += " [Double 9 active: anger and legal risks are aggravated.]" if lang == "en" else (" [दोहरा 9 होने से मंगल कमजोर होकर उग्रता व संकट को बढ़ाता है।]" if lang == "hi" else " [બેવડો 9 હોવાથી ગુસ્સો અને કાનૂની જોખમ વધે છે.]")
        inauspicious.append({
            "id": "bandhan_yog_94",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": desc,
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [9, 4],
            "category": "inauspicious"
        })

    # 2. Bandhan Yog (5-4 with missing 9)
    if counts.get(5, 0) > 0 and counts.get(4, 0) > 0 and counts.get(9, 0) == 0:
        c4 = counts.get(4, 0)
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["bandhan_yog_54"]
        desc = item["desc"].get(lang, item["desc"]["en"])
        if c4 % 2 == 0:
            desc += " [Even 4s present: dispute intensity reduced.]" if lang == "en" else (" [सम संख्या 4 (44) होने से विवाद का प्रभाव कम होता है।]" if lang == "hi" else " [બેવડા 4 થી વિવાદની અસર ઓછી રહે છે.]")
        inauspicious.append({
            "id": "bandhan_yog_54",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": desc,
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [5, 4],
            "category": "inauspicious"
        })

    # 3. Apaman Yog (1-8 with missing 7)
    if counts.get(1, 0) > 0 and counts.get(8, 0) > 0 and counts.get(7, 0) == 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["apaman_yog_18"]
        inauspicious.append({
            "id": "apaman_yog_18",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": item["desc"].get(lang, item["desc"]["en"]),
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [1, 8],
            "category": "inauspicious"
        })

    # 4. Vish Yog (2-8 with missing 4)
    if counts.get(2, 0) > 0 and counts.get(8, 0) > 0 and counts.get(4, 0) == 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["vish_yog_28"]
        desc = item["desc"].get(lang, item["desc"]["en"])
        if counts.get(8, 0) >= 2:
            desc += " [Double 8 (88) present: emotional resilience improves substantially.]" if lang == "en" else (" [दोहरा 8 (88) उपस्थित होने से मानसिक दृढ़ता में सुधार होता है।]" if lang == "hi" else " [બેવડો 8 (88) હોવાથી માનસિક મનોબળ સુધરે છે.]")
        inauspicious.append({
            "id": "vish_yog_28",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": desc,
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [2, 8],
            "category": "inauspicious"
        })

    # 5. Hava Mahal Yog (8-4 with missing 2)
    if counts.get(8, 0) > 0 and counts.get(4, 0) > 0 and counts.get(2, 0) == 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["hava_mahal_84"]
        inauspicious.append({
            "id": "hava_mahal_84",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": item["desc"].get(lang, item["desc"]["en"]),
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [8, 4],
            "category": "inauspicious"
        })

    # 6. Plastic Love Yog (7-5 with missing 6)
    if counts.get(7, 0) > 0 and counts.get(5, 0) > 0 and counts.get(6, 0) == 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["plastic_love_75"]
        inauspicious.append({
            "id": "plastic_love_75",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": item["desc"].get(lang, item["desc"]["en"]),
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [7, 5],
            "category": "inauspicious"
        })

    # 7. Agni Sangharsh (1-9 with missing 3)
    if counts.get(1, 0) > 0 and counts.get(9, 0) > 0 and counts.get(3, 0) == 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["agni_sangharsh_19"]
        inauspicious.append({
            "id": "agni_sangharsh_19",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": item["desc"].get(lang, item["desc"]["en"]),
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [1, 9],
            "category": "inauspicious"
        })

    # 8. Kalaha Yog (66 with 2)
    if counts.get(6, 0) >= 2 and counts.get(2, 0) == 1:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["kalaha_yog_66_2"]
        inauspicious.append({
            "id": "kalaha_yog_66_2",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": item["desc"].get(lang, item["desc"]["en"]),
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [6, 2],
            "category": "inauspicious"
        })

    # 9. Slow Mind Yog (99 with 5, missing 4)
    if counts.get(9, 0) >= 2 and counts.get(5, 0) == 1 and counts.get(4, 0) == 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["slow_mind_99_5"]
        inauspicious.append({
            "id": "slow_mind_99_5",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": item["desc"].get(lang, item["desc"]["en"]),
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [9, 5],
            "category": "inauspicious"
        })

    # 10. Hyper-Mercury Ati-Chaturya (Multiple 5s with 9, missing 4)
    if counts.get(5, 0) >= 2 and counts.get(9, 0) >= 1 and counts.get(4, 0) == 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["chaturya_fraud_55_9"]
        inauspicious.append({
            "id": "chaturya_fraud_55_9",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": item["desc"].get(lang, item["desc"]["en"]),
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [5, 9],
            "category": "inauspicious"
        })

    # 11. Action Plane Turbulence (2-8-4 all present)
    if counts.get(2, 0) > 0 and counts.get(8, 0) > 0 and counts.get(4, 0) > 0:
        item = INAUSPICIOUS_YOGAS_DEFINITIONS["turbulence_plane_284"]
        desc = item["desc"].get(lang, item["desc"]["en"])
        if counts.get(4, 0) >= 2 or counts.get(8, 0) >= 2:
            desc += " [Double 4 or 8 present: significantly cushions the volatility.]" if lang == "en" else (" [दोहरा 4 या 8 उपस्थित होने से उतार-चढ़ाव काफी हद तक शांत होता है।]" if lang == "hi" else " [બેવડો 4 કે 8 હોવાથી ઉતાર-ચઢાવ ઘણો અંકુશમાં રહે છે.]")
        inauspicious.append({
            "id": "turbulence_plane_284",
            "name": item["name"].get(lang, item["name"]["en"]),
            "tag": item["tag"].get(lang, item["tag"]["en"]),
            "desc": desc,
            "remedy": item["remedy"].get(lang, item["remedy"]["en"]),
            "numbers": [2, 8, 4],
            "category": "inauspicious"
        })

    all_yogas = auspicious + inauspicious
    return {
        "auspicious": auspicious,
        "inauspicious": inauspicious,
        "all": all_yogas
    }

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

def calculate_dasha_grid(
    grid_info: Dict[str, Any], active_md: int, active_ad: int, active_pd: int, dn: int, lang: str = "en"
) -> Dict[str, Any]:
    """
    Constructs the Dasha & Transit Activation Grid.
    Combines Natal Birth numbers with current Active Mahadasha (MD), Antardasha (AD),
    and Pratyantar Dasha (PD) numbers with distinct color coding:
    - Natal Inborn: Sacred Gold (#d4af37)
    - Mahadasha (Long-Term): Sky Blue (#38bdf8)
    - Antardasha (Yearly): Emerald Green (#22c55e)
    - Pratyantar Dasha (Monthly): Sunset Orange (#fb923c)
    """
    natal_counts = grid_info["counts"]
    items_by_num = {i: [] for i in range(1, 10)}
    
    # Add Natal occurrences
    for d in grid_info["digits"]:
        items_by_num[d].append({
            "val": d,
            "source": "natal",
            "source_code": "NAT",
            "source_name": UI_TEXT[lang]["legend_natal"],
            "color": "#d4af37" # Sacred Gold
        })
        
    # Add Active Mahadasha (MD - Long Term)
    if active_md and 1 <= active_md <= 9:
        items_by_num[active_md].append({
            "val": active_md,
            "source": "md",
            "source_code": "MD",
            "source_name": UI_TEXT[lang]["legend_md"],
            "color": "#38bdf8" # Sky Blue
        })
        
    # Add Active Antardasha (AD - Yearly)
    if active_ad and 1 <= active_ad <= 9:
        items_by_num[active_ad].append({
            "val": active_ad,
            "source": "ad",
            "source_code": "AD",
            "source_name": UI_TEXT[lang]["legend_ad"],
            "color": "#22c55e" # Emerald Green
        })
        
    # Add Active Pratyantar Dasha (PD - Monthly)
    if active_pd and 1 <= active_pd <= 9:
        items_by_num[active_pd].append({
            "val": active_pd,
            "source": "pd",
            "source_code": "PD",
            "source_name": UI_TEXT[lang]["legend_pd"],
            "color": "#7c3aed" # Royal Purple
        })
        
    total_counts = {i: len(items_by_num[i]) for i in range(1, 10)}
    period_vibrations = evaluate_vibrations(total_counts, dn)
    
    # 3x3 Vedic Grid Layout Order: 3, 1, 9, 6, 7, 5, 2, 8, 4
    dasha_cells = []
    for num in [3, 1, 9, 6, 7, 5, 2, 8, 4]:
        natal_c = natal_counts.get(num, 0)
        tot_c = total_counts[num]
        items = items_by_num[num]
        
        has_md = any(it["source"] == "md" for it in items)
        has_ad = any(it["source"] == "ad" for it in items)
        has_pd = any(it["source"] == "pd" for it in items)
        is_new = natal_c == 0 and tot_c > 0
        is_amp = natal_c > 0 and tot_c > natal_c
        
        dasha_cells.append({
            "num": num,
            "natal_count": natal_c,
            "total_count": tot_c,
            "items": items,
            "is_active": tot_c > 0,
            "is_newly_activated": is_new,
            "is_amplified": is_amp,
            "has_md": has_md,
            "has_ad": has_ad,
            "has_pd": has_pd,
            "natal_vibe": evaluate_vibrations(natal_counts, dn).get(num, "absent"),
            "period_vibe": period_vibrations.get(num, "absent")
        })
        
    return {
        "cells": dasha_cells,
        "total_counts": total_counts,
        "items_by_num": items_by_num,
        "period_vibrations": period_vibrations
    }

def generate_three_tier_predictions(
    bn: int, dn: int, natal_grid: Dict[str, Any], dasha_grid: Dict[str, Any],
    md_info: Dict[str, Any], ad_info: Dict[str, Any], pd_info: Dict[str, Any],
    lang: str = "en"
) -> Dict[str, Any]:
    """
    Generates 3-Tier Time Horizon Predictions:
    1. Mahadasha: Long-term Macro Period (multi-year cycle)
    2. Antardasha: Yearly Forecast (1-year cycle from birthday to birthday)
    3. Pratyantar Dasha: Monthly Forecast (active sub-phase & 9-phase calendar roadmap)
    """
    active_md_num = md_info["active_md"]["number"]
    active_md_planet = PLANET_INFO[active_md_num][lang]["planet"]
    md_start_str = md_info["active_md"]["start_str"]
    md_end_str = md_info["active_md"]["end_str"]
    md_duration = md_info["active_md"]["duration"]
    
    active_ad_num = ad_info["ad_number"]
    active_ad_planet = PLANET_INFO[active_ad_num][lang]["planet"]
    ad_start_str = ad_info["start_str"]
    ad_end_str = ad_info["end_str"]
    
    active_pd_num = pd_info["active_pd"]["number"]
    active_pd_planet = PLANET_INFO[active_pd_num][lang]["planet"]
    pd_start_str = pd_info["active_pd"]["start_str"]
    pd_end_str = pd_info["active_pd"]["end_str"]
    pd_days = pd_info["active_pd"]["duration_days"]
    
    natal_counts = natal_grid["counts"]
    tot_counts = dasha_grid["total_counts"]
    period_vibes = dasha_grid["period_vibrations"]
    
    # ---------------- 1. MAHADASHA (LONG-TERM MACRO CYCLE) ----------------
    # Finance rule: +3, +6, +8, +5 activates -> very good for finance / growth; -4, -8, -9, -6, -1, -3 -> caution
    is_md_fin_fav = active_md_num in [3, 5, 6, 8]
    
    md_descriptions = {
        1: {
            "en": f"You are traversing the 1-Year Mahadasha of Sun ({active_md_planet}). This is a golden macro period for career elevation, supreme executive authority, and founding new life milestones. Government relations, promotions, and public recognition are heavily favored. Maintain magnanimity and guard against ego clash.",
            "hi": f"आप सूर्य ({active_md_planet}) की 1-वर्षीय महादशा से गुजर रहे हैं। यह उच्च प्रशासनिक प्रतिष्ठा, शासकीय लाभ और जीवन में नए कीर्तिमान स्थापित करने का स्वर्णिम काल है। पदोन्नति और सामाजिक सम्मान प्रबल रहेगा। अहंकार और क्रोध से बचें।",
            "gu": f"આપ સૂર્ય ({active_md_planet}) ની 1-વર્ષીય મહાદશામાંથી પસાર થઈ રહ્યા છો. આ ઉચ્ચ વહીવટી પ્રતિષ્ઠા, સરકારી લાભ અને જીવનમાં નવી સિદ્ધિઓ હાંસલ કરવાનો સુવર્ણ કાળ છે. પદોન્નતિ અને સામાજિક સન્માન વધશે. અહંકાર ટાળવો."
        },
        2: {
            "en": f"You are traversing the 2-Year Mahadasha of Moon ({active_md_planet}). This period emphasizes domestic peace, emotional partnerships, creative arts, and maternal blessings. Intuition and empathetic leadership flourish. Practice meditation and daily pranayama to maintain emotional stability.",
            "hi": f"आप चंद्रमा ({active_md_planet}) की 2-वर्षीय महादशा में हैं। यह अवधि पारिवारिक सुख, दांपत्य सामंजस्य, कलात्मक सृजन और माता के आशीर्वाद की है। अंतःप्रेरणा बलवान रहेगी। मानसिक शांति और अनिद्रा से बचाव हेतु नियमित ध्यान आवश्यक है।",
            "gu": f"આપ ચંદ્ર ({active_md_planet}) ની 2-વર્ષીય મહાદશામાં છો. આ સમયગાળો કૌટુંબિક સુખ, ભાગીદારી, કલા અને માતાના આશીર્વાદનો છે. મનોબળ સ્થિર રાખવા અને અનિદ્રા ટાળવા રોજેરોજ ધ્યાન અને પ્રાણાયામ કરવા."
        },
        3: {
            "en": f"You are traversing the 3-Year Mahadasha of Jupiter ({active_md_planet}). An extraordinarily auspicious period for intellect, advisory roles, children's prosperity, and financial accumulation. Your counsel will be sought after, and ethical business ventures yield substantial long-term wealth.",
            "hi": f"आप देवगुरु बृहस्पति ({active_md_planet}) की 3-वर्षीय महादशा में हैं। यह अवधि ज्ञान, विद्या, संतान सुख और उत्तम धन संचय के लिए अत्यंत फलदायी है। आपके परामर्श की समाज में मांग बढ़ेगी और नैतिक व्यापारिक उपक्रमों में दीर्घकालिक समृद्धि प्राप्त होगी।",
            "gu": f"આપ દેવગુરુ બૃહસ્પતિ ({active_md_planet}) ની 3-વર્ષીય મહાદશામાં છો. આ સમય જ્ઞાન, શિક્ષણ, સંતાન સુખ અને અઢળક ધન સંચય માટે અતિ ઉત્તમ છે. સમાજમાં આપનું માન વધશે અને પ્રામાણિક વેપારમાં ભારે સફળતા મળશે."
        },
        4: {
            "en": f"You are traversing the 4-Year Mahadasha of Rahu ({active_md_planet}). A period of dramatic shifts, out-of-the-box thinking, technological breakthroughs, and unconventional wealth avenues. Ensure all contracts are legally scrutinized; refrain from purchasing property exclusively in your own name.",
            "hi": f"आप राहु ({active_md_planet}) की 4-वर्षीय महादशा में हैं। यह आकस्मिक परिवर्तनों, विदेशी संपर्कों, तकनीकी अनुसंधान और अपरंपरागत सफलता का काल है। कानूनी समझौतों में अत्यधिक सावधानी बरतें और संपत्ति केवल अपने अकेले नाम पर खरीदने से बचें।",
            "gu": f"આપ રાહુ ({active_md_planet}) ની 4-વર્ષીય મહાદશામાં છો. આ અણધાર્યા ફેરફારો, વિદેશી સંપર્કો, ટેકનોલોજી અને વિશેષ આવકનો ગાળો છે. કાનૂની દસ્તાવેજોમાં ચકાસણી રાખવી અને મિલકત ફક્ત પોતાના એકલા નામે ન લેવી."
        },
        5: {
            "en": f"You are traversing the 5-Year Mahadasha of Mercury ({active_md_planet}). A powerhouse phase for commercial trading, marketing, intellectual investments, and rapid financial liquidity. Communication and deal negotiations will run at peak agility. Cash flow remains abundant.",
            "hi": f"आप बुध ({active_md_planet}) की 5-वर्षीय महादशा में हैं। यह व्यापारिक विस्तार, वित्तीय लेन-देन, बौद्धिक कार्य और प्रचुर धन लाभ का सर्वोच्च काल है। आपके निर्णय सटीक रहेंगे और वाक्पटुता से बड़े व्यापारिक अनुबंध सहज संपन्न होंगे।",
            "gu": f"આપ બુધ ({active_md_planet}) ની 5-વર્ષીય મહાદશામાં છો. આ વેપાર-ધંધાનો વ્યાપ વધારવાનો, શેરબજાર/રોકાણ અને પ્રચુર નાણાકીય પ્રવાહનો સમય છે. આપની કુશાગ્ર બુદ્ધિથી અટકેલા નાણાં છૂટા થશે."
        },
        6: {
            "en": f"You are traversing the 6-Year Mahadasha of Venus ({active_md_planet}). A splendid multi-year cycle of worldly luxuries, vehicles, marital bliss, artistic elegance, and aristocratic comforts. Business in lifestyle, hospitality, and luxury goods experiences exponential expansion.",
            "hi": f"आप शुक्र ({active_md_planet}) की 6-वर्षीय महादशा में हैं। यह भौतिक सुख-सुविधाओं, वाहन क्रय, दांपत्य प्रेम और ऐश्वर्य का काल है। सौंदर्य, फैशन, कला और विलासिता से जुड़े कार्यों में अप्रत्याशित सफलता और मान-सम्मान मिलेगा।",
            "gu": f"આપ શુક્ર ({active_md_planet}) ની 6-વર્ષીય મહાદશામાં છો. આ ભૌતિક સુખ-સગવડો, નવા વાહન, દાંપત્ય સુખ અને વૈભવી જીવનશૈલીનો સમય છે. કલા, ફેશન, આભૂષણો અને સુંદરતાના ક્ષેત્રમાં અપ્રતિમ લાભ થશે."
        },
        7: {
            "en": f"You are traversing the 7-Year Mahadasha of Ketu ({active_md_planet}). A profound chapter for spiritual realization, research, philosophical mastery, and long-distance travel or foreign settlement. High intuition protects you from adversities. Practice selfless philanthropy.",
            "hi": f"आप केतु ({active_md_planet}) की 7-वर्षीय महादशा में हैं। यह गहन आध्यात्मिक जागृति, शोध, गुप्त विद्याओं और विदेश गमन/स्थायी निवास का प्रमुख समय है। आपकी छठी इंद्री (सहज ज्ञान) अत्यंत तीव्र रहेगी जो हर संकट से रक्षा करेगी।",
            "gu": f"આપ કેતુ ({active_md_planet}) ની 7-વર્ષીય મહાદશામાં છો. આ આધ્યાત્મિક સાધના, સંશોધન, રહસ્ય વિદ્યાઓ અને વિદેશ વસવાટનો પ્રબળ કાળ છે. આપની આંતરિક પ્રેરણા આપને યોગ્ય માર્ગ બતાવશે."
        },
        8: {
            "en": f"You are traversing the 8-Year Mahadasha of Saturn ({active_md_planet}). The grand cycle of perseverance, karmic justice, solid wealth foundations, and real estate consolidation. Hard work translates into unbreakable empire building. Avoid shortcuts and maintain discipline.",
            "hi": f"आप शनिदेव ({active_md_planet}) की 8-वर्षीय महादशा में हैं। यह कर्म फल, कठोर परिश्रम, स्थायी अचल संपत्ति और अटूट साम्राज्य निर्माण का काल है। ધીરજ અને નિયમિતતા સે किया गया परिश्रम आपको समाज में शीर्ष स्थान प्रदान करेगा।",
            "gu": f"આપ શનિદેવ ({active_md_planet}) ની 8-વર્ષીય મહાદશામાં છો. આ કર્મ ફળ, અથાક પરિશ્રમ, સ્થાવર મિલકતો અને કાયમી સામ્રાજ્ય રચવાનો ગાળો છે. શોર્ટકટ ટાળવા અને ધીરજ રાખવાથી અનંત સફળતા મળશે."
        },
        9: {
            "en": f"You are traversing the 9-Year Mahadasha of Mars ({active_md_planet}). A dynamic period of valor, physical drive, competitive dominance, real estate deals, and executive command. Bold moves bring decisive victories. Keep impulsive anger and blood pressure strictly managed.",
            "hi": f"आप मंगल ({active_md_planet}) की 9-वर्षीय महादशा में हैं। यह असीम ऊर्जा, साहस, प्रतिस्पर्धी विजय, भूमि क्रय और प्रशासनिक नेतृत्व का काल है। साहसिक निर्णयों में विजय मिलेगी। उग्रता व जल्दबाजी पर नियंत्रण रखें।",
            "gu": f"આપ મંગળ ({active_md_planet}) ની 9-વર્ષીય મહાદશામાં છો. આ અદમ્ય ઉત્સાહ, સાહસ, જમીન-મિલકતના સોદા અને વહીવટી નેતૃત્વનો સમય છે. ઉતાવળિયો ગુસ્સો ટાળીને લીધેલા નિર્ણયો વિજય અપાવશે."
        }
    }
    
    # ---------------- 2. ANTARDASHA (YEARLY FORECAST) ----------------
    has_travel_in_ad = (natal_counts.get(4, 0) > 0 or natal_counts.get(7, 0) > 0) and active_ad_num in [4, 5, 6, 7]
    has_property_in_ad = (period_vibes.get(1) == "+" or period_vibes.get(8) == "+") or active_ad_num in [1, 5, 6]
    
    ad_annual_themes = {
        1: {
            "en": "Year of Authority & New Career Breakthroughs: High recognition, promotion, leadership assignments, and administrative triumphs.",
            "hi": "अधिकार एवं नए व्यावसायिक आरंभ का वर्ष: उच्च पद, पदोन्नति, नेतृत्व के अवसर और प्रशासनिक कार्यों में विशेष विजय।",
            "gu": "અધિકાર અને નવી શરૂઆતનું વર્ષ: ઉચ્ચ પદ, પ્રમોશન, નેતૃત્વની તકો અને સરકારી કાર્યોમાં વિશેષ યશ."
        },
        2: {
            "en": "Year of Emotional Partnerships & Creative Balance: Auspicious for joint ventures, diplomatic negotiations, and artistic expressions.",
            "hi": "भावनात्मक साझेदारी एवं रचनात्मक संतुलन का वर्ष: संयुक्त व्यापार, कूटनीतिक समझौतों और कलात्मक कार्यों हेतु अत्यंत शुभ।",
            "gu": "ભાગીદારી અને રચનાત્મક સંતુલનનું વર્ષ: સંયુક્ત વેપાર, કરારો અને કલા ક્ષેત્રે ઉત્તમ પરિણામો આપશે."
        },
        3: {
            "en": "Year of Wisdom, Family Expansion & Wealth Multiplier: Academic achievements, guru guidance, high financial gains, and family celebrations.",
            "hi": "ज्ञान, पारिवारिक मांगलिक कार्य एवं धन वृद्धि का वर्ष: उच्च शिक्षा, गुरु कृपा, वित्तीय लाभ और परिवार में उत्सव के योग।",
            "gu": "જ્ઞાન, પરિવારમાં શુભ પ્રસંગો અને ધનવૃદ્ધિનું વર્ષ: ઉચ્ચ અભ્યાસ, વડીલોના આશીર્વાદ અને નાણાકીય પ્રગતિ."
        },
        4: {
            "en": "Year of Sudden Shifts & Technical Innovation: Unconventional opportunities, foreign connections; maintain strict contractual vigilance.",
            "hi": "आकस्मिक परिवर्तन एवं तकनीकी प्रगति का वर्ष: नए अपरंपरागत अवसर, विदेशी संपर्क; अनुबंधों व वाहन मामलों में सतर्कता रखें।",
            "gu": "અણધાર્યા ફેરફારો અને ટેકનિકલ પ્રગતિનું વર્ષ: નવીન તકો, વિદેશી સંપર્કો; લખાણો અને વાહનોમાં સાવચેતી રાખવી."
        },
        5: {
            "en": "Year of Commercial Expansion & High Liquidity: Lucrative business trading, quick deal turnover, travel, and strong cash flow.",
            "hi": "व्यापारिक विस्तार एवं प्रचुर नकदी प्रवाह का वर्ष: व्यावसायिक अनुबंध, विपणन में भारी सफलता, यात्राएं और सुदृढ़ आर्थिक लाभ।",
            "gu": "વેપાર વૃદ્ધિ અને પ્રચુર ધનલાભનું વર્ષ: નવા કરારો, માર્કેટિંગમાં સફળતા, મુસાફરી અને ઉત્તમ રોકડ પ્રવાહ."
        },
        6: {
            "en": "Year of Luxuries, Marital Bliss & Asset Comforts: Purchase of luxury vehicles, home beautification, harmonious relationships, and female support.",
            "hi": "ऐश्वर्य, दांपत्य सुख एवं वाहन-संपत्ति का वर्ष: विलासिता सामग्री, नवीन वाहन क्रय, गृह सज्जा और दांपत्य में प्रगाढ़ता।",
            "gu": "વૈભવ, દાંપત્ય સુખ અને વાહન-મિલકતનું વર્ષ: નવા વાહનની ખરીદી, ઘર સુશોભન અને સંબધોમાં મધુરતા."
        },
        7: {
            "en": "Year of Spiritual Awakening & Far Travel: Deep research, philosophical clarity, foreign journeys, and peaceful inner contentment.",
            "hi": "आध्यात्मिक उन्नति, शोध एवं विदेश यात्रा का वर्ष: गहन चिंतन, तीर्थाटन, दूरस्थ यात्राएं और आत्मिक शांति का संचय।",
            "gu": "આધ્યાત્મિક ઉન્નતિ, સંશોધન અને વિદેશ પ્રવાસનું વર્ષ: ઊંડું ચિંતન, યાત્રાઓ અને આંતરિક શાંતિ."
        },
        8: {
            "en": "Year of Karmic Fruition & Solid Property Consolidation: Concrete business foundations, long-term investments, real estate acquisitions.",
            "hi": "कर्म फल एवं अचल संपत्ति सुदृढ़ीकरण का वर्ष: स्थायी व्यापारिक नींव, भूमि-भवन क्रय और गंभीर दीर्घकालिक उपलब्धियां।",
            "gu": "કર્મ ફળ અને સ્થાવર મિલકત પ્રાપ્તિનું વર્ષ: મજબૂત વેપાર પાયો, જમીન-મકાન ખરીદી અને ગંભીર સિદ્ધિઓ."
        },
        9: {
            "en": "Year of Dynamic Energy, Courage & Bold Conquest: Decisive initiatives, clearing old hurdles, administrative command; avoid heated disputes.",
            "hi": "ऊर्जा, साहस एवं लक्ष्य सिद्धि का वर्ष: साहसिक कदम, पुरानी बाधाओं की समाप्ति, प्रशासनिक धाक; विवादों से बचें।",
            "gu": "ઊર્જા, સાહસ અને ધ્યેય પ્રાપ્તિનું વર્ષ: સાહસિક નિર્ણયો, જૂની અડચણોનો અંત; વિવાદો ટાળવા."
        }
    }
    
    # ---------------- 3. PRATYANTAR DASHA (MONTHLY FORECAST & ROADMAP) ----------------
    pd_dos_donts = {
        1: {
            "dos": {
                "en": ["Meet government authorities or senior management", "Launch bold executive initiatives", "Perform morning Surya Arghya"],
                "hi": ["उच्च अधिकारियों या प्रबंधकों से भेंट करें", "नए प्रशासनिक निर्णय लें", "प्रातःकाल सूर्य अर्घ्य दें"],
                "gu": ["ઉચ્ચ અધિકારીઓ કે વડીલો સાથે બેઠક કરો", "નવા વહીવટી નિર્ણયો લો", "સવારે સૂર્યને અર્ઘ્ય આપો"]
            },
            "donts": {
                "en": ["Avoid ego friction with colleagues", "Do not ignore cardiovascular health or blood pressure"],
                "hi": ["सहकर्मियों से अहंकार का टकराव न करें", "रक्तचाप व हृदय स्वास्थ्य की अनदेखी न करें"],
                "gu": ["સાથીદારો સાથે અહંકારનો ટકરાવ ટાળવો", "બ્લડ પ્રેશર બાબતે બેદરકાર ન રહેવું"]
            }
        },
        2: {
            "dos": {
                "en": ["Sign partnership agreements", "Focus on creative design and marketing", "Spend quality time with mother"],
                "hi": ["साझेदारी के अनुबंध संपन्न करें", "रचनात्मक व कलात्मक कार्यों पर ध्यान दें", "माता की सेवा करें"],
                "gu": ["ભાગીદારીના કરારો પૂરા કરો", "કલાત્મક અને ડિઝાઇનિંગ કાર્યો કરો", "માતાની સેવા-આશીર્વાદ લો"]
            },
            "donts": {
                "en": ["Avoid mood swings and over-thinking", "Refrain from taking major financial decisions late at night"],
                "hi": ["मानसिक चंचलता व अवसाद से बचें", "देर रात में कोई बड़ा आर्थिक फैसला न लें"],
                "gu": ["મૂડ સ્વિંગ્સ અને વધુ પડતો વિચાર ટાળવો", "મોડી રાત્રે કોઈ મોટો નાણાકીય નિર્ણય ન લેવો"]
            }
        },
        3: {
            "dos": {
                "en": ["Take blessings from mentors, teachers, and gurus", "Enroll in high-value education/certifications", "Offer yellow sweets/chana to cows"],
                "hi": ["गुरुजनों व आचार्यों का आशीर्वाद लें", "ज्ञानवर्धक कोर्स या प्रमाणन आरंभ करें", "गुरुवार को गाय को चना-गुड़ खिलाएं"],
                "gu": ["ગુરુજનો અને વડીલોના આશીર્વાદ લો", "જ્ઞાનવર્ધક અભ્યાસ કે કોર્સ શરૂ કરો", "ગાયને ચણા-ગોળ અર્પણ કરો"]
            },
            "donts": {
                "en": ["Do not compromise on business ethics", "Avoid overeating sweets or heavy foods"],
                "hi": ["व्यापारिक नैतिकता से समझौता न करें", "अत्यधिक मीठे या भारी भोजन से बचें"],
                "gu": ["વેપારની નૈતિકતા સાથે બાંધછોડ ન કરવી", "વધુ પડતો ભારે ખોરાક ટાળવો"]
            }
        },
        4: {
            "dos": {
                "en": ["Harness technology and modern automation tools", "Explore foreign tie-ups or digital expansion", "Worship Lord Ganesha to remove obstacles"],
                "hi": ["आधुनिक तकनीकी व डिजिटल उपकरणों का उपयोग करें", "विदेशी संपर्कों पर काम करें", "भगवान गणेश की आराधना करें"],
                "gu": ["નવીન ટેકનોલોજી અને ડિજિટલ સાધનો વાપરો", "વિદેશી સંપર્કો પર કામ કરો", "ભગવાન ગણેશની પૂજા કરો"]
            },
            "donts": {
                "en": ["Do not purchase vehicle/gadgets purely in personal name", "Avoid unverified speculative schemes"],
                "hi": ["वाहन या गैजेट केवल अपने अकेले नाम पर न खरीदें", "सट्टेबाजी और अनिश्चित योजनाओं से दूर रहें"],
                "gu": ["વાહન ફક્ત પોતાના એકલા નામે ન ખરીદવું", "સટ્ટાકીય કે અજાણી સ્કીમોથી દૂર રહેવું"]
            }
        },
        5: {
            "dos": {
                "en": ["Close sales deals and client contracts", "Organize budgets and optimize cash flows", "Offer green fodder to cows on Wednesday"],
                "hi": ["व्यापारिक सौदों व अनुबंधों पर हस्ताक्षर करें", "वित्तीय बजट व्यवस्थित करें", "बुधवार को गाय को हरा चारा खिलाएं"],
                "gu": ["વેપારી ડીલ અને ગ્રાહક કરારો પાકા કરો", "બજેટ અને રોકડ વ્યવહારો ગોઠવો", "બુધવારે ગાયને લીલું ઘાસ ખવડાવો"]
            },
            "donts": {
                "en": ["Avoid sharp, blunt or sarcastic speech", "Do not scatter focus across too many tasks"],
                "hi": ["कड़वी या व्यंग्यपूर्ण वाणी से बचें", "एक साथ बहुत अधिक कार्यों में ध्यान न भटकाएं"],
                "gu": ["કડવી કે કટાક્ષભરી વાણી ટાળવી", "એકસાથે બહુ બધા કામોમાં ધ્યાન ન વહેંચવું"]
            }
        },
        6: {
            "dos": {
                "en": ["Purchase lifestyle assets, gifts, and fine clothing", "Host celebratory social gatherings", "Respect and support female associates"],
                "hi": ["सौंदर्य सामग्री, वस्त्र व उपहार क्रय करें", "पारिवारिक व सामाजिक उत्सव आयोजित करें", "स्त्री वर्ग का सम्मान करें"],
                "gu": ["નવા વસ્ત્રો, આભૂષણો કે ભેટની ખરીદી કરો", "કૌટુંબિક પ્રસંગોનું આયોજન કરો", "સ્ત્રીઓનું સન્માન અને સહયોગ કરો"]
            },
            "donts": {
                "en": ["Do not indulge in wasteful luxury expenditures", "Avoid frivolous romantic entanglements"],
                "hi": ["दिखावे और फिजूलखर्ची से बचें", "अनावश्यक वासनात्मक आकर्षणों से दूर रहें"],
                "gu": ["ખોટા દેખાડા અને ઉડાઉ ખર્ચા ટાળવા", "અનૈતિક આકર્ષણોથી દૂર રહેવું"]
            }
        },
        7: {
            "dos": {
                "en": ["Dedicate time to spiritual research, mantras, and yoga", "Undertake peaceful retreat journeys", "Donate to orphanages or feed street animals"],
                "hi": ["मंत्र साधना, योग व शोध कार्यों में समय लगाएं", "तीर्थ यात्रा या शांत स्थलों का भ्रमण करें", "अनाथों को दान दें या मूक जीवों को भोजन कराएं"],
                "gu": ["મંત્ર સાધના, ધ્યાન અને સંશોધનમાં સમય આપો", "તીર્થયાત્રા કે શાંત સ્થળે પ્રવાસ કરો", "અનાથોને દાન આપો અને અબોલ જીવોને ચણ નાખો"]
            },
            "donts": {
                "en": ["Avoid over-analyzing past events or suspecting close ones", "Do not isolate yourself completely"],
                "hi": ["अतीत की बातों का बाल की खाल न निकालें", "दूसरों पर अकारण संदेह न करें"],
                "gu": ["ભૂતકાળની વાતોનું વધુ વિશ્લેષણ ન કરવું", "બીજા પર અકારણ શંકા ન કરવી"]
            }
        },
        8: {
            "dos": {
                "en": ["Execute rigorous physical and professional duties", "Invest in long-term blue-chip assets and real estate", "Help laborers and underprivileged persons on Saturday"],
                "hi": ["कठोर परिश्रम व संगठित कार्यशैली अपनाएं", "दीर्घकालिक अचल संपत्ति पर विचार करें", "शनिवार को निर्धनों या श्रमिकों को भोजन/वस्त्र दें"],
                "gu": ["શિસ્તબદ્ધ અને યોજનાબદ્ધ મહેનત કરો", "લાંબા ગાળાના રોકાણ અને જમીન-મકાન બાબતે આગળ વધો", "શનિવારે શ્રમિકો અને ગરીબોને મદદ કરો"]
            },
            "donts": {
                "en": ["Avoid quick-rich shortcuts or speculative trading", "Refrain from buying iron items on Saturdays"],
                "hi": ["सट्टेबाजी व शीघ्र धन कमाने के प्रलोभन से बचें", "शनिवार को लोहे का फर्नीचर या धातु न खरीदें"],
                "gu": ["ઝડપી પૈસા કમાવાના શોર્ટકટ ટાળવા", "શનિવારે લોખંડની ચીજવસ્તુઓ ન ખરીદવી"]
            }
        },
        9: {
            "dos": {
                "en": ["Take decisive executive decisions", "Engage in energetic fitness, sports, or property deals", "Recite Hanuman Chalisa daily"],
                "hi": ["साहसिक व त्वरित निर्णय लें", "भूमि सौदों व शारीरिक फिटनेस पर ध्यान दें", "प्रतिदिन श्री हनुमान चालीसा का पाठ करें"],
                "gu": ["સાહસિક અને ત્વરિત નિર્ણયો લો", "જમીન-મિલકતના સોદા અને સ્વાસ્થ્ય પર ધ્યાન આપો", "રોજેરોજ શ્રી હનુમાન ચાલીસાનો પાઠ કરો"]
            },
            "donts": {
                "en": ["Avoid hot-headed arguments and rash driving", "Control blood pressure and avoid excess salt on Tuesday"],
                "hi": ["क्रोध, उग्र बहस और तेज वाहन चलाने से बचें", "मंगलवार को नमक का कम सेवन करें"],
                "gu": ["ઉગ્ર બોલાચાલી અને ઝડપી વાહન ચલાવવું ટાળવું", "મંગળવારે મીઠાનું સેવન ઓછું કરવું"]
            }
        }
    }
    
    # 9-Phase Roadmap Assembly
    pd_roadmap = []
    for idx, p in enumerate(pd_info["periods"], 1):
        p_num = p["number"]
        p_planet = PLANET_INFO[p_num][lang]["planet"]
        p_tone = "Auspicious (+)" if p_num in [1, 3, 5, 6] else ("Favorable" if p_num in [7, 8] else "Dynamic / Caution")
        if lang == "hi":
            p_tone = "अत्यंत शुभ (+)" if p_num in [1, 3, 5, 6] else ("अनुकूल" if p_num in [7, 8] else "सावधानी / ऊर्जा")
        elif lang == "gu":
            p_tone = "અતિ શુભ (+)" if p_num in [1, 3, 5, 6] else ("સાનુકૂળ" if p_num in [7, 8] else "સાવચેતી / સક્રિય")
            
        pd_roadmap.append({
            "phase": idx,
            "number": p_num,
            "planet": p_planet,
            "duration_days": p["duration_days"],
            "start_str": p["start_str"],
            "end_str": p["end_str"],
            "is_active": p["is_active"],
            "tone": p_tone
        })

    return {
        "mahadasha": {
            "title": UI_TEXT[lang]["tier_mahadasha_title"],
            "number": active_md_num,
            "planet": active_md_planet,
            "duration": f"{md_duration} Years",
            "start_str": md_start_str,
            "end_str": md_end_str,
            "financial_tone": "Expansive (+)" if is_md_fin_fav else "Consolidating / Hedged (-)",
            "description": md_descriptions[active_md_num][lang],
            "rule_note": "Rule: If Mahadasha activates numbers +3, +5, +6, or +8, finance and status expand exponentially; while challenging numbers advise protective asset hedging."
        },
        "antardasha": {
            "title": UI_TEXT[lang]["tier_antardasha_title"],
            "number": active_ad_num,
            "planet": active_ad_planet,
            "duration": "1 Year (Annual)",
            "start_str": ad_start_str,
            "end_str": ad_end_str,
            "annual_theme": ad_annual_themes[active_ad_num][lang],
            "travel_forecast": "High probability of domestic or foreign journey" if has_travel_in_ad else "Standard local travel",
            "asset_forecast": "Favorable annual alignment for real estate or vehicle acquisition" if has_property_in_ad else "Maintain existing assets"
        },
        "pratyantar_dasha": {
            "title": UI_TEXT[lang]["tier_pratyantar_title"],
            "number": active_pd_num,
            "planet": active_pd_planet,
            "duration_days": pd_days,
            "start_str": pd_start_str,
            "end_str": pd_end_str,
            "dos": pd_dos_donts[active_pd_num]["dos"][lang],
            "donts": pd_dos_donts[active_pd_num]["donts"][lang]
        },
        "pd_roadmap": pd_roadmap
    }

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
    pd_info = calculate_pratyantar_dasha(ad_info["ad_number"], ad_info["start"], target_date, ad_info["end"])
    lifetime_ad = calculate_lifetime_antardasha(birth_date, target_date, md_info["all_periods"])
    nine_year_grids = calculate_nine_year_grids_and_outlook(grid_info["counts"], bn, dn, lifetime_ad, lang)
    
    # Active Dasha & Transit Grid (MD + AD + PD Infusion)
    active_md_num = md_info["active_md"]["number"]
    active_ad_num = ad_info["ad_number"]
    active_pd_num = pd_info["active_pd"]["number"]
    dasha_grid_info = calculate_dasha_grid(grid_info, active_md_num, active_ad_num, active_pd_num, dn, lang)
    
    # 3-Tier Period Forecast (Mahadasha, Antardasha, Pratyantar Dasha)
    three_tier = generate_three_tier_predictions(
        bn, dn, grid_info, dasha_grid_info, md_info, ad_info, pd_info, lang
    )
    
    # Active Yogas (Evaluating both Natal and Period-amplified)
    yogas_result = detect_active_yogas(grid_info["counts"], vibrations, lang)
    active_yogas = yogas_result["all"]
    auspicious_yogas = yogas_result["auspicious"]
    inauspicious_yogas = yogas_result["inauspicious"]
    
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
    
    # Build Dynamic Vibrations Analysis (Period vs Natal Shifts)
    vibrations_data = build_vibrations_analysis(
        grid_info["counts"], dasha_grid_info["total_counts"], dn, lang
    )
    vibration_list = vibrations_data["active_period"]

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

    # Per-number remedies for all afflicted / negative numbers in natal or active period
    remedies_by_number = []
    seen_rem_nums = set()
    for vib in vibrations_data["active_period"]:
        num = vib["number"]
        if (vib["type"] == "-" or vib["count"] >= 2) and num not in seen_rem_nums:
            seen_rem_nums.add(num)
            rem_obj = NUMBER_REMEDIES[num]
            p_obj = PLANET_INFO[num][lang]
            natal_cnt = grid_info["counts"].get(num, 0)
            remedies_by_number.append({
                "number": num,
                "planet": p_obj["planet"],
                "natal_count": natal_cnt,
                "total_count": vib["count"],
                "type": vib["type"],
                "mantra": rem_obj["mantra"][lang],
                "seva": rem_obj["seva"][lang],
                "donation": rem_obj["donation"][lang],
                "colors": p_obj["colors"],
                "fasting": rem_obj["fasting"][lang],
                "crystal": rem_obj["crystal"][lang],
                "gem": rem_obj["gem"][lang],
            })

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
        "natal_grid": grid_info,
        "dasha_grid": dasha_grid_info,
        "three_tier_forecast": three_tier,
        "color_legend": {
            "natal": {"name": UI_TEXT[lang]["legend_natal"], "code": "NAT", "color": "#d4af37"},
            "md": {"name": UI_TEXT[lang]["legend_md"], "code": "MD", "color": "#38bdf8"},
            "ad": {"name": UI_TEXT[lang]["legend_ad"], "code": "AD", "color": "#22c55e"},
            "pd": {"name": UI_TEXT[lang]["legend_pd"], "code": "PD", "color": "#7c3aed"}
        },
        "vibrations": vibration_list,
        "period_vibrations": vibrations_data["active_period"],
        "natal_vibrations": vibrations_data["natal_baseline"],
        "vibration_shifts": vibrations_data,
        "moolank_qualities": NUMBER_QUALITIES[bn][lang],
        "moolank_precautions": NUMBER_PRECAUTIONS[bn][lang],
        "bhagyank_qualities": NUMBER_QUALITIES[dn][lang],
        "bhagyank_precautions": NUMBER_PRECAUTIONS[dn][lang],
        "dasha": {
            "active_md": md_info["active_md"],
            "active_ad": ad_info,
            "active_pd": pd_info["active_pd"],
            "md_timeline": md_info["periods"],
            "all_md_timeline": md_info["all_periods"],
            "lifetime_ad": lifetime_ad,
            "nine_year_grids": nine_year_grids,
            "pratyantar_full": pd_info.get("full_periods", pd_info["periods"])
        },
        "remedies_by_number": remedies_by_number,
        "yogas": active_yogas,
        "auspicious_yogas": auspicious_yogas,
        "inauspicious_yogas": inauspicious_yogas,
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


def compile_matchmaking_report(
    boy_name: str,
    boy_dob: str,
    girl_name: str,
    girl_dob: str,
    lang: str = "en",
) -> Dict[str, Any]:
    """
    Computes the 5-pillar NumberWise Vedic Numerology Match Making Report (100 points total)
    for Boy (Groom) and Girl (Bride).
    """
    boy_profile = compile_full_numerology_profile(boy_name, boy_dob, gender="Male", lang=lang)
    girl_profile = compile_full_numerology_profile(girl_name, girl_dob, gender="Female", lang=lang)

    today = date.today()
    def _age_from_iso(iso_str: str) -> int:
        b = date.fromisoformat(iso_str)
        return today.year - b.year - ((today.month, today.day) < (b.month, b.day))

    boy_age = _age_from_iso(boy_profile["client"]["dob_iso"])
    girl_age = _age_from_iso(girl_profile["client"]["dob_iso"])

    boy_pos = {v["number"] for v in boy_profile["natal_vibrations"] if v["type"] == "+"}
    girl_pos = {v["number"] for v in girl_profile["natal_vibrations"] if v["type"] == "+"}

    def _presence_label(in_boy: bool, in_girl: bool) -> str:
        if in_boy and in_girl:
            return f"{boy_name} and {girl_name}"
        if in_boy:
            return boy_name
        if in_girl:
            return girl_name
        return "neither"

    # Pillar 1: Emotional Quotient (+2 in both grids)
    p1_b, p1_g = (2 in boy_pos), (2 in girl_pos)
    p1_score = 20 if (p1_b and p1_g) else (10 if (p1_b or p1_g) else 0)

    # Pillar 2: Practical Quotient (+1, +3 or +9 in both grids)
    p2_b = any(n in boy_pos for n in (1, 3, 9))
    p2_g = any(n in girl_pos for n in (1, 3, 9))
    p2_score = 20 if (p2_b and p2_g) else (10 if (p2_b or p2_g) else 0)

    # Pillar 3: Money Compatibility (+3, +5, +6 or +8 in both grids)
    p3_b = any(n in boy_pos for n in (3, 5, 6, 8))
    p3_g = any(n in girl_pos for n in (3, 5, 6, 8))
    p3_score = 20 if (p3_b and p3_g) else (10 if (p3_b or p3_g) else 0)

    # Pillar 4: Root & Destiny Matching (Basic 10 pts + Destiny 10 pts)
    grp_a = {1, 2, 4, 7}
    grp_b = {3, 6, 9}
    def _pair_compat(n1: int, n2: int) -> tuple:
        if n1 == 8 and n2 in (8, 4) or (n2 == 8 and n1 in (8, 4)):
            return 0, "should avoid pairing (Rule 3: 8 with 8/4) (0/10)"
        if n1 == 5 and n2 == 5:
            return 10, "both are 5 — ideal match (10/10)"
        if 5 in (n1, n2):
            return 5, "5 with non-5 — neutral/moderate (5/10)"
        if (n1 in grp_a and n2 in grp_a) or (n1 in grp_b and n2 in grp_b):
            return 10, "are in the same compatibility group (10/10)"
        from vedic_translations import PLANET_INFO
        en_str = PLANET_INFO[n1]["en"]["enemy_nums"]
        enemies = [int(x.strip()) for x in en_str.split(",") if x.strip().isdigit()]
        if n2 in enemies:
            return 0, "are in opposing groups (0/10)"
        return 5, "are neutral (5/10)"

    b_bn, g_bn = boy_profile["core_numbers"]["bn"], girl_profile["core_numbers"]["bn"]
    b_dn, g_dn = boy_profile["core_numbers"]["dn"], girl_profile["core_numbers"]["dn"]
    bn_pts, bn_desc = _pair_compat(b_bn, g_bn)
    dn_pts, dn_desc = _pair_compat(b_dn, g_dn)
    p4_score = bn_pts + dn_pts

    # Pillar 5: Marriage-saving numbers (+3, +7, +8 in either grid)
    ms_nums = [n for n in (3, 7, 8) if (n in boy_pos or n in girl_pos)]
    p5_score = min(20, len(ms_nums) * 10)

    total_score = p1_score + p2_score + p3_score + p4_score + p5_score

    if total_score > 70:
        verdict = "Good matching"
        verdict_sub = "Above 70% — strong overall alignment across the five pillars."
        verdict_level = "good"
    elif total_score >= 50:
        verdict = "Suggestive matching"
        verdict_sub = "50–70% — workable alignment with conscious communication and remedies."
        verdict_level = "moderate"
    else:
        verdict = "Not suggested"
        verdict_sub = "Below 50% — the course does not suggest this match."
        verdict_level = "low"

    # Evaluate Rules 1-8 from NumberWise Course Notes
    rules_checks = []
    # Rules 1-4: Basic Number Group Matching
    if b_bn == 5 or g_bn == 5:
        r14_ok = (b_bn == 5 and g_bn == 5)
        rules_checks.append({
            "rule": "Rule 4",
            "status": "ok" if r14_ok else "warn",
            "title": "Basic Number 5 should marry only Basic 5",
            "detail": f"Boy is {b_bn} and Girl is {g_bn}."
        })
    elif b_bn == 8 or g_bn == 8:
        r3_bad = (b_bn == 8 and g_bn in (8, 4)) or (g_bn == 8 and b_bn in (8, 4))
        rules_checks.append({
            "rule": "Rule 3",
            "status": "reject" if r3_bad else "ok",
            "title": "Basic Number 8 should avoid marrying 8 or 4",
            "detail": f"Boy is {b_bn} and Girl is {g_bn}."
        })
    else:
        same_grp = ((b_bn in grp_a and g_bn in grp_a) or (b_bn in grp_b and g_bn in grp_b))
        rules_checks.append({
            "rule": "Rules 1 · 2",
            "status": "ok" if same_grp else "warn",
            "title": "Basic Numbers 1,2,4,7 marry within group; 3,6,9 within group",
            "detail": f"Here {b_bn} and {g_bn} are {'in the same group' if same_grp else 'in different groups'}."
        })

    # Rule 5: Reject grids with D5 or D1 if 2, 6, 8 are ALL missing
    def _check_r5(prof, label):
        cnts = prof["natal_grid"]["counts"]
        d = prof["core_numbers"]["dn"]
        if d in (1, 5) and all(cnts.get(x, 0) == 0 for x in (2, 6, 8)):
            return f"{label} (D{d} with 2, 6, 8 all missing)"
        return None
    r5_hits = [x for x in [_check_r5(boy_profile, boy_name), _check_r5(girl_profile, girl_name)] if x]
    rules_checks.append({
        "rule": "Rule 5",
        "status": "reject" if r5_hits else "ok",
        "title": "Reject grids with D5 or D1 if 2, 6, and 8 are missing",
        "detail": ", ".join(r5_hits) if r5_hits else "Neither grid has D1/D5 missing 2, 6, and 8."
    })

    # Rule 6: Reject grids containing 222, 333, 444, or 777
    def _check_r6(prof, label):
        cnts = prof["natal_grid"]["counts"]
        bad = [str(n) * cnts[n] for n in (2, 3, 4, 7) if cnts.get(n, 0) >= 3]
        return f"{label} ({', '.join(bad)})" if bad else None
    r6_hits = [x for x in [_check_r6(boy_profile, boy_name), _check_r6(girl_profile, girl_name)] if x]
    rules_checks.append({
        "rule": "Rule 6",
        "status": "reject" if r6_hits else "ok",
        "title": "Reject grids containing extreme repetitions (222, 333, 444, 777)",
        "detail": ", ".join(r6_hits) if r6_hits else "No extreme repetitions (222/333/444/777) in either grid."
    })

    # Rule 7: D4 or D8 should marry after age 30
    r7_hits = []
    if b_dn in (4, 8) and boy_age < 30:
        r7_hits.append(f"{boy_name} (D{b_dn}, age {boy_age} < 30)")
    if g_dn in (4, 8) and girl_age < 30:
        r7_hits.append(f"{girl_name} (D{g_dn}, age {girl_age} < 30)")
    rules_checks.append({
        "rule": "Rule 7",
        "status": "warn" if r7_hits else "ok",
        "title": "People with D4 or D8 should marry after age 30",
        "detail": ", ".join(r7_hits) if r7_hits else "Age/Destiny maturity check passed."
    })

    # Rule 8: D6 requires strong support (positive 2, 4, 8, or 9)
    r8_hits = []
    if b_dn == 6 and not any(n in boy_pos for n in (2, 4, 8, 9)):
        r8_hits.append(f"{boy_name} (D6 lacks positive 2/4/8/9 support)")
    if g_dn == 6 and not any(n in girl_pos for n in (2, 4, 8, 9)):
        r8_hits.append(f"{girl_name} (D6 lacks positive 2/4/8/9 support)")
    rules_checks.append({
        "rule": "Rule 8",
        "status": "warn" if r8_hits else "ok",
        "title": "D6 requires strong support in the grid (good 2, 4, 8, or 9)",
        "detail": ", ".join(r8_hits) if r8_hits else "D6 support check passed."
    })

    # 5-Year Litigation Check (Page 47 & 87: 9&4, 5&4, or -6 active for 2+ years in next 5 years)
    def _litigation_5yr(prof, label):
        ad_rows = prof["dasha"].get("lifetime_ad", [])
        act_idx = next((i for i, r in enumerate(ad_rows) if r.get("is_active")), 0)
        next5 = ad_rows[act_idx : act_idx + 5]
        nat_counts = prof["natal_grid"]["counts"]
        lit_years = []
        for yr_row in next5:
            comb = dict(nat_counts)
            comb[yr_row["md"]] = comb.get(yr_row["md"], 0) + 1
            comb[yr_row["ad"]] = comb.get(yr_row["ad"], 0) + 1
            v = evaluate_vibrations(comb, prof["core_numbers"]["dn"])
            has_94 = comb.get(9, 0) > 0 and comb.get(4, 0) > 0
            has_54 = comb.get(5, 0) > 0 and comb.get(4, 0) > 0
            has_neg6 = v.get(6) == "-"
            if has_94 or has_54 or has_neg6:
                lit_years.append(str(yr_row["year"]))
        return {
            "name": label,
            "risk": len(lit_years) >= 2,
            "years": lit_years,
        }

    litigation_check = {
        "boy": _litigation_5yr(boy_profile, boy_name),
        "girl": _litigation_5yr(girl_profile, girl_name),
    }

    same_bn_group = ((b_bn in grp_a and g_bn in grp_a) or (b_bn in grp_b and g_bn in grp_b))

    pillars = [
        {
            "key": "emotional",
            "title": "Emotional Quotient",
            "score": p1_score,
            "max": 20,
            "desc": f"How each expresses emotion, handles conflict and stays steady day to day. Points for +2 in both grids — present in: {_presence_label(p1_b, p1_g)}.",
        },
        {
            "key": "practical",
            "title": "Practical Quotient",
            "score": p2_score,
            "max": 20,
            "desc": f"Decision-making, responsibility and long-term planning. Points for +1, +3 or +9 in both grids — present in: {_presence_label(p2_b, p2_g)}.",
        },
        {
            "key": "money",
            "title": "Money Compatibility",
            "score": p3_score,
            "max": 20,
            "desc": f"Spending, saving, financial discipline and money mindset. Points for +3, +5, +6 or +8 in both grids — present in: {_presence_label(p3_b, p3_g)}.",
        },
        {
            "key": "root_destiny",
            "title": "Root & Destiny Matching",
            "score": p4_score,
            "max": 20,
            "desc": f"Basic Numbers {b_bn} and {g_bn} {bn_desc}. Destiny Numbers {b_dn} and {g_dn} {dn_desc} — how well their life purposes align.",
        },
        {
            "key": "marriage_saving",
            "title": "Marriage-saving numbers",
            "score": p5_score,
            "max": 20,
            "desc": (
                f"Extra points for +3, +7 or +8 in either grid. Found: {', '.join('+' + str(n) for n in ms_nums)}."
                if ms_nums else
                "Extra points for +3, +7 or +8 in either grid. None found. +3 brings communication harmony, +7 spiritual bonding, +8 discipline and long-term commitment."
            ),
        },
    ]

    weak_pillars = [p["title"].lower() for p in pillars if p["score"] < 15]
    weak_str = " and ".join(weak_pillars[:2]) if weak_pillars else "none"

    return {
        "consultant": boy_profile["consultant"],
        "boy": {
            "name": boy_name,
            "dob": boy_profile["client"]["dob"].replace("/", "-"),
            "age": boy_age,
            "bn": b_bn,
            "dn": b_dn,
            "bn_planet": boy_profile["core_numbers"]["bn_planet"],
            "dn_planet": boy_profile["core_numbers"]["dn_planet"],
            "grid": boy_profile["natal_grid"],
            "vibrations": boy_profile["natal_vibrations"],
            "yogas": boy_profile["yogas"],
        },
        "girl": {
            "name": girl_name,
            "dob": girl_profile["client"]["dob"].replace("/", "-"),
            "age": girl_age,
            "bn": g_bn,
            "dn": g_dn,
            "bn_planet": girl_profile["core_numbers"]["bn_planet"],
            "dn_planet": girl_profile["core_numbers"]["dn_planet"],
            "grid": girl_profile["natal_grid"],
            "vibrations": girl_profile["natal_vibrations"],
            "yogas": girl_profile["yogas"],
        },
        "total_score": total_score,
        "verdict": verdict,
        "verdict_sub": verdict_sub,
        "verdict_level": verdict_level,
        "pillars": pillars,
        "rules_checks": rules_checks,
        "litigation_check": litigation_check,
        "same_bn_group": same_bn_group,
        "weak_summary": weak_str,
        "generated_on": today.strftime("%d %B %Y"),
    }
