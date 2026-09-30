# HealthCare AI — Appointment Manager

An **AI-powered**, fully **Streamlit-deployable** healthcare application for managing patient appointments, with a machine-learning no-show risk predictor and a **Gemini 2.5 Flash** conversational AI assistant.

---

## 🗂️ Project Structure

```
healthcare_app/
├── app.py                      # Main entry point
├── config.py                   # App-wide settings
├── requirements.txt            # Python dependencies
├── .streamlit/
│   ├── config.toml             # Streamlit theme
│   └── secrets.toml            # API keys (do not commit)
├── pages/
│   ├── booking.py              # Patient booking module
│   ├── admin.py                # Admin dashboard
│   ├── predictor.py            # ML risk predictor page
│   └── ai_assistant.py         # Gemini AI chat
└── utils/
    ├── database.py             # SQLite data layer + seeding
    ├── ml_model.py             # Gradient Boosting predictor
    └── gemini_client.py        # Gemini 2.5 Flash wrapper
```

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
cd healthcare_app
pip install -r requirements.txt
```

### 2. Add your Gemini API key
Edit `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "AIza..."
```
Get your **free** API key at [aistudio.google.com](https://aistudio.google.com).

### 3. Run the app
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deploy to Streamlit Cloud

1. Push this folder to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Point to `healthcare_app/app.py`
4. Add `GEMINI_API_KEY` in **Secrets** (Settings → Secrets)

---

## 📋 Features

### 📅 Booking Module
- Multi-specialty appointment scheduling (10 specialties)
- 15 time slots per day
- Real-time **ML no-show risk assessment** on every booking
- **AI-generated** personalised appointment confirmation (Gemini)
- Patient history lookup

### 🏥 Admin Dashboard *(password: `admin123`)*
- Live KPI metrics (total, scheduled, completed, no-shows, high-risk)
- Interactive charts: status pie, specialty bar, daily trend, risk distribution
- Filterable & searchable appointment table
- Per-appointment status management and admin notes
- **AI risk insight** for individual patients (Gemini)
- Train / retrain ML model with one click
- Batch risk scoring for all scheduled appointments

### 🔮 ML No-Show Risk Predictor
- **Gradient Boosting Classifier** (scikit-learn)
- 10 features: age, gender, advance-booking days, historical no-show rate, distance, SMS reminder, weekday, hour
- Interactive gauge chart for probability display
- Trained on 600 synthetic records seeded on first run
- Supports retraining from the admin panel

### 🤖 MediAssist AI (Gemini 2.5 Flash)
- Multi-turn health conversation
- Symptom → specialist recommendation
- Pre-appointment preparation tips
- Inline API key entry for demos
- 6 quick-start prompt buttons in the sidebar

---

## ⚙️ Configuration

| Variable | Default | Description |
|---|---|---|
| `GEMINI_API_KEY` | *(empty)* | Google Gemini API key |
| `ADMIN_PASSWORD` | `admin123` | Admin dashboard password |

Set via `.streamlit/secrets.toml` or environment variable.

---

## 🧠 ML Model Details

| Attribute | Value |
|---|---|
| Algorithm | Gradient Boosting (scikit-learn) |
| Features | 10 engineered features |
| Training data | 600 synthetic historical records |
| Target | No-Show probability (0–1) |
| Thresholds | Low < 30% ≤ Medium < 60% ≤ High |
| Persistence | `data/noshow_model.pkl` |

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| LLM | Google Gemini 2.5 Flash |
| ML | scikit-learn (Gradient Boosting) |
| Data | Pandas, NumPy |
| Charts | Plotly Express |
| Database | SQLite (built-in) |
| Language | Python 3.10+ |
