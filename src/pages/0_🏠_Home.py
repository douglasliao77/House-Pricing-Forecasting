import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from components.sidebar import render_sidebar
from components.footer import render_footer
import utils.helpers as helpers
from utils.data_loader import DataLoader
from figures.price_development import get_price_development
from figures.rooms import get_room_prices
from figures.sales import get_sales
from figures.bubble import get_summary


# Page configuration
st.set_page_config(
    page_title="Bostadspriser Sverige - Marknadsanalys",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
helpers.load_css()

# Render sidebar and get selected page
selected_page = render_sidebar()

st.markdown("""
<div style="text-align: center;">
    <h1 style="color: white; font-size: 4rem; margin-bottom: 0.5rem;">
        🏠 Bostadspriser i Sverige
    </h1>
    <h2 style="color: #ccc; font-size: 1.8rem; font-weight: 400; margin-top: 0;">
        Analys av bostadsmarknaden i hela Sverige
    </h2>
</div>
""", unsafe_allow_html=True)


tab1, tab2 = st.tabs(["Bostadsrätter", "Villor"])
helpers.style_tabs()

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        fig = get_sales()
        st.plotly_chart(fig, use_container_width=True)
    
    with col2: 
        fig = get_room_prices()
        st.plotly_chart(fig, use_container_width=True)

    fig = get_summary()
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    pass
render_footer()