import streamlit as st
from utils.helpers import get_sidebar_style

def render_sidebar():
    """Render a stylish sidebar with navigation"""
    
    # Apply custom sidebar styling
    st.markdown(get_sidebar_style(), unsafe_allow_html=True)
    
    
