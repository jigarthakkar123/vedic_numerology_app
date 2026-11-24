# -*- coding: utf-8 -*-
"""
Vedic Numerology Studio - Automated Email Delivery Engine
Sends personalized trilingual Vedic Numerology reports (PDF attachments)
to clients immediately upon successful checkout.
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from typing import Dict, Any

# Email Configuration from environment variables
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
GMAIL_USER = os.environ.get("GMAIL_USER", "jigar93776@gmail.com").strip()
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "cvwjbdjadnvykuos").strip()
SENDER_NAME = os.environ.get("SENDER_NAME", "Jigar Thakkar - Vedic Numerology Studio")

EMAIL_TEMPLATES = {
    "en": {
        "subject": "🕉️ Your Personalized Vedic Numerology Report & Dasha Roadmap - Jigar Thakkar",
        "greeting": "Namaste",
        "body_intro": "Thank you for ordering your sacred <strong>Vedic Numerology Blueprint & Dasha Roadmap</strong>. Your personalized 10-page consultation report has been mathematically calculated according to authentic Vedic principles and is attached to this email as a PDF document.",
        "whats_inside_title": "What Is Included in Your 10-Page Blueprint:",
        "items": [
            "<strong>Page 1:</strong> Lifetime Inborn Natal Matrix, Basic & Destiny Planetary Vibrations, Life Compass & Auspicious Gemstones/Metals.",
            "<strong>Page 2:</strong> 3-Tier Horizon Predictions (Active Mahadasha, Antardasha & Annual 9-Phase Pratyantar Dasha Roadmap).",
            "<strong>Page 3:</strong> Auspicious Raj Yogs, Karmic Dosha Remedies & Dynamic Dasha Vibration Polarity Shifts (+ / -).",
            "<strong>Page 4:</strong> 8 Core Life Dimension Predictions (Finance, Real Estate, Vehicle, Marriage/Divorce, Travel, Litigation, Health) & Vedic Remedies."
        ],
        "contact_note": "For personalized 1-on-1 consultations, gemstone recommendations, or Vastu guidance, feel free to contact:",
        "copyright": "© 2026 Jigar Thakkar • Certified Vedic Numerologist & Vastu Consultant. All Rights Reserved."
    },
    "hi": {
        "subject": "🕉️ आपकी व्यक्तिगत वैदिक अंक ज्योतिष रिपोर्ट और दशा रोडमैप - जिगर ठक्कर",
        "greeting": "नमस्ते",
        "body_intro": "आपकी व्यक्तिगत <strong>वैदिक अंक ज्योतिष ब्लूप्रिंट और दशा रोडमैप</strong> रिपोर्ट सफलतापूर्वक तैयार कर ली गई है। प्रमाणिक वैदिक गणनाओं पर आधारित आपकी 4-पृष्ठीय संपूर्ण परामर्श रिपोर्ट इस ईमेल के साथ पीडीएफ (PDF) के रूप में संलग्न है।",
        "whats_inside_title": "आपकी 4-पृष्ठीय रिपोर्ट में क्या शामिल है:",
        "items": [
            "<strong>पृष्ठ 1:</strong> जन्मकालीन वैदिक ग्रिड, मूलांक एवं भाग्यांक ग्रहीय स्पंदन, जीवन दिशा कंपास तथा शुभ रत्न/धातु।",
            "<strong>पृष्ठ 2:</strong> 3-स्तरीय सटीक भविष्यफल (सक्रिय महादशा, अंतर्दशा एवं 360-दिवसीय 9-चरणीय प्रत्यंतर दशा कैलेंडर)।",
            "<strong>पृष्ठ 3:</strong> शुभ राजयोग, कार्मिक दोष निवारण उपाय एवं दशा ग्रहीय स्पंदन परिवर्तन (+ / -)।",
            "<strong>पृष्ठ 4:</strong> जीवन के 8 प्रमुख क्षेत्रों की भविष्यवाणियां (वित्त, संपत्ति, वाहन, वैवाहिक जीवन, विदेश यात्रा, कानूनी मामले, स्वास्थ्य) एवं वैदिक अचूक उपाय।"
        ],
        "contact_note": "व्यक्तिगत परामर्श, रत्न चयन अथवा वास्तु सलाह के लिए संपर्क करें:",
        "copyright": "© 2026 जिगर ठक्कर • प्रमाणित वैदिक अंकशास्त्री एवं वास्तु सलाहकार। सर्वाधिकार सुरक्षित।"
    },
    "gu": {
        "subject": "🕉️ તમારો અંગત વૈદિક અંકશાસ્ત્ર અહેવાલ અને દશા રોડમેપ - જીગર ઠક્કર",
        "greeting": "નમસ્તે",
        "body_intro": "તમારો પવિત્ર <strong>વૈદિક અંકશાસ્ત્ર બ્લુપ્રિન્ટ અને દશા રોડમેપ</strong> સફળતાપૂર્વક તૈયાર કરવામાં આવ્યો છે. અધિકૃત વૈદિક સિદ્ધાંતો મુજબ ગણતરી કરેલ તમારો 4-પેજનો સંપૂર્ણ કન્સલ્ટેશન રિપોર્ટ આ ઈમેલ સાથે પીડીએફ (PDF) તરીકે જોડાયેલ છે.",
        "whats_inside_title": "તમારા 4-પેજના રિપોર્ટમાં શું સમાવિષ્ટ છે:",
        "items": [
            "<strong>પેજ 1:</strong> જન્મકાલીન વૈદિક ગ્રીડ, મૂળાંક અને ભાગ્યાંક વાઇબ્રેશન, જીવન દિશા કંપાસ તથા શુભ રત્ન/ધાતુ.",
            "<strong>પેજ 2:</strong> 3-સ્તરીય ચોક્કસ ભવિષ્યવાણી (મહાદશા, અંતર્દશા અને વાર્ષિક 9-તબક્કા પ્રત્યંતર દશા કેલેન્ડર).",
            "<strong>પેજ 3:</strong> શુભ રાજયોગ, કર્મિક દોષ નિવારણ ઉપાયો અને સક્રિય દશા વાઇબ્રેશન શિફ્ટ (+ / -).",
            "<strong>પેજ 4:</strong> જીવનના 8 મુખ્ય ક્ષેત્રોની આગાહીઓ (નાણાકીય સંપત્તિ, વાહન, લગ્નજીવન, વિદેશ પ્રવાસ, કોર્ટ-કચેરી, સ્વાસ્થ્ય) અને વૈદિક ઉપાયો."
        ],
        "contact_note": "અંગત પરામર્શ, રત્ન માર્ગદર્શન અથવા વાસ્તુ સલાહ માટે સંપર્ક કરો:",
        "copyright": "© 2026 જીગર ઠક્કર • સર્ટિફાઇડ વૈદિક ન્યૂમરોલોજિસ્ટ અને વાસ્તુ કન્સલ્ટન્ટ. સર્વાધિકાર સુરક્ષિત."
    }
}


def build_email_html(recipient_name: str, lang: str = "en") -> str:
    """Builds a luxury HTML email body matching the Vedic Studio theme."""
    t = EMAIL_TEMPLATES.get(lang, EMAIL_TEMPLATES["en"])
    items_html = "".join(f"<li style='margin-bottom: 6px;'>{item}</li>" for item in t["items"])

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{t['subject']}</title>
</head>
<body style="margin: 0; padding: 20px; background-color: #060913; font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #f8fafc;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: #0f172a; border: 1.5px solid #d4af37; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.6);">
        <!-- Top Sacred Header -->
        <tr>
            <td align="center" style="background: linear-gradient(180deg, #0b1329 0%, #080d1a 100%); padding: 30px 20px 20px; border-bottom: 1.5px solid #d4af37;">
                <div style="font-size: 42px; color: #fbbf24; line-height: 1; margin-bottom: 8px;">ॐ</div>
                <h1 style="color: #fbbf24; font-size: 19px; letter-spacing: 1.2px; margin: 0 0 4px 0; font-family: Georgia, serif; text-transform: uppercase;">
                    Jigar Thakkar's Vedic Numerology Studio
                </h1>
                <p style="color: #94a3b8; font-size: 12px; margin: 0; letter-spacing: 0.4px;">
                    Certified Vedic Numerologist & Vastu Consultant • Automated Trilingual Blueprint Engine
                </p>
            </td>
        </tr>

        <!-- Main Body -->
        <tr>
            <td style="padding: 28px 24px;">
                <p style="font-size: 16px; color: #fbbf24; margin-top: 0; font-weight: 600;">
                    {t['greeting']} {recipient_name},
                </p>
                <p style="font-size: 14px; line-height: 1.6; color: #cbd5e1; margin-bottom: 22px;">
                    {t['body_intro']}
                </p>

                <!-- Highlight Box -->
                <div style="background: rgba(212, 175, 55, 0.08); border: 1px solid rgba(212, 175, 55, 0.35); border-left: 4px solid #d4af37; border-radius: 8px; padding: 16px 18px; margin-bottom: 24px;">
                    <h3 style="color: #fbbf24; font-size: 14px; margin: 0 0 10px 0; letter-spacing: 0.5px;">
                        📜 {t['whats_inside_title']}
                    </h3>
                    <ul style="color: #e2e8f0; font-size: 12.5px; line-height: 1.55; margin: 0; padding-left: 18px;">
                        {items_html}
                    </ul>
                </div>

                <!-- Attached Notice -->
                <div style="background: #1e293b; border: 1px dashed rgba(212, 175, 55, 0.4); border-radius: 8px; padding: 12px 16px; margin-bottom: 24px; text-align: center;">
                    <span style="font-size: 18px; vertical-align: middle;">📎</span>
                    <strong style="color: #4ade80; font-size: 13px; vertical-align: middle; margin-left: 6px;">
                        Your personalized 10-page PDF report is attached to this email.
                    </strong>
                </div>

                <!-- Contact & Consultation Info -->
                <div style="border-top: 1px solid #334155; padding-top: 18px; font-size: 13px; color: #94a3b8; line-height: 1.6;">
                    <p style="margin: 0 0 6px 0;">{t['contact_note']}</p>
                    <p style="margin: 0; font-weight: 600; color: #f8fafc;">
                        📞 Phone / WhatsApp: <a href="tel:+919377614772" style="color: #fbbf24; text-decoration: none;">+91 9377614772</a><br>
                        ✉ Email: <a href="mailto:jigar93776@gmail.com" style="color: #fbbf24; text-decoration: none;">jigar93776@gmail.com</a>
                    </p>
                </div>
            </td>
        </tr>

        <!-- Footer -->
        <tr>
            <td align="center" style="background-color: #060913; padding: 16px; border-top: 1px solid #1e293b; font-size: 11px; color: #64748b;">
                {t['copyright']}
            </td>
        </tr>
    </table>
</body>
</html>
"""


def send_report_email(
    recipient_email: str,
    recipient_name: str,
    lang: str,
    pdf_path: str
) -> Dict[str, Any]:
    """
    Sends the 10-page Vedic Numerology report via SMTP.
    Returns status dictionary with success flag and details.
    """
    if not recipient_email or "@" not in recipient_email:
        return {"success": False, "reason": "Invalid recipient email address"}

    if not GMAIL_APP_PASSWORD:
        # App password not configured yet; log notice and return gracefully
        print(f"[MAILER NOTICE] GMAIL_APP_PASSWORD not set in environment. Email to {recipient_email} skipped in demo/dev mode.")
        return {
            "success": False,
            "reason": "GMAIL_APP_PASSWORD not configured. Please set GMAIL_APP_PASSWORD in Render environment variables.",
            "demo_mode": True
        }

    try:
        t = EMAIL_TEMPLATES.get(lang, EMAIL_TEMPLATES["en"])
        msg = MIMEMultipart()
        msg["From"] = f"{SENDER_NAME} <{GMAIL_USER}>"
        msg["To"] = recipient_email
        msg["Subject"] = t["subject"]

        # HTML Body
        html_content = build_email_html(recipient_name, lang)
        msg.attach(MIMEText(html_content, "html", "utf-8"))

        # Attach PDF
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                pdf_data = f.read()
            attachment = MIMEApplication(pdf_data, _subtype="pdf")
            pdf_filename = os.path.basename(pdf_path)
            attachment.add_header("Content-Disposition", "attachment", filename=pdf_filename)
            msg.attach(attachment)
        else:
            print(f"[MAILER WARNING] PDF path {pdf_path} not found; sending email without attachment.")

        # Connect and send via SMTP with TLS
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20)
        server.ehlo()
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)

        # Also send an instant consultation notification with PDF to Jigar Thakkar
        if recipient_email.lower().strip() != GMAIL_USER.lower().strip():
            try:
                notify_msg = MIMEMultipart()
                notify_msg["From"] = f"{SENDER_NAME} <{GMAIL_USER}>"
                notify_msg["To"] = GMAIL_USER
                notify_msg["Subject"] = f"💰 [NEW PAID CLIENT] Report Delivered to {recipient_name} ({recipient_email})"
                notify_body = f"""
                <div style="font-family: sans-serif; padding: 16px; background: #0f172a; color: #f8fafc; border-radius: 8px; border: 1px solid #d4af37;">
                    <h2 style="color: #fbbf24; margin-top: 0;">🎉 New Paid Order Received!</h2>
                    <p>A client has completed payment on your Vedic Funnel and their 10-page Blueprint was delivered.</p>
                    <ul style="line-height: 1.6;">
                        <li><strong>Client Name:</strong> {recipient_name}</li>
                        <li><strong>Client Email:</strong> {recipient_email}</li>
                        <li><strong>Report Language:</strong> {lang.upper()}</li>
                    </ul>
                    <p style="color: #4ade80;">✔ The client's exact 10-page report is attached below for your consultation records.</p>
                </div>
                """
                notify_msg.attach(MIMEText(notify_body, "html", "utf-8"))
                if pdf_path and os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        pdf_data = f.read()
                    attach_notify = MIMEApplication(pdf_data, _subtype="pdf")
                    attach_notify.add_header("Content-Disposition", "attachment", filename=os.path.basename(pdf_path))
                    notify_msg.attach(attach_notify)
                server.send_message(notify_msg)
            except Exception as notify_err:
                print(f"[MAILER NOTIFY WARNING] {notify_err}")

        server.quit()

        print(f"[MAILER SUCCESS] Report successfully delivered to {recipient_email}")
        return {"success": True, "recipient": recipient_email}

    except Exception as e:
        print(f"[MAILER ERROR] Failed to send email to {recipient_email}: {str(e)}")
        return {"success": False, "reason": str(e)}
