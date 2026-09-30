# -*- coding: utf-8 -*-

"""
app.py
Main entry point for the Healthcare AI Appointment Manager.
Run with:  streamlit run app.py
"""

import os
import sys

# Ensure project root is importable
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st

from config import APP_TITLE, APP_ICON
from utils.database import init_db

# ══════════════════════════════════════════════════════════
#  Page configuration — MUST be first Streamlit call
# ══════════════════════════════════════════════════════════
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════
#  Initialise database (idempotent)
# ══════════════════════════════════════════════════════════
@st.cache_resource(show_spinner="Initialising database...")
def _init():
    init_db()
    return True

_init()

# ══════════════════════════════════════════════════════════
#  Navigation
# ══════════════════════════════════════════════════════════
PAGES = {
    "🏠 Home"                : "home",
    "📅 Book Appointment"    : "booking",
    "🏥 Admin Dashboard"     : "admin",
    "🔮 Risk Predictor"      : "predictor",
    "🤖 AI Assistant"        : "ai_assistant",
}

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"# {APP_ICON} HealthCare AI")
    st.markdown("**AI-Powered Appointment Manager**")
    st.markdown("---")

    selection = st.radio(
        "Navigate",
        list(PAGES.keys()),
        key="nav_selection",
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown(
        """
        <small>
        <b>Stack:</b> Streamlit · Gemini 2.5 Flash<br>
        Scikit-learn · Plotly · SQLite<br><br>
        <b>ML Model:</b> Gradient Boosting<br>
        <b>LLM:</b> Google Gemini 2.5 Flash
        </small>
        """,
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════
#  Page routing
# ══════════════════════════════════════════════════════════
page = PAGES[selection]

if page == "home":
    # ── Landing page ──────────────────────────────────────
    st.title("🏥 HealthCare AI — Appointment Manager")
    st.markdown("### AI-Powered Patient Appointment System with No-Show Risk Prediction")
    st.divider()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
<div style='background:#EBF5FB;padding:20px;border-radius:10px;text-align:center'>
<h2>📅</h2>
<h4>Book Appointment</h4>
<p>Schedule consultations with specialists. AI-assisted specialty suggestions.</p>
</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
<div style='background:#E9F7EF;padding:20px;border-radius:10px;text-align:center'>
<h2>🏠</h2>
<h4>Admin Dashboard</h4>
<p>Analytics, appointment management, risk overview and status updates.</p>
</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
<div style='background:#FEF9E7;padding:20px;border-radius:10px;text-align:center'>
<h2>🔮</h2>
<h4>Risk Predictor</h4>
<p>ML-powered no-show risk scoring with Gradient Boosting classifier.</p>
</div>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""
<div style='background:#F5EEF8;padding:20px;border-radius:10px;text-align:center'>
<h2>🤖</h2>
<h4>AI Assistant</h4>
<p>Gemini 2.5 Flash chat for symptoms, specialist guidance, and health Q&A.</p>
</div>""", unsafe_allow_html=True)

    st.divider()

    # Live stats
    from utils.database import get_stats
    stats = get_stats()
    st.markdown("### 📊 Live Statistics")
    s1, s2, s3, s4, s5 = st.columns(5)
    s1.metric("Total Appointments", stats["total"])
    s2.metric("Scheduled",          stats["scheduled"])
    s3.metric("Completed",          stats["completed"])
    s4.metric("No-Shows",           stats["noshow"])
    s5.metric("High Risk (Active)", stats["high_risk"])

    st.divider()

    # Feature highlights
    st.markdown("### ✨ Key Features")
    fc1, fc2 = st.columns(2)
    with fc1:
        st.markdown("""
**🧠 Machine Learning**
- Gradient Boosting no-show predictor
- Trains on your own appointment history
- 10 engineered features including historical no-show rate, advance booking days, distance, and SMS reminders
- Live batch scoring for all scheduled appointments

**📅 Smart Booking**
- Multi-specialty appointment scheduling
- Real-time risk assessment on booking
- AI-generated appointment confirmation summaries
- Patient history lookup
""")
    with fc2:
        st.markdown("""
**🤖 Gemini 2.5 Flash AI**
- Multi-turn health chat assistant
- Symptom-to-specialist recommendation
- AI risk explanation for high-risk patients
- Pre-appointment preparation guidance

**🏠 Admin Control Center**
- Filterable appointment table
- Status management (Scheduled → Completed / No-Show / Cancelled)
- Analytics charts (status, specialty, daily trend, risk)
- Admin notes per appointment
""")

    st.divider()
    st.markdown("""
<div style='background:#F8F9FA;padding:15px;border-radius:8px;border-left:4px solid #2E86AB'>
<b>🚀 Quick Start:</b><br>
1. Navigate to <b>📅 Book Appointment</b> to create a test booking<br>
2. Visit <b>🏥 Admin Dashboard</b> (password: <code>admin123</code>) to see analytics<br>
3. Try the <b>🔮 Risk Predictor</b> for manual risk scoring<br>
4. Configure your Gemini API key and chat with the <b>🤖 AI Assistant</b>
</div>
""", unsafe_allow_html=True)

elif page == "booking":
    from pages.booking import show
    show()

elif page == "admin":
    from pages.admin import show
    show()

elif page == "predictor":
    from pages.predictor import show
    show()

elif page == "ai_assistant":
    from pages.ai_assistant import show
    show()
