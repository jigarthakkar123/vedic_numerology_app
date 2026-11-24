# -*- coding: utf-8 -*-
"""
Vedic Numerology Orders Database & Client CRM Module
Manages client transaction history, multi-tier orders (₹299, ₹499, ₹1,199),
report references, and VIP meeting scheduling.
"""

import os
import sqlite3
import csv
import io
import json
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vedic_orders.db")
REGISTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "orders_registry.json")

def _load_registry_orders() -> List[Dict[str, Any]]:
    if not os.path.exists(REGISTRY_PATH):
        return []
    try:
        with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[REGISTRY LOAD ERROR] {e}")
        return []

def _save_registry_orders(orders: List[Dict[str, Any]]) -> None:
    try:
        with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
            json.dump(orders, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[REGISTRY SAVE ERROR] {e}")

TIER_NAMES = {
    "test_1": "Live Verification Trial (₹1)",
    "essential_299": "Essential Blueprint (No Remedies)",
    "complete_499": "Complete Life Manual (With Remedies)",
    "vip_1199": "VIP 1-on-1 Consultation + Full Report"
}

TIER_AMOUNTS = {
    "test_1": 1,
    "essential_299": 299,
    "complete_499": 499,
    "vip_1199": 1199
}

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the SQLite database schema."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT DEFAULT 'Male',
                lang TEXT DEFAULT 'en',
                email TEXT NOT NULL,
                phone TEXT DEFAULT '',
                tier TEXT NOT NULL DEFAULT 'complete_499',
                tier_name TEXT NOT NULL DEFAULT 'Complete Life Manual',
                amount INTEGER NOT NULL DEFAULT 499,
                currency TEXT DEFAULT 'INR',
                order_id TEXT NOT NULL,
                payment_id TEXT NOT NULL,
                status TEXT DEFAULT 'paid',
                pdf_filename TEXT DEFAULT '',
                meeting_status TEXT DEFAULT 'none', -- 'none', 'pending', 'scheduled', 'completed'
                meeting_notes TEXT DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_email ON orders(email)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_phone ON orders(phone)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_tier ON orders(tier)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_created ON orders(created_at)")
        conn.commit()

        # Auto-sync persistent orders from registry JSON if missing in DB
        reg_orders = _load_registry_orders()
        for o in reg_orders:
            cursor.execute("SELECT 1 FROM orders WHERE order_id = ? OR payment_id = ?", (o.get("order_id"), o.get("payment_id")))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO orders (
                        client_name, dob, gender, lang, email, phone,
                        tier, tier_name, amount, currency, order_id, payment_id,
                        status, pdf_filename, meeting_status, meeting_notes, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'INR', ?, ?, 'paid', ?, ?, ?, ?, ?)
                """, (
                    o.get("client_name", "Client"),
                    o.get("dob", ""),
                    o.get("gender", "Male"),
                    o.get("lang", "en"),
                    o.get("email", ""),
                    o.get("phone", ""),
                    o.get("tier", "complete_499"),
                    o.get("tier_name", "Complete Life Manual"),
                    o.get("amount", 499),
                    o.get("order_id", ""),
                    o.get("payment_id", ""),
                    o.get("pdf_filename", ""),
                    o.get("meeting_status", "none"),
                    o.get("meeting_notes", ""),
                    o.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                    o.get("updated_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                ))
        conn.commit()

def save_order(
    client_name: str,
    dob: str,
    gender: str,
    lang: str,
    email: str,
    phone: str,
    tier: str,
    amount: int,
    order_id: str,
    payment_id: str,
    pdf_filename: str = ""
) -> Dict[str, Any]:
    """Saves a verified paid order into the database."""
    init_db()
    now_iso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tier_clean = tier.lower().strip() if tier else "complete_499"
    tier_name = TIER_NAMES.get(tier_clean, "Complete Life Manual (₹499)")
    meeting_status = "pending" if tier_clean == "vip_1199" else "none"

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO orders (
                client_name, dob, gender, lang, email, phone,
                tier, tier_name, amount, currency, order_id, payment_id,
                status, pdf_filename, meeting_status, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'INR', ?, ?, 'paid', ?, ?, ?, ?)
        """, (
            client_name, dob, gender, lang, email, phone,
            tier_clean, tier_name, amount, order_id, payment_id,
            pdf_filename, meeting_status, now_iso, now_iso
        ))
        conn.commit()
        order_row_id = cursor.lastrowid
        saved_order = get_order_by_id(order_row_id)
        if saved_order:
            reg_orders = _load_registry_orders()
            exists = False
            for idx, item in enumerate(reg_orders):
                if item.get("order_id") == order_id or item.get("payment_id") == payment_id:
                    reg_orders[idx] = dict(saved_order)
                    exists = True
                    break
            if not exists:
                reg_orders.append(dict(saved_order))
            _save_registry_orders(reg_orders)
        return saved_order

def get_order_by_id(order_row_id) -> Optional[Dict[str, Any]]:
    """Retrieves an order by its primary database ID or order_id."""
    init_db()
    if isinstance(order_row_id, dict):
        order_row_id = order_row_id.get("id")
    int_id = None
    try:
        int_id = int(order_row_id)
    except (TypeError, ValueError):
        pass
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE id = ? OR order_id = ?", (int_id, str(order_row_id)))
        row = cursor.fetchone()
        return dict(row) if row else None

def get_orders(
    search: Optional[str] = None,
    tier_filter: Optional[str] = None,
    limit: int = 100,
    offset: int = 0
) -> Tuple[List[Dict[str, Any]], int]:
    """Retrieves list of orders with optional search and filtering."""
    init_db()
    query = "SELECT * FROM orders WHERE 1=1"
    params = []

    if search:
        query += " AND (client_name LIKE ? OR email LIKE ? OR phone LIKE ? OR order_id LIKE ?)"
        s = f"%{search}%"
        params.extend([s, s, s, s])

    if tier_filter and tier_filter != "all":
        query += " AND tier = ?"
        params.append(tier_filter)

    count_query = query.replace("SELECT *", "SELECT COUNT(*)")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(count_query, params)
        total_count = cursor.fetchone()[0]

        query += " ORDER BY id DESC LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        cursor.execute(query, params)
        rows = [dict(r) for r in cursor.fetchall()]
        return rows, total_count

def get_order_stats() -> Dict[str, Any]:
    """Computes high-level business analytics for the consultant studio dashboard."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*), COALESCE(SUM(amount), 0) FROM orders")
        total_orders, total_revenue = cursor.fetchone()

        cursor.execute("""
            SELECT tier, COUNT(*), COALESCE(SUM(amount), 0)
            FROM orders
            GROUP BY tier
        """)
        tier_breakdown = {}
        tier_counts = {"test_1": 0, "essential_299": 0, "complete_499": 0, "vip_1199": 0}
        for row in cursor.fetchall():
            tier_breakdown[row[0]] = {
                "count": row[1],
                "revenue": row[2]
            }
            tier_counts[row[0]] = row[1]

        cursor.execute("SELECT COUNT(*) FROM orders WHERE tier = 'vip_1199' AND meeting_status = 'pending'")
        pending_meetings = cursor.fetchone()[0]

        return {
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "tier_counts": tier_counts,
            "tier_breakdown": tier_breakdown,
            "pending_meetings": pending_meetings
        }

def update_meeting_status(order_row_id, status: str, notes: str = "") -> bool:
    """Updates meeting consultation status for VIP orders."""
    init_db()
    if isinstance(order_row_id, dict):
        order_row_id = order_row_id.get("id")
    
    int_id = None
    try:
        int_id = int(order_row_id)
    except (TypeError, ValueError):
        pass

    now_iso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE orders
            SET meeting_status = ?, meeting_notes = ?, updated_at = ?
            WHERE id = ? OR order_id = ?
        """, (status, notes, now_iso, int_id, str(order_row_id)))
        conn.commit()
        if cursor.rowcount > 0:
            reg_orders = _load_registry_orders()
            for item in reg_orders:
                if str(item.get("id")) == str(order_row_id) or item.get("order_id") == str(order_row_id):
                    item["meeting_status"] = status
                    item["meeting_notes"] = notes
                    item["updated_at"] = now_iso
                    break
            _save_registry_orders(reg_orders)
        return cursor.rowcount > 0

def export_orders_csv() -> str:
    """Generates a downloadable CSV string of all orders for Excel."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders ORDER BY id DESC")
        rows = cursor.fetchall()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow([
            "ID", "Client Name", "DOB", "Gender", "Language",
            "Email", "Phone", "Tier", "Tier Name", "Amount (INR)",
            "Razorpay Order ID", "Payment ID", "Status",
            "PDF File", "VIP Meeting Status", "Meeting Notes", "Order Date"
        ])
        for r in rows:
            writer.writerow([
                r["id"], r["client_name"], r["dob"], r["gender"], r["lang"],
                r["email"], r["phone"], r["tier"], r["tier_name"], r["amount"],
                r["order_id"], r["payment_id"], r["status"],
                r["pdf_filename"], r["meeting_status"], r["meeting_notes"], r["created_at"]
            ])
        return output.getvalue()

# Automatically initialize table on import
init_db()
