import streamlit as st

st.set_page_config(page_title="Sidebar Test", layout="wide", initial_sidebar_state="expanded")

st.markdown("<h3 style='color:white;'>Sidebar Visibility Test</h3>", unsafe_allow_html=True)

st.markdown("""
<style>
.sidebar .sidebar-content { width: 280px !important; background-color: #0f1116 !important; }
section[data-testid="stSidebar"] { background-color: #0f1116 !important; border-right: 1px solid #1e1e1e; width: 280px !important; display:block !important; }
section[data-testid="stSidebar"] * { color: white !important; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ Sidebar Test")
    st.selectbox("Select option", ["One", "Two", "Three"])
    st.info("✅ Sidebar visible!")

st.write("Main content area")
