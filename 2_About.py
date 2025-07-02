import streamlit as st

def show_about():
    st.markdown("""
    <style>
    body, .stApp {
        color: #fff !important;
    }
    .about-title {
        color: #40a9ff;
        font-weight: 800;
        font-size: 2.1rem;
        margin-bottom: 0.5rem;
    }
    .about-section, .about-section-title, ul, li, em {
        color: #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='about-title'>ℹ️ About the Online Fraud Detection System</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='about-section'>
    Welcome to the Online Fraud Detection System, an AI-powered Streamlit web application designed to identify potentially fraudulent transactions in real-time. This intelligent system accepts key transaction details such as amount, prior fraudulent activity, failed transaction history, and daily activity, then calculates a risk score to assess the likelihood of fraud.<br><br>
    Built as part of a capstone project, the system uses a two-stage machine learning approach: a regression model first predicts the risk factor, and a classification model then determines whether the transaction is legitimate or fraudulent. The app offers an interactive and user-friendly interface, making fraud detection both accessible and insightful. While based on synthetic data, the application reflects realistic scenarios and showcases the power of AI in digital security.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='about-section-title'>📊 Dataset</div>", unsafe_allow_html=True)
    st.markdown("<ul style='font-size: 1.08rem; font-weight: 500;'><li>The models are trained on a synthetic dataset simulating real-world transaction patterns, including features like transaction amount, previous fraud history, and transaction frequency.</li></ul>", unsafe_allow_html=True)
    st.markdown("<div class='about-section-title'>🚀 Motivation</div>", unsafe_allow_html=True)
    st.markdown("<ul style='font-size: 1.08rem; font-weight: 500;'><li>Online fraud is a growing threat. Early detection can save money and protect users.</li><li>This project demonstrates how AI can be used to automate and improve fraud detection.</li></ul>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top: 2rem;'><em>Built by <b>Aakhil Shaik</b>.</em></div>", unsafe_allow_html=True) 