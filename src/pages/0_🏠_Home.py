import streamlit as st
from components.sidebar import render_sidebar
from components.footer import render_footer
import utils.helpers as helpers
from figures.rooms import plot_room_prices
from figures.sales import plot_bostadsratter_sales
from figures.summary import plot_bostadboratter_summary
from figures.villor_summary import plot_villor_summary
from figures.villor_sales import plot_villor_sales


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
        plot_bostadsratter_sales()
    
    with col2: 
        plot_room_prices()

    plot_bostadboratter_summary()

with tab2:
    plot_villor_sales()
    fig = plot_villor_summary()
    st.plotly_chart(fig,key="unique_id_10" ,use_container_width=True)
    pass



render_footer()

