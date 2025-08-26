import streamlit as st
import plotly.express as px
import utils.helpers as helpers
from utils.data_loader import DataLoader

def plot_room_prices():

    with st.spinner("📊 Loading data..."):
        rooms = DataLoader.load_bostadratter_room_price()

    fig = px.line(
            rooms,
            x="Datum",
            y="Pris",    
            color="Rooms",  
            markers=True,
        )
    fig.update_traces(
        hovertemplate="%{fullData.name}: %{y} kr/kvm <extra></extra>"
    )
    fig.update_layout(hovermode="x unified")
    fig = helpers.add_source(fig)
    fig = helpers.plotly_title(fig, 
                "Kvadratmeterpriser per lägenhetsstorlek")
    
    st.plotly_chart(fig, use_container_width=True)
    return fig