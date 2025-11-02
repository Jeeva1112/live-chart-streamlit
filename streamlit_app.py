import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from streamlit_navigation_bar import st_navbar
# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="Digital Finance Chart Studio", layout="wide",initial_sidebar_state="collapsed")

# ---------------------- STYLES ----------------------
styles = {
    "nav": {
        "background-color": "rgb(58, 55, 212)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
page = st_navbar(styles=styles)

with st.sidebar:
    st.write("Sidebar")
