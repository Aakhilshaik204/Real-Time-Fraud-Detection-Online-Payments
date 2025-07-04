import streamlit as st
import importlib
from pathlib import Path

# Set global background color to black
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #111 !important;
    }
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: #181c24 !important;
        color: #fff !important;
        border-right: 1.5px solid #222;
    }
    .sidebar-title {
        color: #40a9ff;
        font-size: 1.5rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        text-align: left;
        letter-spacing: 1px;
    }
    .sidebar-tagline {
        color: #fff;
        font-size: 1.02rem;
        margin-bottom: 1.5rem;
        margin-top: -0.5rem;
    }
    .sidebar-footer {
        color: #888;
        font-size: 0.95rem;
        margin-top: 2.5rem;
        text-align: left;
    }
    .sidebar-radio label {
        color: #fff !important;
        font-weight: 600 !important;
        font-size: 1.08rem !important;
        padding-left: 0.3rem;
    }
    .sidebar-radio .stRadio > div {
        gap: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Online Fraud Detection System", page_icon="🛡️", layout="centered")

# Enhanced Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-title">🛡️ Fraud Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">AI-powered security for your transactions</div>', unsafe_allow_html=True)
    st.markdown('---')
    page = st.radio(
        "Go to",
        ["Home", "Check a Transaction", "About","How It Works", "Contact"],
        key="sidebar-radio"
    )
    st.markdown('---')
    st.markdown('<div class="sidebar-footer">Built<br>by <b>Aakhil Shaik</b></div>', unsafe_allow_html=True)

pages = {
    "Home": ("Home", "show_home"),
    "Check a Transaction": ("Check", "show_check"),
    "About": ("2_About", "show_about"),
    "Contact": ("3_Contact", "show_contact"),
    "How It Works": ("HowItWorks", "show_how_it_works"),
}

module_name, func_name = pages[page]
mod = importlib.import_module(module_name)
getattr(mod, func_name)() 