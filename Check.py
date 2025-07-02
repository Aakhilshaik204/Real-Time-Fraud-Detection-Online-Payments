import streamlit as st
import joblib
import numpy as np
from pathlib import Path

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
        with col2:
            failed_7d = st.number_input("Failed Transaction Count (7d)", min_value=0, step=1)
            daily_count = st.number_input("Daily Transaction Count", min_value=0, step=1)
        submitted = st.form_submit_button("Predict", use_container_width=True)

    if submitted:
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
        st.markdown(
            f"""
            <div style='color: #fff; margin-top: 1.5rem; text-align: center;'>
                <h3 style='color: {"#ff6f6f" if is_fraud else "#90ee90"}; margin: 0;'>
                    {'⚠️ Fraudulent Transaction' if is_fraud else '✅ Legitimate Transaction'}
                </h3>
            </div>
            """, unsafe_allow_html=True
        ) 