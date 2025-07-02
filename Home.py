import streamlit as st

def show_home():
    st.markdown(
        """
        <style>
        body, .stApp {
            color: #fff !important;
        }
        .main-title {
            color: #40a9ff;
            font-size: 2.7rem;
            font-weight: 900;
            letter-spacing: 1px;
            margin-bottom: 0.5rem;
        }
        .main-subtitle, .main-desc, .main-navhint, .main-extra {
            color: #fff !important;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown("<div class='main-title'>🛡️ Online Fraud Detection System</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-subtitle'>Secure your transactions with AI-powered fraud detection</div>", unsafe_allow_html=True)
    st.markdown("<div class='main-desc'>This project leverages machine learning to identify potentially fraudulent online transactions in real time. Enter transaction details and get instant feedback on risk and legitimacy.</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='main-extra' style='margin-top:1.5rem; font-size:1.08rem;'>
        <b>How it works:</b> Our system uses a two-stage AI model: first, it calculates a risk score based on your transaction details, then it predicts whether the transaction is likely to be legitimate or fraudulent.<br><br>
        <b>Why use this app?</b> Early fraud detection can help protect your finances and personal information. This tool is designed for both educational and practical use, demonstrating the power of AI in digital security.<br><br>
        <b>Privacy Note:</b> All data you enter stays on your device and is not stored or shared. Your privacy and security are our top priorities.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='main-navhint' style='margin-top:2.2rem; font-size:1.13rem; font-weight:700;'>✨ To check a transaction, use the sidebar navigation! 🧭</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div style='margin-top: 2.5rem; text-align: center; color: #444;'>
        <hr style='border: none; border-top: 1px solid #bbdefb; margin: 1.5rem 0;'>
        <span>Built by <b>Aakhil Shaik</b></span>
    </div>
    """, unsafe_allow_html=True) 