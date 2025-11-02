import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# ---------------------- CONFIG ----------------------
st.set_page_config(page_title="Chart Studio", layout="wide")

# ---------------------- CUSTOM STYLES ----------------------
st.markdown("""
    <style>
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
        }
        .stApp {
            background-color: #0f1116;
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .sidebar .sidebar-content {
            width: 280px;
        }
        .css-1v3fvcr {padding-top: 0 !important;}
        .nav-tabs {
            background-color: #003366;
            color: white;
            border-radius: 6px;
            padding: 0.6rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
with st.container():
    col1, col2 = st.columns([0.15, 0.85])
    with col1:
        st.image("philips.svg", width=70)
    with col2:
        st.markdown("<h3 style='color:white;margin-top:10px;'>📊 Digital Finance Chart Studio</h3>", unsafe_allow_html=True)

# ---------------------- NAVBAR ----------------------
selected = option_menu(
    None,
    ["Dashboard", "Data", "Settings"],
    icons=["bar-chart", "database", "gear"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "#003366", "border-radius": "5px"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {
            "color": "white",
            "font-size": "15px",
            "margin": "0px",
            "padding": "10px 25px",
        },
        "nav-link-selected": {"background-color": "#0073e6"},
    },
)

# ---------------------- DATA LOAD ----------------------
if selected == "Dashboard":
    st.write("")
    uploaded_file = st.file_uploader("📁 Upload CSV or JSON file", type=["csv", "json"])

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_json(uploaded_file)
    else:
        st.info("Using sample data (Gapminder 2007).")
        df = px.data.gapminder().query("year == 2007")

    # ---------------------- CONTROL PANEL ----------------------
    with st.sidebar:
        st.markdown("### ⚙️ Chart Controls")
        chart_type = st.selectbox(
            "Chart Type",
            [
                "Bar", "Line", "Area", "Scatter", "Pie", "Donut",
                "Histogram", "Box", "Heatmap", "Treemap"
            ]
        )
        x_axis = st.selectbox("X-axis", df.columns)
        y_axis = st.multiselect("Y-axis", df.columns)
        color_col = st.selectbox("Color (optional)", [None] + df.columns.tolist())
        theme = st.selectbox(
            "Theme",
            ["plotly", "plotly_white", "plotly_dark", "seaborn", "ggplot2", "simple_white"]
        )
        color_scheme = st.selectbox(
            "Color Palette",
            ["Plotly", "Viridis", "Cividis", "Plasma", "Turbo", "RdBu", "Earth"]
        )
        show_legend = st.checkbox("Show Legend", True)
        smooth_line = st.checkbox("Smooth Lines (Line/Area)", False)

    # ---------------------- CHART GENERATION ----------------------
    fig = None

    # Define color args properly
    color_args = {}
    if chart_type in ["Heatmap"]:  # continuous color scale
        color_args = {"color_continuous_scale": color_scheme}
    else:
        color_args = {"color_discrete_sequence": px.colors.qualitative.Plotly}

    if chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis, color=color_col, template=theme, **color_args)
    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis, color=color_col, template=theme, **color_args)
        if smooth_line:
            fig.update_traces(line_shape="spline")
    elif chart_type == "Area":
        fig = px.area(df, x=x_axis, y=y_axis, color=color_col, template=theme, **color_args)
    elif chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis[0] if y_axis else None, color=color_col, template=theme, **color_args)
    elif chart_type == "Pie":
        fig = px.pie(df, names=x_axis, values=y_axis[0] if y_axis else None, template=theme)
    elif chart_type == "Donut":
        fig = px.pie(df, names=x_axis, values=y_axis[0] if y_axis else None, hole=0.5, template=theme)
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis, color=color_col, template=theme, **color_args)
    elif chart_type == "Box":
        fig = px.box(df, x=x_axis, y=y_axis[0] if y_axis else None, color=color_col, template=theme, **color_args)
    elif chart_type == "Heatmap":
        fig = px.density_heatmap(df, x=x_axis, y=y_axis[0] if y_axis else None, template=theme, color_continuous_scale=color_scheme)
    elif chart_type == "Treemap":
        fig = px.treemap(df, path=[x_axis, color_col] if color_col else [x_axis], values=y_axis[0] if y_axis else None, template=theme)

    if fig:
        fig.update_layout(
            title=dict(text=f"{chart_type} Chart", x=0.5, font=dict(size=20)),
            legend=dict(orientation="h", y=-0.2, x=0.5, xanchor="center", yanchor="top") if show_legend else dict(visible=False),
            margin=dict(t=30, b=50),
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please select at least one Y-axis column.")


# ---------------------- DATA TAB ----------------------
elif selected == "Data":
    st.subheader("📊 Data Preview")
    uploaded_file = st.file_uploader("Upload CSV or JSON file", type=["csv", "json"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_json(uploaded_file)
        st.dataframe(df)
    else:
        st.info("Upload a dataset to preview here.")

# ---------------------- SETTINGS TAB ----------------------
elif selected == "Settings":
    st.subheader("⚙️ App Settings")
    st.write("Here you can add branding, themes, or default behavior options later.")
