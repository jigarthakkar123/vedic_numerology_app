# Vedic Numerology Studio (Automated Client Blueprint Engine)

> **Authored & Certified by:**  
> **Jigar Thakkar** (*Certified Vedic Numerologist & Vastu Consultant*)  
> 📞 **Phone / WhatsApp:** +91 9377614772  
> ✉ **Email:** jigar93776@gmail.com  
> ⚖ **Copyright:** © 2026 Jigar Thakkar. All Rights Reserved.

---

## Overview

**Vedic Numerology Studio** is a professional, full-stack client consultation platform and automated PDF report generator built on classical Vedic Astrology & Numerology principles. It enables certified numerologists to calculate complete client natal charts, Dasha timelines, active Yogas, domain predictions, and prescribed remedial blueprints, instantly generating print-ready luxury A4 PDFs in **3 languages: English, Hindi (हिन्दी), and Gujarati (ગુજરાતી)**.

---

## Key Features

1. **Vedic Natal Kundali (3x3 Birth Grid):**
   - Precise Vedic digit placement rules (Century excluded; compound day digits + compound BN added; DN always added).
   - Frequency counts with glowing active cells and dormant indicators.

2. **Positive vs. Negative Planetary Vibrations:**
   - Evaluates all numbers 1–9 based on single vs. multiple occurrences and Destiny Number overrides (e.g. `+1` executive leadership vs `-1` ego clashes; `88` real estate empire vs `-8` struggles; `44` technical success vs single `4` hurdles; `-9` surgery/accident alertness).

3. **Planetary Dasha Cycles (Timeline Schedule):**
   - **Mahadasha (MD):** Lifetime 45-year cyclic schedule starting from birth with the Basic Number (durations 1 to 9 years).
   - **Antardasha (AD):** 1-year sub-period calculated via `Date + Month + Last2DigitsOfLastBirthday + DayOfWeekNumber`.
   - **Pratyantar Dasha (PD):** 9 sub-periods in the 360-day year (`Root Number × 8 days`).

4. **Planetary Friendship & Compatibility Compass (81 Combinations Matrix):**
   - Friendly Numbers (Allies & Business Partners)
   - Neutral Numbers
   - Unfriendly / Enemy Numbers to Avoid
   - Auspicious Vastu Direction & Lucky Metal

5. **Name Number (Namank) Harmonic Vibration Audit:**
   - Classical Chaldean reduction of client name.
   - Audits whether current spelling harmonizes with Basic & Destiny numbers or indicates a need for name correction.

6. **Active Yogas in Birth Kundali:**
   - **Planes:** Thought Plane (`3-1-9`), Will Plane (`6-7-5`), Action Plane (`2-8-4`).
   - **Verticals:** Vision/Knowledge Line (`3-6-2`), Balance/Organization Line (`1-7-8`), Business Line (`9-5-4`).
   - **Pairs & Combinations:** `3-1`, `1-9`, `6-5` (Lakshmi/Kuber Yog), `8-4` (Shani-Rahu technical breakthrough), `2-8` (Chandra-Shani real estate), `9-4`, `7-8`, and Imperial Raj Yog.

7. **8 Domain-Specific Life Predictions:**
   - **Finance & Wealth** (Standard of Living assessment, liquidity, beneficial dasha periods).
   - **Property & Real Estate** (Land ownership potential, timing triggers, joint registration advice).
   - **Vehicles & Luxury** (Automobile timing, lucky vehicle registration number sums).
   - **Education & Career** (Aptitudes, recommended professions per root number).
   - **Travel & Foreign Settlement** (Number `7` luxury/developed countries, Destiny `7` foreign settlement/PR, Number `4` work travel).
   - **Litigation & Court Cases** (`9 & 4`, `5 & 4`, `-6` indicators, 2+ consecutive years dasha activation rule, stabilizers).
   - **Marriage & Domestic Harmony** (Marital peace, separator vibrations, stabilizing practices).
   - **Health & Anatomical Sensitivities** (Organ vulnerabilities 1–9, blood pressure/surgery alert `-9`, anxiety alert `-2`).

8. **Prescribed Vedic Remedies:**
   - Gemstone with exact Ratti weight, metal, and wearing finger.
   - Sacred Vedic Mantras with japa counts.
   - Vrat/Fasting rules, Charity/Daana items, and Karma Seva.
   - General Vedic Remedies for Cash Box, Health, and Harmony.

9. **1-Click WhatsApp Client Delivery:**
   - Pre-composes a personalized WhatsApp message with your name, contact details, and direct PDF download link.

10. **Trilingual Localization:**
    - Full English, Hindi (हिन्दी), and Gujarati (ગુજરાતી) support in both web dashboard and generated PDFs.

---

## Technology Stack

- **Backend:** Python FastAPI, Uvicorn, Pydantic
- **Frontend:** Vanilla HTML5, CSS3, Modern JavaScript (Single Page Architecture, no heavy framework needed)
- **PDF Engine:** Cross-platform Headless Browser Engine (Edge on Windows, Chromium on Linux Docker)
- **Deployment:** Dockerfile with Debian slim, Chromium, and Indian fonts (`fonts-deva`, `fonts-gujr`)

---

## 1-Click Cloud Deployment (Render.com)

1. Fork or push this repository to your GitHub account (`https://github.com/jigarthakkar123/vedic_numerology_app`).
2. Go to [Render.com](https://render.com) and click **New +** $\to$ **Web Service**.
3. Connect your GitHub repository.
4. Render automatically detects the `Dockerfile` and selects the **Free** plan.
5. Click **Deploy Web Service**!
6. In 3–5 minutes, your live secure URL (e.g. `https://jigar-vedic-numerology.onrender.com`) will be online and accessible from any smartphone, tablet, or PC worldwide!

---

## Local Development & Running

```bash
# Clone the repository
git clone https://github.com/jigarthakkar123/vedic_numerology_app.git
cd vedic_numerology_app

# Install dependencies
pip install -r requirements.txt

# Start the web server
python vedic_server.py
```
Open [http://127.0.0.1:8765](http://127.0.0.1:8765) in your web browser.

---

## License & Copyright

**© 2026 Jigar Thakkar. All Rights Reserved.**  
This software and associated astrological algorithms are proprietary. Unauthorized duplication, commercial redistribution, or reproduction without prior written permission is strictly prohibited.
