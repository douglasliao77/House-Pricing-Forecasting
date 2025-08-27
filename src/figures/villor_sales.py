import streamlit as st
import plotly.express as px
import utils.helpers as helpers
from utils.data_loader import DataLoader
import plotly.graph_objects as go

def plot_villor_sales():

    with st.spinner("📊 Loading data..."):
        df = DataLoader.load_villor_sales()

    fig = go.Figure()

    # 1. Add bars first
    fig.add_trace(go.Bar(
        x=df["Månad"],
        y=df["antal försäljningar"],
        name="Antal försäljningar",
        yaxis="y2",
        marker_color="rgba(100,149,237,0.6)",
        zorder=1
    ))

    # 2. Add line last (so it's above bars)
    fig.add_trace(go.Scatter(
        x=df["Månad"],
        y=df["K/T"],
        name="K/T",
        mode="lines+markers",
        line=dict(color="firebrick", width=3),
        zorder=2
    ))

    # Layout
    fig.update_layout(
        xaxis=dict(title="Månad"),
        yaxis=dict(title="K/T"),
        yaxis2=dict(title="Antal försäljningar", overlaying="y", side="right"),
        template="plotly_white",
        legend=dict(
            orientation="h", 
            y=1.0,           
            x=0.5,          
            xanchor='center',  
            yanchor='bottom'  
            ),
        hovermode="x unified"
    )
    fig = helpers.add_source(fig)
    fig = helpers.plotly_title(fig, 
                "Köpeskillingskoefficienten och Försäljningsvolym")
    st.plotly_chart(fig,key="unique_id_9", use_container_width=True)
    return fig