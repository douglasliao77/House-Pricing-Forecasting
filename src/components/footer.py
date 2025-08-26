import streamlit as st

def render_footer():
    """Render application footer"""
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>Built on a rainy night in Stoke | © 2025 bostadspriser.streamlit.app</p>
    </div>
    """, unsafe_allow_html=True)