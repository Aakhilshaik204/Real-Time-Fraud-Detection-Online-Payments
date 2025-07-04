import streamlit as st

def show_how_it_works():
    st.markdown(
        """
        <style>
        .how-title {
            color: #40a9ff;
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 0.7rem;
        }
        .how-section {
            color: #fff;
            font-size: 1.1rem;
            margin-bottom: 1.2rem;
        }
        .how-step {
            margin-bottom: 0.8rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<div class='how-title'>🔍 How It Works</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='how-section'>
        Our Online Fraud Detection System uses a two-stage AI approach to analyze your transaction:
        <ol>
            <li class='how-step'><b>Risk Score Calculation:</b> The system first evaluates your transaction details (such as amount, type, and other features) to generate a risk score. This score reflects the likelihood of the transaction being suspicious based on patterns learned from historical data.</li>
            <li class='how-step'><b>Fraud Prediction:</b> Using the risk score and other transaction features, a second AI model predicts whether the transaction is likely to be <b>legitimate</b> or <b>fraudulent</b>. This model is trained on real-world fraud data for high accuracy.</li>
        </ol>
        <b>What happens when you check a transaction?</b><br>
        <ul>
            <li>Your input is processed instantly on your device.</li>
            <li>The models analyze the data and return a result: <b>Legitimate</b> or <b>Fraudulent</b>.</li>
            <li>No data is stored or sent to any server—your privacy is protected.</li>
        </ul>
        <b>Why two models?</b><br>
        The risk score helps the main fraud detection model make more accurate predictions, especially for borderline cases.
        <br><br>
        <b>Technology Used:</b> XGBoost, Scikit-learn, Streamlit, Python
        </div>
        """,
        unsafe_allow_html=True
    ) 