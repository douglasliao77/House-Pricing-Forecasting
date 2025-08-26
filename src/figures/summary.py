import streamlit as st
import plotly.express as px
import utils.helpers as helpers
from utils.data_loader import DataLoader
import plotly.graph_objects as go

with st.spinner("📊 Loading data..."):
    df = DataLoader.load_bostadratter_summary()

def get_data():
    row = df.iloc[0]
    print(row)

    return row

def get_summary():
    # Example: use 3-month sales for bubble size
    fig = px.scatter(
        df,
        x="Prisutveckling 3m",
        y="Prisutveckling 12m",
        size="Antal sålda 3m",   # <-- must match exact column name
        color="Områden",
        text="Områden",
        size_max=80,
        labels={
            "Prisutveckling 3m": "Prisförändring 3m (%)",
            "Prisutveckling 12m": "Prisförändring 12m (%)",
            "Antal sålda 3m": "Antal försäljningar",
            "Kr/kvm 3m": "Kr/kvm"
        },
    )

    fig = helpers.plotly_title(fig, 
        "Market Quadrant: Short-term vs Long-term Price Change")


    fig.update_traces(textposition='top center')
    fig.update_layout(
        xaxis=dict(title="3-månaders prisutveckling (%)"),
        yaxis=dict(title="12-månaders prisutveckling (%)"),
        template="plotly_white",
        hovermode="closest"
    )

    fig.add_shape(type="line", x0=0, x1=0, y0=df["Prisutveckling 12m"].min(), y1=df["Prisutveckling 12m"].max(),
              line=dict(color="gray", dash="dash"))
    fig.add_shape(type="line", y0=0, y1=0, x0=df["Prisutveckling 3m"].min(), x1=df["Prisutveckling 3m"].max(),
                line=dict(color="gray", dash="dash"))


    return fig