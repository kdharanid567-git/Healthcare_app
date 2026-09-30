# -*- coding: utf-8 -*-

# ============================================================
#  config.py  –  Application-wide settings
# ============================================================
import os

# ── Gemini ────────────────────────────────────────────────
GEMINI_API_KEY   = os.getenv("GEMINI_API_KEY", "")   # set via env or Streamlit secrets
GEMINI_MODEL     = "gemini-2.5-flash"

# ── Database ──────────────────────────────────────────────
DB_PATH = os.path.join(os.path.dirname(__file__), "data", "healthcare.db")

# ── App meta ──────────────────────────────────────────────
APP_TITLE    = "🏥 HealthCare AI — Appointment Manager"
APP_ICON     = "🏥"
ADMIN_PASS   = os.getenv("ADMIN_PASSWORD", "admin123")   # change in production

# ── Appointment settings ──────────────────────────────────
SPECIALTIES = [
    "General Physician",
    "Cardiologist",
    "Dermatologist",
    "Neurologist",
    "Orthopaedic",
    "Gynaecologist",
    "Paediatrician",
    "Psychiatrist",
    "Ophthalmologist",
    "ENT Specialist",
]

APPOINTMENT_SLOTS = [
    "09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM",
    "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM",
    "02:00 PM", "02:30 PM", "03:00 PM", "03:30 PM",
    "04:00 PM", "04:30 PM", "05:00 PM",
]

STATUS_OPTIONS   = ["Scheduled", "Completed", "Cancelled", "No-Show"]
RISK_THRESHOLDS  = {"low": 0.30, "medium": 0.60}   # above 0.60 → high risk

# ── ML model ──────────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(__file__), "data", "noshow_model.pkl")

# ── Colour palette (used in charts) ───────────────────────
COLORS = {
    "primary"  : "#2E86AB",
    "success"  : "#27AE60",
    "warning"  : "#F39C12",
    "danger"   : "#E74C3C",
    "muted"    : "#95A5A6",
    "bg"       : "#F8F9FA",
}

RISK_COLORS = {
    "Low"    : "🟢",
    "Medium" : "🟡",
    "High"   : "🔴",
}
