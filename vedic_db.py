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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS saved_clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_slug TEXT DEFAULT 'default',
                client_name TEXT NOT NULL,
                dob TEXT NOT NULL,
                gender TEXT DEFAULT 'Male',
                phone TEXT DEFAULT '',
                email TEXT DEFAULT '',
                notes TEXT DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        try:
            cursor.execute("ALTER TABLE saved_clients ADD COLUMN tenant_slug TEXT DEFAULT 'default'")
        except Exception:
            pass
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_clients_name ON saved_clients(client_name)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_clients_tenant ON saved_clients(tenant_slug)")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tenants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT UNIQUE NOT NULL,
                brand_name TEXT NOT NULL,
                consultant_name TEXT NOT NULL,
                subtitle TEXT DEFAULT 'Certified Vedic Numerologist & Vastu Consultant',
                phone TEXT DEFAULT '',
                email TEXT DEFAULT '',
                copyright_text TEXT DEFAULT '',
                logo_url TEXT DEFAULT '',
                accent_color TEXT DEFAULT '#7c3aed',
                access_pin TEXT DEFAULT '1234',
                plan_name TEXT DEFAULT 'Pro',
                status TEXT DEFAULT 'active',
                pdf_quota INTEGER DEFAULT -1,
                pdf_count INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_tenants_slug ON tenants(slug)")
        cursor.execute("SELECT 1 FROM tenants WHERE slug = 'default'")
        if not cursor.fetchone():
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO tenants (
                    slug, brand_name, consultant_name, subtitle, phone, email,
                    copyright_text, access_pin, plan_name, status, pdf_quota, pdf_count,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                "default",
                "Jigar Thakkar's Vedic Numerology Studio",
                "Jigar Thakkar",
                "Certified Vedic Numerologist & Vastu Consultant",
                "+91 9377614772",
                "jigar93776@gmail.com",
                "© 2026 Jigar Thakkar · Certified Vedic Numerologist & Vastu Consultant",
                "93776",
                "Master",
                "active",
                -1,
                0,
                now_str,
                now_str,
            ))
        cursor.execute("SELECT 1 FROM tenants WHERE slug = 'demo'")
        if not cursor.fetchone():
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO tenants (
                    slug, brand_name, consultant_name, subtitle, phone, email,
                    copyright_text, access_pin, plan_name, status, pdf_quota, pdf_count,
                    created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                "demo",
                "Vedic Numerology Studio (LIVE DEMO)",
                "Demo Numerologist",
                "Trilingual White-Label Software Demo • Licensed by Jigar Thakkar",
                "+91 9377614772",
                "jigar93776@gmail.com",
                "© 2026 Jigar Thakkar • DEMO VERSION — FOR EVALUATION ONLY",
                "",
                "Demo",
                "active",
                -1,
                0,
                now_str,
                now_str,
            ))
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

def get_order_by_pdf(pdf_filename: str) -> Optional[Dict[str, Any]]:
    """Finds an order matching the given PDF filename."""
    init_db()
    clean = os.path.basename(pdf_filename)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE pdf_filename = ? OR pdf_filename LIKE ? ORDER BY id DESC LIMIT 1", (clean, f"%{clean}%"))
        row = cursor.fetchone()
        if row:
            return dict(row)
    reg_orders = _load_registry_orders()
    for o in reversed(reg_orders):
        if o.get("pdf_filename") == clean or clean in o.get("pdf_filename", ""):
            return o
    return None

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

def save_client_profile(data: Dict[str, Any], tenant_slug: str = "default") -> Dict[str, Any]:
    """Saves or updates a client in the Saved Client Directory (scoped by tenant)."""
    now = datetime.now().isoformat()
    t_slug = (tenant_slug or "default").strip().lower() or "default"
    name = (data.get("client_name") or data.get("name") or "").strip()
    dob = (data.get("dob") or "").strip()
    gender = (data.get("gender") or "Male").strip()
    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()
    notes = (data.get("notes") or "").strip()
    if not name or not dob:
        raise ValueError("Client Name and DOB are required.")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM saved_clients WHERE LOWER(client_name) = LOWER(?) AND dob = ? AND COALESCE(tenant_slug, 'default') = ?",
            (name, dob, t_slug)
        )
        existing = cursor.fetchone()
        if existing:
            cid = existing["id"]
            cursor.execute(
                """UPDATE saved_clients
                   SET gender = ?, phone = ?, email = ?, notes = ?, updated_at = ?
                   WHERE id = ?""",
                (gender, phone, email, notes, now, cid)
            )
        else:
            cursor.execute(
                """INSERT INTO saved_clients (tenant_slug, client_name, dob, gender, phone, email, notes, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (t_slug, name, dob, gender, phone, email, notes, now, now)
            )
            cid = cursor.lastrowid
        conn.commit()
        cursor.execute("SELECT * FROM saved_clients WHERE id = ?", (cid,))
        return dict(cursor.fetchone())


def list_saved_clients(search: str = "", limit: int = 100, tenant_slug: str = "default") -> List[Dict[str, Any]]:
    """Lists saved clients for a tenant with optional search filter."""
    t_slug = (tenant_slug or "default").strip().lower() or "default"
    with get_connection() as conn:
        cursor = conn.cursor()
        q = (search or "").strip()
        if q:
            like = f"%{q}%"
            cursor.execute(
                """SELECT * FROM saved_clients
                   WHERE COALESCE(tenant_slug, 'default') = ?
                     AND (client_name LIKE ? OR phone LIKE ? OR dob LIKE ?)
                   ORDER BY updated_at DESC LIMIT ?""",
                (t_slug, like, like, like, limit)
            )
        else:
            cursor.execute(
                "SELECT * FROM saved_clients WHERE COALESCE(tenant_slug, 'default') = ? ORDER BY updated_at DESC LIMIT ?",
                (t_slug, limit)
            )
        return [dict(r) for r in cursor.fetchall()]


def delete_saved_client(client_id: int, tenant_slug: str = "default") -> bool:
    """Deletes a saved client by ID (scoped to tenant)."""
    t_slug = (tenant_slug or "default").strip().lower() or "default"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM saved_clients WHERE id = ? AND COALESCE(tenant_slug, 'default') = ?",
            (client_id, t_slug)
        )
        conn.commit()
        return cursor.rowcount > 0


# ==========================================
# White-Label Multi-Tenant SaaS Helpers
# ==========================================

def _sanitize_slug(raw_slug: str) -> str:
    import re
    s = re.sub(r"[^a-z0-9-]+", "-", (raw_slug or "").strip().lower()).strip("-")
    if not s or s in ("studio", "admin", "api", "order"):
        raise ValueError("Invalid or reserved tenant slug.")
    return s


def get_tenant_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    """Fetches a tenant record by slug."""
    s = (slug or "default").strip().lower() or "default"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tenants WHERE slug = ?", (s,))
        row = cursor.fetchone()
        return dict(row) if row else None


def list_tenants() -> List[Dict[str, Any]]:
    """Lists all white-label numerologist tenants."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tenants ORDER BY CASE WHEN slug='default' THEN 0 ELSE 1 END, created_at DESC")
        return [dict(r) for r in cursor.fetchall()]


def create_tenant(data: Dict[str, Any]) -> Dict[str, Any]:
    """Creates a new white-label numerologist tenant account."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    slug = _sanitize_slug(data.get("slug") or data.get("consultant_name") or "")
    consultant_name = (data.get("consultant_name") or "").strip()
    brand_name = (data.get("brand_name") or f"{consultant_name}'s Vedic Numerology Studio").strip()
    if not consultant_name:
        raise ValueError("Consultant Name is required.")
    subtitle = (data.get("subtitle") or "Certified Vedic Numerologist & Vastu Consultant").strip()
    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()
    copyright_text = (data.get("copyright_text") or f"© {datetime.now().year} {consultant_name} · All Rights Reserved").strip()
    logo_url = (data.get("logo_url") or "").strip()
    accent_color = (data.get("accent_color") or "#7c3aed").strip()
    access_pin = (data.get("access_pin") or "1234").strip()
    plan_name = (data.get("plan_name") or "Pro").strip()
    status = (data.get("status") or "active").strip()
    pdf_quota = int(data.get("pdf_quota") if data.get("pdf_quota") is not None else -1)

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM tenants WHERE slug = ?", (slug,))
        if cursor.fetchone():
            raise ValueError(f"Tenant slug '{slug}' already exists.")
        cursor.execute("""
            INSERT INTO tenants (
                slug, brand_name, consultant_name, subtitle, phone, email,
                copyright_text, logo_url, accent_color, access_pin, plan_name,
                status, pdf_quota, pdf_count, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?)
        """, (
            slug, brand_name, consultant_name, subtitle, phone, email,
            copyright_text, logo_url, accent_color, access_pin, plan_name,
            status, pdf_quota, now, now
        ))
        conn.commit()
        return get_tenant_by_slug(slug)


def update_tenant(slug: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Updates an existing white-label tenant."""
    s = (slug or "").strip().lower()
    existing = get_tenant_by_slug(s)
    if not existing:
        raise ValueError(f"Tenant '{s}' not found.")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fields = [
        "brand_name", "consultant_name", "subtitle", "phone", "email",
        "copyright_text", "logo_url", "accent_color", "access_pin",
        "plan_name", "status", "pdf_quota"
    ]
    updates = []
    params = []
    for f in fields:
        if f in data and data[f] is not None:
            updates.append(f"{f} = ?")
            params.append(int(data[f]) if f == "pdf_quota" else str(data[f]).strip())
    if not updates:
        return existing
    updates.append("updated_at = ?")
    params.append(now)
    params.append(s)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE tenants SET {', '.join(updates)} WHERE slug = ?", tuple(params))
        conn.commit()
    return get_tenant_by_slug(s)


def delete_tenant(slug: str) -> bool:
    """Deletes a white-label tenant (cannot delete 'default')."""
    s = (slug or "").strip().lower()
    if s == "default":
        raise ValueError("Cannot delete the default master tenant.")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tenants WHERE slug = ?", (s,))
        conn.commit()
        return cursor.rowcount > 0


def increment_tenant_pdf_count(slug: str) -> None:
    """Increments the generated PDF counter for a tenant."""
    s = (slug or "default").strip().lower() or "default"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tenants SET pdf_count = COALESCE(pdf_count, 0) + 1, updated_at = ? WHERE slug = ?",
            (now, s)
        )
        conn.commit()


# Automatically initialize table on import
init_db()
