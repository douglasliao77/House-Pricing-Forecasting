import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import DataLoader

# Set page config (if needed for this specific page)
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard")

# Load sample data
data = DataLoader.load_sample_data()
metrics = DataLoader.get_metrics()

# Display metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Users", metrics['total_users'])
with col2:
    st.metric("Active Users", metrics['active_users'])
with col3:
    st.metric("Conversion Rate", f"{metrics['conversion_rate']*100:.1f}%")
with col4:
    st.metric("Revenue", f"${metrics['revenue']:,.2f}")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Value Distribution by Category")
    fig = px.box(data, x='Category', y='Value1')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Time Series Data")
    time_data = data.groupby('Date')['Value2'].mean().reset_index()
    st.line_chart(time_data, x='Date', y='Value2')

# Data table
st.subheader("Raw Data Preview")
st.dataframe(data.head(10), use_container_width=True)