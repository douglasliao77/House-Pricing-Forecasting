import streamlit as st
import plotly.express as px
import utils.helpers as helpers
from utils.data_loader import DataLoader
import plotly.graph_objects as go


def plot_villor_summary():
    with st.spinner("📊 Loading data..."):
        df = DataLoader.load_villor_summary()   

    values = df.iloc[0]
    st.subheader("3 månader")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Antalet sålda", values["Antal sålda 3m"])
    with col2:
        st.metric("kr/kvm", values["Kr/kvm 3m"])
    with col3:
        st.metric("Medelpriset", values["Medelpris kr 3m"])
    with col4:
        st.metric("Prisutveckling", values["Prisutveckling 3m"])

    st.subheader("12 månader")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Antalet sålda", values["Antal sålda 12m"])
    with col2:
        st.metric("kr/kvm", values["Kr/kvm 12m"])
    with col3:
        st.metric("Medelpriset", values["Medelpris kr 12m"])
    with col4:
        st.metric("Prisutveckling", values["Prisutveckling 12m"])

    fig = px.scatter(
        df,
        x="Prisutveckling 3m",
        y="Prisutveckling 12m",
        size="Antal sålda 3m",   
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
        "Marknadskvadrant: Korttids- vs Långtidsprisförändring")


    fig.update_traces(textposition='top center')
    fig.update_layout(
        xaxis=dict(title="3-månaders prisutveckling (%)"),
        yaxis=dict(title="12-månaders prisutveckling (%)"),
        template="plotly_white",
        hovermode="closest"
    )
    fig = helpers.add_source(fig)
    fig.add_shape(type="line", x0=0, x1=0, y0=df["Prisutveckling 12m"].min(), y1=df["Prisutveckling 12m"].max(),
              line=dict(color="gray", dash="dash"))
    fig.add_shape(type="line", y0=0, y1=0, x0=df["Prisutveckling 3m"].min(), x1=df["Prisutveckling 3m"].max(),
                line=dict(color="gray", dash="dash"))


    return fig