# -*- coding: utf-8 -*-
"""
Vedic Numerology Knowledge Base & Trilingual Dictionaries
Languages: English (en), Hindi (hi), Gujarati (gu)
Derived strictly from NumberWise Vedic Numerology Course Levels 1 & 2 and Vedic Remedies.
"""

# Consultant & Legal Copyright Information
CONSULTANT_INFO = {
    "name": "Jigar Thakkar",
    "phone": "+91 9377614772",
    "phone_raw": "9377614772",
    "email": "jigar93776@gmail.com",
    "title": {
        "en": "Certified Vedic Numerologist & Vastu Consultant",
        "hi": "प्रमाणित वैदिक अंकशास्त्री एवं वास्तु परामर्शदाता",
        "gu": "પ્રમાણિત વૈદિક અંકશાસ્ત્રી અને વાસ્તુ સલાહકાર"
    },
    "copyright": {
        "en": "© 2026 Jigar Thakkar. All Rights Reserved. Prepared exclusively for the named client through authenticated Vedic Numerology. Unauthorized copying or redistribution is strictly prohibited.",
        "hi": "© 2026 जिगर ठक्कर। सर्वाधिकार सुरक्षित। यह रिपोर्ट प्रामाणिक वैदिक अंकशास्त्र द्वारा केवल संबंधित जातक हेतु तैयार की गई है। अनुमति के बिना प्रतिलिपि बनाना वर्जित है।",
        "gu": "© 2026 જીગર ઠક્કર. સર્વાધિકાર સુરક્ષિત. આ રિપોર્ટ પ્રામાણિક વૈદિક અંકશાસ્ત્ર દ્વારા ફક્ત સંબંધિત જાતક માટે તૈયાર કરવામાં આવ્યો છે. નકલ કરવી કાનૂની ગુનો છે."
    }
}

# UI Strings for Reports and Dashboard
UI_TEXT = {
    "en": {
        "title": "Vedic Numerology Studio",
        "consultant_title": "Jigar Thakkar • Certified Numerologist",
        "report_title": "Personal Vedic Numerology Blueprint",
        "sub_title": "Prepared by Jigar Thakkar (Certified Numerologist) • Contact: +91 9377614772",
        "client_profile": "Client Profile & Planetary Alignments",
        "full_name": "Client Name",
        "dob": "Date of Birth",
        "gender": "Gender",
        "weekday": "Day of Birth",
        "basic_number": "Basic Number (Moolank)",
        "destiny_number": "Destiny Number (Bhagyank)",
        "name_number": "Name Number (Namank)",
        "name_harmony": "Name Vibration Alignment",
        "ruling_planet": "Ruling Planet",
        "favourable_numbers": "Favourable Numbers",
        "favourable_days": "Favourable Days",
        "favourable_colors": "Favourable Colors",
        "friendly_numbers": "Friendly Numbers (Allies)",
        "neutral_numbers": "Neutral Numbers",
        "enemy_numbers": "Unfriendly / Avoid Numbers",
        "auspicious_direction": "Auspicious Vastu Direction",
        "auspicious_metal": "Auspicious Metal",
        "gemstone": "Recommended Gemstone",
        "vedic_grid_title": "Vedic Birth Grid (Natal Kundali)",
        "grid_explanation": "Vedic 3x3 Natal Grid reveals the distribution of planetary vibrations in life.",
        "natal_grid_title": "Natal Birth Grid (Lifetime Inborn Matrix)",
        "natal_grid_sub": "Permanent inborn planetary frequencies & lifetime karmic foundation",
        "dasha_grid_title": "Dasha & Transit Activation Grid (Active Period)",
        "dasha_grid_sub": "Dynamic activation: Natal (Gold) + Mahadasha (Sky Blue) + Antardasha (Green) + Pratyantar (Orange)",
        "legend_natal": "Natal Inborn (Gold)",
        "legend_md": "Mahadasha • Multi-Year (Sky Blue)",
        "legend_ad": "Antardasha • Yearly (Emerald Green)",
        "legend_pd": "Pratyantar Dasha • Monthly Sub-Phase (Royal Purple)",
        "tier_mahadasha_title": "Mahadasha: Long-Term Macro Life Cycle",
        "tier_antardasha_title": "Antardasha: Annual 1-Year Forecast",
        "tier_pratyantar_title": "Pratyantar Dasha: Active Monthly Sub-Phase",
        "pd_roadmap_title": "Annual 9-Phase Pratyantar Dasha Roadmap",
        "monthly_dos": "Favorable Focus for Active Month",
        "monthly_donts": "Precautions for Active Month",
        "active_vibrations": "Planetary Vibrations Analysis (+ / -)",
        "vibrations_tab_period": "★ Active Dasha Period (Current Year/Phase)",
        "vibrations_tab_natal": "👑 Lifetime Inborn Natal Matrix (Permanent Baseline)",
        "vibrations_disclaimer": "Dynamic Vedic Principle: Unlike permanent inborn traits, planetary vibrations dynamically fluctuate under active Mahadasha, Antardasha, and Pratyantar Dasha cycles. A number that is challenging in the inborn chart can become auspicious during a Dasha (e.g. Number 8 becoming 88 / Even 8), and an auspicious number can become challenging (e.g. Number 9 becoming 99 / Multiple 9) for that specific period.",
        "shift_neg_to_pos": "★ Transformed to Positive (+) in Active Dasha",
        "shift_pos_to_neg": "⚠ Shifted to Challenging (-) in Active Dasha",
        "shift_newly_activated": "✦ Dynamically Activated via Current Dasha",
        "shift_stable": "Consistent Baseline Vibration",
        "positive": "Positive (+)",
        "negative": "Challenging / Negative (-)",
        "neutral": "Neutral",
        "moolank_qualities": "Core Personality Traits (Moolank / Root Number)",
        "bhagyank_qualities": "Life Path & Destiny Traits (Bhagyank / Destiny Number)",
        "moolank_precautions": "Key Precautions for Moolank",
        "bhagyank_precautions": "Key Precautions for Bhagyank",
        "dasha_timeline": "Planetary Dasha Cycles (Timeline)",
        "mahadasha": "Mahadasha (Major Period)",
        "antardasha": "Antardasha (Sub-Period)",
        "pratyantar_dasha": "Pratyantar Dasha (Current Active Phase)",
        "active_yogas": "Active Yogas in Birth Chart",
        "auspicious_yogas_title": "Auspicious Planetary Yogas (Divine Alignments)",
        "inauspicious_yogas_title": "Challenging Planetary Yogas & Doshas (Karmic Hurdles & Remedial Protection)",
        "mitigation_remedy": "Remedial Mitigation Key:",
        "predictions_title": "Comprehensive Life Predictions",
        "pred_finance": "Finance & Wealth Predictions",
        "pred_property": "Property & Real Estate Predictions",
        "pred_vehicle": "Vehicle Acquisition Predictions",
        "pred_education": "Education & Intellectual Strengths",
        "pred_travel": "Travel & Foreign Settlement",
        "pred_litigation": "Litigation, Disputes & Court Cases",
        "pred_relationship": "Marriage, Harmony & Divorce Predictions",
        "pred_health": "Health & Vitality Predictions",
        "remedies_title": "Vedic Remedial Measures & Guidance",
        "gemstone_remedy": "Gemstone & Crystal Recommendation",
        "mantra_remedy": "Sacred Vedic Mantras",
        "fasting_remedy": "Vrat & Fasting Discipline",
        "donation_remedy": "Charity & Daana (Donations)",
        "seva_remedy": "Seva (Selfless Service & Karma Correction)",
        "lifestyle_remedy": "Color & Lifestyle Harmonization",
        "general_remedies": "General Vedic Remedies (Wealth, Health, Harmony)",
        "certified_box_title": "Certified Astrological Verification & Seal",
        "certified_box_text": "This report is prepared and certified by Jigar Thakkar, Certified Numerologist, adhering strictly to authenticated Vedic Numerology algorithms and planetary principles. May the planetary energies guide you towards prosperity, good health, and spiritual enlightenment.",
        "signature_line": "Jigar Thakkar (Certified Numerologist)",
        "page": "Page",
        "of": "of",
        "consultant_notes": "Personalized Notes & Special Instructions from Jigar Thakkar",
        "phone_label": "Phone / WhatsApp",
        "email_label": "Email",
                "toc_title": "10-Chapter Master Life Index",
        "p1_title": "Personal Vedic Numerology Blueprint & Life Manual",
        "p1_sub": "Authentic Mathematical Calculation & Karmic Roadmap",
        "chap_1_badge": "CHAPTER 1 OF 9 • SACRED GRID MATRIX",
        "chap_1_title": "Dual Vedic Grids: Lifetime Natal Blueprint & Active Dasha Activation",
        "chap_2_badge": "CHAPTER 2 OF 9 • HARMONY COMPASS",
        "chap_2_title": "Cosmic Allies, Auspicious Vastu Orientations & Name Frequency Alignment",
        "chap_3_badge": "CHAPTER 3 OF 9 • SOUL IDENTITY",
        "chap_3_title": "Core Personality, Inborn Superpowers & Mindful Guardrails (Moolank)",
        "chap_4_badge": "CHAPTER 4 OF 9 • DESTINY BLUEPRINT",
        "chap_4_title": "Karmic Calling, Higher Life Mission & Soul Purpose (Bhagyank)",
        "chap_5_badge": "CHAPTER 5 OF 9 • MACRO TIME WHEEL",
        "chap_5_title": "Mahadasha: 9-Year Macro Planetary Life Cycle & Wealth Directives",
        "chap_6_badge": "CHAPTER 6 OF 9 • ANNUAL & MONTHLY TIMING",
        "chap_6_title": "Antardasha (Annual 1-Year Forecast) & Active Pratyantar Action Window",
        "chap_7_badge": "CHAPTER 7 OF 9 • TIMING ROADMAP",
        "chap_7_title": "Annual 9-Phase Pratyantar Dasha Timeline & Golden Timing Windows",
        "chap_8_badge": "CHAPTER 8 OF 9 • YOGAS & DOSHAS",
        "chap_8_title": "Rare Planetary Yogas, Karmic Afflictions & Dynamic Vibrational Polarities",
        "chap_9_badge": "CHAPTER 9 OF 9 • FUTURE PREDICTIONS & REMEDIES",
        "chap_9_title": "8-Pillar Life Predictions, Sacred Vedic Remedies & Official Certification",
        "curiosity_hook_1": "🔮 CHAPTER 1 PREVIEW: Turn to Page 2 to examine your authentic 3x3 Natal Birth Grid and witness how active planetary Dashas awaken your dormant frequencies...",
        "curiosity_hook_2": "🧭 CHAPTER 2 PREVIEW: Turn to Page 3 to discover your Cosmic Allies, Auspicious Vastu Direction, lucky gemstone, and Name Numerology harmony...",
        "curiosity_hook_3": "🌟 CHAPTER 3 PREVIEW: Turn to Page 4 to deep dive into your Inborn Soul Powers, core psychological strengths, and what pitfalls you must avoid...",
        "curiosity_hook_4": "🎯 CHAPTER 4 PREVIEW: Turn to Page 5 to unveil your Destiny Number (Bhagyank), your soul's higher karmic calling, and life purpose...",
        "curiosity_hook_5": "⏳ CHAPTER 5 PREVIEW: Turn to Page 6 to enter the Time Wheel: Discover your active 9-Year Mahadasha macro life cycle and wealth directive...",
        "curiosity_hook_6": "📅 CHAPTER 6 PREVIEW: Turn to Page 7 to zoom into your Annual 1-Year Forecast (Antardasha) and your active 30-day action window...",
        "curiosity_hook_7": "🗓️ CHAPTER 7 PREVIEW: Turn to Page 8 for your complete 12-Month Calendar Roadmap, highlighting your Golden Timing Phases...",
        "curiosity_hook_8": "⚡ CHAPTER 8 PREVIEW: Turn to Page 9 to reveal the rare Divine Yogas and Karmic Doshas active in your birth chart, plus your vibrational polarities...",
        "curiosity_hook_9": "🔮 CHAPTER 9 PREVIEW: Turn to Page 10 for your 8-Pillar Life Predictions, personalized Vedic Remedies, and Official Verification Seal...",
        "empowerment_blessing": "✨ YOUR SACRED ROADMAP TO TRANSFORMATION: Apply these prescribed remedies with faith and dedication. For deeper 1-on-1 personalized guidance, birth chart analysis, or Vastu audits, connect directly with Jigar Thakkar at +91 9377614772."
    },
    "hi": {
        "title": "वैदिक अंकशास्त्र स्टूडियो",
        "consultant_title": "जिगर ठक्कर • प्रमाणित अंकशास्त्री",
        "report_title": "व्यक्तिगत वैदिक अंकशास्त्र परामर्श रिपोर्ट",
        "sub_title": "परामर्शदाता: जिगर ठक्कर (प्रमाणित अंकशास्त्री) • संपर्क: +91 9377614772",
        "client_profile": "जातक विवरण एवं ग्रहीय समीकरण",
        "full_name": "जातक का नाम",
        "dob": "जन्म तिथि",
        "gender": "लिंग",
        "weekday": "जन्म वार (दिन)",
        "basic_number": "मूलांक (मूल संख्या)",
        "destiny_number": "भाग्यांक (भाग्य संख्या)",
        "name_number": "नामांक (नाम संख्या)",
        "name_harmony": "नाम स्पंदन संतुलन",
        "ruling_planet": "स्वामी ग्रह",
        "favourable_numbers": "शुभ अंक",
        "favourable_days": "शुभ वार (दिन)",
        "favourable_colors": "शुभ रंग",
        "friendly_numbers": "मित्र अंक (सहयोगी)",
        "neutral_numbers": "सम अंक (तटस्थ)",
        "enemy_numbers": "शत्रु / वर्जित अंक",
        "auspicious_direction": "शुभ वास्तु दिशा",
        "auspicious_metal": "शुभ धातु",
        "gemstone": "अनुशंसित रत्न",
        "vedic_grid_title": "वैदिक जन्म चक्र (3x3 ग्रिड)",
        "grid_explanation": "वैदिक 3x3 जन्म चक्र जातक के जीवन में ग्रहीय ऊर्जा के प्रभाव और संतुलन को दर्शाता है।",
        "natal_grid_title": "मूल जन्म चक्र (जीवनकालीन जन्म ग्रिड)",
        "natal_grid_sub": "स्थायी जन्मकालीन ग्रहीय ऊर्जा एवं जीवन की मूल आधारशिला",
        "dasha_grid_title": "दशा एवं गोचर सक्रिय चक्र (वर्तमान ग्रहीय स्पंदन)",
        "dasha_grid_sub": "गतिक सक्रियता: मूल जन्म (स्वर्ण) + महादशा (आसमानी) + अंतर्दशा (हरा) + प्रत्यंतर दशा (नारंगी)",
        "legend_natal": "जन्मकालीन मूल (स्वर्ण)",
        "legend_md": "महादशा • दीर्घकालीन (आसमानी)",
        "legend_ad": "अंतर्दशा • वार्षिक (पन्ना हरा)",
        "legend_pd": "प्रत्यंतर दशा • मासिक उप-चक्र (शाही बैंगनी / Royal Purple)",
        "tier_mahadasha_title": "महादशा: दीर्घकालीन मुख्य जीवन चक्र फलादेश",
        "tier_antardasha_title": "अंतर्दशा: वार्षिक १-वर्षीय विस्तृत फलादेश",
        "tier_pratyantar_title": "प्रत्यंतर दशा: सक्रिय मासिक सूक्ष्म फलादेश",
        "pd_roadmap_title": "वार्षिक ९-चरणीय प्रत्यंतर दशा समयरेखा व कैलेंडर",
        "monthly_dos": "इस सक्रिय माह में करने योग्य कार्य",
        "monthly_donts": "इस सक्रिय माह में विशेष सावधानियां",
        "active_vibrations": "ग्रहीय स्पंदन विश्लेषण (+ / -)",
        "vibrations_tab_period": "★ सक्रिय दशा चक्र (वर्तमान सामयिक स्पंदन)",
        "vibrations_tab_natal": "👑 स्थायी जन्म चक्र (आजीवन मूल आधार स्पंदन)",
        "vibrations_disclaimer": "वैदिक ज्योतिष सिद्धांत: स्थायी जन्मजात प्रवृत्तियों के विपरीत, महादशा, अंतर्दशा एवं प्रत्यंतर दशा के प्रभाव से ग्रहीय स्पंदन समय-समय पर परिवर्तित होते हैं। जन्म चक्र में कठिन (-) फल देने वाला अंक दशा में सम संख्या बनकर अत्यंत शुभ (+) हो सकता है (जैसे अंक 8 का 88 बनना), और शुभ अंक दोहरी ऊर्जा से कठिन (-) हो सकता है (जैसे अंक 9 का 99 बनना)।",
        "shift_neg_to_pos": "★ सक्रिय दशा में शुभ (+) में परिवर्तित",
        "shift_pos_to_neg": "⚠ सक्रिय दशा में कठिन (-) में परिवर्तित",
        "shift_newly_activated": "✦ वर्तमान दशा द्वारा तात्कालिक सक्रियता",
        "shift_stable": "स्थिर ग्रहीय स्पंदन",
        "positive": "सकारात्मक (+)",
        "negative": "कठिन / नकारात्मक (-)",
        "neutral": "तटस्थ",
        "moolank_qualities": "मूलांक के मूल स्वभाव एवं गुण",
        "bhagyank_qualities": "भाग्यांक के जीवन पथ एवं भाग्य प्रभाव",
        "moolank_precautions": "मूलांक हेतु अनिवार्य सावधानियाँ",
        "bhagyank_precautions": "भाग्यांक हेतु अनिवार्य सावधानियाँ",
        "dasha_timeline": "ग्रहीय दशा चक्र (समय रेखा)",
        "mahadasha": "महादशा (मुख्य अवधि)",
        "antardasha": "अंतर्दशा (उप-अवधि)",
        "pratyantar_dasha": "प्रत्यंतर दशा (वर्तमान सक्रिय सूक्ष्म चरण)",
        "active_yogas": "जन्म चक्र में उपस्थित सक्रिय योग",
        "auspicious_yogas_title": "शुभ ग्रहीय योग (दैवीय ऊर्जा चक्र)",
        "inauspicious_yogas_title": "अशुभ योग एवं दोष (कर्म बाधाएं एवं निवारण उपाय)",
        "mitigation_remedy": "दोष निवारण एवं शांति उपाय:",
        "predictions_title": "विस्तृत जीवन भविष्यवाणियाँ",
        "pred_finance": "वित्त एवं धन संपदा भविष्यवाणी",
        "pred_property": "भूमि, भवन एवं अचल संपत्ति भविष्यवाणी",
        "pred_vehicle": "वाहन क्रय एवं सुख भविष्यवाणी",
        "pred_education": "शिक्षा एवं बौद्धिक क्षमता",
        "pred_travel": "यात्रा एवं विदेश गमन योग",
        "pred_litigation": "मुकदमेबाजी, विवाद एवं न्यायालय भविष्यवाणी",
        "pred_relationship": "विवाह, संबंध एवं दांपत्य जीवन",
        "pred_health": "स्वास्थ्य, रोग एवं सुरक्षा भविष्यवाणी",
        "remedies_title": "वैदिक उपचारात्मक उपाय एवं मार्गदर्शन",
        "gemstone_remedy": "रत्न एवं क्रिस्टल परामर्श",
        "mantra_remedy": "पवित्र वैदिक मंत्र साधना",
        "fasting_remedy": "व्रत एवं उपवास नियम",
        "donation_remedy": "दान एवं पुण्य कर्म",
        "seva_remedy": "सेवा एवं कर्म सुधार",
        "lifestyle_remedy": "रंग एवं जीवनशैली संतुलन",
        "general_remedies": "सामान्य वैदिक उपाय (धन, स्वास्थ्य एवं शांति)",
        "certified_box_title": "प्रमाणित वैदिक अंकशास्त्र सत्यापन एवं आशीर्वाद",
        "certified_box_text": "यह रिपोर्ट प्रमाणित अंकशास्त्री जिगर ठक्कर द्वारा प्रामाणिक वैदिक अंकशास्त्र गणनाओं और ग्रहीय नियमों के आधार पर तैयार की गई है। नवग्रह आपके जीवन में सुख, समृद्धि, स्वास्थ्य और शांति का संचार करें।",
        "signature_line": "जिगर ठक्कर (प्रमाणित अंकशास्त्री)",
        "page": "पृष्ठ",
        "of": "का",
        "consultant_notes": "जिगर ठक्कर की विशेष व्यक्तिगत टिप्पणी एवं परामर्श",
        "phone_label": "फोन / व्हाट्सएप",
        "email_label": "ईमेल",
                "toc_title": "१०-अध्यायीय संपूर्ण जीवन विषय-सूची",
        "p1_title": "व्यक्तिगत वैदिक अंकशास्त्र महा-परामर्श एवं जीवन निर्देशिका",
        "p1_sub": "प्रामाणिक गणितीय फलादेश एवं कर्मिक समय चक्र",
        "chap_1_badge": "अध्याय १ / ९ • पावन वैदिक चक्र",
        "chap_1_title": "युगल वैदिक चक्र: आजीवन जन्म कुंडली एवं सक्रिय दशा गोचर संरेखण",
        "chap_2_badge": "अध्याय २ / ९ • समन्वय दिशा-सूचक",
        "chap_2_title": "ग्रहीय मित्र मंडली, शुभ वास्तु दिशाएं एवं नामांक स्पंदन संतुलन",
        "chap_3_badge": "अध्याय ३ / ९ • आत्मिक चेतना",
        "chap_3_title": "मूल स्वभाव, जन्मजात शक्तियां एवं आवश्यक सावधानियां (मूलांक)",
        "chap_4_badge": "अध्याय ४ / ९ • भाग्य प्रारब्ध",
        "chap_4_title": "कर्मिक लक्ष्य, उच्चतर जीवन उद्देश्य एवं उन्नति की कुंजी (भाग्यांक)",
        "chap_5_badge": "अध्याय ५ / ९ • दीर्घकालिक महा-चक्र",
        "chap_5_title": "महादशा: ९-वर्षीय दीर्घकालिक महा-चक्र एवं धन संपदा फलादेश",
        "chap_6_badge": "अध्याय ६ / ९ • वार्षिक एवं मासिक समय चक्र",
        "chap_6_title": "अंतर्दशा (वार्षिक १-वर्षीय फलादेश) एवं सक्रिय मासिक सूक्ष्म काल",
        "chap_7_badge": "अध्याय ७ / ९ • वार्षिक समयरेखा",
        "chap_7_title": "वार्षिक ९-चरणीय प्रत्यंतर दशा कैलेंडर एवं स्वर्णिम मुहूर्त काल",
        "chap_8_badge": "अध्याय ८ / ९ • राजयोग एवं ग्रह दोष",
        "chap_8_title": "दुर्लभ ग्रह योग, कर्मिक दोष शांति एवं गतिज स्पंदन विश्लेषण",
        "chap_9_badge": "अध्याय ९ / ९ • अष्ट-स्तंभ फलादेश एवं सिद्ध उपाय",
        "chap_9_title": "अष्ट-स्तंभ जीवन भविष्यवाणियां, प्रमाणित वैदिक उपचार एवं सत्यापन मुहर",
        "curiosity_hook_1": "🔮 अध्याय १ की झलक: पृष्ठ २ पर जाएं और अपनी जन्मकालीन ३x३ वैदिक कुंडली देखें, और जानें कि वर्तमान दशाएं आपकी सोई हुई ऊर्जाओं को कैसे जगा रही हैं...",
        "curiosity_hook_2": "🧭 अध्याय २ की झलक: पृष्ठ ३ पर जानें अपने सच्चे मित्र अंक, शुभ वास्तु दिशा, भाग्यशाली रत्न और अपने नाम का जादुई स्पंदन...",
        "curiosity_hook_3": "🌟 अध्याय ३ की झलक: पृष्ठ ४ पर जानें अपने मूलांक की अलौकिक शक्तियां, जन्मजात योग्यताएं और किन गलतियों से आपको बचना है...",
        "curiosity_hook_4": "🎯 अध्याय ४ की झलक: पृष्ठ ५ पर जानें अपना भाग्यांक और इस जन्म में ब्रह्मांड ने आपके लिए क्या बड़ा लक्ष्य निर्धारित किया है...",
        "curiosity_hook_5": "⏳ अध्याय ५ की झलक: पृष्ठ ६ पर प्रवेश करें महा-समय चक्र में: जानें अपनी सक्रिय ९-वर्षीय महादशा और धन वृद्धि के नियम...",
        "curiosity_hook_6": "📅 अध्याय ६ की झलक: पृष्ठ ७ पर देखें अपना वार्षिक फलादेश और वर्तमान ३० दिनों का सटीक कार्य मार्गदर्शन...",
        "curiosity_hook_7": "🗓️ अध्याय ७ की झलक: पृष्ठ ८ पर पाएं अपना संपूर्ण १२ महीनों का कैलेंडर जिसमें शुभ और सतर्कता की अवधियां चिन्हित हैं...",
        "curiosity_hook_8": "⚡ अध्याय ८ की झलक: पृष्ठ ९ पर जानें आपकी कुंडली में कौन से दुर्लभ राजयोग या कर्म दोष सक्रिय हैं...",
        "curiosity_hook_9": "🔮 अध्याय ९ की झलक: पृष्ठ १० पर पाएं अपनी ८ प्रमुख जीवन भविष्यवाणियां, सिद्ध वैदिक उपाय और ज्योतिषाचार्य जिगर ठक्कर की मुहर...",
        "empowerment_blessing": "✨ आपकी सफलता एवं उत्थान का मार्ग: इन पवित्र वैदिक उपायों को पूरी निष्ठा से अपनाएं। व्यक्तिगत 1-on-1 परामर्श अथवा वास्तु निरीक्षण हेतु सीधे ज्योतिषाचार्य जिगर ठक्कर से संपर्क करें (+91 9377614772)।"
    },
    "gu": {
        "title": "વૈદિક અંકશાસ્ત્ર સ્ટુડિયો",
        "consultant_title": "જીગર ઠક્કર • પ્રમાણિત અંકશાસ્ત્રી",
        "report_title": "વૈયક્તિક વૈદિક અંકશાસ્ત્ર માર્ગદર્શન અહેવાલ",
        "sub_title": "તૈયાર કરનાર: જીગર ઠક્કર (સર્ટિફાઇડ ન્યુમેરોલોજિસ્ટ) • સંપર્ક: +91 9377614772",
        "client_profile": "જાતકની વિગત અને ગ્રહીય સ્થિતિ",
        "full_name": "જાતકનું નામ",
        "dob": "જન્મ તારીખ",
        "gender": "જાતિ",
        "weekday": "જન્મ વાર",
        "basic_number": "મૂળાંક (મૂળ અંક)",
        "destiny_number": "ભાગ્યાંક (ભાગ્ય અંક)",
        "name_number": "નામાંક (નામ અંક)",
        "name_harmony": "નામ સ્પંદન સંતુલન",
        "ruling_planet": "સ્વામી ગ્રહ",
        "favourable_numbers": "શુભ અંકો",
        "favourable_days": "શુભ વાર",
        "favourable_colors": "શુભ રંગો",
        "friendly_numbers": "મિત્ર અંકો (સહયોગી)",
        "neutral_numbers": "સમ અંકો (તટસ્થ)",
        "enemy_numbers": "શત્રુ / વર્જિત અંકો",
        "auspicious_direction": "શુભ વાસ્તુ દિશા",
        "auspicious_metal": "શુભ ધાતુ",
        "gemstone": "અનુકૂળ રત્ન",
        "vedic_grid_title": "વૈદિક જન્મ ચક્ર (3x3 ગ્રિડ)",
        "grid_explanation": "વૈદિક 3x3 જન્મ કુંડળી જાતકના જીવનમાં ગ્રહોના પ્રભાવ અને સંતુલનનું દર્શન કરાવે છે.",
        "natal_grid_title": "મૂળ જન્મ ચક્ર (આજીવન જન્મકાલીન ગ્રિડ)",
        "natal_grid_sub": "કાયમી જન્મકાલીન ગ્રહીય ઉર્જા અને જીવનનો મૂળ આધાર",
        "dasha_grid_title": "દશા અને ગોચર સક્રિય ચક્ર (હાલના ગ્રહીય સ્પંદનો)",
        "dasha_grid_sub": "ગતિશીલ સક્રિયતા: મૂળ જન્મ (સુવર્ણ) + મહાદશા (આકાશી) + અંતર્દશા (લીલો) + પ્રત્યંતર દશા (નારંગી)",
        "legend_natal": "જન્મકાલીન મૂળ (સુવર્ણ)",
        "legend_md": "મહાદશા • દીર્ઘકાલીન (આકાશી વાદળી)",
        "legend_ad": "અંતર્દશા • વાર્ષિક (પન્ના લીલો)",
        "legend_pd": "પ્રત્યંતર દશા • માસિક ઉપ-ચક્ર (રોયલ પર્પલ / Royal Purple)",
        "tier_mahadasha_title": "મહાદશા: દીર્ઘકાલીન મુખ્ય જીવન ચક્ર ફલાદેશ",
        "tier_antardasha_title": "અંતર્દશા: વાર્ષિક ૧-વર્ષીય વિસ્તૃત ફલાદેશ",
        "tier_pratyantar_title": "પ્રત્યંતર દશા: સક્રિય માસિક સૂક્ષ્મ ફલાદેશ",
        "pd_roadmap_title": "વાર્ષિક ૯-તબક્કાવાર પ્રત્યંતર દશા સમયરેખા અને કેલેન્ડર",
        "monthly_dos": "આ સક્રિય મહિનામાં કરવા યોગ્ય કાર્યો",
        "monthly_donts": "આ સક્રિય મહિનામાં રાખવાની સાવચેતીઓ",
        "active_vibrations": "ગ્રહીય સ્પંદન વિશ્લેષણ (+ / -)",
        "vibrations_tab_period": "★ સક્રિય દશા ચક્ર (વર્તમાન સામાયિક સ્પંદન)",
        "vibrations_tab_natal": "👑 સ્થાયી જન્મ કુંડળી (આજીવન મૂળ આધાર સ્પંદન)",
        "vibrations_disclaimer": "વૈદિક જ્યોતિષ સિદ્ધાંત: સ્થાયી જન્મજાત લક્ષણોથી વિપરીત, મહાદશા, અંતર્દશા અને પ્રત્યંતર દશાના પ્રભાવ હેઠળ ગ્રહીય સ્પંદનો સમય અનુસાર બદલાય છે. જન્મ કુંડળીમાં પડકારરૂપ (-) અંક દશામાં બેવડો બનીને શુભ (+) થઈ શકે છે (જેમ કે અંક 8 નું 88 બનવું), અને શુભ અંક બેવડી ઉર્જાથી પડકારરૂપ (-) બની શકે છે (જેમ કે અંક 9 નું 99 બનવું).",
        "shift_neg_to_pos": "★ સક્રિય દશામાં શુભ (+) માં પરિવર્તિત",
        "shift_pos_to_neg": "⚠ સક્રિય દશામાં પડકારરૂપ (-) માં પરિવર્તિત",
        "shift_newly_activated": "✦ વર્તમાન દશા દ્વારા તાત્કાલિક સક્રિયતા",
        "shift_stable": "સ્થિર ગ્રહીય સ્પંદન",
        "positive": "સકારાત્મક (+)",
        "negative": "પડકારરૂપ / નકારાત્મક (-)",
        "neutral": "તટસ્થ",
        "moolank_qualities": "મૂળાંકના મૂળભૂત ગુણધર્મો અને સ્વભાવ",
        "bhagyank_qualities": "ભાગ્યાંકના જીવન પથ અને ભાગ્ય પ્રભાવ",
        "moolank_precautions": "મૂળાંક માટે અગત્યની સાવચેતીઓ",
        "bhagyank_precautions": "ભાગ્યાંક માટે અગત્યની સાવચેતીઓ",
        "dasha_timeline": "ગ્રહીય દશા ચક્ર (સમયરેખા)",
        "mahadasha": "મહાદશા (મુખ્ય સમયગાળો)",
        "antardasha": "અંતર્દશા (પેટા-સમયગાળો)",
        "pratyantar_dasha": "પ્રત્યંતર દશા (હાલનો સક્રિય તબક્કો)",
        "active_yogas": "જન્મ કુંડળીમાં સક્રિય મુખ્ય યોગો",
        "auspicious_yogas_title": "શુભ ગ્રહીય યોગ (દૈવી ઉર્જા ચક્ર)",
        "inauspicious_yogas_title": "અશુભ યોગ અને દોષ (કર્મ અવરોધો અને નિવારણ ઉપાયો)",
        "mitigation_remedy": "દોષ નિવારણ અને શાંતિ ઉપાય:",
        "predictions_title": "વિગતવાર જીવન ભવિષ્યવાણી",
        "pred_finance": "નાણાકીય સંપત્તિ અને આવકની આગાહી",
        "pred_property": "જમીન, મકાન અને સ્થાવર મિલકત યોગ",
        "pred_vehicle": "વાહન ખરીદી અને સુખ ભવિષ્યવાણી",
        "pred_education": "શિક્ષણ અને બૌદ્ધિક ક્ષમતા",
        "pred_travel": "પ્રવાસ અને વિદેશ ગમન યોગ",
        "pred_litigation": "વિવાદ, કોર્ટ કચેરી અને મુકદ્દમા ભવિષ્યવાણી",
        "pred_relationship": "લગ્ન જીવન, સંબંધો અને સુમેળ",
        "pred_health": "સ્વાસ્થ્ય, રોગ અને સુરક્ષા માર્ગદર્શન",
        "remedies_title": "વૈદિક નિવારક ઉપાયો અને માર્ગદર્શન",
        "gemstone_remedy": "રત્ન અને ક્રિસ્ટલ પરામર્શ",
        "mantra_remedy": "પવિત્ર વૈદિક મંત્ર સાધના",
        "fasting_remedy": "વ્રત અને ઉપવાસ નિયમો",
        "donation_remedy": "દાન અને પુણ્ય કર્મ",
        "seva_remedy": "સેવા અને કર્મ સુધારણા",
        "lifestyle_remedy": "રંગ અને જીવનશૈલી સંતુલન",
        "general_remedies": "સામાન્ય વૈદિક ઉપાયો (ધન, આરોગ્ય અને શાંતિ)",
        "certified_box_title": "પ્રમાણિત વૈદિક અંકશાસ્ત્ર પ્રમાણીકરણ અને આશીર્વાદ",
        "certified_box_text": "આ અહેવાલ સર્ટિફાઇડ ન્યુમેરોલોજિસ્ટ જીગર ઠક્કર દ્વારા પ્રમાણિત વૈદિક અંકશાસ્ત્ર ગણતરીઓ અને પ્રાચીન ગ્રહીય નિયમોના આધારે તૈયાર કરવામાં આવ્યો છે. નવગ્રહો આપના જીવનમાં સુખ, સમૃદ્ધિ, ઉત્તમ આરોગ્ય અને શાંતિ લાવે એવી મંગલ કામના.",
        "signature_line": "જીગર ઠક્કર (સર્ટિફાઇડ ન્યુમેરોલોજિસ્ટ)",
        "page": "પાનું",
        "of": "નું",
        "consultant_notes": "જીગર ઠક્કરની વિશેષ અંગત નોંધ અને ઉપાયો",
        "phone_label": "ફોન / વ્હોટ્સએપ",
        "email_label": "ઇમેઇલ",
                "toc_title": "૧૦-પ્રકરણ સંપૂર્ણ જીવન વિષય-સૂચિ",
        "p1_title": "વૈયક્તિક વૈદિક અંકશાસ્ત્ર મહા-માર્ગદર્શન અને જીવન દર્પણ",
        "p1_sub": "પ્રમાણિત ગાણિતિક ફલાદેશ અને દૈવી સમય ચક્ર",
        "chap_1_badge": "પ્રકરણ ૧ / ૯ • પવિત્ર વૈદિક કુંડળી",
        "chap_1_title": "યુગલ વૈદિક ચક્ર: આજીવન જન્મ કુંડળી અને સક્રિય દશા ગોચર સ્પંદન",
        "chap_2_badge": "પ્રકરણ ૨ / ૯ • શુભ દિશા-સૂચક",
        "chap_2_title": "ગ્રહીય મિત્ર અંકો, શુભ વાસ્તુ દિશાઓ અને નામાંક સ્પંદન સંતુલન",
        "chap_3_badge": "પ્રકરણ ૩ / ૯ • આત્મિક ચેતના",
        "chap_3_title": "મૂળ વ્યક્તિત્વ, જન્મજાત અલૌકિક શક્તિઓ અને સાવચેતીઓ (મૂળાંક)",
        "chap_4_badge": "પ્રકરણ ૪ / ૯ • ભાગ્ય પ્રારબ્ધ",
        "chap_4_title": "કર્મિક લક્ષ્ય, ઉચ્ચ જીવન ઉદ્દેશ્ય અને ભાગ્યોદયની ચાવી (ભાગ્યાંક)",
        "chap_5_badge": "પ્રકરણ ૫ / ૯ • મહા-સમય ચક્ર",
        "chap_5_title": "મહાદશા: ૯-વર્ષીય દીર્ઘકાલીન મહા-ચક્ર અને ધન સંચય ફલાદેશ",
        "chap_6_badge": "પ્રકરણ ૬ / ૯ • વાર્ષિક અને માસિક સમય ચક્ર",
        "chap_6_title": "અંતર્દશા (વાર્ષિક ૧-વર્ષીય ફલાદેશ) અને સક્રિય માસિક સમયગાળો",
        "chap_7_badge": "પ્રકરણ ૭ / ૯ • વાર્ષિક સમયરેખા",
        "chap_7_title": "વાર્ષિક ૯-તબક્કાવાર પ્રત્યંતર દશા કેલેન્ડર અને સુવર્ણ તકો",
        "chap_8_badge": "પ્રકરણ ૮ / ૯ • રાજયોગ અને ગ્રહ દોષો",
        "chap_8_title": "દુર્લભ ગ્રહ યોગો, કર્મિક દોષ નિવારણ અને ગ્રહીય સ્પંદન",
        "chap_9_badge": "પ્રકરણ ૯ / ૯ • ૮-સ્તંભ ફલાદેશ અને સિદ્ધ ઉપાયો",
        "chap_9_title": "૮-સ્તંભ જીવન આગાહીઓ, પ્રમાણિત વૈદિક ઉપચાર અને પ્રમાણપત્ર મુદ્રા",
        "curiosity_hook_1": "🔮 પ્રકરણ ૧ ની ઝલક: પેજ ૨ પર જુઓ તમારી ૩x૩ વૈદિક જન્મ કુંડળી અને જાણો કે હાલની ગ્રહ દશાઓ તમારી શક્તિઓને કેવી રીતે જાગૃત કરે છે...",
        "curiosity_hook_2": "🧭 પ્રકરણ ૨ ની ઝલક: પેજ ૩ પર જાણો તમારા સાચા મિત્ર અંકો, શુભ વાસ્તુ દિશા, અનુકૂળ રત્ન અને તમારા નામના સ્પંદનનું રહસ્ય...",
        "curiosity_hook_3": "🌟 પ્રકરણ ૩ ની ઝલક: પેજ ૪ પર જાણો તમારા મૂળાંકની છુપાયેલી શક્તિઓ અને કઈ આદતોથી તમારે સાવધાન રહેવું...",
        "curiosity_hook_4": "🎯 પ્રકરણ ૪ ની ઝલક: પેજ ૫ પર જાણો તમારો ભાગ્યાંક અને આ જન્મમાં કુદરતે તમારા માટે કયું મોટું લક્ષ્ય રાખ્યું છે...",
        "curiosity_hook_5": "⏳ પ્રકરણ ૫ ની ઝલક: પેજ ૬ પર જુઓ મહા-સમય ચક્ર: તમારી ૯-વર્ષીય મહાદશા અને નાણાકીય પ્રગતિના નિયમો...",
        "curiosity_hook_6": "📅 પ્રકરણ ૬ ની ઝલક: પેજ ૭ પર જુઓ વાર્ષિક ફલાદેશ અને હાલના ૩૦ દિવસનું ચોક્કસ કાર્ય માર્ગદર્શન...",
        "curiosity_hook_7": "🗓️ પ્રકરણ ૭ ની ઝલક: પેજ ૮ પર મેળવો સંપૂર્ણ ૧૨ મહિનાનું કેલેન્ડર જેમાં શુભ સમય અને સાવચેતીના દિવસો દર્શાવેલ છે...",
        "curiosity_hook_8": "⚡ પ્રકરણ ૮ ની ઝલક: પેજ ૯ પર જાણો તમારી કુંડળીમાં કયા દૈવી રાજયોગો કે કર્મ દોષો છુપાયેલા છે...",
        "curiosity_hook_9": "🔮 પ્રકરણ ૯ ની ઝલક: પેજ ૧૦ પર મેળવો તમારી ૮ મુખ્ય જીવન આગાહીઓ, સિદ્ધ વૈદિક ઉપાયો અને સર્ટિફિકેશન મુદ્રા...",
        "empowerment_blessing": "✨ તમારી સફળતા અને ભાગ્યોદયનો પવિત્ર માર્ગ: આપેલા વૈદિક ઉપાયો પૂર્ણ શ્રદ્ધાથી અપનાવો. વિશેષ 1-on-1 અંગત માર્ગદર્શન અથવા વાસ્તુ નિરીક્ષણ માટે જીગર ઠક્કરનો સીધો સંપર્ક કરો (+91 9377614772)."
    }
}

PLANET_INFO = {
    1: {
        "en": {"planet": "Sun (Surya)", "element": "Fire", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5", "enemy_nums": "8, 6, 4", "direction": "East", "metal": "Copper & Gold", "days": "Sunday", "colors": "Orange, Red, Gold, Yellow", "gem": "Ruby (Manikya)"},
        "hi": {"planet": "सूर्य (Surya)", "element": "अग्नि", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5", "enemy_nums": "8, 6, 4", "direction": "पूर्व दिशा (East)", "metal": "तांबा एवं सोना", "days": "रविवार", "colors": "नारंगी, लाल, सुनहरा, पीला", "gem": "माणिक्य (Ruby)"},
        "gu": {"planet": "સૂર્ય (Surya)", "element": "અગ્નિ", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5", "enemy_nums": "8, 6, 4", "direction": "પૂર્વ દિશા (East)", "metal": "તાંબુ અને સોનું", "days": "રવિવાર", "colors": "કેસરી, લાલ, સોનેરી, પીળો", "gem": "માણેક (Ruby)"}
    },
    2: {
        "en": {"planet": "Moon (Chandra)", "element": "Water", "favourable_nums": "1, 2, 5", "friendly_nums": "1, 2, 5", "neutral_nums": "3, 7", "enemy_nums": "8, 9, 4, 6", "direction": "North-West", "metal": "Pure Silver", "days": "Monday", "colors": "White, Cream, Silver, Light Green", "gem": "Pearl (Moti)"},
        "hi": {"planet": "चंद्र (Chandra)", "element": "जल", "favourable_nums": "1, 2, 5", "friendly_nums": "1, 2, 5", "neutral_nums": "3, 7", "enemy_nums": "8, 9, 4, 6", "direction": "वायव्य दिशा (North-West)", "metal": "शुद्ध चांदी", "days": "सोमवार", "colors": "सफेद, क्रीम, चांदी, हल्का हरा", "gem": "मोती (Pearl)"},
        "gu": {"planet": "ચંદ્ર (Chandra)", "element": "જળ", "favourable_nums": "1, 2, 5", "friendly_nums": "1, 2, 5", "neutral_nums": "3, 7", "enemy_nums": "8, 9, 4, 6", "direction": "વાયવ્ય દિશા (North-West)", "metal": "શુદ્ધ ચાંદી", "days": "સોમવાર", "colors": "સફેદ, ક્રીમ, સિલ્વર, આછો લીલો", "gem": "મોતી (Pearl)"}
    },
    3: {
        "en": {"planet": "Jupiter (Guru)", "element": "Ether / Space", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5, 7", "enemy_nums": "6", "direction": "North-East (Ishanya)", "metal": "Gold & Brass", "days": "Thursday", "colors": "Yellow, Golden, Saffron", "gem": "Yellow Sapphire (Pukhraj)"},
        "hi": {"planet": "बृहस्पति (Guru)", "element": "आकाश", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5, 7", "enemy_nums": "6", "direction": "ईशान कोण (North-East)", "metal": "सोना एवं पीतल", "days": "गुरुवार", "colors": "पीला, सुनहरा, केसरिया", "gem": "पुखराज (Yellow Sapphire)"},
        "gu": {"planet": "ગુરુ (Guru)", "element": "આકાશ", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5, 7", "enemy_nums": "6", "direction": "ઈશાન ખૂણો (North-East)", "metal": "સોનું અને પિત્તળ", "days": "ગુરુવાર", "colors": "પીળો, સોનેરી, કેસરી", "gem": "પોખરાજ (Yellow Sapphire)"}
    },
    4: {
        "en": {"planet": "Rahu (Dragon's Head)", "element": "Air", "favourable_nums": "4, 5, 6, 8", "friendly_nums": "4, 5, 6, 8", "neutral_nums": "7, 3", "enemy_nums": "1, 2, 9", "direction": "South-West (Nairritya)", "metal": "Silver & Panchdhatu", "days": "Saturday / Wednesday", "colors": "Electric Blue, Grey, Khaki", "gem": "Hessonite (Gomed)"},
        "hi": {"planet": "राहु (Rahu)", "element": "वायु", "favourable_nums": "4, 5, 6, 8", "friendly_nums": "4, 5, 6, 8", "neutral_nums": "7, 3", "enemy_nums": "1, 2, 9", "direction": "नैऋत्य कोण (South-West)", "metal": "चांदी एवं पंचधातु", "days": "शनिवार / बुधवार", "colors": "इलेक्ट्रिक ब्लू, ग्रे, खाकी", "gem": "गोमेद (Hessonite)"},
        "gu": {"planet": "રાહુ (Rahu)", "element": "વાયુ", "favourable_nums": "4, 5, 6, 8", "friendly_nums": "4, 5, 6, 8", "neutral_nums": "7, 3", "enemy_nums": "1, 2, 9", "direction": "નૈઋત્ય ખૂણો (South-West)", "metal": "ચાંદી અને પંચધાતુ", "days": "શનિવાર / બુધવાર", "colors": "ઇલેક્ટ્રિક બ્લુ, ગ્રે, ખાખી", "gem": "ગોમેદ (Hessonite)"}
    },
    5: {
        "en": {"planet": "Mercury (Budh)", "element": "Earth", "favourable_nums": "1, 5, 6", "friendly_nums": "1, 5, 6", "neutral_nums": "3, 4, 7, 8, 9", "enemy_nums": "2", "direction": "North", "metal": "Gold & Bronze", "days": "Wednesday", "colors": "Green, Emerald Green, White", "gem": "Emerald (Panna)"},
        "hi": {"planet": "बुध (Budh)", "element": "पृथ्वी", "favourable_nums": "1, 5, 6", "friendly_nums": "1, 5, 6", "neutral_nums": "3, 4, 7, 8, 9", "enemy_nums": "2", "direction": "उत्तर दिशा (North)", "metal": "सोना एवं कांस्य", "days": "बुधवार", "colors": "हरा, पन्ना हरा, सफेद", "gem": "पन्ना (Emerald)"},
        "gu": {"planet": "બુધ (Budh)", "element": "પૃથ્વી", "favourable_nums": "1, 5, 6", "friendly_nums": "1, 5, 6", "neutral_nums": "3, 4, 7, 8, 9", "enemy_nums": "2", "direction": "ઉત્તર દિશા (North)", "metal": "સોનું અને કાંસું", "days": "બુધવાર", "colors": "લીલો, પન્ના લીલો, સફેદ", "gem": "પન્ના (Emerald)"}
    },
    6: {
        "en": {"planet": "Venus (Shukra)", "element": "Water", "favourable_nums": "5, 6, 8", "friendly_nums": "5, 6, 8", "neutral_nums": "1, 4, 7, 9", "enemy_nums": "3", "direction": "South-East (Agneya)", "metal": "Silver & White Gold", "days": "Friday", "colors": "White, Pink, Silver, Pastel Shades", "gem": "Diamond / White Zircon / Opal"},
        "hi": {"planet": "शुक्र (Shukra)", "element": "जल", "favourable_nums": "5, 6, 8", "friendly_nums": "5, 6, 8", "neutral_nums": "1, 4, 7, 9", "enemy_nums": "3", "direction": "आग्नेय कोण (South-East)", "metal": "चांदी एवं सफेद सोना", "days": "शुक्रवार", "colors": "सफेद, गुलाबी, सिल्वर, पेस्टल शेड्स", "gem": "हीरा / सफेद जरकन / ओपल"},
        "gu": {"planet": "શુક્ર (Shukra)", "element": "જળ", "favourable_nums": "5, 6, 8", "friendly_nums": "5, 6, 8", "neutral_nums": "1, 4, 7, 9", "enemy_nums": "3", "direction": "આગ્નેય ખૂણો (South-East)", "metal": "ચાંદી અને સફેદ સોનું", "days": "શુક્રવાર", "colors": "સફેદ, ગુલાબી, સિલ્વર, પેસ્ટલ શેડ્સ", "gem": "હીરો / સફેદ ઝરકન / ઓપલ"}
    },
    7: {
        "en": {"planet": "Ketu (Dragon's Tail)", "element": "Water / Fire", "favourable_nums": "1, 3, 7", "friendly_nums": "1, 3, 7", "neutral_nums": "4, 5, 6, 8, 9", "enemy_nums": "2", "direction": "North-East / Centre", "metal": "Pure Silver", "days": "Tuesday / Thursday", "colors": "Light Green, White, Grey, Multi-color", "gem": "Cat's Eye (Lehsuniya)"},
        "hi": {"planet": "केतु (Ketu)", "element": "जल / अग्नि", "favourable_nums": "1, 3, 7", "friendly_nums": "1, 3, 7", "neutral_nums": "4, 5, 6, 8, 9", "enemy_nums": "2", "direction": "ईशान कोण अथवा ब्रह्मस्थान", "metal": "शुद्ध चांदी", "days": "मंगलवार / गुरुवार", "colors": "हल्का हरा, सफेद, ग्रे, बहुरंगी", "gem": "लहसुनिया (Cat's Eye)"},
        "gu": {"planet": "કેતુ (Ketu)", "element": "જળ / અગ્નિ", "favourable_nums": "1, 3, 7", "friendly_nums": "1, 3, 7", "neutral_nums": "4, 5, 6, 8, 9", "enemy_nums": "2", "direction": "ઈશાન ખૂણો અથવા બ્રહ્મસ્થાન", "metal": "શુદ્ધ ચાંદી", "days": "મંગળવાર / ગુરુવાર", "colors": "આછો લીલો, સફેદ, ગ્રે, બહુરંગી", "gem": "લહસુનિયા (Cat's Eye)"}
    },
    8: {
        "en": {"planet": "Saturn (Shani)", "element": "Earth / Air", "favourable_nums": "4, 5, 6, 8", "friendly_nums": "4, 5, 6, 8", "neutral_nums": "3, 7", "enemy_nums": "1, 2, 9", "direction": "West", "metal": "Silver & Iron / Lead", "days": "Saturday", "colors": "Navy Blue, Dark Blue, Black, Grey", "gem": "Blue Sapphire (Neelam) / Amethyst"},
        "hi": {"planet": "शनि (Shani)", "element": "पृथ्वी / वायु", "favourable_nums": "4, 5, 6, 8", "friendly_nums": "4, 5, 6, 8", "neutral_nums": "3, 7", "enemy_nums": "1, 2, 9", "direction": "पश्चिम दिशा (West)", "metal": "चांदी एवं लोहा", "days": "शनिवार", "colors": "गहरा नीला, नेवी ब्लू, काला, ग्रे", "gem": "नीलम (Blue Sapphire) / जमुनिया"},
        "gu": {"planet": "શનિ (Shani)", "element": "પૃથ્વી / વાયુ", "favourable_nums": "4, 5, 6, 8", "friendly_nums": "4, 5, 6, 8", "neutral_nums": "3, 7", "enemy_nums": "1, 2, 9", "direction": "પશ્ચિમ દિશા (West)", "metal": "ચાંદી અને લોખંડ", "days": "શનિવાર", "colors": "ઘેરો વાદળી, નેવી બ્લુ, કાળો, ગ્રે", "gem": "નીલમ (Blue Sapphire) / જમુનિયા"}
    },
    9: {
        "en": {"planet": "Mars (Mangal)", "element": "Fire", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5, 7", "enemy_nums": "4, 8, 6", "direction": "South", "metal": "Copper & Gold", "days": "Tuesday", "colors": "Red, Crimson, Coral, Orange", "gem": "Red Coral (Moonga)"},
        "hi": {"planet": "मंगल (Mangal)", "element": "अग्नि", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5, 7", "enemy_nums": "4, 8, 6", "direction": "दक्षिण दिशा (South)", "metal": "तांबा एवं सोना", "days": "मंगलवार", "colors": "लाल, सिंदूरी, मूंगा लाल, नारंगी", "gem": "मूंगा (Red Coral)"},
        "gu": {"planet": "મંગળ (Mangal)", "element": "અગ્નિ", "favourable_nums": "1, 2, 3, 9", "friendly_nums": "1, 2, 3, 9", "neutral_nums": "5, 7", "enemy_nums": "4, 8, 6", "direction": "દક્ષિણ દિશા (South)", "metal": "તાંબુ અને સોનું", "days": "મંગળવાર", "colors": "લાલ, સિંદૂરી, પરવાળું, કેસરી", "gem": "પરવાળું (Red Coral)"}
    }
}

# Number Qualities & Characteristics for Root Numbers (1-9)
NUMBER_QUALITIES = {
    1: {
        "en": [
            "Natural born leader with immense vitality, self-confidence, and authoritative presence.",
            "Pioneering vision; prefers taking full initiative rather than following orders of others.",
            "Inventive, ambitious, and driven by high principles of dignity, self-respect, and honor.",
            "Dynamic organizational ability; thrives in executive positions, governance, and entrepreneurship."
        ],
        "hi": [
            "जन्मजात नेतृत्व क्षमता, प्रचंड आत्मबल, दृढ़ आत्मविश्वास और प्रभावशाली व्यक्तित्व।",
            "दूरदर्शी सोच; दूसरों के आदेशों पर चलने के बजाय स्वयं नई पहल और मार्ग प्रशस्त करने वाले।",
            "अत्यंत महत्वाकांक्षी, स्वाभिमानी, मर्यादावान और उच्च जीवन मूल्यों के प्रति समर्पित।",
            "उत्कृष्ट प्रशासनिक एवं संगठनात्मक कौशल; उच्च पदों, व्यापार व शासन में शीर्ष सफलता।"
        ],
        "gu": [
            "જન્મજાત નેતૃત્વ ક્ષમતા, પ્રચંડ આત્મવિશ્વાસ, તેજસ્વી વ્યક્તિત્વ અને દૃઢ સંકલ્પશક્તિ.",
            "નવીન દ્રષ્ટિકોણ; અન્યના માર્ગદર્શન હેઠળ રહેવા કરતાં પોતાના દમ પર નવો માર્ગ કંડારવાનું વલણ.",
            "અત્યંત મહત્વાકાંક્ષી, ખુમારીવાળા, સ્વમાની અને ઉચ્ચ જીવનમૂલ્યોને વરેલા.",
            "ઉત્તમ વહીવટી અને સંગઠનાત્મક આવડત; શાસન, ઉચ્ચ હોદ્દાઓ અને વેપારમાં સર્વોચ્ચ સ્થાન."
        ]
    },
    2: {
        "en": [
            "Gentle, intuitive, imaginative, and deeply diplomatic with exceptional emotional intelligence.",
            "Peace-loving mediator who harmonizes disputes and builds trusting relationships.",
            "Artistic, poetic sensibility with an appreciation for elegance, music, and aesthetics.",
            "Cooperative team player; works best in supportive, advisory, or partnership environments."
        ],
        "hi": [
            "सौम्य, संवेदनशील, तीव्र अंतर्ज्ञान युक्त और असाधारण भावनात्मक समझ से परिपूर्ण।",
            "शांतिप्रिय मध्यस्थ जो विवादों को सुलझाने और मधुर संबंध स्थापित करने में कुशल हैं।",
            "कलात्मक, कल्पनाशील और काव्यमयी दृष्टि; सौंदर्य, संगीत और सुरुचिपूर्ण वस्तुओं के प्रेमी।",
            "सहयोगात्मक कार्यशैली; साझेदारी, परामर्श और सहभागिता के कार्यों में श्रेष्ठ प्रदर्शन।"
        ],
        "gu": [
            "સૌમ્ય, સંવેદનશીલ, તીવ્ર આંતરિક સૂઝ (ઇન્ટ્યુશન) અને ઉચ્ચ ભાવનાત્મક સમજ ધરાવતા.",
            "શાંતિપ્રિય મધ્યસ્થી જે વિવાદો શાંત પાડીને સૌહાર્દપૂર્ણ સંબંધો બાંધવામાં કુશળ હોય છે.",
            "કલાત્મક અને કલ્પનાશીલ દ્રષ્ટિકોણ; સંગીત, કલા, સાહિત્ય અને સૌંદર્ય પ્રત્યે ઊંડો પ્રેમ.",
            "સહકારી કાર્યશૈલી; ભાગીદારી, માર્ગદર્શન અને સલાહકાર તરીકે શ્રેષ્ઠ કામગીરી."
        ]
    },
    3: {
        "en": [
            "Wise, intellectual, optimistic, and natural teachers endowed with profound knowledge.",
            "Philosophical depth, righteous moral compass, and respected advice across society.",
            "Inspiring verbal communication; excellent public speakers, mentors, and educators.",
            "Magnanimous, generous heart with an innate quest for truth, law, and spiritual wisdom."
        ],
        "hi": [
            "ज्ञानवान, प्रखर बुद्धिजीवी, आशावादी और स्वभाव से श्रेष्ठ मार्गदर्शक व शिक्षक।",
            "दार्शनिक गहराई, धर्मनिष्ठ आचरण और समाज में सम्मानजनक सलाह देने वाले मार्गदर्शक।",
            "प्रेरणादायक वाक्पटुता; प्रभावशाली वक्ता, उच्च कोटि के शिक्षक और परामर्शदाता।",
            "उदार हृदय, सत्य, न्याय और आध्यात्मिक ज्ञान की निरंतर खोज करने वाले पुण्यात्मा।"
        ],
        "gu": [
            "જ્ઞાની, બુદ્ધિશાળી, આશાવાદી અને જન્મજાત ઉત્તમ શિક્ષક કે માર્ગદર્શક.",
            "દાર્શનિક ઊંડાણ, ધર્મનિષ્ઠ નીતિમત્તા અને સમાજમાં આદરણીય સલાહ આપનાર વ્યક્તિ.",
            "પ્રેરણાદાયી વાક્ચાતુર્ય; ઉત્કૃષ્ટ વક્તા, કાઉન્સિલર અને પ્રબુદ્ધ કેળવણીકાર.",
            "ઉદાર હૃદય, સત્ય, કાયદા અને આધ્યાત્મિક જ્ઞાનની ખોજ કરનાર તેજસ્વી સ્વભાવ."
        ]
    },
    4: {
        "en": [
            "Highly practical, methodical, disciplined, and revolutionary thinker with sharp technical acumen.",
            "Unconventional problem solver; questions dogmas and constructs solid structural foundations.",
            "Remarkable endurance and perseverance; capable of executing complex, detailed operations.",
            "Deeply analytical mind, championing modernization, research, and systematized workflows."
        ],
        "hi": [
            "अत्यंत व्यावहारिक, योजनाबद्ध, अनुशासित और क्रांतिकारी सोच वाले तकनीकी विशेषज्ञ।",
            "रूढ़ियों से हटकर नवीन समाधान खोजने वाले; ठोस धरातल पर मजबूत संरचना का निर्माण करने वाले।",
            "अभूतपूर्व धैर्य, सहनशीलता और जटिल से जटिल कार्यों को सफलता से पूरा करने का सामर्थ्य।",
            "गहन विश्लेषणात्मक बुद्धि; आधुनिकीकरण, अनुसंधान एवं सुव्यवस्थित प्रणालियों के निर्माता।"
        ],
        "gu": [
            "અત્યંત વ્યવહારુ, પદ્ધતિસરના, શિસ્તબદ્ધ અને ક્રાંતિકારી વિચારો ધરાવતા ટેકનિકલ દિમાગ.",
            "પરંપરાગત રીતોથી અલગ હટીને મજબૂત વ્યવસ્થા ઊભી કરનાર અનન્ય વિચારક.",
            "અસાધારણ પરિશ્રમ અને સહનશક્તિ; જટિલ અને બારીક કાર્યોને પણ આસાનીથી પાર પાડવાની ક્ષમતા.",
            "ઊંડી વિશ્લેષણાત્મક બુદ્ધિ; આધુનિકતા, સંશોધન અને વ્યવસ્થિત પ્રણાલીઓના ઘડવૈયા."
        ]
    },
    5: {
        "en": [
            "Quick-witted, versatile, adaptable, and master of communication and commercial enterprise.",
            "Dynamic, enthusiastic risk-taker with a magnetic charisma and sharp business sense.",
            "Lifelong learner who thrives on networking, travel, commerce, and media communication.",
            "Maintains equilibrium and bridges connections between diverse groups and ideas."
        ],
        "hi": [
            "हाजिरजवाब, बहुमुखी प्रतिभा संपन्न, परिस्थितियों के अनुकूल ढलने वाले और व्यापार के कुशल ज्ञाता।",
            "ऊर्जावान, त्वरित निर्णय लेने वाले, चुंबकीय व्यक्तित्व और असाधारण व्यावसायिक समझ वाले।",
            "नेटवर्किंग, यात्रा, वाणिज्य और जनसंचार माध्यमों में सहज निपुणता रखने वाले।",
            "जीवन में संतुलन बनाए रखने और विभिन्न विचारों व व्यक्तियों को आपस में जोड़ने में पारंगत।"
        ],
        "gu": [
            "હાજરજવાબી, બહુમુખી પ્રતિભા ધરાવતા, ઝડપથી અનુકૂલન સાધનાર અને વેપાર-વાણિજ્યમાં નિષ્ણાત.",
            "ઉર્જાવાન, જોખમ લેવાની હિંમત ધરાવતા, આકર્ષક વ્યક્તિત્વ અને વેપારી સૂઝબૂઝવાળા.",
            "નેટવર્કિંગ, મુસાફરી, શેરબજાર, મીડિયા અને માર્કેટિંગમાં કુદરતી આવડત ધરાવતા.",
            "સંતુલન જાળવવામાં અગ્રેસર અને વિવિધ લોકો કે વિચારોને સરળતાથી જોડનાર કડીરૂપ."
        ]
    },
    6: {
        "en": [
            "Charming, magnetic, refined, loving luxury, beauty, artistic pursuits, and domestic harmony.",
            "Natural caregiver with deep affection for family, community, aesthetics, and fine living.",
            "Excellent taste in fashion, interior decor, gastronomy, cinema, and hospitality.",
            "Attracts abundance, goodwill, and comfort through gracious manners and warmth."
        ],
        "hi": [
            "आकर्षक, सम्मोहक, कलात्मक और भौतिक सुख-सुविधाओं, सौंदर्य व पारिवारिक सुख के प्रेमी।",
            "सहज स्नेहशील स्वभाव; परिवार, मित्रों, सौंदर्य और विलासितापूर्ण जीवनशैली के प्रति समर्पित।",
            "फैशन, गृह सज्जा, सुरुचिपूर्ण भोजन, संगीत और आतिथ्य सत्कार में उत्कृष्ट रुचि।",
            "सौम्य व्यवहार और आकर्षण से जीवन में प्रचुरता, ऐश्वर्य और सद्भावना को आकर्षित करने वाले।"
        ],
        "gu": [
            "આકર્ષક, સંમોહક, કલાપ્રેમી અને ભૌતિક સુખ-સગવડો, સુંદરતા તથા કૌટુંબિક સુખના ચાહક.",
            "સ્નેહાળ સ્વભાવ; પરિવાર, મિત્રો, સુંદર વાતાવરણ અને વૈભવી જીવન પ્રત્યે વિશેષ આકર્ષણ.",
            "ફેશન, ઇન્ટિરિયર ડેકોરેશન, ઉત્તમ ભોજન, સિનેમા અને હોસ્પિટાલિટીમાં શ્રેષ્ઠ રુચિ.",
            "નમ્ર વર્તન અને સંમોહનથી જીવનમાં સમૃદ્ધિ, લક્ષ્મી અને આદર પ્રાપ્ત કરનાર."
        ]
    },
    7: {
        "en": [
            "Deeply spiritual, intuitive, introspective, philosophical, and endowed with occult insight.",
            "Natural researcher and mystic who delves beneath surfaces to uncover hidden truths.",
            "Independent thinker; values solitude, scholarly study, meditation, and quiet reflection.",
            "Connected to foreign cultures, ancient wisdom, technical analysis, and metaphysical sciences."
        ],
        "hi": [
            "गहन आध्यात्मिक, अंतर्मुखी, दार्शनिक और गूढ़ रहस्यों व पराविज्ञान की सूक्ष्म समझ रखने वाले।",
            "जन्मजात शोधकर्ता और मर्मज्ञ; सतह से परे जाकर छिपे हुए गूढ़ सत्यों को उजागर करने वाले।",
            "स्वतंत्र विचारक; एकांत, गंभीर अध्ययन, ध्यान और आत्ममंथन को सर्वोच्च प्राथमिकता देने वाले।",
            "विदेशी संस्कृतियों, प्राचीन ग्रंथों, तकनीकी विश्लेषण और आध्यात्मिक विज्ञान से विशेष जुड़ाव।"
        ],
        "gu": [
            "ગહન આધ્યાત્મિક, અંતર્મુખી, દાર્શનિક અને ગૂઢ રહસ્યો તથા સંશોધનમાં અનોખી સૂઝ ધરાવતા.",
            "જન્મજાત સંશોધક; સપાટીથી ઊંડા ઊતરીને છૂપાયેલા ગૂઢ સત્યો બહાર લાવવાની કુદરતી આવડત.",
            "સ્વતંત્ર વિચારક; એકાંત, ઊંડો અભ્યાસ, ધ્યાન અને ચિંતન-મનનને મહત્વ આપનાર.",
            "વિદેશી સંસ્કૃતિ, પ્રાચીન વિજ્ઞાન, ટેકનિકલ રિસર્ચ અને આધ્યાત્મિકતા સાથે ગાઢ જોડાણ."
        ]
    },
    8: {
        "en": [
            "Master of discipline, tireless perseverance, justice, massive organizational execution, and material empires.",
            "Steadfast resilience; rises steadily through hard work, overcoming obstacles to reach the summit.",
            "Exceptional financial and asset-building acumen; excels in heavy industries, land, law, and corporate structures.",
            "Fair, uncompromising integrity; acts as a guardian of structure, order, and karmic justice."
        ],
        "hi": [
            "कठोर अनुशासन, अथक परिश्रम, न्यायप्रियता, विशाल संगठनात्मक क्षमता और अचल संपत्ति के निर्माता।",
            "अटूट धैर्य; चुनौतियों और संघर्षों को पार करते हुए निरंतर परिश्रम से शिखर पर पहुँचने वाले।",
            "गंभीर वित्तीय एवं संपत्ति निर्माण समझ; भारी उद्योग, भूमि, कानून और कॉरपोरेट तंत्र में शीर्षस्थ।",
            "निष्पक्ष और अडिग सत्यनिष्ठ; व्यवस्था, न्याय और कर्मफल के सजग प्रहरी।"
        ],
        "gu": [
            "ચુસ્ત શિસ્ત, અથાક પરિશ્રમ, ન્યાયપ્રિયતા, વિરાટ સંગઠન ક્ષમતા અને સ્થાવર મિલકતોના ઘડવૈયા.",
            "અડગ ધૈર્યવાન; સંઘર્ષો અને અડચણો સામે ઝૂક્યા વિના સતત મહેનતથી ટોચ પર પહોંચનાર.",
            "નાણાકીય અને જમીન-મકાન સર્જનની ઊંડી સૂઝ; ભારે ઉદ્યોગો, કાયદો અને મોટા કોર્પોરેટ ક્ષેત્રે અગ્રેસર.",
            "નિષ્પક્ષ અને સિદ્ધાંતવાદી; શિસ્ત, વ્યવસ્થા અને કર્મફળના મજબૂત રક્ષક."
        ]
    },
    9: {
        "en": [
            "Dynamic warrior spirit, boundless physical vitality, courageous, humanitarian, and protective.",
            "Fearless defender of the vulnerable; champions social justice and acts swiftly with conviction.",
            "High energy, enthusiasm, and competitive drive; excels in sports, defense, engineering, and surgery.",
            "Noble, generous, and passionately committed to serving humanity on a grand scale."
        ],
        "hi": [
            "ओजस्वी यौद्धा स्वभाव, असीम शारीरिक ऊर्जा, निडर, मानवीय संवेदनाओं से युक्त और रक्षक प्रवृत्ति।",
            "निर्भीक और साहसी; निर्बलों के अधिकारों के लिए तुरंत खड़े होने वाले और त्वरित निर्णय लेने वाले।",
            "उच्च ऊर्जा और प्रतिस्पर्धी भावना; खेल, सेना, पुलिस, इंजीनियरिंग और शल્ય चिकित्सा में अग्रणी।",
            "उदारमना, परोपकारी और मानवता की सेवा के लिए सदैव तत्पर रहने वाले महान व्यक्तित्व।"
        ],
        "gu": [
            "તેજસ્વી યોદ્ધા જેવો સ્વભાવ, અખૂટ શારીરિક શક્તિ, નીડર, પરોપકારી અને સાહસિક વ્યક્તિત્વ.",
            "નિર્ભય રક્ષક; નબળા લોકોના હક માટે તરત આગળ આવનાર અને ઝડપી નિર્ણયો લેનાર.",
            "અસીમ ઉત્સાહ અને હરીફાઈની ભાવના; રમતગમત, સંરક્ષણ, પોલીસ, એન્જિનિયરિંગ અને સર્જરીમાં તેજસ્વી.",
            "ઉદાર, દેશપ્રેમી અને માનવ કલ્યાણના કાર્યો માટે પોતાનું સર્વસ્વ સમર્પિત કરનાર."
        ]
    }
}

# Precautions for Root Numbers (1-9)
NUMBER_PRECAUTIONS = {
    1: {
        "en": [
            "Guard strictly against arrogance, ego clashes, and an overbearing attitude with subordinates.",
            "Avoid imposing your will forcefully upon family members and business partners.",
            "Do not make rash speculative financial investments out of sheer overconfidence.",
            "Maintain patience; realize that genuine leadership inspires rather than dominates."
        ],
        "hi": [
            "अहंकार, अति-स्वाभिमान और अधीनस्थों के साथ प्रभुत्व जमाने की प्रवृत्ति पर पूर्ण नियंत्रण रखें।",
            "पारिवारिक सदस्यों या व्यावसायिक साझेदारों पर अपनी इच्छा जबरन थोपने से बचें।",
            "अत्यधिक आत्मविश्वास के आवेश में आकर सट्टेबाजी या जोखिम भरे वित्तीय निवेश न करें।",
            "धैर्य बनाए रखें; वास्तविक नेतृत्व दूसरों को प्रेरित करने में है, उन पर हुक्म चलाने में नहीं।"
        ],
        "gu": [
            "અહંકાર, વધુ પડતા અભિમાન અને હાથ નીચેના માણસો પર હુકમ ચલાવવાની ટેવ પર કાબૂ રાખવો.",
            "પરિવારના સભ્યો કે ભાગીદારો પર પોતાના વિચારો બળજબરીથી થોપવાનું ટાળવું.",
            "અતિ-આત્મવિશ્વાસના આવેશમાં આવીને જોખમી કે સટ્ટાકીય રોકાણો કરવાથી દૂર રહેવું.",
            "ધૈર્ય રાખવું; સાચું નેતૃત્વ બીજા પર શાસન કરવામાં નહીં, પરંતુ પ્રેરણા પૂરી પાડવામાં રહેલું છે."
        ]
    },
    2: {
        "en": [
            "Avoid mood swings, emotional hypersensitivity, and unnecessary overthinking.",
            "Do not lend money purely based on emotional appeals without formal documentation.",
            "Overcome indecisiveness; build emotional resilience and avoid chronic self-doubt.",
            "Stay away from negative or cynical company that drains your delicate energy."
        ],
        "hi": [
            "मन के उतार-चढ़ाव (मूड स्विंग्स), अत्यधिक संवेदनशीलता और व्यर्थ की अति-चिंता से बचें।",
            "केवल भावनात्मक बातों में आकर बिना लिखित दस्तावेज के किसी को भी धन उधार न दें।",
            "अनिर्णय की स्थिति से बचें; भावनात्मक मजबूती विकसित करें और आत्म-संदेह से बाहर निकलें।",
            "नकारात्मक और निराशावादी व्यक्तियों की संगति से दूर रहें जो आपकी मानसिक शांति छीनते हैं।"
        ],
        "gu": [
            "મનના વહેમ, મૂડ સ્વિંગ્સ, વધુ પડતી સંવેદનશીલતા અને અતિ-વિચારથી બચવું.",
            "માત્ર લાગણીમાં તણાઈને કાગળિયા વગર કોઈને પણ નાણાં ઉછીના ન આપવા.",
            "નિર્ણય લેવામાં ઢીલ કે અસમંજસ ટાળવી; મનની મક્કમતા કેળવવી અને આત્મસંદેહ છોડવો.",
            "નકારાત્મક અને નિરાશાવાદી લોકોની સોબતથી દૂર રહેવું જે તમારી માનસિક શાંતિ હણી લે છે."
        ]
    },
    3: {
        "en": [
            "Avoid preaching unsolicited advice or carrying an intellectual superiority complex.",
            "Do not scatter energies across too many philosophical or business pursuits simultaneously.",
            "Beware of digestive, liver, or metabolic strain by regulating dietary sweets and fats.",
            "Respect differing viewpoints; avoid becoming overly dogmatic or rigid in discussions."
        ],
        "hi": [
            "बिना मांगे दूसरों को उपदेश देने या अपने ज्ञान का अहंकार प्रदर्शित करने से बचें।",
            "एक साथ बहुत सारे कार्यों में हाथ डालकर अपनी बौद्धिक ऊर्जा को बिखरने न दें।",
            "अधिक मीठे और तैलीय भोजन से बचें ताकि लिवर और पाचन तंत्र पर अनुचित भार न पड़े।",
            "दूसरों के विचारों का भी सम्मान करें; चर्चाओं में अत्यधिक हठधर्मी बनने से बचें।"
        ],
        "gu": [
            "વગર માંગ્યે સલાહ આપવાની કે પોતાના જ્ઞાનનું અભિમાન રાખવાની વૃત્તિથી દૂર રહેવું.",
            "એક સાથે બહુ બધા ક્ષેત્રોમાં ધ્યાન ભટકાવીને શક્તિનો વ્યય ન કરવો.",
            "વધુ પડતી મીઠાઈ અને તળેલો ખોરાક ટાળવો જેથી પાચન અને લીવરની તંદુરસ્તી જળવાય.",
            "સામેવાળાના વિચારોનો પણ આદર કરવો; ચર્ચા-વિચારણામાં જિદ્દી કે હઠીલા ન બનવું."
        ]
    },
    4: {
        "en": [
            "Exercise extreme caution against legal entanglements, court disputes, and unclear contracts.",
            "Avoid engaging in arguments with government authorities, tax officials, or law enforcement.",
            "Avoid speculative gambling, get-rich-quick schemes, and unverified electronic investments.",
            "Ensure that you and your spouse practice transparent communication to avoid emotional distance."
        ],
        "hi": [
            "अस्पष्ट अनुबंधों, कानूनी विवादों, कोर्ट-कचहरी और विवादित सौदों से अत्यधिक सावधान रहें।",
            "सरकारी अधिकारियों, कर विभागों या कानून प्रवर्तन तंत्र से अनावश्यक वाद-विवाद से बचें।",
            "सट्टेबाजी, लॉटरी, तुरंत अमीर बनने के लालच और अपुष्ट डिजिटल निवेशों से दूर रहें।",
            "दांपत्य जीवन में गलतफहमियों और भावनात्मक दूरी से बचने हेतु सदैव पारदर्शी संवाद रखें।"
        ],
        "gu": [
            "અસ્પષ્ટ કરારો, કાનૂની ગૂંચવણો, કોર્ટ કેસો અને વિવાદાસ્પદ સોદાઓથી અત્યંત સાવચેત રહેવું.",
            "સરકારી અધિકારીઓ, ટેક્સ વિભાગ કે કાયદાના રક્ષકો સાથે બિનજરૂરી દલીલો ટાળવી.",
            "સટ્ટો, જુગાર, રાતોરાત અમીર બનવાની યોજનાઓ અને શંકાસ્પદ ડિજિટલ રોકાણોથી દૂર રહેવું.",
            "દામ્પત્ય જીવનમાં ગેરસમજ કે અબોલા ન થાય તે માટે પારદર્શક સંવાદ જાળવવો."
        ]
    },
    5: {
        "en": [
            "Combat restlessness, lack of concentration, and nervous exhaustion through grounding practices.",
            "Avoid changing business plans, jobs, or ventures impulsively without seeing them through.",
            "Keep speech polite and thoughtful; avoid sarcasm or speaking before thinking.",
            "Guard against stress-induced nervous debility and irregular sleeping patterns."
        ],
        "hi": [
            "चंचलता, एकाग्रता की कमी और घबराहट पर नियंत्रण रखने हेतु नियमित ध्यान व प्राणायाम करें।",
            "बिना किसी योजना को परिपक्व किए बार-बार व्यापार या नौकरी बदलने की जल्दबाजी न करें।",
            "वाणी में मधुरता रखें; व्यंग्यात्मक बोलने या बिना सोचे-समझे बोलने से बचें।",
            "अनिद्रा और मानसिक तनाव से बचने के लिए नियमित दिनचर्या का पालन करें।"
        ],
        "gu": [
            "મનની અતિ-ચંચળતા, એકાગ્રતાનો અભાવ અને ગભરામણ પર કાબૂ રાખવા ધ્યાન અને પ્રાણાયામ કરવા.",
            "કોઈપણ વ્યવસાય કે નોકરીને પૂરતો સમય આપ્યા વગર ઉતાવળમાં વારંવાર બદલવાનું ટાળવું.",
            "વાણીમાં મીઠાશ રાખવી; કટાક્ષવાળા શબ્દો કે વિચાર્યા વગર બોલવાનું ટાળવું.",
            "માનસિક તણાવ અને અનિદ્રાથી બચવા માટે નિયમિત ઊંઘ અને સમયપત્રકનું પાલન કરવું."
        ]
    },
    6: {
        "en": [
            "Control extravagance, impulsive spending on luxury, and living beyond financial means.",
            "Avoid entering into extramarital distractions or secret affairs that ruin reputation.",
            "Do not indulge in addictions, rich heavy food, alcohol, or unchecked sensual pleasures.",
            "Ensure financial savings are strictly automated to protect future liquidity."
        ],
        "hi": [
            "दिखावे, फिजूलखर्ची और विलासिता की वस्तुओं पर आमदनी से अधिक खर्च करने पर नियंत्रण रखें।",
            "विवाहेतर आकर्षणों और अनैतिक संबंधों से पूरी तरह दूर रहें जो मान-सम्मान को हानि पहुँचा सकते हैं।",
            "नशे, अत्यधिक गरिष्ठ भोजन और अनियंत्रित वासनाओं के प्रभाव में आने से बचें।",
            "भविष्य की सुरक्षा के लिए अपनी बचत को सुरक्षित एवं सुनियोजित निवेशों में लगाएं।"
        ],
        "gu": [
            "દેખાડા, ઉડાઉપણા અને ગજા ઉપરાંતની વૈભવી ચીજો પાછળ આડેધડ ખર્ચ કરવા પર કાબૂ રાખવો.",
            "લગ્નેતર સંબંધો અને ગુપ્ત આકર્ષણોથી સદંતર દૂર રહેવું જે પ્રતિષ્ઠાને હાનિ પહોંચાડી શકે.",
            "વ્યસન, ભારે ખોરાક, મદિરાપાન અને વધુ પડતી વિષયવાસનાઓથી પોતાને બચાવવા.",
            "ભવિષ્યની સુરક્ષા માટે આવકમાંથી ફરજિયાત બચત અને નક્કર રોકાણ કરવાની ટેવ પાડવી."
        ]
    },
    7: {
        "en": [
            "Do not withdraw into extreme social isolation, cynicism, or emotional detachment.",
            "Verify all business proposals thoroughly; do not trust blindly without due diligence.",
            "Avoid harboring secret grudges or skepticism toward well-wishers and life partners.",
            "Channel your analytical thoughts into constructive research rather than anxious self-pity."
        ],
        "hi": [
            "अत्यधिक एकांतप्रियता, दुनिया से कट जाने या संन्यास की भावना में डूबने से बचें।",
            "व्यावसायिक प्रस्तावों की पूरी छानबीन करें; किसी पर भी आंख मूंदकर भरोसा न करें।",
            "अपने शुभचिंतकों और जीवनसाथी के प्रति अकारण संशय या अविश्वास का भाव न पालें।",
            "अपने गहन विचारों को निराशा के बजाय सकारात्मक अनुसंधान और साधना में लगाएं।"
        ],
        "gu": [
            "અતિશય એકલવાયાપણું, સંસારથી વિમુક્ત થઈ જવાની વૃત્તિ કે હતાશાથી દૂર રહેવું.",
            "ધંધાકીય સોદાઓમાં પૂરી તપાસ કરવી; કોઈના પર પણ આંધળો વિશ્વાસ ન મૂકવો.",
            "પોતાના શુભચિંતકો અને જીવનસાથી પ્રત્યે બિનજરૂરી શંકા કે વહેમ રાખવાનું ટાળવું.",
            "પોતાના ઊંડા વિચારોને નકારાત્મક ચિંતામાં વેડફવાને બદલે સર્જનાત્મક સંશોધનમાં વાળવા."
        ]
    },
    8: {
        "en": [
            "Avoid chronic pessimism, bitterness, or feeling victimized by delays in life.",
            "Never mistreat or underpay servants, manual laborers, drivers, or domestic assistants.",
            "Refrain from shortcuts, unethical wealth, tax evasion, or taking revenge on adversaries.",
            "Keep joints and spinal posture healthy; do not neglect physical exercise and hydration."
        ],
        "hi": [
            "जीवन में होने वाले विलंब के कारण निराशा, कड़वाहट या हीनभावना का शिकार होने से बचें।",
            "अधीनस्थ कर्मचारियों, सफाईकर्मियों, चालकों और घरेलू सहायकों का कभी अपमान या शोषण न करें।",
            "अनियमित रास्तों, अनैतिक धन, कर चोरी या बदले की भावना से सर्वथा दूर रहें।",
            "रीढ़ की हड्डी और जोड़ों के स्वास्थ्य का ध्यान रखें; नियमित व्यायाम और जलपान न भूलें।"
        ],
        "gu": [
            "કામમાં થતા વિલંબથી હતાશ થઈને કડવાશ, નકારાત્મકતા કે હતાશાનો ભોગ ન બનવું.",
            "મજૂરો, સફાઈ કર્મચારીઓ, ડ્રાઇવરો કે ઘરના નોકરોનું ક્યારેય અપમાન કે શોષણ ન કરવું.",
            "ગેરકાયદેસર કમાણી, ટેક્સ ચોરી, શોર્ટકટ્સ કે બદલાની ભાવનાથી હંમેશા દૂર રહેવું.",
            "સાંધા અને કરોડરજ્જુની તંદુરસ્તી જાળવવી; નિયમિત કસરત અને પૂરતું પાણી પીવું."
        ]
    },
    9: {
        "en": [
            "Control sudden bursts of extreme anger, impulsiveness, and aggressive language.",
            "Practice defensive driving; avoid road rage, rash speeding, and hazardous sports without gear.",
            "Do not jump into physical confrontations, arguments, or unnecessary battles for pride.",
            "Maintain cardiovascular and blood pressure health through calming breathwork and moderate diet."
        ],
        "hi": [
            "क्रोध के अचानक आवेग, आक्रामकता और कटु भाषा के प्रयोग पर कड़ा नियंत्रण रखें।",
            "वाहन चलाते समय अत्यधिक सावधानी बरतें; तेज गति और सड़क पर विवादों से बचें।",
            "झूठी प्रतिष्ठा के लिए शारीरिक विवादों, लड़ाई-झगड़ों या व्यर्थ की बहसों में न उलझें।",
            "शांत प्राणायाम और सुपाच्य भोजन के माध्यम से रक्तचाप और हृदय स्वास्थ्य को संतुलित रखें।"
        ],
        "gu": [
            "અચાનક આવતા ગુસ્સાના આવેશ, ઉગ્રતા અને કડવી ભાષા બોલવા પર કડક નિયંત્રણ રાખવું.",
            "વાહન ચલાવતી વખતે ખૂબ કાળજી રાખવી; અતિ-ઝડપ અને રસ્તા પરના વિવાદોથી બચવું.",
            "ખોટા દેખાડા કે જીદ ખાતર મારામારી, ઝઘડા કે બિનજરૂરી વિવાદોમાં ક્યારેય ન પડવું.",
            "ધ્યાન, પ્રાણાયામ અને સાત્વિક આહાર દ્વારા બ્લડ પ્રેશર અને હૃદયની તંદુરસ્તી જાળવવી."
        ]
    }
}

# Positive vs Negative Vibrations of Numbers in the Grid
# Enriched Deep Planetary Vibrations Breakdown (Detailed multi-sentence analysis based on authentic course texts)
VIBRATION_DETAILS = {
    1: {
        "pos": {
            "en": "Positive (+1 Solar Vitality): Endows the native with supreme solar vitality, majestic authority, charismatic leadership, and regal confidence ('King-like life'). Natural pioneer and executive decision-maker with an indomitable aura; commands high institutional respect, attracts lucrative financial opportunities, and steadfastly protects subordinates.",
            "hi": "सकारात्मक (+1 सूर्य का दिव्य तेज): जातक को सूर्य का दिव्य तेज, राजसी मान-सम्मान, निर्भीक नेतृत्व और अटूट आत्मविश्वास ('राजा जैसा जीवन') प्रदान करता है। स्वभाव से स्वाभाविक अगुआ और उच्च प्रशासक, जिनका आभामंडल समाज में सर्वोच्च प्रतिष्ठा, सत्ता और अकूत धन-संपत्ति आकर्षित करता है।",
            "gu": "સકારાત્મક (+1 સૂર્યનું દિવ્ય તેજ): જાતકને સૂર્યનું દિવ્ય તેજ, રાજા સમાન માન-પ્રતિષ્ઠા, નિર્ભય નેતૃત્વ અને અખૂટ આત્મવિશ્વાસ ('રાજા જેવું જીવન') પ્રદાન કરે છે. વહીવટી સત્તા અને મક્કમ નિર્ણયશક્તિથી સમાજમાં ઉચ્ચ મોભો, અધિકાર તથા વિપુલ આર્થિક સમૃદ્ધિ મેળવે છે."
        },
        "neg": {
            "en": "Challenging (-1 Solar Affliction): Over-vibration manifests as extreme egoism, rigid authoritarianism ('my way or highway'), contempt for others' viewpoints, dictatorial dominance, and explosive temper. Tendency to alienate family, severe friction with father or superiors, and susceptibility to deceptive financial schemes or unearned public blame.",
            "hi": "कठिन (-1 सूर्य अहंकार दोष): अति-ऊर्जा अहंकार, हठधर्मिता ('मेरी मर्जी या कुछ नहीं'), तानाशाही रवैया और उग्र क्रोध का रूप ले लेती है। पिता या उच्चाधिकारियों से निरंतर टकराव, परिजनों की भावनाओं की उपेक्षा और जल्दबाजी में वित्तीय नुकसान या धोखे का गंभीर जोखिम रहता है।",
            "gu": "પડકારરૂપ (-1 સૂર્ય અહંકાર દોષ): અહંકાર, હઠીલો સ્વભાવ ('મારી વાત જ સાચી'), હુકમશાહી વલણ અને અચાનક આવતો ક્રોધ લાવે છે. પિતા અથવા ઉચ્ચ અધિકારીઓ સાથે મતભેદ, અન્યોની લાગણીઓની અવગણના અને ઉતાવળે નાણાકીય નુકસાન કે છેતરપિંડીનું જોખમ રહે છે."
        }
    },
    2: {
        "pos": {
            "en": "Positive (+2 Lunar Grace): Endows gentle motherly empathy, soothing artistic elegance, deep psychological intuition, and hypnotic diplomatic charm. Exceptional ability to build harmonious partnerships, diffuse conflicts, and provide profound emotional healing and aesthetic comfort to loved ones.",
            "hi": "सकारात्मक (+2 चंद्र का वात्सल्य): चंद्र का शीतल वात्सल्य, कलात्मक लालित्य, गहन अंतर्ज्ञान और चुंबकीय राजनयिक आकर्षण प्रदान करता है। साझेदारी में अभूतपूर्व सफलता, विवादों को सहज शांत करने का हुनर और दूसरों को भावनात्मक संबल व सुख देने की अद्वितीय क्षमता।",
            "gu": "સકારાત્મક (+2 ચંદ્રની શીતળતા): ચંદ્રનો શીતળ પ્રેમ, કલાત્મક સૂઝ, ઊંડી આંતરિક પ્રેરણા અને શાંત રાજદ્વારી કુશળતા આપે છે. ભાગીદારીમાં ઉત્તમ સંવાદિતા, સંબંધોમાં સ્નેહ અને સાથીદારોને સાચો દિલાસો તથા શાંતિ આપવાની અજોડ આવડત."
        },
        "neg": {
            "en": "Challenging (-2 Lunar Vulnerability): Hypersensitivity, emotional vulnerability, chronic anxiety, and unpredictable mood swings. Suffers from acute fear of rejection, painful over-dependency on others' approval, deep melancholy/depression, and escapist coping habits when under sustained emotional pressure.",
            "hi": "कठिन (-2 चंद्र अवसाद एवं चिंता): अत्यधिक भावुकता, मन का विचलन, अवसाद (डिप्रेशन), असुरक्षा की भावना और गंभीर चिंता। अस्वीकृति का असहनीय भय, दूसरों की प्रशंसा पर अत्यधिक निर्भरता, अकेलेपन का डर और तनाव में नकारात्मक आदतों में फंसने की प्रवृत्ति।",
            "gu": "પડકારરૂપ (-2 ચંદ્ર અસ્થિરતા દોષ): અતિ સંવેદનશીલતા, માનસિક અસ્થિરતા, સતત ઉદાસીનતા (ડિપ્રેશન) અને નકારાત્મક ચિંતાઓ. બીજા પર વધુ પડતી પરાધીનતા, નિષ્ફળતાનો અસહ્ય ડર અને તણાવમાં વ્યસન કે એકલતા તરફ ઢળી જવાની પ્રવૃત્તિ."
        }
    },
    3: {
        "pos": {
            "en": "Positive (+3 Jupiterian Wisdom): Supreme Guru wisdom, uncompromising moral ethics, profound advisory eloquence, and visionary academic intellect. Natural counselor, teacher, and spiritual strategist; deeply rooted in family harmony, incorruptible integrity, and revered societal honor.",
            "hi": "सकारात्मक (+3 देवगुरु बृहस्पति प्रज्ञा): देवगुरु बृहस्पति की दिव्य प्रज्ञा, अक्षुण्ण नैतिक मूल्य, प्रभावशाली परामर्श वाणी और उत्कृष्ट दूरदर्शिता। स्वाभाविक गुरु, परामर्शदाता एवं नीतिवान मार्गदर्शक, जो परिवार के प्रति समर्पित, रिश्वत व प्रलोभनों से परे और समाज में पूज्यनीय प्रतिष्ठा प्राप्त करते हैं।",
            "gu": "સકારાત્મક (+3 ગુરુ બૃહસ્પતિ જ્ઞાન): ગુરુ બૃહસ્પતિની દિવ્ય વિદ્વત્તા, અડગ નૈતિક મૂલ્યો, પ્રભાવશાળી માર્ગદર્શન અને ઉચ્ચ શૈક્ષણિક બુદ્ધિ. પરિવાર પ્રત્યે સમર્પણ, પ્રમાણિકતા અને સમાજમાં પૂજનીય મોભો ધરાવતા ઉત્તમ સલાહકાર અને શિક્ષક."
        },
        "neg": {
            "en": "Challenging (-3 Jupiter Dogma): Intellectual dogma, moral preachiness, hypocrisy, and obstinate refusal to acknowledge errors. Over-expansion leads to domestic disputes, detachment from family, superficial display of piety, and dictatorial lecturing toward subordinates and kin.",
            "hi": "कठिन (-3 वैचारिक हठ एवं क्लेश): वैचारिक हठधर्मिता, उपदेशात्मक अहंकार, अपनी भूल न स्वीकारना और नैतिक दिखावा। अधिक संख्या होने पर पारिवारिक क्लेश या वैराग्य, परिजनों से अलगाव, और दूसरों पर अनचाहा नियंत्रण थोपने की कमजोरी।",
            "gu": "પડકારરૂપ (-3 બૌદ્ધિક અહંકાર દોષ): બૌદ્ધિક અહંકાર, જિદ્દી વલણ, પોતાની ભૂલ ક્યારેય ન સ્વીકારવી અને ધાર્મિકતાનો દેખાડો. વધુ પડતા પ્રભાવથી પારિવારિક અશાંતિ, સંબંધોમાં અણબનાવ અને અન્યો ઉપર પોતાના વિચારો થોપવાની નબળાઈ."
        }
    },
    4: {
        "pos": {
            "en": "Positive (+4 Rahu Innovation): Groundbreaking out-of-the-box unconventional genius, extraordinary research intellect, sharp analytical logic, and uncanny mastery over modern technology and sales persuasion. Unshakable perseverance that converts unprecedented ideas into tangible reality.",
            "hi": "सकारात्मक (+4 राहु का नवाचार): लीक से हटकर सोचने की क्रांतिकारी प्रतिभा (आउट-ऑफ-द-बॉक्स), असाधारण शोध बुद्धि, तार्किक विश्लेषण और आधुनिक तकनीक व जनसंपर्क पर अद्भुत पकड़। जटिलतम समस्याओं का अभिनव समाधान निकालने की सामर्थ्य।",
            "gu": "સકારાત્મક (+4 રાહુનું ક્રાંતિકારી ચિંતન): લકીરથી હટીને વિચારવાની ક્રાંતિકારી પ્રતિભા (આઉટ-ઓફ-ધ-બોક્સ), અસાધારણ સંશોધન બુદ્ધિ અને આધુનિક ટેકનોલોજી તથા સેલ્સ-માર્કેટિંગમાં અદભુત સફળતા. મુશ્કેલ કોયડાઓને સરળતાથી ઉકેલવાની શક્તિ."
        },
        "neg": {
            "en": "Challenging (-4 Rahu Volatility): Unpredictable volatility, erratic decision-making, unexpected sudden financial drains, and vulnerability to legal/confinement traps (Bandhan). Restless nature leading to fruitless travels, chronic dissatisfaction, and defiance of established order.",
            "hi": "कठिन (-4 राहु बंधन एवं व्यय): अप्रत्याशित मानसिक उथल-पुथल, अचानक वित्तीय नुकसान, कानूनी विवाद या बंधन/अस्पताल के योग। बिना योजना के कार्य, व्यर्थ की भागदौड़, अत्यधिक फिजूलखर्ची और मानसिक अस्थिरता का खतरा।",
            "gu": "પડકારરૂપ (-4 રાહુ બંધન દોષ): અનિશ્ચિત વર્તન, અચાનક આર્થિક નુકસાન, કાનૂની અડચણો અથવા બંધન/હોસ્પિટલના યોગ. આયોજન વગર કામ કરવાની ટેવ, નકામી મુસાફરી, બેફામ ખર્ચ અને અશાંત મગજ."
        }
    },
    5: {
        "pos": {
            "en": "Positive (+5 Mercury Commercial Genius): Lightning-fast commercial intellect, magnetic communication eloquence, supreme negotiation mastery, and cash-flow agility. Supreme networking strategist and business dealmaker who turns every market opportunity into profitable enterprise with joyful versatility.",
            "hi": "सकारात्मक (+5 बुध की व्यापारिक प्रखरता): तीव्रतम व्यापारिक बुद्धि, वाकपटुता, कुशल सौदेबाजी और द्रुत गति से धन उपार्जन की महारत। व्यावहारिक नेटवर्किंग, बहुआयामी प्रतिभा और कठिन परिस्थितियों में तुरंत लाभ का मार्ग प्रशस्त करने की अद्भुत क्षमता।",
            "gu": "સકારાત્મક (+5 બુધ વેપાર કુશળતા): અતિ તેજ વેપારી બુદ્ધિ, અદભુત વાકચાતુર્ય, ઉત્કૃષ્ટ સોદાબાજી અને ઝડપી નાણાકીય વૃદ્ધિ કરવાની કુશળતા. સંબંધોનું ઉત્તમ નેટવર્કિંગ અને ગમે તેવી સ્થિતિમાંથી નફો કમાઈ લેવાની વ્યવહારિક સૂઝ."
        },
        "neg": {
            "en": "Challenging (-5 Mercury Calculation): Over-calculative mercantile obsession, extreme restless nervous energy, chronic insomnia, and unscrupulous temptation to cut corners or commit financial fraud ('Iski topi uske sar'). Flitting from venture to venture without sustained commitment.",
            "hi": "कठिन (-5 अति-चतुराई एवं अनिद्रा): अत्यधिक स्वार्थपरक गणना, धन का लोभ, मानसिक उद्वेग, अनिद्रा (नींद न आना) और अनुचित चतुराई या धोखेबाजी की जोखिम भरी प्रवृत्ति। एक कार्य में स्थिरता न रख पाना और अति-सट्टेबाजी में धन गंवाना।",
            "gu": "પડકારરૂપ (-5 અતિ-ચતુરતા દોષ): વધુ પડતી સ્વાર્થી ગણતરી, અનિદ્રા, માનસિક અશાંતિ અને છેતરપિંડી કે અયોગ્ય માર્ગે ધન કમાવવાની લાલચ ('આની ટોપી તેના માથે'). કાર્યમાં સ્થિરતા ન રહેવી અને અતિશય ચતુરાઈથી નુકસાન થવું."
        }
    },
    6: {
        "pos": {
            "en": "Positive (+6 Venusian Elegance & Luxury): Sovereign aesthetic refinement, magnetic social charisma, supreme hospitality, and effortless attraction of luxury vehicles, designer estates, and lavish comforts. Endowed with profound creative genius in cinema, arts, culinary delights, and joyful romantic fidelity.",
            "hi": "सकारात्मक (+6 शुक्र का राजसी ऐश्वर्य): शुक्र का ऐश्वर्य, सम्मोहक सौंदर्य, विलासिता, उत्तम वाहन-भवन सुख और कलात्मक प्रतिभा। पाक कला, संगीत, फैशन एवं सिनेमा में अपार सफलता, उदार आतिथ्य सत्कार और जीवन में सहजता से सुख-सुविधाएं आकर्षित करने का वरदान।",
            "gu": "સકારાત્મક (+6 શુક્રનું ભવ્ય ઐશ્વર્ય): શુક્રનું અપ્રતિમ સૌંદર્ય, ચુંબકીય આકર્ષણ, ભવ્ય વૈભવ, ઉત્તમ વાહન-મકાન સુખ અને કલાત્મક પ્રતિભા. સિનેમા, ફેશન, સંગીત અને મહેમાનગતિમાં અગ્રેસર રહેવાની અને વૈભવી જીવન જીવવાની કૃપા."
        },
        "neg": {
            "en": "Challenging (-6 Venusian Excess & Kalaha): Extravagant hedonism, showy brand obsession, marital conflicts, harsh aggressive speech toward partners, and domestic turbulence (Kalaha). Tendency to live beyond means and vulnerability to scandalous controversies or reproductive challenges.",
            "hi": "कठिन (-6 शुक्र कलह एवं विलासिता दोष): भौतिक दिखावे का अंधानुकरण, कटु वाणी, जीवनसाथी या स्त्रियों से कलह-विवाद, और बेहिसाब फिजूलखर्ची। वासना व अत्यधिक भोग में समय गंवाना, रिश्तों में अविश्वास और संतान प्राप्ति में बाधाएं।",
            "gu": "પડકારરૂપ (-6 શુક્ર કલહ દોષ): બાહ્ય દેખાડો અને બ્રાન્ડ મોહ, કડવી વાણી, સ્ત્રીઓ કે જીવનસાથી સાથે વિવાદ-ઝઘડા અને અતિશય ખર્ચાળ સ્વભાવ. લક્ઝરી પાછળ દેવું કરવું, સંબંધોમાં અણબનાવ અને પારિવારિક અશાંતિ."
        }
    },
    7: {
        "pos": {
            "en": "Positive (+7 Ketu Spiritual Fortitude): Transcendent spiritual awakening, penetrating analytical intuition, divine crisis protection, and profound mastery in healing and occult sciences. Blessed with exceptional good fortune in overcoming hurdles, foreign settlement success, and peaceful karmic stability.",
            "hi": "सकारात्मक (+7 केतु की आध्यात्मिक कृपा): आध्यात्मिक मुक्ति, गहरी सूक्ष्म अंतर्दृष्टि, पराविद्याओं व हीलिंग में महारत और संकटों में ईश्वरीय दैवीय रक्षा। विदेश गमन एवं बसने के प्रबल योग, आकस्मिक भाग्योदय और विपरीत परिस्थितियों से सहजता से उबरने का सौभाग्य।",
            "gu": "સકારાત્મક (+7 કેતુની આધ્યાત્મિક કૃપા): આધ્યાત્મિક જાગૃતિ, ગહન આંતરિક દ્રષ્ટિ, રહસ્યમય વિદ્યાઓ અને હીલિંગમાં નિપુણતા તથા મુશ્કેલીઓમાં ઈશ્વરીય રક્ષણ. વિદેશ પ્રવાસ અને સ્થાયી થવાના ઉત્તમ યોગ, અણધાર્યો ભાગ્યોદય અને શાંત પ્રકૃતિ."
        },
        "neg": {
            "en": "Challenging (-7 Ketu Skepticism & Disconnect): Hyper-skeptical over-analysis ('splitting hairs'), emotional detachment, vulnerability to sudden betrayals, and deep disillusionment in romance ('plastic love'). Chronic restlessness, aimless travels, and acute marital misunderstandings.",
            "hi": "कठिन (-7 केतु संशय एवं भटकाव): अत्यधिक शक्की मिजाज ('बाल की खाल निकालना'), भावनात्मक अलगाव, विश्वासघात का शिकार होना और वैवाहिक जीवन में असंतोष (प्लास्टिक प्रेम)। व्यर्थ की यात्राएं, मन का भटकाव और एकांतवास की अति।",
            "gu": "પડકારરૂપ (-7 કેતુ વહેમ દોષ): અતિશય વહેમી સ્વભાવ ('વાળની ખાલ કાઢવી'), લાગણીશૂન્યતા, દગો થવો અને દાંપત્ય જીવનમાં અસંતોષ (પ્લાસ્ટિક લવ). નકામી રઝળપાટ, એકલતા અને જીવનમાં અચાનક આવતા વિષમ ઉતાર-ચઢાવ."
        }
    },
    8: {
        "pos": {
            "en": "Positive (+8 Saturnian Endurance & Titan Wealth): Indomitable perseverance, monumental financial architecture, organizational titan strength, and selfless compassion for the underprivileged. Possesses unyielding karmic patience; reaches supreme heights in industry, heavy enterprise, real estate, and public justice through relentless hard work.",
            "hi": "सकारात्मक (+8 शनि देव का साम्राज्य): शनि देव का असीम धैर्य, अटूट कर्मठता, विशाल वित्तीय साम्राज्य निर्माण की क्षमता और वंचितों के प्रति सच्ची करुणा। कठिन परिश्रम से शून्य से शिखर तक पहुंचने की शक्ति, अचल संपत्ति, उद्योग व न्याय क्षेत्र में सर्वोच्च कीर्ति।",
            "gu": "સકારાત્મક (+8 શનિદેવનું સ્થાયી સામ્રાજ્ય): શનિદેવનું અડગ ધૈર્ય, અથાગ પરિશ્રમ, વિશાળ નાણાકીય આયોજન અને દીન-દુખિયાં પ્રત્યે ખરી સંવેદના. શૂન્યમાંથી સર્જન કરવાની શક્તિ, સ્થાવર મિલકતો, મોટા ઉદ્યોગો અને ન્યાયપ્રિયતામાં સર્વોચ્ચ શિખરે પહોંચવાની ક્ષમતા."
        },
        "neg": {
            "en": "Challenging (-8 Saturnian Delay & Vish Yoga): Grinding struggle, agonizing career delays, chronic melancholia/depression (Vish Yoga), and bitter stubbornness. Tendency to hold long grudges, isolation, bone/joint ailments, and building castles in the air (Hava Mahal) if paired with ungrounded speculation.",
            "hi": "कठिन (-8 शनि संघर्ष एवं विष दोष): अत्यधिक संघर्ष, कार्यों में भारी विलंब, मानसिक अवसाद (विष दोष), हठधर्मिता और अकेलापन। पुरानी बातों को लेकर मन में कड़वाहट रखना, हड्डियों/जोड़ों के रोग, और सट्टेबाजी में हवा हवाई महल बनाकर धन गंवाना।",
            "gu": "પડકારરૂપ (-8 શનિ વિષ દોષ): અતિશય સંઘર્ષ, કામોમાં વિલંબ, માનસિક નિરાશા (વિષ દોષ), જીદ્દીપણું અને એકલતા. જૂના અણબનાવ મનમાં રાખી મૂકવા, સાંધા/હાડકાના રોગો અને સટ્ટાકીય આકાંક્ષાઓમાં હવાઈ કિલ્લા બનાવી ધન ગુમાવવું."
        }
    },
    9: {
        "pos": {
            "en": "Positive (+9 Martial Valor & Commander Power): Heroic valor, explosive dynamic energy, fearless righteous leadership, and fiery passion for universal justice. Natural protector and powerhouse executor who excels in defense, real estate, sports, surgery, and large-scale administrative operations without backing down.",
            "hi": "सकारात्मक (+9 मंगल का अदम्य शौर्य): मंगल का अतुलित शौर्य, अदम्य ऊर्जा, अन्याय के विरुद्ध निर्भीक संघर्ष और दृढ़ नेतृत्व क्षमता। रक्षा, खेलकूद, शल्य चिकित्सा (सर्जरी), रियल एस्टेट और बड़े अभियानों में निडरता से विजय प्राप्त करने वाला तेजस्वी सेनापति।",
            "gu": "સકારાત્મક (+9 મંગળનું પરાક્રમ): મંગળનું અજોડ શૌર્ય, અખૂટ ઉર્જા, અન્યાય સામે લડવાની નિર્ભય હિંમત અને પ્રભાવશાળી નેતૃત્વ. સંરક્ષણ, રમતગમત, સર્જરી, જમીન-મકાન અને સાહસિક કાર્યોમાં વિજય અપાવતો પરાક્રમી સેનાપતિ."
        },
        "neg": {
            "en": "Challenging (-9 Martial Wrath & Bandhan Risk): Explosive volcanic rage, reckless impatience, belligerent argumentation, and vulnerability to accidents or litigation (Bandhan Yoga). Tendency to act on hot impulses, burning valuable relationships, and imposing domineering force over subordinates.",
            "hi": "कठिन (-9 मंगल उग्रता एवं बंधन जोखिम): ज्वालामुखी जैसा उग्र क्रोध, अत्यधिक आक्रामकता, व्यर्थ के विवाद और दुर्घटना या कानूनी विवाद (बंधन दोष) में फंसने की आशंका। जल्दबाजी में गलत निर्णय, कटु भाषा से आत्मीय संबंध बिगाड़ना और अशांत रक्तचाप।",
            "gu": "પડકારરૂપ (-9 મંગળ ક્રોધ દોષ): જ્વાળામુખી જેવો ભયંકર ક્રોધ, અધીરાઈ, આક્રમક વાણી અને અકસ્માત કે કોર્ટ-કચેરી (બંધન દોષ) માં ફસાઈ જવાનું જોખમ. ઉતાવળા નિર્ણયોથી સંબંધોમાં તિરાડ પાડવી અને રક્તચાપ/અશાંતિ ભોગવવી."
        }
    }
}

# Authentic Auspicious Planetary Alignments (Shubh Yogas)
AUSPICIOUS_YOGAS_DEFINITIONS = {
    "thought_plane": {
        "numbers": [3, 1, 9],
        "name": {"en": "Mahapurush Thought Plane (Mental Power & Dominance Yog)", "hi": "महापुरुष विचार तल (मानसिक शक्ति एवं प्रभुत्व योग)", "gu": "મહાપુરુષ વિચાર તલ (માનસિક શક્તિ અને પ્રભુત્વ યોગ)"},
        "tag": {"en": "Horizontal Line 1 (3-1-9)", "hi": "प्रथम क्षैतिज रेखा (3-1-9)", "gu": "પ્રથમ આડી લાઇન (3-1-9)"},
        "desc": {
            "en": "Complete harmony of Jupiter (3), Sun (1), and Mars (9). Bestows visionary intellect, supreme leadership dominance, unshakable memory, and massive executive authority. The native rises to commanding heights in society.",
            "hi": "गुरु (3), सूर्य (1) और मंगल (9) का त्रिवेणी संगम। जातक को अद्भुत दूरदर्शिता, सर्वोच्च प्रशासनिक प्रभुत्व, तीव्र स्मरण शक्ति और समाज में निर्विवाद नेतृत्व प्रदान करता है।",
            "gu": "ગુરુ (3), સૂર્ય (1) અને મંગળ (9) નો દિવ્ય સંગમ. જાતકને અસાધારણ દીર્ઘદ્રષ્ટિ, સર્વોચ્ચ વહીવટી પ્રભુત્વ, તીક્ષ્ણ સ્મરણશક્તિ અને સમાજમાં અગ્રણી નેતૃત્વ પ્રદાન કરે છે."
        }
    },
    "will_plane": {
        "numbers": [6, 7, 5],
        "name": {"en": "Kuber Lakshmi Will Plane (Material Luxury & Fortune Yog)", "hi": "कुबेर लक्ष्मी इच्छा तल (भौतिक ऐश्वर्य एवं संकल्प योग)", "gu": "કુબેર લક્ષ્મી ઈચ્છા તલ (ભૌતિક ઐશ્વર્ય અને સંકલ્પ યોગ)"},
        "tag": {"en": "Horizontal Line 2 (6-7-5)", "hi": "द्वितीय क्षैतिज रेखा (6-7-5)", "gu": "બીજી આડી લાઇન (6-7-5)"},
        "desc": {
            "en": "Synthesis of Venus (6), Ketu (7), and Mercury (5). Confers lifelong material luxuries, premium vehicles, prime properties, magnetic sales oratory, and unyielding willpower. Attracts abundance effortlessly.",
            "hi": "शुक्र (6), केतु (7) और बुध (5) का दिव्य योग। जीवनभर प्रचुर विलासिता, लक्जरी वाहन, भव्य भवन, सम्मोहक वाकपटुता और किसी भी संकट से उबरने का अडिग संकल्प प्रदान करता है।",
            "gu": "શુક્ર (6), કેતુ (7) અને બુધ (5) નો મહાન યોગ. જીવનભર અખૂટ ભૌતિક સુખ-સગવડ, વૈભવી વાહન-મકાન, વાકચાતુર્ય અને સંકલ્પબળ દ્વારા લક્ષ્મી કૃપા પ્રાપ્ત કરાવે છે."
        }
    },
    "intuition_plane": {
        "numbers": [3, 7, 9],
        "name": {"en": "Tri-Netra Spiritual & Intuition Plane (Occult Awakening Yog)", "hi": "त्रिनेत्र आध्यात्मिक एवं अंतर्ज्ञान तल (गूढ़ रहस्य योग)", "gu": "ત્રિનેત્ર આધ્યાત્મિક અને અંતર્જ્ઞાન તલ (ગૂઢ રહસ્ય યોગ)"},
        "tag": {"en": "Spiritual Diagonal (3-7-9)", "hi": "आध्यात्मिक विकर्ण (3-7-9)", "gu": "આધ્યાત્મિક વિકર્ણ (3-7-9)"},
        "desc": {
            "en": "Union of Jupiter (3), Ketu (7), and Mars (9). Unlocks penetrating psychic intuition, prophetic foresight, profound occult aptitude, and divine crisis protection. Inspires selfless humanitarian service.",
            "hi": "गुरु (3), केतु (7) और मंगल (9) का आध्यात्मिक संगम। जातक को त्रिकालदर्शी अंतर्ज्ञान, पराविद्याओं में सिद्धि, संकटों में ईश्वरीय दैवीय रक्षा और जनकल्याणकारी भावना प्रदान करता है।",
            "gu": "ગુરુ (3), કેતુ (7) અને મંગળ (9) નો દિવ્ય આધ્યાત્મિક સમન્વય. જાતકને ઊંડી આંતરિક સૂઝ, રહસ્ય વિદ્યાઓમાં નિપુણતા, ઈશ્વરીય સહાય અને પરોપકારની ભાવના આપે છે."
        }
    },
    "vision_line": {
        "numbers": [3, 6, 2],
        "name": {"en": "Kala-Vidya Knowledge Line (Guru-Shukra-Chandra Yog)", "hi": "कला-विद्या ज्ञान रेखा (गुरु-शुक्र-चंद्र योग)", "gu": "કલા-વિદ્યા જ્ઞાન રેખા (ગુરુ-શુક્ર-ચંદ્ર યોગ)"},
        "tag": {"en": "Vertical Line 1 (3-6-2)", "hi": "प्रथम ऊर्ध्वाधर रेखा (3-6-2)", "gu": "પ્રથમ ઊભી લાઇન (3-6-2)"},
        "desc": {
            "en": "Melds Guru's wisdom, Venus's artistic refinement, and Moon's emotional empathy. Bestows unmatched flair for media, performing arts, high-level counseling, and aesthetic cultural leadership.",
            "hi": "गुरु का ज्ञान, शुक्र का कलात्मक वैभव और चंद्र की संवेदनशीलता। मीडिया, सिनेमा, संगीत, उच्चस्तरीय परामर्श और रचनात्मक क्षेत्रों में शिखर प्रतिष्ठा दिलाता है।",
            "gu": "ગુરુનું જ્ઞાન, શુક્રનું કલાત્મક સૌંદર્ય અને ચંદ્રની સંવેદનશીલતા. મીડિયા, કલા, સંગીત અને શ્રેષ્ઠ સલાહકાર તરીકે સમાજમાં વિશિષ્ટ નામના અપાવે છે."
        }
    },
    "balance_line": {
        "numbers": [1, 7, 8],
        "name": {"en": "Rajyadhikari Balance & Executive Sovereign Line (1-7-8)", "hi": "राज्याधिकारी संतुलन एवं प्रशासनिक संप्रभु रेखा (1-7-8)", "gu": "રાજ્યાધિકારી સંતુલન અને વહીવટી સાર્વભૌમ રેખા (1-7-8)"},
        "tag": {"en": "Vertical Line 2 (1-7-8)", "hi": "द्वितीय ऊर्ध्वाधर रेखा (1-7-8)", "gu": "બીજી ઊભી લાઇન (1-7-8)"},
        "desc": {
            "en": "Imperial alignment of Sun (1), Ketu (7), and Saturn (8). Endows massive endurance, administrative justice, institutional command, and capacity to build and govern massive organizations.",
            "hi": "सूर्य (1), केतु (7) और शनि (8) का दुर्लभ राजयोग। जातक को महान प्रशासनिक, न्यायिक और संगठनात्मक शक्ति प्रदान करता है; विशाल संस्थानों व उद्यमों के संचालन में समर्थ।",
            "gu": "સૂર્ય (1), કેતુ (7) અને શનિ (8) નો દુર્લભ રાજયોગ. જાતકને ઉત્તમ વહીવટી, ન્યાયિક અને સંગઠનાત્મક શક્તિ આપે છે; વિશાળ સંસ્થાઓ ચલાવવામાં અજોડ નિપુણતા."
        }
    },
    "business_line": {
        "numbers": [9, 5, 4],
        "name": {"en": "Vyapar Samriddhi Enterprise & Commercial Line (9-5-4)", "hi": "व्यापार समृद्धि एवं वाणिज्य रेखा (9-5-4)", "gu": "વેપાર સમૃદ્ધિ અને વાણિજ્ય રેખા (9-5-4)"},
        "tag": {"en": "Vertical Line 3 (9-5-4)", "hi": "तृतीय ऊर्ध्वाधर रेखा (9-5-4)", "gu": "ત્રીજી ઊભી લાઇન (9-5-4)"},
        "desc": {
            "en": "Combines Mars's courage, Mercury's trading acumen, and Rahu's unconventional genius. Creates commercial empires, master negotiators, international trade tycoons, and tech innovators.",
            "hi": "मंगल का साहस, बुध की व्यापारिक समझ और राहु की क्रांतिकारी सोच। बड़े वाणिज्यिक साम्राज्य, अंतरराष्ट्रीय व्यापार और तकनीकी नवाचारों में अभूतपूर्व सफलता दिलाता है।",
            "gu": "મંગળનું સાહસ, બુધની વેપારી સૂઝ અને રાહુની અનોખી શોધક બુદ્ધિ. મોટા વેપાર, આંતરરાષ્ટ્રીય વ્યવસાય અને નવી ટેકનોલોજીમાં અઢળક નફો કરાવે છે."
        }
    },
    "combination_1_7": {
        "numbers": [1, 7],
        "name": {"en": "Surya-Ketu Raja Bhagyodaya Yog (Lucky Early Earning)", "hi": "सूर्य-केतु राज भाग्योदय योग (शीघ्र आजीविका एवं भाग्य वृद्धि)", "gu": "સૂર્ય-કેતુ રાજ ભાગ્યોદય યોગ (ઝડપી કારકિર્દી અને ભાગ્યોદય)"},
        "tag": {"en": "Pair 1-7 (Surya-Ketu)", "hi": "युगल 1-7 (सूर्य-केतु)", "gu": "જોડી 1-7 (સૂર્ય-કેતુ)"},
        "desc": {
            "en": "Both 1 and 7 are intrinsically lucky. Brings early employment/income in youth, prestigious government connections or civil stature, and steadfast loyalty in interpersonal relationships.",
            "hi": "अंक 1 और 7 दोनों अत्यंत भाग्यशाली हैं। जातक को अल्पायु में ही रोजगार/धनार्जन, सरकारी तंत्र से लाभ या उच्च प्रतिष्ठा, तथा प्रेम व संबंधों में गहरी वफादारी प्रदान करता है।",
            "gu": "અંક 1 અને 7 બંને અતિ ભાગ્યશાળી છે. જાતકને નાની ઉંમરે નોકરી/આવક, સરકારી લાભ કે મોભાદાર પદ અને સંબંધોમાં અડગ વફાદારી અપાવે છે."
        }
    },
    "combination_3_1": {
        "numbers": [3, 1],
        "name": {"en": "Guru-Surya Brahmavidya & Adhyaksh Yog (Authority & Honor)", "hi": "गुरु-सूर्य ब्रह्मविद्या एवं अध्यक्ष योग (सर्वोच्च सम्मान एवं सत्ता)", "gu": "ગુરુ-સૂર્ય બ્રહ્મવિદ્યા અને અધ્યક્ષ યોગ (સર્વોચ્ચ સન્માન અને સત્તા)"},
        "tag": {"en": "Pair 3-1 (Guru-Surya)", "hi": "युगल 3-1 (गुरु-सूर्य)", "gu": "જોડી 3-1 (ગુરુ-સૂર્ય)"},
        "desc": {
            "en": "Scholastic brilliance, higher academic degrees, and revered professional stature. The native earns enduring renown as an advisor, institutional director, consultant, or moral thought leader.",
            "hi": "उच्च शिक्षा, विद्वता और समाज में पूज्यनीय स्थान। जातक एक श्रेष्ठ सलाहकार, प्रशासनिक निर्देशक, प्राध्यापक अथवा नीतिवान मार्गदर्शक बनकर सर्वोच्च ख्याति प्राप्त करता है।",
            "gu": "ઉચ્ચ શિક્ષણ, પ્રખર જ્ઞાન અને સમાજમાં આદરણીય સ્થાન. જાતક ઉત્તમ સલાહકાર, ડિરેક્ટર, પ્રોફેસર કે માર્ગદર્શક બનીને દીર્ઘકાલીન યશ પ્રાપ્ત કરે છે."
        }
    },
    "combination_1_2": {
        "numbers": [1, 2],
        "name": {"en": "Surya-Chandra Rajyadhikari Yog (Executive & Political Rise)", "hi": "सूर्य-चंद्र राज्याधिकारी योग (प्रशासनिक एवं राजनीतिक उत्थान)", "gu": "સૂર્ય-ચંદ્ર રાજ્યાધિકારી યોગ (વહીવટી અને રાજકીય ઉત્થાન)"},
        "tag": {"en": "Pair 1-2 (Surya-Chandra)", "hi": "युगल 1-2 (सूर्य-चंद्र)", "gu": "જોડી 1-2 (સૂર્ય-ચંદ્ર)"},
        "desc": {
            "en": "Blends solar executive willpower with lunar emotional mass-appeal. Propels native into top management, political governance, or public leadership with substantial financial stature.",
            "hi": "सूर्य का दृढ़ संकल्प और चंद्र का जन-आकर्षण। जातक को उच्च प्रशासनिक पदों, राजनीतिक नेतृत्व या विशाल जनसमूह के संचालक के रूप में अपार सम्मान व वैभव दिलाता है।",
            "gu": "સૂર્યનો દ્રઢ સંકલ્પ અને ચંદ્રનું જન-આકર્ષણ. જાતકને સિનિયર મેનેજમેન્ટ, રાજકારણ કે જાહેર જીવનમાં મોખરાનું સ્થાન અને ઉત્તમ નાણાકીય મોભો આપે છે."
        }
    },
    "combination_9_5": {
        "numbers": [9, 5],
        "name": {"en": "Mangal-Budh Vyapar Ratna Yog (Street-Smart Commercial Acumen)", "hi": "मंगल-बुध व्यापार रत्न योग (कुशाग्र व्यापारिक प्रतिभा)", "gu": "મંગળ-બુધ વેપાર રત્ન યોગ (તીક્ષ્ણ વ્યાપારી સૂઝ)"},
        "tag": {"en": "Pair 9-5 (Mangal-Budh)", "hi": "युगल 9-5 (मंगल-बुध)", "gu": "જોડી 9-5 (મંગળ-બુધ)"},
        "desc": {
            "en": "Mars dramatically accelerates Mercury's mental speed. Generates razor-sharp street smartness, fast deal closures, lucrative commercial margins, and fearless business execution without loss.",
            "hi": "मंगल बुध की बौद्धिक गति को कई गुना बढ़ा देता है। जातक अत्यंत चतुर, व्यावहारिक, त्वरित सौदे करने वाला और व्यापार में कभी घाटा न खाने वाला सफल उद्यमी बनता है।",
            "gu": "મંગળ બુધની ગતિને અત્યંત ઝડપી બનાવે છે. જાતક વ્યવહારુ, સમયસૂચક, નફાકારક સોદા પાર પાડનાર અને વેપારમાં ક્યારેય નુકસાન ન કરનાર સફળ વેપારી બને છે."
        }
    },
    "combination_6_7": {
        "numbers": [6, 7],
        "name": {"en": "Shukra-Ketu Akarshan & Chamatkar Yog (Charisma & Sudden Luck)", "hi": "शुक्र-केतु आकर्षण एवं चमत्कार योग (सम्मोहन एवं आकस्मिक लाभ)", "gu": "શુક્ર-કેતુ આકર્ષણ અને ચમત્કાર યોગ (મોહકતા અને આકસ્મિક લાભ)"},
        "tag": {"en": "Pair 6-7 (Shukra-Ketu)", "hi": "युगल 6-7 (शुक्र-केतु)", "gu": "જોડી 6-7 (શુક્ર-કેતુ)"},
        "desc": {
            "en": "Magnetic romantic charisma, captivating artistic presence, passion for luxury and music, and sudden unexpected windfalls or strokes of fortune.",
            "hi": "सम्मोहक व्यक्तित्व, विपरीत लिंग के प्रति आकर्षण, संगीत व कला में गहरी रुचि और जीवन में अचानक धन लाभ व चमत्कारी भाग्योदय के योग बनाता है।",
            "gu": "આકર્ષક વ્યક્તિત્વ, કળા-સંગીતનો શોખ, રોમેન્ટિક સંબંધો અને જીવનમાં અણધાર્યા આર્થિક લાભ તથા ચમત્કારિક પ્રગતિના યોગ બનાવે છે."
        }
    },
    "combination_6_5": {
        "numbers": [6, 5],
        "name": {"en": "Lakshmi-Kuber Yog (Commercial Fortune & Wealth Magnetism)", "hi": "लक्ष्मी-कुबेर योग (अखंड धन एवं व्यापारिक ऐश्वर्य)", "gu": "લક્ષ્મી-કુબેર યોગ (અખંડ ધન અને વેપારી ઐશ્વર્ય)"},
        "tag": {"en": "Pair 6-5 (Budh-Shukra)", "hi": "युगल 6-5 (बुध-शुक्र)", "gu": "જોડી 6-5 (બુધ-શુક્ર)"},
        "desc": {
            "en": "Unites Lakshmi's luxury (6) with Mercury's trade acumen (5). Creates lucrative wealth inflows, retail expansion, glamorous brand enterprises, and enduring prosperity.",
            "hi": "शुक्र के विलासिता सुख और बुध की वाणिज्यिक समझ का मिलन। निरंतर धन प्रवाह, ब्रांडेड व्यवसाय, विपुल बचत और जीवन में समस्त भौतिक ऐश्वर्य प्रदान करता है।",
            "gu": "શુક્રના ભૌતિક સુખ અને બુધની વેપારી બુદ્ધિનો અદભુત યોગ. અવિરત ધનલાભ, બ્રાન્ડેડ બિઝનેસ, મબલક બચત અને સુખી સમૃદ્ધ જીવન આપે છે."
        }
    },
    "combination_6_2": {
        "numbers": [6, 2],
        "name": {"en": "Shukra-Chandra Kala Ratna Yog (Aesthetic & Media Acumen)", "hi": "शुक्र-चंद्र कला रत्न योग (सौंदर्य एवं मीडिया ख्याति)", "gu": "શુક્ર-ચંદ્ર કલા રત્ન યોગ (સૌંદર્ય અને મીડિયા ખ્યાતિ)"},
        "tag": {"en": "Pair 6-2 (Shukra-Chandra)", "hi": "युगल 6-2 (शुक्र-चंद्र)", "gu": "જોડી 6-2 (શુક્ર-ચંદ્ર)"},
        "desc": {
            "en": "Deep artistic sensitivity, glamorous creative flair, and emotional magnetism. Flourishes in media, cinema, culinary arts, fashion, and interpersonal PR.",
            "hi": "गहन कलात्मक संवेदनशीलता, आकर्षक छवि और रचनात्मक लालित्य। फिल्म, संगीत, जनसंपर्क, आतिथ्य और सौंदर्य प्रसाधनों के क्षेत्र में व्यापक ख्याति दिलाता है।",
            "gu": "ગહન કલાત્મક સંવેદના, આકર્ષક દેખાવ અને સર્જનાત્મકતા. ફિલ્મ, મીડિયા, સંગીત, પબ્લિક રિલેશન્સ અને ફેશનમાં ઉત્કૃષ્ટ સફળતા અપાવે છે."
        }
    },
    "combination_1_5": {
        "numbers": [1, 5],
        "name": {"en": "Surya-Budh Budhaditya Yog (Intellect & Oratory Excellence)", "hi": "सूर्य-बुध बुधादित्य योग (प्रखर बुद्धि एवं ओजस्वी वाणी)", "gu": "સૂર્ય-બુધ બુધાદિત્ય યોગ (પ્રખર બુદ્ધિ અને ઓજસ્વી વાણી)"},
        "tag": {"en": "Pair 1-5 (Surya-Budh)", "hi": "युगल 1-5 (सूर्य-बुध)", "gu": "જોડી 1-5 (સૂર્ય-બુધ)"},
        "desc": {
            "en": "Superior analytical intelligence, eloquence in speech, rapid problem-solving, and revered stature in commerce, publishing, law, or public administration.",
            "hi": "शास्त्रीय बुधादित्य योग। प्रखर तार्किक बुद्धि, ओजस्वी वक्ता, त्वरित निर्णय क्षमता और व्यापार, कानून या प्रशासनिक सेवाओं में उच्च आदर दिलाता है।",
            "gu": "શાસ્ત્રીય બુધાદિત્ય યોગ. તેજસ્વી બુદ્ધિ, સચોટ વક્તૃત્વ, ત્વરિત નિર્ણયશક્તિ અને વેપાર, કાયદો કે વહીવટી ક્ષેત્રે મોટો મોભો આપે છે."
        }
    },
    "combination_1_6": {
        "numbers": [1, 6],
        "name": {"en": "Surya-Shukra Vaibhav Yog (Royal Prosperity & Grandeur)", "hi": "सूर्य-शुक्र वैभव योग (राजसी ऐश्वर्य एवं भव्य जीवनशैली)", "gu": "સૂર્ય-શુક્ર વૈભવ યોગ (રાજસી ઐશ્વર્ય અને ભવ્ય જીવનશૈલી)"},
        "tag": {"en": "Pair 1-6 (Surya-Shukra)", "hi": "युगल 1-6 (सूर्य-शुक्र)", "gu": "જોડી 1-6 (સૂર્ય-શુક્ર)"},
        "desc": {
            "en": "Harmonizes solar authority with Venusian luxury. Bestows a regal standard of living, high social prestige, taste for fine luxuries, and executive magnetism.",
            "hi": "सूर्य के अधिकार और शुक्र की विलासिता का समन्वय। जातक को उच्च रहन-सहन, सामाजिक रुतबा, सुरुचिपूर्ण जीवनशैली और चुम्बकीय आकर्षण प्रदान करता है।",
            "gu": "સૂર્યના અધિકાર અને શુક્રના વૈભવનો સમન્વય. જાતકને શાહી જીવનશૈલી, સામાજિક મોભો, વૈભવી શોખ અને આકર્ષક નેતૃત્વ પ્રદાન કરે છે."
        }
    }
}

# Authentic Challenging Planetary Combinations & Doshas (With Root Causes & Concrete Remedial Mitigations)
INAUSPICIOUS_YOGAS_DEFINITIONS = {
    "bandhan_yog_94": {
        "numbers": [9, 4],
        "name": {"en": "Mars-Rahu Bandhan Dosha (Confinement, Court Litigation & Injury)", "hi": "मंगल-राहु बंधन दोष (न्यायालयीन विवाद, कारावास एवं स्वास्थ्य बंधन)", "gu": "મંગળ-રાહુ બંધન દોષ (કાનૂની અડચણો, કોર્ટ-કચેરી અને સ્વાસ્થ્ય બંધન)"},
        "tag": {"en": "Pair 9-4 (Missing 5) • Bandhan Dosha", "hi": "युगल 9-4 (अनुपस्थित 5) • बंधन दोष", "gu": "જોડી 9-4 (ગેરહાજર 5) • બંધન દોષ"},
        "desc": {
            "en": "Activated when 9 and 4 appear together with missing 5. Restricts native's freedom through legal disputes, sudden court litigation, police inquiries, hospitalization bed-rest, or reckless verbal outbursts. Note: Even fours (double 44) reduce the severity, enabling rapid bail or recovery, whereas double nines (99) aggravate anger and legal vulnerabilities.",
            "hi": "जब चक्र में 9 और 4 उपस्थित हों और 5 अनुपस्थित हो। यह जातक की स्वतंत्रता को बाधित करता है—मुकदमेबाजी, अदालती विवाद, अचानक अस्पताल में भर्ती होना, या अनियंत्रित वाणी से विवाद। विशेष: 4 की सम संख्या (44) होने पर प्रभाव घटता है तथा जमानत या स्वास्थ्य लाभ शीघ्र होता है, जबकि 99 होने पर उग्रता व संकट बढ़ते हैं।",
            "gu": "જ્યારે કુંડળીમાં 9 અને 4 હોય પણ 5 ગેરહાજર હોય. આ જાતકની સ્વતંત્રતા છીનવે છે—કોર્ટ-કચેરી, કાનૂની વિવાદ, અચાનક હોસ્પિટલના ખાટલે પડવું કે જીભ પર કાબૂ ન રહેવો. વિશેષ: જો બેવડો 4 (44) હોય તો અસર ઓછી થાય છે અને જામીન કે રિકવરી ઝડપી મળે છે, પણ બેવડો 9 (99) હોય તો ગુસ્સો અને જોખમ વધે છે."
        },
        "remedy": {
            "en": "Recite Hanuman Chalisa daily; chant Rahu Beej Mantra ('Om Bhram Bhreem Bhroum Sah Rahave Namah') 108 times on Wednesday/Saturday evenings; donate dark blankets to sweepers; keep a solid silver square plate in wallet; strictly avoid signing hasty legal guarantees.",
            "hi": "प्रतिदिन हनुमान चालीसा का पाठ करें; शनिवार व बुधवार शाम राहु बीज मंत्र ('ॐ भ्रां भ्रीं भ्रौं सः राहवे नमः') का 108 बार जप करें; सफाईकर्मियों को काले कंबल या तिल का दान करें; चांदी का ठोस चौकोर टुकड़ा जेब में रखें; बिना सोचे किसी की कानूनी जमानत न लें।",
            "gu": "દરરોજ હનુમાન ચાલીસાનો પાઠ કરવો; બુધવાર/શનિવારે સાંજે રાહુ બીજ મંત્ર ('ૐ ભ્રાં ભ્રીં ભ્રૌં સઃ રાહવે નમઃ') નો 108 વાર જાપ કરવો; સફાઈ કર્મચારીઓને ધાબળાનું દાન કરવું; પર્સમાં ચાંદીનો ચોરસ ટુકડો રાખવો; ઉતાવળે કોઈના જામીન ન બનવું."
        }
    },
    "bandhan_yog_54": {
        "numbers": [5, 4],
        "name": {"en": "Mercury-Rahu Bandhan Dosha (Contractual Traps & Health Confinement)", "hi": "बुध-राहु बंधन दोष (दस्तावेजी विवाद, धोखाधड़ी एवं स्वास्थ्य बाधा)", "gu": "બુધ-રાહુ બંધન દોષ (કરાર વિવાદ, છેતરપિંડી અને સ્વાસ્થ્ય અડચણ)"},
        "tag": {"en": "Pair 5-4 (Missing 9) • Bandhan Dosha", "hi": "युगल 5-4 (अनुपस्थित 9) • बंधन दोष", "gu": "જોડી 5-4 (ગેરહાજર 9) • બંધન દોષ"},
        "desc": {
            "en": "Activated when 5 and 4 combine with missing 9. Ties the native down through ambiguous contractual disputes, bureaucratic audit inquiries, audit penalties, or prolonged clinical bed-rest. Even fours (44) mitigate the affliction and ensure swift release.",
            "hi": "जब 5 और 4 एक साथ आएं और 9 न हो। यह अस्पष्ट अनुबंधों में फंसने, कानूनी ऑडिट नोटिसों, वित्तीय विवादों या लंबी बीमारी के कारण बेड-रेस्ट का योग बनाता है। 44 की उपस्थिति होने पर कानूनी राहत शीघ्र मिलती है।",
            "gu": "જ્યારે 5 અને 4 સાથે આવે અને 9 ગેરહાજર હોય. આ અસ્પષ્ટ કરારોમાં ફસાવું, ઓડિટ/કાનૂની નોટિસો આવવી કે બીમારીને લીધે લાંબો સમય પથારીવશ થવાનો યોગ બનાવે છે. બેવડા 4 (44) ની હાજરીથી રાહત ઝડપી મળે છે."
        },
        "remedy": {
            "en": "Feed green spinach/fodder to cows every Wednesday; chant 'Om Budhaya Namah' and 'Om Gan Ganapataye Namah' 108 times; get all legal and business agreements thoroughly audited by an advocate before signing.",
            "hi": "प्रत्येक बुधवार गाय को हरा चारा या पालक खिलाएं; 'ॐ बुधाय नमः' और 'ॐ गं गणपतये नमः' का 108 बार जप करें; किसी भी व्यावसायिक अनुबंध पर हस्ताक्षर करने से पहले कानूनी परामर्श अवश्य लें।",
            "gu": "દર બુધવારે ગાયને લીલું ઘાસ કે પાલક ખવડાવવી; 'ૐ બુધાય નમઃ' અને 'ૐ ગં ગણપતયે નમઃ' નો 108 વાર જાપ કરવો; કોઈપણ કરાર પર સહી કરતા પહેલા વકીલની સલાહ અચૂક લેવી."
        }
    },
    "apaman_yog_18": {
        "numbers": [1, 8],
        "name": {"en": "Sun-Saturn Apaman & Pitru Sangharsh Dosha (Public Insult & Ego Clash)", "hi": "सूर्य-शनि अपमान एवं पितृ संघर्ष दोष (सार्वजनिक तिरस्कार व मतभेद)", "gu": "સૂર્ય-શનિ અપમાન અને પિતૃ સંઘર્ષ દોષ (જાહેર અપમાન અને મતભેદ)"},
        "tag": {"en": "Pair 1-8 (Missing 7) • Apaman Dosha", "hi": "युगल 1-8 (अनुपस्थित 7) • अपमान दोष", "gu": "જોડી 1-8 (ગેરહાજર 7) • અપમાન દોષ"},
        "desc": {
            "en": "Activated when numbers 1 and 8 combine with missing 7. Sun (father) and Saturn (son) are planetary arch-rivals. Subjects native to unmerited insults, false accusations at workplace, friction with father or superiors, and delayed recognition.",
            "hi": "जब 1 और 8 उपस्थित हों और 7 न हो। सूर्य और शनि के परस्पर शत्रुता के कारण जातक को बिना कारण अपमान, कार्यस्थल पर झूठे आक्षेप, पिता से गंभीर वैचारिक मतभेद और अथक परिश्रम के बाद भी श्रेय न मिलने का दंश झेलना पड़ता है।",
            "gu": "જ્યારે 1 અને 8 હોય અને 7 ગેરહાજર હોય. સૂર્ય અને શનિના પરસ્પર વેરને કારણે જાતકને વગર વાંકે અપમાન, ઓફિસમાં ખોટા આક્ષેપ, પિતા સાથે વિખવાદ અને સખત મહેનત છતાં યશ ન મળવાની પીડા ભોગવવી પડે છે."
        },
        "remedy": {
            "en": "Offer Arghya (fresh water mixed with kumkum, red sandalwood, and red flowers in a copper vessel) to the rising Sun daily; touch father's feet every morning for blessings; recite Aditya Hridaya Stotram; strictly abstain from alcohol and leather products on Saturdays.",
            "hi": "नित्य प्रातः तांबे के लोटे में जल, कुमकुम व लाल पुष्प डालकर सूर्य देव को अर्घ्य दें; प्रतिदिन पिता के चरण स्पर्श कर आशीर्वाद लें; आदित्य हृदय स्तोत्र का पाठ करें; शनिवार को मदिरा व चमड़े की वस्तुओं से पूर्ण परहेज रखें।",
            "gu": "રોજ સવારે તાંબાના લોટામાં જળ, કંકુ અને લાલ ફૂલ પધરાવી સૂર્યનારાયણને અર્ઘ્ય આપવું; રોજ પિતાના ચરણસ્પર્શ કરી આશીર્વાદ લેવા; આદિત્ય હૃદય સ્તોત્રનો પાઠ કરવો; શનિવારે દારૂ કે ચામડાની વસ્તુઓથી દૂર રહેવું."
        }
    },
    "vish_yog_28": {
        "numbers": [2, 8],
        "name": {"en": "Moon-Saturn Vish Dosha (Depression, Emotional Toxicity & Melancholy)", "hi": "चंद्र-शनि विष दोष (मानसिक अवसाद, विषाद एवं भावनात्मक संताप)", "gu": "ચંદ્ર-શનિ વિષ દોષ (માનસિક તણાવ, ડિપ્રેશન અને ભાવનાત્મક પીડા)"},
        "tag": {"en": "Pair 2-8 (Missing 4) • Vish Dosha", "hi": "युगल 2-8 (अनुपस्थित 4) • विष दोष", "gu": "જોડી 2-8 (ગેરહાજર 4) • વિષ દોષ"},
        "desc": {
            "en": "Occurs when Moon (2) and Saturn (8) appear with missing 4. Creates heavy emotional toxicity, chronic depressive thoughts, anxiety loops, and delays in marital happiness. Native oscillates between superiority complex (if 1 or 9 present) or inferiority complex. Note: Situation stabilizes significantly with double eight (88).",
            "hi": "चंद्र (2) और शनि (8) का मिलन जब 4 अनुपस्थित हो। यह विष योग जातक को मानसिक अवसाद (डिप्रेशन), अकेलेपन की पीड़ा, निराशा और दांपत्य में नीरसता देता है। चार्ट में 1 या 9 होने पर सुपीरियरिटी कॉम्प्लेक्स अन्यथा हीनभावना रहती है। विशेष: 88 होने पर स्थिति संभलती है।",
            "gu": "ચંદ્ર (2) અને શનિ (8) નો યોગ જ્યારે 4 ગેરહાજર હોય. આ વિષ દોષ જાતકને ઊંડું ડિપ્રેશન, એકલતા, નિરાશા અને દાંપત્યજીવનમાં અશાંતિ આપે છે. કુંડળીમાં 1 કે 9 હોય તો અહંકાર અને ન હોય તો લઘુતાગ્રંથિ અનુભવાય છે. બેવડા 8 (88) થી સ્થિતિમાં ઘણો સુધારો થાય છે."
        },
        "remedy": {
            "en": "Perform Shiv Abhishekam with raw milk and water on Mondays; wear a natural 2-Mukhi Rudraksha capped in silver; immerse a silver square coin in running river water; strictly avoid wearing black or dark navy blue clothes on Mondays.",
            "hi": "प्रत्येक सोमवार शिवलिंग पर कच्चे दूध और जल से अभिषेक करें; चांदी में मढ़ा 2-मुखी रुद्राક્ષ धारण करें; बहते जल में एक चांदी का चौकोर सिक्का प्रवाहित करें; सोमवार को काले व गहरे नीले वस्त्र पहनने से बचें।",
            "gu": "દર સોમવારે શિવલિંગ પર કાચા દૂધ અને જળથી અભિષેક કરવો; ચાંદીમાં મઢાવેલો 2-મુખી રુદ્રાક્ષ ધારણ કરવો; વહેતા પાણીમાં ચાંદીનો ચોરસ સિક્કો પધરાવવો; સોમવારે કાળા કે ઘાટા વાદળી કપડાં ન પહેરવા."
        }
    },
    "hava_mahal_84": {
        "numbers": [8, 4],
        "name": {"en": "Saturn-Rahu Hava Mahal & Kasht Dosha (Air Castles, Speculation Losses & Accidents)", "hi": "शनि-राहु हवा महल एवं कष्ट दोष (काल्पनिक योजनाएं, सट्टे में हानि व दुर्घटना)", "gu": "શનિ-રાહુ હવા મહેલ અને કષ્ટ દોષ (હવાઈ કિલ્લા, સટ્ટામાં નુકસાન અને અકસ્માત)"},
        "tag": {"en": "Pair 8-4 (Missing 2) • Hava Mahal Dosha", "hi": "युगल 8-4 (अनुपस्थित 2) • हवा महल दोष", "gu": "જોડી 8-4 (ગેરહાજર 2) • હવા મહેલ દોષ"},
        "desc": {
            "en": "Triggered when 8 and 4 appear with missing 2. Induces tendency to build unrealistic castles in the air, falling into high-risk get-rich-quick speculative traps (crypto, intraday, lottery), physical accident-proneness, and turbulence in married life.",
            "hi": "जब 8 और 4 उपस्थित हों और 2 न हो। जातक हवाई योजनाएं बनाता है ('हवा महल'), बिना आधार के सट्टेबाजी या जोखिम भरे निवेश में धन गंवाता है। यह योग दुर्घटना प्रवणता और दांपत्य जीवन में कलह उत्पन्न करता है।",
            "gu": "જ્યારે 8 અને 4 હોય પણ 2 ગેરહાજર હોય. જાતક વ્યવહારિકતા ભૂલીને હવાઈ કિલ્લા બનાવે છે, સટ્ટો કે જોખમી સ્કીમોમાં મોટું નુકસાન કરે છે. આ યોગ અકસ્માતનો ભય અને દાંપત્યજીવનમાં તણાવ પેદા કરે છે."
        },
        "remedy": {
            "en": "Strictly refrain from speculative day-trading, gambling, or unverified schemes; worship Lord Bhairav or Hanuman; keep a solid silver square block at home; feed mustard-oil smeared rotis to black stray dogs on Saturdays.",
            "hi": "सट्टेबाजी, शेयर बाजार के इंट्राडे ट्रेडिंग व लॉटरी से पूर्ण दूरी बनाएं; श्री भैरव या हनुमान जी की आराधना करें; घर में चांदी की ठोस ईंट या गोली रखें; शनिवार शाम काले श्वान (कुत्ते) को सरसों के तेल से चुपड़ी रोटी खिलाएं।",
            "gu": "શેરબજારના સટ્ટા, ક્રિપ્ટો કે લૉટરીથી સંપૂર્ણ દૂર રહેવું; કાળભૈરવ કે હનુમાનજીની ઉપાસના કરવી; ઘરમાં ચાંદીની નાની ચોરસ લગડી રાખવી; શનિવારે કાળા કૂતરાને સરસવનું તેલ લગાડેલી રોટલી ખવડાવવી."
        }
    },
    "plastic_love_75": {
        "numbers": [7, 5],
        "name": {"en": "Ketu-Mercury Plastic Love & Maya Dosha (Superficial Romance & Betrayal)", "hi": "केतु-बुध प्लास्टिक प्रेम एवं माया दोष (दिखावटी आकर्षण व विछोह)", "gu": "કેતુ-બુધ પ્લાસ્ટિક લવ અને માયા દોષ (દેખાડાનો પ્રેમ અને વિશ્વાસઘાત)"},
        "tag": {"en": "Pair 7-5 (Missing 6) • Plastic Love Dosha", "hi": "युगल 7-5 (अनुपस्थित 6) • प्लास्टिक प्रेम दोष", "gu": "જોડી 7-5 (ગેરહાજર 6) • પ્લાસ્ટિક લવ દોષ"},
        "desc": {
            "en": "Occurs when 7 and 5 appear without 6. Fosters superficial romantic relations devoid of genuine emotional depth ('plastic love and plastic beauty'), heartbreaks, unstable commitments, and vulnerability to betrayal despite witty communication skills.",
            "hi": "जब 7 और 5 उपस्थित हों और 6 न हो। रिश्तों में भावनात्मक गहराई का अभाव रहता है जिसे 'प्लास्टिक प्रेम' कहा जाता है। दिखावटी आकर्षण, कई प्रेम संबंधों में भटकाव, विश्वासघात और वैवाहिक जीवन में असंतोष उत्पन्न होता है।",
            "gu": "જ્યારે 7 અને 5 હોય અને 6 ગેરહાજર હોય. સંબંધોમાં સાચા પ્રેમ અને લાગણીનો અભાવ રહે છે જેને 'પ્લાસ્ટિક લવ' કહે છે. બાહ્ય આકર્ષણ પાછળ અંજાવું, પ્રેમમાં દગો મળવો અને દાંપત્યજીવનમાં અસંતોષ ઊભો થાય છે."
        },
        "remedy": {
            "en": "Worship Lord Ganesha with 21 Durva grass shoots every Wednesday; chant 'Om Gan Ganapataye Namah'; offer green whole moong to wild birds; verify partner's emotional integrity and family background before making marriage commitments.",
            "hi": "प्रत्येक बुधवार भगवान श्री गणेश को 21 दूर्वा अर्पित करें; 'ॐ गं गणपतये नमः' का जप करें; पक्षियों को साबुत हरा मूंग डालें; वैवाहिक या प्रेम संबंधों में केवल बाहरी चमक पर न जाएं, आत्मिक सत्यता परखें।",
            "gu": "દર બુધવારે ગણપતિ બાપ્પાને 21 દૂર્વા અર્પણ કરવી; 'ૐ ગં ગણપતયે નમઃ' નો જાપ કરવો; પક્ષીઓને આખા મગ ચણવા; લગ્ન કે પ્રેમ સંબંધોમાં માત્ર દેખાવ પર ન જતા પારિવારિક સંસ્કારો ચકાસવા."
        }
    },
    "agni_sangharsh_19": {
        "numbers": [1, 9],
        "name": {"en": "Sun-Mars Agni Sangharsh Dosha (Fiery Temper, Impatience & Collision)", "hi": "सूर्य-मंगल अग्नि संघर्ष दोष (उग्र क्रोध, अधीरता एवं टकराव)", "gu": "સૂર્ય-મંગળ અગ્નિ સંઘર્ષ દોષ (તીવ્ર ક્રોધ, અધીરાઈ અને ટકરાવ)"},
        "tag": {"en": "Pair 1-9 (Missing 3) • Agni Dosha", "hi": "युगल 1-9 (अनुपस्थित 3) • અગ્નિ દોષ", "gu": "જોડી 1-9 (ગેરહાજર 3) • અગ્નિ દોષ"},
        "desc": {
            "en": "Both Sun and Mars are extremely hot fiery planets. When present without Jupiter (3)'s stabilizing wisdom, native suffers from persistent anger, burning impatience, friction with teammates, and blood pressure fluctuations despite brilliant surgical/technical intellect.",
            "hi": "सूर्य और मंगल दोनों अग्नि तत्व के अत्यंत उष्ण ग्रह हैं। गुरु (3) के अभाव में यह उग्र क्रोध, अत्यधिक जल्दबाजी, साथियों से टकराव और रक्तचाप संबंधी परेशानियां देता है, यद्यपि यह तकनीकी व शल्य चिकित्सा में सफलता भी दिलाता है।",
            "gu": "સૂર્ય અને મંગળ બંને અતિશય ગરમ અગ્નિતત્વના ગ્રહો છે. ગુરુ (3) ના નિયંત્રણ વગર આ ક્રોધ, અધીરાઈ, સાથીદારો સાથે ઝઘડા અને બ્લડ પ્રેશરની તકલીફ આપે છે, જોકે સર્જરી કે ટેકનિકલ ક્ષેત્રે સફળતા પણ અપાવે છે."
        },
        "remedy": {
            "en": "Drink water stored overnight in a silver glass; practice 10 minutes of Anulom-Vilom and Sheetali Pranayama daily; avoid excessively hot and spicy foods; cultivate a 5-second pause before responding in anger.",
            "hi": "चांदी के गिलास में रखा जल पिएं; प्रतिदिन 10 मिनट अनुलोम-विलोम व शीतली प्राणायाम करें; अत्यधिक तीखे-मसालेदार भोजन से बचें; क्रोध आने पर तुरंत प्रतिक्रिया देने के बजाय 5 सेकंड का मौन रखें।",
            "gu": "ચાંદીના પ્યાલામાં રાખેલું પાણી પીવું; દરરોજ 10 મિનિટ અનુલોમ-વિલોમ અને શીતળી પ્રાણાયામ કરવા; વધુ પડતો તીખો-મસાલેદાર ખોરાક ટાળવો; ક્રોધ આવે ત્યારે 5 સેકન્ડ શાંત રહેવાની ટેવ પાડવી."
        }
    },
    "kalaha_yog_66_2": {
        "numbers": [6, 2],
        "name": {"en": "Shukra-Chandra Kalaha Dosha (Domestic Discord, Foul Speech & Marital Disputes)", "hi": "शुक्र-चंद्र कलह दोष (घरेलू विवाद, कटु वाणी एवं दांपत्य क्लेश)", "gu": "શુક્ર-ચંદ્ર કલહ દોષ (ઘરેલું કંકાસ, કડવી વાણી અને દાંપત્ય ક્લેશ)"},
        "tag": {"en": "Double 6 with Single 2 • Kalaha Dosha", "hi": "दोहरा 6 एवं 2 • कलह दोष", "gu": "બેવડો 6 અને 2 • કલહ દોષ"},
        "desc": {
            "en": "Activated when double six (66) combines with single two (2). Triggers frequent domestic quarrels, foul/abusive language during anger, instigating fights with opposite sex, and persistent friction with spouse.",
            "hi": "जब चक्र में दो बार 6 (66) और एक बार 2 हो। यह व्यक्ति को गुस्सैल, कटुभाषी, बात-बात पर गाली-गलौज या अपशब्द बोलने वाला और जीवनसाथी या स्त्रियों से बार-बार कलह करने वाला बना देता है।",
            "gu": "જ્યારે કુંડળીમાં બે વાર 6 (66) અને એક વાર 2 હોય. આ વ્યક્તિને વાતવાતમાં ઉશ્કેરાઈ જનાર, અપશબ્દો બોલનાર અને જીવનસાથી કે સ્ત્રીઓ સાથે વારંવાર ઝઘડા ઊભા કરનાર બનાવે છે."
        },
        "remedy": {
            "en": "Offer white sweets (Rasgulla or Kheer) to young girls on Fridays; wear a natural South Sea pearl in silver on the little finger; place a natural camphor lamp in the bedroom for marital peace; strictly avoid using expletives.",
            "hi": "शुक्रवार को कन्याओं को सफेद मिठाई (रसगुल्ला या खीर) खिलाएं; कनिष्ठिका अंगुली में चांदी में मोती धारण करें; शयनकक्ष में प्राकृतिक कपूर का डिफ्यूज़र जलाएं; अपशब्दों के प्रयोग से पूरी तरह बचें।",
            "gu": "શુક્રવારે નાની કન્યાઓને સફેદ મીઠાઈ (રસગુલ્લા કે ખીર) આપવી; ટચલી આંગળીમાં ચાંદીમાં મોતી ધારણ કરવું; બેડરૂમમાં કપૂરનો દીવો પ્રગટાવવો; અપશબ્દો બોલવાની ટેવ સદંતર બંધ કરવી."
        }
    },
    "slow_mind_99_5": {
        "numbers": [9, 5],
        "name": {"en": "Mangal-Budh Mati-Bhram Dosha (Mental Sluggishness, Confusion & Indecision)", "hi": "मंगल-बुध मतिभ्रम दोष (मंद बुद्धि, भ्रम एवं निर्णयहीनता)", "gu": "મંગળ-બુધ મતિભ્રમ દોષ (મનની મંદ ગતિ, મૂંઝવણ અને અનિર્ણાયકતા)"},
        "tag": {"en": "Double 9 with Single 5 (Missing 4) • Mati-Bhram", "hi": "दोहरा 9 एवं 5 (अनुपस्थित 4) • मतिभ्रम दोष", "gu": "બેવડો 9 અને 5 (ગેરહાજર 4) • મતિભ્રમ દોષ"},
        "desc": {
            "en": "Activated when double nine (99) combines with single five (5) with missing 4. Mars's excessive heat overpowers Mercury, drastically slowing mental processing speed; causes chronic confusion, poor study retention, and trade hesitation.",
            "hi": "जब दो बार 9 (99) और एक 5 उपस्थित हों तथा 4 न हो। मंगल का अत्यधिक प्रभाव बुध की गति को दबा देता है जिससे जातक भ्रमित रहता है, दिमाग धीमा काम करता है और पढ़ाई व व्यापारिक निर्णय लेने में कठिनाई होती है।",
            "gu": "જ્યારે બે વાર 9 (99) અને એક 5 હોય તથા 4 ગેરહાજર હોય. મંગળનો અતિ પ્રભાવ બુધને દબાવી દે છે જેથી મગજ ધીમું ચાલે છે, સતત મૂંઝવણ રહે છે અને અભ્યાસ કે વેપારના નિર્ણયોમાં મુશ્કેલી પડે છે."
        },
        "remedy": {
            "en": "Chant Saraswati Beej Mantra ('Om Aim Saraswatyai Namah') 108 times daily; consume 5 soaked almonds in the morning; wear an energized Budh Yantra in bronze; avoid multi-tasking under time pressure.",
            "hi": "प्रतिदिन सरस्वती बीज मंत्र ('ॐ ऐं सरस्वत्यै नमः') का 108 बार जप करें; प्रातःकाल 5 भीगे हुए बादाम खाएं; कांसे में प्राण-प्रतिष्ठित बुध यंत्र धारण करें; एक समय में एक ही कार्य पर ध्यान केंद्रित करें।",
            "gu": "દરરોજ સરસ્વતી બીજ મંત્ર ('ૐ ઐં સરસ્વત્યૈ નમઃ') નો 108 વાર જાપ કરવો; સવારે 5 પલાળેલી બદામ ખાવી; કાંસામાં પ્રાણપ્રતિષ્ઠિત બુધ યંત્ર ધારણ કરવું; એક સમયે એક જ કામ પર ધ્યાન આપવું."
        }
    },
    "chaturya_fraud_55_9": {
        "numbers": [5, 9],
        "name": {"en": "Hyper-Mercury Ati-Chaturya Dosha (Scheming Mind, Deception & Audit Risk)", "hi": "अति-चातुर्य एवं छल दोष (अति-चालाकी, धोखाधड़ी व वित्तीय जांच का जोखिम)", "gu": "અતિ-ચાતુર્ય અને કપટ દોષ (વધુ પડતી ચાલાકી, છેતરપિંડી અને કાનૂની તપાસનું જોખમ)"},
        "tag": {"en": "Multiple 5s with Mars (Missing 4) • Ati-Chaturya", "hi": "अनेक 5 एवं 9 (अनुपस्थित 4) • अति-चातुर्य दोष", "gu": "એકથી વધુ 5 અને 9 (ગેરહાજર 4) • અતિ-ચાતુર્ય દોષ"},
        "desc": {
            "en": "Activated when multiple 5s (55 or 555) combine with Mars (9) with missing 4. Generates an over-scheming, hyper-cunning intellect ('Iski topi uske sar') that is tempted to cut ethical corners, risking major financial fraud investigations, tax audits, or sudden insolvency.",
            "hi": "जब चार्ट में 55 या 555 के साथ 9 हो और 4 अनुपस्थित हो। दिमाग इतना अधिक सक्रिय और धूर्त हो जाता है कि जातक शॉर्टकट या अनैतिक तरीकों ('इसकी टोपी उसके सर') से धन कमाने की फिराक में रहता है, जिससे भारी कानूनी ऑडिट या धोखेबाजी का शिकार होने का खतरा रहता है।",
            "gu": "જ્યારે કુંડળીમાં 55 કે 555 સાથે 9 હોય અને 4 ન હોય. મગજ અતિશય ચતુર બની જાય છે અને અનૈતિક શોર્ટકટ ('આની ટોપી તેના માથે') વાપરવાની લાલચ જાગે છે, જેથી ઇન્કમટેક્સ ઓડિટ કે છેતરપિંડીના ગંભીર કેસમાં ફસાવાનું જોખમ રહે છે."
        },
        "remedy": {
            "en": "Practice uncompromising integrity in accounting and taxation; chant Vishnu Sahasranama every Wednesday; feed green grass to cows; consult certified financial advisors before finalizing aggressive leveraged investments.",
            "hi": "खातों व टैक्स में पूर्ण ईमानदारी और पारदर्शिता बरतें; प्रत्येक बुधवार विष्णु सहस्रनाम का पाठ करें; गाय को हरा चारा खिलाएं; अत्यधिक जोखिम भरे सट्टे या अनैतिक सौदों से पूरी तरह दूर रहें।",
            "gu": "હિસાબ-કિતાબ અને ટેક્સમાં સંપૂર્ણ પ્રમાણિકતા રાખવી; દર બુધવારે વિષ્ણુ સહસ્રનામનો પાઠ કરવો; ગાયને લીલું ઘાસ ખવડાવવું; વધુ પડતા જોખમી સોદા કે અયોગ્ય રસ્તાઓથી દૂર રહેવું."
        }
    },
    "turbulence_plane_284": {
        "numbers": [2, 8, 4],
        "name": {"en": "Chandra-Shani-Rahu Action Plane (Extreme Karmic Ups & Downs)", "hi": "चंद्र-शनि-राहु कर्म तल (अत्यधिक उतार-चढ़ाव एवं बेलगाम वाणी)", "gu": "ચંદ્ર-શનિ-રાહુ કર્મ તલ (અતિશય ઉતાર-ચઢાવ અને અંકુશહીન વાણી)"},
        "tag": {"en": "Horizontal Line 3 (2-8-4) • Turbulence Axis", "hi": "तृतीय क्षैतिज रेखा (2-8-4) • कर्म उथल-पुथल", "gu": "ત્રીજી આડી લાઇન (2-8-4) • કર્મ ઉતાર-ચઢાવ"},
        "desc": {
            "en": "Occurs when 2, 8, and 4 assemble across the Action Plane. Native witnesses roller-coaster fortunes—soaring to great heights only to face sudden crashes. Speech can become completely unfiltered ('speaking whatever, whenever, wherever'), and married life is frequently troubled. Note: Even numbers of 4 (44) or 8 (88) significantly stabilize this volatility.",
            "hi": "जब 2, 8 और 4 तीनों उपस्थित हों। जातक के जीवन में तीव्र उतार-चढ़ाव आते हैं—ऊंचे उठते हैं और अचानक गिरते भी हैं। बिना सोचे-समझे कहीं भी कुछ भी बोल देने की आदत ('व्हाटएवर, व्हेनेवर, व्हेयरएवर') और वैवाहिक जीवन में असंतोष रहता है। 44 या 88 होने पर यह दोष काफी हद तक शांत होता है।",
            "gu": "જ્યારે 2, 8 અને 4 ત્રણેય હાજર હોય. જીવનમાં તીવ્ર ઉતાર-ચઢાવ આવે છે—ખૂબ ઊંચે પહોંચે અને અચાનક નીચે પડે. ગમે ત્યાં ગમે તે બોલી દેવાની ટેવ અને દાંપત્યજીવનમાં અશાંતિ રહે છે. જો બેવડો 4 (44) કે 8 (88) હોય તો આ દોષ ઘણો શાંત થાય છે."
        },
        "remedy": {
            "en": "Keep a solid pure silver coin gifted by mother always in possession; chant Maha Mrityunjaya Mantra 11 times daily; consciously cultivate disciplined silence in heated arguments; support physically challenged individuals on Saturdays.",
            "hi": "माता से आशीर्वाद स्वरूप प्राप्त चांदी का ठोस सिक्का सदैव अपने पास रखें; नित्य 11 बार महामृत्युंजय मंत्र का जप करें; आवेश में मौन रहने का अभ्यास करें; शनिवार को दिव्यांग जनों की सेवा व सहायता करें।",
            "gu": "માતા પાસેથી આશીર્વાદરૂપે મેળવેલો ચાંદીનો સિક્કો હંમેશા પાસે રાખવો; રોજ 11 વાર મહામૃત્યુંજય મંત્રનો જાપ કરવો; આવેશમાં મૌન રહેવાની ટેવ પાડવી; શનિવારે દિવ્યાંગ વ્યક્તિઓની સેવા કરવી."
        }
    }
}

# Consolidated Yogas Registry for System Compatibility
YOGA_DEFINITIONS = {**AUSPICIOUS_YOGAS_DEFINITIONS, **INAUSPICIOUS_YOGAS_DEFINITIONS}

PROFESSIONS_INFO = {
    1: {
        "en": "Government Services, Administration, CEO/Director, Politics, Defense Leadership, Gold/Jewelry, Solar Energy, Entrepreneurship.",
        "hi": "प्रशासनिक सेवाएं (IAS/IPS), सरकारी नौकरी, कंपनी निदेशक/सीईओ, राजनीति, सेना/पुलिस नेतृत्व, स्वर्ण व्यापार, सौर ऊर्जा, स्वतंत्र व्यवसाय।",
        "gu": "સરકારી વહીવટી સેવાઓ, કંપની ડાયરેક્ટર/CEO, રાજકારણ, સંરક્ષણ દળો, સોના-ઝવેરાતનો વેપાર, સોલાર એનર્જી, સ્વતંત્ર વેપાર."
    },
    2: {
        "en": "Hospitality, Dairy/Liquids, Tourism, Creative Writing, Nursing/Medicine, Public Relations, Psychology, Import-Export via sea.",
        "hi": "होटल व खानपान, दुग्ध व तरल पदार्थ, पर्यटन, ललित कला व लेखन, चिकित्सा/नर्सिंग, जनसंपर्क, मनोविज्ञान, जलमार्ग द्वारा आयात-निर्यात।",
        "gu": "હોટેલ અને હોસ્પિટાલિટી, ડેરી અને પ્રવાહી વેપાર, પ્રવાસન, કલા-સાહિત્ય, નર્સિંગ/દવાઓ, જનસંપર્ક, મનોવિજ્ઞાન, જળમાર્ગે આયાત-નિકાસ."
    },
    3: {
        "en": "Teaching, Education, Law/Judiciary, Vedic Sciences/Astrology, Banking/Finance, Publishing, Spiritual Counseling, Advisory Roles.",
        "hi": "अध्यापन, शिक्षा संस्थान, वकालत/न्यायालय, वैदिक ज्योतिष व दर्शन, बैंकिंग व वित्त, पुस्तक प्रकाशन, आध्यात्मिक मार्गदर्शन, उच्च सलाहकार।",
        "gu": "શિક્ષણ અને પ્રોફેસર, કાયદો અને ન્યાયતંત્ર, જ્યોતિષ અને શાસ્ત્રો, બેંકિંગ અને ફાઇનાન્સ, પ્રકાશન, આધ્યાત્મિક માર્ગદર્શન, સલાહકાર."
    },
    4: {
        "en": "Information Technology, Software/AI, Architecture, Heavy Engineering, Stock Market Analytics, Contracting, Forensics, Electronics.",
        "hi": "सूचना प्रौद्योगिकी (IT/AI), सॉफ्टवेयर, वास्तुकला, भारी इंजीनियरिंग, शेयर बाजार विश्लेषण, ठेकेदारी, फोरेंसिक जांच, इलेक्ट्रॉनिक्स।",
        "gu": "ઇન્ફોર્મેશન ટેકનોલોજી, સોફ્ટવેર/AI, આર્કિટેક્ચર, હેવી એન્જિનિયરિંગ, શેરબજાર એનાલિટિક્સ, કોન્ટ્રાક્ટિંગ, ઇલેક્ટ્રોનિક્સ."
    },
    5: {
        "en": "Commerce, Trading, Media/Journalism, Stock Broking, Marketing & Sales, Public Speaking, Logistics, Telecommunications, Event Management.",
        "hi": "वाणिज्य व व्यापार, पत्रकारिता व मीडिया, शेयर ब्रोकिंग, विपणन (मार्केटिंग) व सेल्स, संचार माध्यम, रसद (लॉजिस्टिक्स), इवेंट मैनेजमेंट।",
        "gu": "વાણિજ્ય અને વેપાર, પત્રકારત્વ અને મીડિયા, શેર બ્રોકિંગ, માર્કેટિંગ અને સેલ્સ, કમ્યુનિકેશન, લોજિસ્ટિક્સ, ઇવેન્ટ મેનેજમેન્ટ."
    },
    6: {
        "en": "Luxury Goods, Fashion/Apparel, Interior Design, Film/Media/Entertainment, Automobile Dealership, Cosmetics, Luxury Hospitality, Jewelry.",
        "hi": "लक्जरी वस्तुएं, फैशन व वस्त्र, इंटीरियर डिजाइन, सिनेमा व मनोरंजन, ऑटोमोबाइल डीलरशिप, सौंदर्य प्रसाधन, पांच सितारा होटल, आभूषण।",
        "gu": "વૈભવી સાધનો, ફેશન અને કાપડ ઉદ્યોગ, ઇન્ટિરિયર ડિઝાઇન, ફિલ્મ અને મનોરંજન, ઓટોમોબાઇલ શોરૂમ, કોસ્મેટિક્સ, લક્ઝરી હોટેલ્સ, ઝવેરાત."
    },
    7: {
        "en": "Scientific Research, Occult Sciences/Astrology, Cyber Security, Software Coding, Pharmaceuticals, Philosophical Writing, Foreign Missions.",
        "hi": "वैज्ञानिक अनुसंधान, गूढ़ ज्ञान व ज्योतिष, साइबर सुरक्षा, सॉफ्टवेयर कोडिंग, औषधि निर्माण (फार्मा), दार्शनिक लेखन, विदेशी मिशन व कूटनीति।",
        "gu": "વૈજ્ઞાનિક સંશોધન, જ્યોતિષ અને ગૂઢ વિજ્ઞાન, સાયબર સિક્યોરિટી, સોફ્ટવેર ડેવલપમેન્ટ, ફાર્માસ્યુટિકલ્સ, ફિલોસોફી, વિદેશી સેવાઓ."
    },
    8: {
        "en": "Real Estate & Construction, Heavy Industry, Steel/Mining, Oil & Gas, Judiciary & Law, Labor Unions, Civil Engineering, Agriculture Machinery.",
        "hi": "रियल एस्टेट व निर्माण कार्य, भारी उद्योग, लोहा व इस्पात, खनन, तेल व गैस, न्यायालय व न्यायपालिका, श्रम संगठन, सिविल इंजीनियरिंग।",
        "gu": "રિયલ એસ્ટેટ અને બાંધકામ, હેવી ઇન્ડસ્ટ્રી, લોખંડ અને સ્ટીલ, ખાણ ઉદ્યોગ, ઓઇલ અને ગેસ, ન્યાયતંત્ર અને કાયદો, સિવિલ એન્જિનિયરિંગ."
    },
    9: {
        "en": "Defense/Army/Police, Surgery/Medicine, Sports, Real Estate Development, Mechanical Engineering, Fire & Safety, Pharmacy, Civil Construction.",
        "hi": "सेना व पुलिस, शल्य चिकित्सा (सर्जरी), खेलकूद, भूमि विकास, मैकेनिकल इंजीनियरिंग, अग्नि व सुरक्षा सेवाएं, फार्मेसी, ढांचागत निर्माण।",
        "gu": "સંરક્ષણ/આર્મી/પોલીસ, સર્જરી અને દવાઓ, રમતગમત, જમીન ડેવલપમેન્ટ, મિકેનિકલ એન્જિનિયરિંગ, ફાયર અને સેફ્ટી, બાંધકામ ક્ષેત્ર."
    }
}

# Number Specific Detailed Remedies (from Level 2 & Astrology Club)
NUMBER_REMEDIES = {
    1: {
        "gem": {
            "en": "Wear Natural Ruby (Manikya) 3.5 to 5.25 Ratti in Gold or Copper on the Ring finger on Sunday morning at sunrise.",
            "hi": "रविवार प्रातः सूर्योदय के समय सोने या तांबे में 3.5 से 5.25 रत्ती का प्राकृतिक माणिक्य अनामिका (रिंग फिंगर) में धारण करें।",
            "gu": "રવિવારે સૂર્યોદય સમયે સોના કે તાંબામાં 3.5 થી 5.25 રત્તીનું શુદ્ધ માણેક અનામિકા (રિંગ ફિંગર) આંગળીમાં ધારણ કરવું."
        },
        "crystal": {"en": "Red Jasper or Sunstone", "hi": "रेड जैस्पर या सनस्टोन", "gu": "રેડ જાસ્પર અથવા સનસ્ટોન"},
        "mantra": {
            "en": "Om Hram Hreem Hroum Sah Suryaya Namah (108 times at sunrise) or Gayatri Mantra.",
            "hi": "ॐ ह्रां ह्रीं ह्रौं सः सूर्याय नमः (प्रातः सूर्योदय पर 108 बार) अथवा गायत्री मंत्र का नित्य जप।",
            "gu": "ૐ હ્રાં હ્રીં હ્રૌં સઃ સૂર્યાય નમઃ (સવારે સૂર્યોદય સમયે 108 વાર) અથવા ગાયત્રી મંત્રનો નિત્ય જાપ."
        },
        "fasting": {"en": "Sunday. Consume wheat rotis or sweet milk dishes without salt.", "hi": "रविवार का व्रत। बिना नमक का गेहूं का भोजन या मीठा दूध-रोटी ग्रहण करें।", "gu": "રવિવારનું વ્રત. મીઠા (નમક) વગરનો ઘઉંનો ખોરાક અથવા મીઠી રોટલી લેવી."},
        "donation": {
            "en": "Donate wheat, jaggery (gur), copper utensils, red sandalwood, or red cloth to a needy temple priest on Sunday.",
            "hi": "रविवार के दिन गेहूं, गुड़, तांबे के पात्र, लाल चंदन या लाल वस्त्र जरूरतमंद या ब्राह्मण को दान करें।",
            "gu": "રવિવારે ઘઉં, ગોળ, તાંબાનું વાસણ, લાલ ચંદન કે લાલ વસ્ત્ર જરૂરિયાતમંદ કે બ્રાહ્મણને દાન કરવું."
        },
        "seva": {
            "en": "Offer Arghya (fresh water with kumkum and red flowers in a copper vessel) to the rising Sun daily. Respect father and elders.",
            "hi": "प्रतिदिन तांबे के लोटे में रोली व लाल पुष्प डालकर उगते सूर्य को अर्घ्य दें। पिता एवं वरिष्ठों का चरण स्पर्श कर आशीर्वाद लें।",
            "gu": "દરરોજ તાંબાના કળશમાં કંકુ અને લાલ ફૂલ પધરાવીને ઊગતા સૂર્યનારાયણને જળ અર્પણ કરવું. પિતા અને વડીલોના આશીર્વાદ લેવા."
        }
    },
    2: {
        "gem": {
            "en": "Wear Natural Basra Pearl (Moti) or South Sea Pearl 4 to 6 Ratti in Silver on the Little finger on Monday evening.",
            "hi": "सोमवार संध्या समय चांदी की अंगूठी में 4 से 6 रत्ती का प्राकृतिक सच्चा मोती कनिष्ठिका (छोटी उंगली) में धारण करें।",
            "gu": "સોમવારે સાંજે ચાંદીની વીંટીમાં 4 થી 6 રત્તીનું સાચું મોતી ટચલી આંગળી (કનિષ્ઠિકા)માં ધારણ કરવું."
        },
        "crystal": {"en": "Moonstone or Selenite", "hi": "मूनस्टोन या सेलेनाइट", "gu": "મૂનસ્ટોન અથવા સેલેનાઇટ"},
        "mantra": {
            "en": "Om Shram Shreem Shroum Sah Chandramase Namah (108 times in evening).",
            "hi": "ॐ श्रां श्रीं श्रौं सः चंद्रमसे नमः (संध्या समय 108 बार जप)।",
            "gu": "ૐ શ્રાં શ્રીં શ્રૌં સઃ ચંદ્રમસે નમઃ (સાંજના સમયે 108 વાર જાપ)."
        },
        "fasting": {"en": "Monday. Drink pure milk and water; avoid heavy salt or sour foods.", "hi": "सोमवार का व्रत। दूध और जल का सेवन करें; खट्टे खाद्य पदार्थों से परहेज करें।", "gu": "સોમવારનું વ્રત. દૂધ અને સાત્વિક આહાર લેવો; ખાટી ચીજોથી દૂર રહેવું."},
        "donation": {
            "en": "Donate white rice, milk, silver, white sweets (kheer), or white clothes to elderly women or girls on Monday.",
            "hi": "सोमवार को सफेद चावल, दूध, चांदी, खीर या सफेद वस्त्र वृद्ध महिलाओं या कन्याओं को दान करें।",
            "gu": "સોમવારે સફેદ ચોખા, દૂધ, ચાંદી, ખીર કે સફેદ વસ્ત્રો વૃદ્ધ સ્ત્રીઓ અથવા કન્યાઓને દાન કરવા."
        },
        "seva": {
            "en": "Touch mother's feet daily for lifelong peace. Drink drinking water regularly from a pure silver glass.",
            "hi": "माता के चरण स्पर्श कर नित्य आशीर्वाद प्राप्त करें। शुद्ध चांदी के गिलास से नित्य जल पीने का नियम बनाएं।",
            "gu": "માતાના ચરણસ્પર્શ કરી રોજેરોજ આશીર્વાદ મેળવવા. નિયમિત ચાંદીના ગ્લાસમાં જળ પીવાનો નિયમ રાખવો."
        }
    },
    3: {
        "gem": {
            "en": "Wear Natural Yellow Sapphire (Pukhraj) 3.25 to 5.25 Ratti in Gold or Brass on the Index finger on Thursday morning.",
            "hi": "गुरुवार प्रातः सोने या अष्टधातु में 3.25 से 5.25 रत्ती का प्राकृतिक पीला पुखराज तर्जनी (इंडेक्स फिंगर) में धारण करें।",
            "gu": "ગુરુવારે સવારે સોના કે પંચધાતુમાં 3.25 થી 5.25 રત્તીનો કુદરતી પીળો પોખરાજ તર્જની (પહેલી આંગળી)માં ધારણ કરવો."
        },
        "crystal": {"en": "Citrine or Yellow Topaz", "hi": "सिट्रीन या पीला पुखराज विकल्प", "gu": "સિટ્રીન અથવા પીળો પોખરાજ"},
        "mantra": {
            "en": "Om Gram Greem Groum Sah Gurave Namah (108 times on Thursday morning).",
            "hi": "ॐ ग्रां ग्रीं ग्रौं सः गुरवे नमः (गुरुवार प्रातः 108 बार जप)।",
            "gu": "ૐ ગ્રાં ગ્રીં ગ્રૌં સઃ ગુરવે નમઃ (ગુરુવારે સવારે 108 વાર જાપ)."
        },
        "fasting": {"en": "Thursday. Wear yellow garments; do not wash hair or cut nails on this day.", "hi": "गुरुवार का व्रत। पीले वस्त्र धारण करें; इस दिन बाल धोना व नाखून काटना वर्जित रखें।", "gu": "ગુરુવારનું વ્રત. પીળા વસ્ત્રો પહેરવા; આ દિવસે માથું ધોવું કે નખ કાપવા નહીં."},
        "donation": {
            "en": "Donate chana dal, turmeric, yellow sweets (laddoo), yellow bananas, or religious scripture books on Thursday.",
            "hi": "गुरुवार को चना दाल, हल्दी की गांठें, बेसन के लड्डू, केले अथवा धार्मिक पुस्तकें मंदिर या गुरु को दान करें।",
            "gu": "ગુરુવારે ચણાની દાળ, હળદર, બેસનના લાડુ, કેળાં કે ધાર્મિક પુસ્તકો મંદિર કે ગુરુજનને દાન કરવા."
        },
        "seva": {
            "en": "Serve mentors and teachers. Offer water and light a mustard oil or ghee lamp near a Peepal or Banana tree on Thursday.",
            "hi": "गुरुजनों व शिक्षकों का सम्मान करें। गुरुवार को केले या पीपल के वृक्ष को जल अर्पित कर दीपक प्रज्वलित करें।",
            "gu": "ગુરુજનો અને શિક્ષકોની સેવા કરવી. ગુરુવારે કેળના કે પીપળાના વૃક્ષને જળ ચડાવીને દીવો પ્રગટાવવો."
        }
    },
    4: {
        "gem": {
            "en": "Wear Natural Ceylon Hessonite (Gomed) 5 to 7.25 Ratti in Silver or Panchdhatu on the Middle finger on Saturday evening.",
            "hi": "शनिवार संध्या समय चांदी या पंचधातु में 5 से 7.25 रत्ती का शुद्ध गोमेद मध्यमा (बीच की उंगली) में धारण करें।",
            "gu": "શનિવારે સાંજે ચાંદી કે પંચધાતુમાં 5 થી 7.25 રત્તીનો શુદ્ધ ગોમેદ વચલી આંગળી (મધ્યમા)માં ધારણ કરવો."
        },
        "crystal": {"en": "Hessonite or Smoky Quartz", "hi": "गोमेद या स्मोकी क्वार्ट्ज", "gu": "ગોમેદ અથવા સ્મોકી ક્વાર્ટ્ઝ"},
        "mantra": {
            "en": "Om Bhram Bhreem Bhroum Sah Rahave Namah (108 times after sunset).",
            "hi": "ॐ भ्रां भ्रीं भ्रौं सः राहवे नमः (सूर्यास्त के पश्चात 108 बार जप)।",
            "gu": "ૐ ભ્રાં ભ્રીં ભ્રૌં સઃ રાહવે નમઃ (સૂર્યાસ્ત પછી 108 વાર જાપ)."
        },
        "fasting": {"en": "Saturday. Avoid eating non-vegetarian food or intoxicating substances.", "hi": "शनिवार को सात्विक रहें। तामसिक भोजन व नशीले पदार्थों से पूर्ण परहेज रखें।", "gu": "શનિવારે સાત્વિક રહેવું. તામસિક આહાર કે નશીલા પદાર્થોથી સદંતર દૂર રહેવું."},
        "donation": {
            "en": "Donate black sesame seeds, mustard oil, dark blankets, or radish to sweepers or lepers on Saturday.",
            "hi": "शनिवार को काले तिल, सरसों का तेल, काला कंबल, या मूली सफाईकर्मियों व कुष्ठ रोगियों को दान करें।",
            "gu": "શનિવારે કાળા તલ, સરસવનું તેલ, કાળો ધાબળો કે મૂળા સફાઈ કામદારોને દાન કરવા."
        },
        "seva": {
            "en": "Feed stray black dogs and birds daily. Keep South-West zone of home clean and clutter-free.",
            "hi": "प्रतिदिन काले श्वान (कुत्तों) और पक्षियों को भोजन दें। घर के नैऋत्य कोण (South-West) को सर्वदा स्वच्छ व व्यवस्थित रखें।",
            "gu": "દરરોજ કૂતરાઓ અને પક્ષીઓને ચણ-રોટલી આપવી. ઘરના નૈઋત્ય ખૂણા (South-West)ને સાફ અને અવ્યવસ્થા વગરનો રાખવો."
        }
    },
    5: {
        "gem": {
            "en": "Wear Natural Emerald (Panna) 3.5 to 5 Ratti in Gold or Bronze on the Little finger on Wednesday morning.",
            "hi": "बुधवार प्रातः सोने या कांस्य में 3.5 से 5 रत्ती का प्राकृतिक हरा पन्ना कनिष्ठिका (छोटी उंगली) में धारण करें।",
            "gu": "બુધવારે સવારે સોના કે કાંસામાં 3.5 થી 5 રત્તીનો કુદરતી લીલો પન્ના ટચલી આંગળીમાં ધારણ કરવો."
        },
        "crystal": {"en": "Green Aventurine or Peridot", "hi": "ग्रीन एवेंट्यूरिन या पेरिडॉट", "gu": "ગ્રીન એવેન્ચ્યુરિન અથવા પેરિડોટ"},
        "mantra": {
            "en": "Om Bram Breem Broum Sah Budhaya Namah (108 times on Wednesday morning).",
            "hi": "ॐ ब्रां ब्रीं ब्रौं सः बुधाय नमः (बुधवार प्रातः 108 बार जप)।",
            "gu": "ૐ બ્રાં બ્રીં બ્રૌં સઃ બુધાય નમઃ (બુધવારે સવારે 108 વાર જાપ)."
        },
        "fasting": {"en": "Wednesday. Consume green moong dal and leafy greens.", "hi": "बुधवार का व्रत। हरी मूंग दाल व हरी पत्तेदार सब्जियों का सात्विक आहार लें।", "gu": "બુધવારનું વ્રત. મગની દાળ અને લીલા શાકભાજીનો સાત્વિક આહાર લેવો."},
        "donation": {
            "en": "Donate whole green moong dal, green clothes, green fruits, or stationery to young girls on Wednesday.",
            "hi": "बुधवार को साबुत हरी मूंग, हरे वस्त्र, हरे फल, या लेखन सामग्री छोटी कन्याओं को दान करें।",
            "gu": "બુધવારે આખા લીલા મગ, લીલા વસ્ત્રો, લીલાં ફળો કે સ્ટેશનરી નાની કન્યાઓને દાન કરવી."
        },
        "seva": {
            "en": "Feed green spinach / fodder to cows on Wednesday. Water a Tulsi plant daily and circumambulate it.",
            "hi": "बुधवार को गौमाता को हरा पालक या चारा खिलाएं। घर में तुलसी जी को नित्य जल अर्पित कर परिक्रमा करें।",
            "gu": "બુધવારે ગાયોને લીલું ઘાસ કે પાલક ખવડાવવી. ઘરમાં તુલસીજીને દરરોજ જળ ચડાવીને પ્રદક્ષિણા કરવી."
        }
    },
    6: {
        "gem": {
            "en": "Wear Natural Diamond, White Zircon, or Australian Opal 5 to 7 Ratti in Silver on the Ring finger on Friday morning.",
            "hi": "शुक्रवार प्रातः चांदी में 5 से 7 रत्ती का सफेद जरकन, हीरा या ऑस्ट्रेलियन ओपल अनामिका में धारण करें।",
            "gu": "શુક્રવારે સવારે ચાંદીમાં 5 થી 7 રત્તીનો સફેદ ઝરકન, હીરો કે ઓસ્ટ્રેલિયન ઓપલ અનામિકા આંગળીમાં ધારણ કરવો."
        },
        "crystal": {"en": "Clear Quartz or Rose Quartz", "hi": "क्लियर क्वार्ट्ज या रोज़ क्वार्ट्ज", "gu": "ક્લિયર ક્વાર્ટ્ઝ અથવા રોઝ ક્વાર્ટ્ઝ"},
        "mantra": {
            "en": "Om Shram Shreem Shroum Sah Shukraya Namah (108 times on Friday morning).",
            "hi": "ॐ शुं शुक्राय नमः अथवा ॐ द्रां द्रीं द्रौं सः शुक्राय नमः (शुक्रवार प्रातः 108 बार)।",
            "gu": "ૐ શુક્રાય નમઃ અથવા ૐ દ્રાં દ્રીં દ્રૌં સઃ શુક્રાય નમઃ (શુક્રવારે સવારે 108 વાર જાપ)."
        },
        "fasting": {"en": "Friday. Strictly avoid sour foods (curd, lemons, pickles) on this day.", "hi": "शुक्रवार का व्रत। इस दिन खटाई (नींबू, अचार आदि) के सेवन से पूर्ण परहेज रखें।", "gu": "શુક્રવારનું વ્રત. આ દિવસે ખાટી વસ્તુઓ (લીંબુ, અથાણું) ખાવાથી દૂર રહેવું."},
        "donation": {
            "en": "Donate white rice, sugar candy (mishri), pure cow ghee, perfumes, or white silk clothes to women on Friday.",
            "hi": "शुक्रवार को मिश्री, सफेद चावल, गाय का शुद्ध घी, इत्र या रेशमी वस्त्र सुहागिन महिलाओं को दान करें।",
            "gu": "શુક્રવારે સાકર, સફેદ ચોખા, ગાયનું ઘી, અત્તર કે સિલ્કના વસ્ત્રો સૌભાગ્યવતી સ્ત્રીઓને દાન કરવા."
        },
        "seva": {
            "en": "Respect women, spouse, and mother. Apply natural non-alcoholic sandalwood or rose attar (perfume) daily.",
            "hi": "नारी जाति और जीवनसंगिनी का सदैव आदर करें। प्रतिदिन प्राकृतिक चंदन या गुलाब का इत्र नाभि व कलाई पर लगाएं।",
            "gu": "સ્ત્રીઓ અને જીવનસાથીનું હંમેશા આદર-સન્માન કરવું. રોજેરોજ કુદરતી ચંદન કે ગુલાબનું અત્તર લગાવવું."
        }
    },
    7: {
        "gem": {
            "en": "Wear Natural Cat's Eye (Lehsuniya) 3.5 to 5.5 Ratti in Silver on the Middle or Little finger on Thursday/Saturday night.",
            "hi": "गुरुवार या शनिवार रात्रि चांदी की अंगूठी में 3.5 से 5.5 रत्ती का प्राकृतिक लहसुनिया मध्यमा अथवा कनिष्ठिका में धारण करें।",
            "gu": "ગુરુવાર કે શનિવારની રાત્રે ચાંદીની વીંટીમાં 3.5 થી 5.5 રત્તીનું શુદ્ધ લહસુનિયા મધ્યમા કે ટચલી આંગળીમાં ધારણ કરવું."
        },
        "crystal": {"en": "Cat's Eye or Tiger Eye", "hi": "लहसुनिया या टाइगर आई", "gu": "લહસુનિયા અથવા ટાઇગર આઇ"},
        "mantra": {
            "en": "Om Stram Streem Stroum Sah Ketave Namah (108 times on Tuesday/Saturday night).",
            "hi": "ॐ स्रां स्रीं स्रौं सः केतवे नमः (मंगलवार या शनिवार रात्रि 108 बार जप)।",
            "gu": "ૐ સ્ત્રાં સ્ત્રીં સ્ત્રૌં સઃ કેતવે નમઃ (મંગળવાર કે શનિવારની રાત્રે 108 વાર જાપ)."
        },
        "fasting": {"en": "Tuesday or Thursday. Practice intermittent fasting and quiet meditation.", "hi": "मंगलवार या गुरुवार का व्रत। मौन साधना एवं आत्मचिंतन के साथ उपवास रखें।", "gu": "મંગળવાર કે ગુરુવારનું વ્રત. મૌન અને ધ્યાન સાધના સાથે સાત્વિક ઉપવાસ કરવો."},
        "donation": {
            "en": "Donate multi-colored blanket, sesame, bananas, seven grains (satnajaa), or warm clothes to holy ascetics.",
            "hi": "बहुरंगी कंबल, तिल, सात प्रकार के अनाज (सतनाजा), या गर्म कपड़े संतों अथवा निर्धनों को दान करें।",
            "gu": "કાબરચીતરો ધાબળો, તલ, સાત ધાન્ય (સતનાજા), કે ગરમ વસ્ત્રો સાધુ-સંતો અથવા ગરીબોને દાન કરવા."
        },
        "seva": {
            "en": "Feed stray spotted or black-and-white street dogs daily. Engage in daily pranayama and spiritual meditation.",
            "hi": "गली के दोरंगे या काले श्वान (कुत्तों) को प्रतिदिन भोजन कराएं। नित्य प्राणायाम और ध्यान का अभ्यास करें।",
            "gu": "શેરીના કાબરચીતરા કે કાળા કૂતરાઓને દરરોજ રોટલી ખવડાવવી. રોજ નિયમિત પ્રાણાયામ અને ધ્યાન કરવું."
        }
    },
    8: {
        "gem": {
            "en": "Wear Natural Blue Sapphire (Neelam) or Dark Amethyst (Katela) 4.5 to 7 Ratti in Silver or Panchdhatu on Middle finger on Saturday evening.",
            "hi": "शनिवार संध्या समय चांदी या पंचधातु में 4.5 से 7 रत्ती का नीलम अथवा जामुनिया मध्यमा (बीच की उंगली) में धारण करें।",
            "gu": "શનિવારે સાંજે ચાંદી કે પંચધાતુમાં 4.5 થી 7 રત્તીનો નીલમ અથવા જમુનિયા (એમિથિસ્ટ) વચલી આંગળીમાં ધારણ કરવો."
        },
        "crystal": {"en": "Amethyst or Black Tourmaline", "hi": "जामुनिया या ब्लैक टूमलाइन", "gu": "જમુનિયા અથવા બ્લેક ટૂરમલાઇન"},
        "mantra": {
            "en": "Om Pram Preem Proum Sah Shanaischaraya Namah (108 times on Saturday evening) or Shani Chalisa.",
            "hi": "ॐ प्रां प्रीं प्रौं सः शनैश्चराय नमः (शनिवार संध्या 108 बार) अथवा शनि चालीसा का पाठ।",
            "gu": "ૐ પ્રાં પ્રીં પ્રૌં સઃ શનૈશ્ચરાય નમઃ (શનિવારે સાંજે 108 વાર જાપ) અથવા શનિ ચાલીસા."
        },
        "fasting": {"en": "Saturday. Consume khichdi with mustard oil or black lentils; avoid salt after sunset.", "hi": "शनिवार का व्रत। उड़द दाल की खिचड़ी का सेवन करें; सूर्यास्त के बाद नमक न लें।", "gu": "શનિવારનું વ્રત. અડદની દાળની ખીચડી ખાવી; સૂર્યાસ્ત પછી મીઠું (નમક) ન લેવું."},
        "donation": {
            "en": "Perform Chhaya Daan (look at face in mustard oil and donate it), donate iron pans, black umbrellas, or leather shoes to poor laborers.",
            "hi": "छाया दान करें (सरसों के तेल में मुख देखकर दान दें), लोहे का तवा, काला छाता, या जूते जरूरतमंद श्रमिकों को दान करें।",
            "gu": "છાયા દાન કરવું (તેલમાં મોં જોઈને તેલનું દાન), લોઢાની તવી, કાળી છત્રી કે ચંપલ જરૂરિયાતમંદ શ્રમિકોને દાન કરવા."
        },
        "seva": {
            "en": "Treat household workers, sweepers, and elderly laborers with dignity. Light a mustard oil lamp under a Peepal tree on Saturday evening.",
            "hi": "घर के सहायकों, सफाईकर्मियों और बुजुर्ग श्रमिकों का सदैव सम्मान करें। शनिवार संध्या पीपल के वृक्ष तले सरसों के तेल का दीपक जलाएं।",
            "gu": "ઘરના નોકરો, સફાઈ કામદારો અને વૃદ્ધ મજૂરોને માન આપવું. શનિવારે સાંજે પીપળા નીચે સરસવના તેલનો દીવો પ્રગટાવવો."
        }
    },
    9: {
        "gem": {
            "en": "Wear Natural Red Coral (Italian Moonga) 5.5 to 7.25 Ratti in Copper or Gold on the Ring finger on Tuesday morning.",
            "hi": "मंगलवार प्रातः तांबे या सोने में 5.5 से 7.25 रत्ती का इटैलियन लाल मूंगा अनामिका (रिंग फिंगर) में धारण करें।",
            "gu": "મંગળવારે સવારે તાંબા કે સોનામાં 5.5 થી 7.25 રત્તીનું ઇટાલિયન લાલ પરવાળું (મૂંગા) અનામિકા આંગળીમાં ધારણ કરવું."
        },
        "crystal": {"en": "Carnelian or Red Jasper", "hi": "कार्नेलियन या लाल जैस्पर", "gu": "કાર્નેલિયન અથવા રેડ જાસ્પર"},
        "mantra": {
            "en": "Om Kram Kreem Kroum Sah Bhaumaya Namah (108 times on Tuesday morning) and recite Hanuman Chalisa daily.",
            "hi": "ॐ क्रां क्रीं क्रौं सः भौमाय नमः (मंगलवार प्रातः 108 बार) तथा नित्य हनुमान चालीसा का पाठ करें।",
            "gu": "ૐ ક્રાં ક્રીં ક્રૌં સઃ ભૌમાય નમઃ (મંગળવારે સવારે 108 વાર જાપ) અને દરરોજ હનુમાન ચાલીસાના પાઠ કરવા."
        },
        "fasting": {"en": "Tuesday. Avoid salt and sour food; consume sweet rotis or jaggery halwa.", "hi": "मंगलवार का व्रत। नमक व खटाई का त्याग करें; मीठी रोटी अथवा गुड़ के हलवे का भोग लगाएं।", "gu": "મંગળવારનું વ્રત. મીઠું અને ખાટી ચીજો છોડવી; ગોળવાળી મીઠી રોટલી કે લાપસી ખાવી."},
        "donation": {
            "en": "Donate red masoor dal, copper utensils, jaggery, red sweets (boondi laddoos), or red vermillion (sindoor) at Hanuman Temple.",
            "hi": "मंगलवार को लाल मसूर दाल, तांबे का बर्तन, गुड़, बूंदी के लड्डू या सिंदूर हनुमान जी के मंदिर में अर्पित करें।",
            "gu": "મંગળવારે લાલ મસૂરની દાળ, તાંબાનું વાસણ, ગોળ, બુંદીના લાડુ કે સિંદૂર હનુમાનજીના મંદિરે અર્પણ કરવા."
        },
        "seva": {
            "en": "Recite Hanuman Chalisa or Bajrang Baan daily. Channel excess energy into physical workouts and sports; protect younger siblings.",
            "hi": "नित्य श्री हनुमान चालीसा या बजरंग बाण का पाठ करें। अतिरिक्त ऊर्जा को व्यायाम या खेल में लगाएं; छोटे भाइयों की रक्षा करें।",
            "gu": "રોજ શ્રી હનુમાન ચાલીસા કે બજરંગ બાણના પાઠ કરવા. અતિરિક્ત ઊર્જાને કસરત કે રમતમાં વાળવી; નાના ભાઈ-બહેનોની સંભાળ રાખવી."
        }
    }
}

# General Holistic Vedic Remedies (Astrology Club & Level 2)
GENERAL_REMEDIES = {
    "health": {
        "title": {
            "en": "Vedic Health & Vitality Booster",
            "hi": "वैदिक स्वास्थ्य एवं जीवनी शक्ति संवर्धन",
            "gu": "વૈદિક સ્વાસ્થ્ય અને જીવનશક્તિ વર્ધન"
        },
        "desc": {
            "en": "Store drinking water in a 100% pure copper jug overnight and drink the first glass on an empty stomach at dawn. Expose the body to gentle morning sunlight for 15 minutes to charge prana.",
            "hi": "रात्रि में तांबे के लोटे या जग में शुद्ध जल भरकर रखें और प्रातःकाल सूर्योदय के समय खाली पेट उसका सेवन करें। प्रातःकाल 15 मिनट कोमल धूप में बैठकर प्राण ऊर्जा को सक्रिय करें।",
            "gu": "રાત્રે શુદ્ધ તાંબાના વાસણમાં પાણી ભરી રાખવું અને વહેલી સવારે સૂર્યોદય સમયે નરણા કોઠે તે જળ પીવું. સવારે 15 મિનિટ સૂર્યના કુમળા તડકામાં બેસી પ્રાણ ઊર્જા મેળવવી."
        }
    },
    "wealth": {
        "title": {
            "en": "Cash Flow & Business Prosperity (Kuber / Lakshmi)",
            "hi": "धन प्रवाह एवं व्यावसायिक समृद्धि (कुबेर / लक्ष्मी)",
            "gu": "ધન પ્રવાહ અને વેપાર સમૃદ્ધિ (કુબેર / લક્ષ્મી)"
        },
        "desc": {
            "en": "Place an energized Shri Kuber Yantra wrapped in clean green or red silk cloth inside your cash locker facing North. Burn pure bhimseni camphor (kapoor) with 2 cloves in the evening to clear stagnant vibrations.",
            "hi": "अपनी तिजोरी या कैश बॉक्स में उत्तर दिशा की ओर मुख करके लाल या हरे रेशमी वस्त्र में श्री कुबेर यंत्र अथवा श्री यंत्र स्थापित करें। संध्या समय शुद्ध भीमसेनी कपूर और दो लौंग जलाकर घर में घुमाएं।",
            "gu": "પોતાની તિજોરી કે ગલ્લામાં ઉત્તર દિશા તરફ મુખ રાખી લાલ કે લીલા રેશમી વસ્ત્રમાં શ્રી કુબેર યંત્ર સ્થાપિત કરવું. સાંજના સમયે શુદ્ધ ભીમસેની કપૂર અને બે લવિંગ પ્રગટાવી ઘરમાં ધૂપ કરવો."
        }
    },
    "harmony": {
        "title": {
            "en": "Relationship Harmony & Vastu Protection",
            "hi": "पारिवारिक सौहार्द एवं वास्तु शुद्धि",
            "gu": "કૌટુંબિક સુમેળ અને વાસ્તુ શુદ્ધિ"
        },
        "desc": {
            "en": "Keep a natural Rose Quartz crystal cluster in the South-West master bedroom. Mop the house floors once a week (especially Tuesdays) with rock salt (sendha namak) dissolved in water to dissolve negativity.",
            "hi": "घर के नैऋत्य कोण (South-West) में बेडरूम में प्राकृतिक रोज क्वार्ट्ज क्रिस्टल रखें। सप्ताह में एक बार (विशेषकर मंगलवार) पानी में सेंधा नमक मिलाकर पोछा लगाएं ताकि नकारात्मक ऊर्जा समाप्त हो सके।",
            "gu": "ઘરના નૈઋત્ય ખૂણાના બેડરૂમમાં કુદરતી રોઝ ક્વાર્ટ્ઝ ક્રિસ્ટલ રાખવું. અઠવાડિયામાં એક વાર (ખાસ કરીને મંગળવારે) પાણીમાં સિંધવ મીઠું નાખીને પોતું કરવું જેથી નકારાત્મક ઊર્જા દૂર થાય."
        }
    }
}
