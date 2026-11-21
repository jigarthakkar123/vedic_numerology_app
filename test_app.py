# -*- coding: utf-8 -*-
"""
End-to-end Integration Test for Vedic Numerology Studio
Tests all endpoints, calculations, trilingual outputs, and Edge PDF generation.
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from fastapi.testclient import TestClient
from vedic_server import app

client = TestClient(app)

def test_static_index():
    print("Testing GET / ...")
    res = client.get("/")
    assert res.status_code == 200
    assert "VEDIC NUMEROLOGY STUDIO" in res.text
    print("GET / OK!")

def test_analyze_english():
    print("Testing POST /api/analyze (EN)...")
    payload = {
        "name": "Gopal Pathak",
        "dob": "1982-11-04",
        "gender": "Male",
        "target_date": "2026-11-21",
        "lang": "en",
        "consultant_notes": "Test notes"
    }
    res = client.post("/api/analyze", json=payload)
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["core_numbers"]["bn"] == 4
    assert data["core_numbers"]["dn"] == 8
    assert data["grid"]["counts"]["1"] == 2 or data["grid"]["counts"][1] == 2
    assert "Action Plane" in [y["name"] for y in data["yogas"]][0]
    print("POST /api/analyze (EN) OK!")

def test_analyze_hindi_gujarati():
    print("Testing POST /api/analyze (HI & GU)...")
    for lang in ["hi", "gu"]:
        payload = {
            "name": "Gopal Pathak",
            "dob": "1982-11-04",
            "gender": "Male",
            "target_date": "2026-11-21",
            "lang": lang
        }
        res = client.post("/api/analyze", json=payload)
        assert res.status_code == 200
        data = res.json()["data"]
        assert len(data["predictions"]) == 8
        assert len(data["remedies"]) >= 8
    print("POST /api/analyze (HI & GU) OK!")

def test_pdf_generation_single():
    print("Testing POST /api/generate-pdf (Gujarati)...")
    payload = {
        "name": "Gopal Pathak",
        "dob": "1982-11-04",
        "gender": "Male",
        "target_date": "2026-11-21",
        "lang": "gu",
        "consultant_notes": "દરરોજ સવારે તાંબાના કળશથી સૂર્ય પૂજા કરવી."
    }
    res = client.post("/api/generate-pdf", json=payload)
    assert res.status_code == 200
    res_data = res.json()
    assert res_data["success"] is True
    assert res_data["size"] > 100000
    filename = res_data["filename"]
    print(f"Generated PDF: {filename} ({res_data['size']} bytes)")

    # Verify download endpoint
    dl_res = client.get(res_data["download_url"])
    assert dl_res.status_code == 200
    assert len(dl_res.content) == res_data["size"]
    print("GET /api/download OK!")

def test_history():
    print("Testing GET /api/history ...")
    res = client.get("/api/history")
    assert res.status_code == 200
    assert len(res.json()["reports"]) > 0
    print("GET /api/history OK!")

if __name__ == "__main__":
    test_static_index()
    test_analyze_english()
    test_analyze_hindi_gujarati()
    test_pdf_generation_single()
    test_history()
    print("\nALL INTEGRATION TESTS PASSED SUCCESSFULLY!")
