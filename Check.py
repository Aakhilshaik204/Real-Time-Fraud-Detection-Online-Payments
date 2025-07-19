import streamlit as st
import joblib
import numpy as np
from pathlib import Path
from datetime import time, datetime

# Simulated user profile for adaptive rules (in real app, fetch from DB)
USER_PROFILE = {
    'usual_device': 'Mobile',
    'usual_location': 'India',
    'usual_hours': (8, 22),  # 8 AM to 10 PM
    'avg_amount': 1500,
    'max_amount': 10000,
    'account_age': 24,  # months
}

# Helper for explainability
RISK_EXPLANATIONS = {
    'risky_time': 'Transaction occurred during unusual hours for this user.',
    'device_change': 'Device type is different from user’s usual device.',
    'location_change': 'Location/Region is different from user’s usual region.',
    'high_risk_region': 'Region is flagged as high-risk for fraud.',
    'high_risk_payment': 'Payment method is considered high-risk.',
    'not_recurring_pattern': 'Non-recurring transaction but matches user’s past activity pattern.',
    'young_account': 'Account is very new and thus riskier.',
    'proxy_detected': 'Proxy or suspicious IP detected.',
    'unusual_amount': 'Transaction amount is much higher than user’s normal range.',
    'failed_txn_spike': 'Unusually high number of failed transactions recently.',
}

def show_check():
    st.markdown(
        """
        <style>
        body, .stApp {
            color: #fff !important;
        }
        .check-title {
            color: #40a9ff;
            font-size: 2.1rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            justify-content: center;
        }
        .check-desc, .stForm label, label {
            color: #fff !important;
            font-weight: 500 !important;
            font-size: 1.08rem !important;
        }
        .stButton > button {
            background-color: #1976d2 !important;
            color: #fff !important;
            font-weight: 700;
            border-radius: 8px;
            padding: 0.5rem 0;
            font-size: 1.08rem;
        }
        .stButton > button:hover {
            background-color: #1565c0 !important;
        }
        .risk-flag {
            display: inline-block;
            background: #ffebee;
            color: #c62828;
            border-radius: 6px;
            padding: 0.18em 0.7em;
            margin: 0.15em 0.3em 0.15em 0;
            font-size: 1.01em;
            font-weight: 600;
        }
        .risk-flag-green {
            display: inline-block;
            background: #e8f5e9;
            color: #2e7d32;
            border-radius: 6px;
            padding: 0.18em 0.7em;
            margin: 0.15em 0.3em 0.15em 0;
            font-size: 1.01em;
            font-weight: 600;
        }
        .explain-box {
            background: #23272f;
            border-radius: 8px;
            padding: 0.7em 1em;
            margin: 0.7em 0 1.2em 0;
            color: #fff;
            font-size: 1.04em;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown("<div class='check-title'>🔍 Check a Transaction</div>", unsafe_allow_html=True)
    st.markdown("<div class='check-desc'>Enter transaction details below to assess risk and detect potential fraud.</div>", unsafe_allow_html=True)

    with st.form("check_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Transaction Amount (₹)", min_value=0.0, step=0.01, format="%.2f")
            prev_fraud = st.selectbox("Previous Fraudulent Activity", ["No", "Yes"])
            txn_time = st.time_input("Transaction Time", value=time(12, 0))
            device_type = st.selectbox("Device Type", ["Mobile", "Desktop", "Tablet"])
            location = st.selectbox("Location/Region", ["India", "USA", "Europe", "Middle East", "Africa", "Other/International"])
        with col2:
            failed_7d = st.number_input("Failed Transaction Count (7d)", min_value=0, step=1)
            daily_count = st.number_input("Daily Transaction Count", min_value=0, step=1)
            payment_method = st.selectbox("Payment Method", ["UPI", "Credit Card", "Wallet", "Crypto"])
            recurring = st.radio("Is Recurring Transaction", ["Yes", "No"])
            account_age = st.number_input("Account Age (months)", min_value=0, step=1)
            proxy = st.radio("IP Address Region / Proxy Detected", ["No", "Yes"])
            unusual_amt = st.checkbox("Unusual Transaction Amount")
        submitted = st.form_submit_button("Predict", use_container_width=True)

    if submitted:
        # ML model logic (unchanged)
        X_risk = np.array([[amount, int(prev_fraud == "Yes"), failed_7d, daily_count]])
        risk_model_path = Path("models/risk_score_model.pkl")
        fraud_model_path = Path("models/xgb_fraud_model.pkl")
        if not (risk_model_path.exists() and fraud_model_path.exists()):
            st.error("Model files not found. Please ensure models are in the 'models/' folder.")
            return
        risk_model = joblib.load(risk_model_path)
        fraud_model = joblib.load(fraud_model_path)
        risk_score = float(risk_model.predict(X_risk)[0])
        X_fraud = np.hstack([X_risk, [[risk_score]]])
        is_fraud = fraud_model.predict(X_fraud)[0]

        # --- Advanced Rule-Based Layer (adaptive/context-aware) ---
        risk_flags = []
        explanations = []
        # 1. Adaptive risky time (user's usual hours)
        if not (USER_PROFILE['usual_hours'][0] <= txn_time.hour < USER_PROFILE['usual_hours'][1]):
            risk_flags.append('risky_time')
        # 2. Device change
        if device_type != USER_PROFILE['usual_device']:
            risk_flags.append('device_change')
        # 3. Location change
        if location != USER_PROFILE['usual_location']:
            risk_flags.append('location_change')
        # 4. High-risk region
        if location in ["Other/International", "Africa", "Middle East"]:
            risk_flags.append('high_risk_region')
        # 5. High-risk payment method
        if payment_method in ["Wallet", "Crypto"]:
            risk_flags.append('high_risk_payment')
        # 6. Not recurring but similar pattern (simulate: if not recurring and daily_count > 2)
        if recurring == "No" and daily_count > 2:
            risk_flags.append('not_recurring_pattern')
        # 7. Young account (adaptive)
        if account_age < 3:
            risk_flags.append('young_account')
        # 8. Proxy detected
        if proxy == "Yes":
            risk_flags.append('proxy_detected')
        # 9. Unusual amount (adaptive)
        if amount > USER_PROFILE['max_amount'] or (unusual_amt and amount > USER_PROFILE['avg_amount']*2):
            risk_flags.append('unusual_amount')
        # 10. Failed txn spike (adaptive)
        if failed_7d > 3:
            risk_flags.append('failed_txn_spike')

        # --- UI Output ---
        st.markdown(
            f"""
            <div style='color: #fff; margin-top: 1.5rem; text-align: center;'>
                <h3 style='color: {"#ff6f6f" if is_fraud else "#90ee90"}; margin: 0;'>
                    {'⚠️ Fraudulent Transaction' if is_fraud else '✅ Legitimate Transaction'}
                </h3>
            </div>
            """, unsafe_allow_html=True
        )
        # Show risk insights with explanations
        st.markdown("<h4 style='margin-top:1.2em;'>Risk Insights</h4>", unsafe_allow_html=True)
        if risk_flags:
            for flag in risk_flags:
                st.markdown(f"<span class='risk-flag'>{RISK_EXPLANATIONS[flag]}</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span class='risk-flag-green'>No additional risk signals detected</span>", unsafe_allow_html=True)

        # Show warning if model says Legitimate but >2 backend flags
        if not is_fraud and len(risk_flags) > 2:
            st.warning("\n⚠️ Model thinks it’s safe, but our system sees risky signals. Review before proceeding.")
        elif is_fraud:
            st.error("Fraud detected by model. Do not proceed with this transaction.")
        else:
            st.success("No fraud detected by model.")

        # --- User Feedback Mechanism ---
        st.markdown("<div class='explain-box'>Was this prediction correct? Help us improve by providing feedback below.</div>", unsafe_allow_html=True)
        feedback_col1, feedback_col2 = st.columns([1,2])
        with feedback_col1:
            user_feedback = st.radio("Your Feedback", ["Correct", "Incorrect", "Unsure"], key="feedback_radio")
        with feedback_col2:
            user_comment = st.text_input("Comments (optional)", key="feedback_comment")
        if st.button("Submit Feedback", use_container_width=True):
            st.success("Thank you for your feedback! (In a real app, this would be logged for review.)") 