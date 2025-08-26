import streamlit as st
from datetime import datetime

def render_header():
    """Render application header"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown(f"### 📅 {datetime.now().strftime('%B %d, %Y')}")
    
    with col2:
        st.markdown("<h1 style='text-align: center;'>My Streamlit Dashboard</h1>", 
                   unsafe_allow_html=True)
    
    with col3:
        if st.button("🔔 Notifications (3)"):
            st.success("Showing notifications...")
    
    st.markdown("---")