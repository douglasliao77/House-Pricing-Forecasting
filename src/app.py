import streamlit as st

# Set page config
st.set_page_config(
    page_title="Real Estate Analytics",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Immediately redirect to home page
st.switch_page("pages/0_🏠_Home.py")