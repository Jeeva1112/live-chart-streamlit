import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Philips Digital Chart Studio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------- CUSTOM STYLES ----------------------
st.markdown("""
    <style>
        .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 0.5rem !important;
        }
        header, footer {visibility: hidden;}

        .stApp {
            background-color: #0f1116;
            color: white !important;
        }

        section[data-testid="stSidebar"] {
            background-color: #0f1116 !important;
            border-right: 1px solid #1e1e1e !important;
            width: 280px !important;
            padding: 1rem !important;
        }
        section[data-testid="stSidebar"] * {
            color: white !important;
            font-size: 14px !important;
        }

        button[kind="header"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
with st.container():
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.image("philips.svg", width=60)
    with col2:
        st.markdown(
            "<h3 style='color:white;margin-top:10px;'>📊 Digital Finance Chart Studio</h3>",
            unsafe_allow_html=True
        )

# ---------------------- SIDEBAR (place it after header) ----------------------
with st.sidebar:
    st.markdown("### ⚙️ Chart Controls")
    chart_type = st.selectbox(
        "Chart Type",
        [
            "Bar", "Line", "Area", "Scatter", "Pie", "Donut",
            "Histogram", "Box", "Heatmap", "Treemap"
        ]
    )
    st.success("✅ Sidebar is now visible!")

# ---------------------- MAIN BODY ----------------------
st.write("This is your main workspace area.")
