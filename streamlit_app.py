import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Chart Studio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <style>
        header, footer {visibility: hidden;}
        .stApp {
            background-color: #0f1116;
            color: white;
        }
        section[data-testid="stSidebar"] {
            background-color: #0f1116 !important;
            border-right: 1px solid #1e1e1e !important;
            padding: 1rem !important;
            width: 300px !important;
            visibility: visible !important;
            display: block !important;
        }
        section[data-testid="stSidebar"] * {
            color: white !important;
            font-size: 14px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
# Force sidebar render with visible widget(s)
with st.sidebar:
    st.title("⚙️ Chart Controls")
    chart_type = st.selectbox(
        "Chart Type",
        ["Bar", "Line", "Area", "Scatter", "Pie", "Donut",
         "Histogram", "Box", "Heatmap", "Treemap"]
    )
    st.write("You selected:", chart_type)
    st.info("✅ Sidebar rendered successfully")

# ---------------- MAIN BODY ----------------
st.title("📊 Digital Finance Chart Studio")
st.write("This is your main workspace area.")
