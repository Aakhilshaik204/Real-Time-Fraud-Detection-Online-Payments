import streamlit as st

def show_contact():
    st.markdown("""
    <style>
    body, .stApp {
        color: #fff !important;
    }
    .contact-title {
        color: #40a9ff;
        font-weight: 800;
        font-size: 2.1rem;
        margin-bottom: 0.5rem;
    }
    .contact-section, em, span, a {
        color: #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='contact-title'>📬 Contact</div>", unsafe_allow_html=True)
    st.markdown("<div class='contact-section'><b>Author:</b> <span>Aakhil Shaik</span><br><b>Email:</b> <span>aakhilshaik204@gmail.com</span><br><b>GitHub:</b> <a href='https://github.com/Aakhilshaik204' target='_blank'>github</a></div>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top: 1.5rem;'><em>For questions, feedback, or collaboration opportunities, feel free to reach out!<br>Thank you for using the Online Fraud Detection System! ✨</em></div>", unsafe_allow_html=True) 