import streamlit as st
import plotly.express as px
import utils.helpers as helpers
from utils.data_loader import DataLoader

def get_price_development():

    with st.spinner("📊 Loading data..."):
        price_development = DataLoader.load_bostadsratter_data()

    fig = px.line(price_development, x="Datum", y="Pris",
                            color_discrete_sequence=['#00D4AA'])
    fig = helpers.plotly_title(fig, "Prisutveckling")
    fig.update_traces(
        hovertemplate="%{fullData.name}: %{y:.0f} kr/kvm<extra></extra>"
    )
    fig.update_layout(hovermode="x unified")
    fig = helpers.add_source(fig)
    return fig