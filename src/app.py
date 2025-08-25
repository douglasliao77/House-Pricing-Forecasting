# import dash
# from dash import dcc, html
# import dash_bootstrap_components as dbc
# import pandas as pd
# import plotly.express as px
# from dash.dependencies import Input, Output, State
# from layout import get_layout, accent 
# from pages.bostadsratten import bostadratten

# app = dash.Dash(
#     __name__,
#     external_stylesheets=[dbc.themes.CYBORG],
#     suppress_callback_exceptions=True
# )

# dcc.Dropdown(
#     id="period-selector",
#     options=[
#         {"label": "3 månader", "value": "3m"},
#         {"label": "12 månader", "value": "12m"},
#     ],
#     value="3m",  # default
#     clearable=False,
#     style={"width": "200px"}
# )


# app.layout = html.Div([
#     get_layout(), 
#     bostadratten
# ])

# if __name__ == "__main__":
#     app.run(debug=True)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- Dummy Data ---
data = {
    "Områden": ["Riket", "Stockholm", "Göteborg", "Malmö"],
    "Medelpris kr": [2900000, 4200000, 3100000, 2500000],
    "Prisutveckling (%)": [-2.1, -3.8, 0.8, 2.2],
    "Medelpris kr 12m": [2970000, 4260000, 3130000, 2510000],
    "Prisutveckling (%) 12m": [-0.1, -0.1, 0, 3.8],
    "Antal sålda": [25104, 9120, 2781, 2551],
    "Antal sålda 12m": [107937, 42419, 11996, 10353]
}

df = pd.DataFrame(data)

st.title("Real Estate Dashboard")

# --- Row 1: 3-month vs 12-month Price/Change ---
col1, col2 = st.columns([1,1])

with col1:
    st.subheader("3 månader")
    fig1 = px.scatter(
        df,
        x="Medelpris kr",
        y="Prisutveckling (%)",
        size="Medelpris kr",
        text="Områden",
        color="Prisutveckling (%)",
        color_continuous_scale="RdYlGn",
        size_max=150,
        hover_data=["Medelpris kr", "Prisutveckling (%)"]
    )
    fig1.update_traces(textposition='middle center')
    fig1.update_layout(height=600, margin=dict(l=20,r=20,t=50,b=20))
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("12 månader")
    fig2 = px.scatter(
        df,
        x="Medelpris kr 12m",
        y="Prisutveckling (%) 12m",
        size="Medelpris kr 12m",
        text="Områden",
        color="Prisutveckling (%) 12m",
        color_continuous_scale="RdYlGn",
        size_max=150,
        hover_data=["Medelpris kr 12m", "Prisutveckling (%) 12m"]
    )
    fig2.update_traces(textposition='middle center')
    fig2.update_layout(height=600, margin=dict(l=20,r=20,t=50,b=20))
    st.plotly_chart(fig2, use_container_width=True)

# --- Row 2: Volume vs Price for 3-month ---
st.subheader("Antal sålda vs Medelpris (3 månader)")
fig3 = px.scatter(
    df,
    x="Medelpris kr",
    y="Antal sålda",
    size="Antal sålda",
    text="Områden",
    color="Prisutveckling (%)",
    color_continuous_scale="RdYlGn",
    size_max=100,
    hover_data=["Medelpris kr", "Prisutveckling (%)", "Antal sålda"]
)
fig3.update_traces(textposition='middle center')
fig3.update_layout(height=500, margin=dict(l=20,r=20,t=50,b=20))
st.plotly_chart(fig3, use_container_width=True)

# --- Row 3: Volume vs Price for 12-month ---
st.subheader("Antal sålda vs Medelpris (12 månader)")
fig4 = px.scatter(
    df,
    x="Medelpris kr 12m",
    y="Antal sålda 12m",
    size="Antal sålda 12m",
    text="Områden",
    color="Prisutveckling (%) 12m",
    color_continuous_scale="RdYlGn",
    size_max=100,
    hover_data=["Medelpris kr 12m", "Prisutveckling (%) 12m", "Antal sålda 12m"]
)
fig4.update_traces(textposition='middle center')
fig4.update_layout(height=500, margin=dict(l=20,r=20,t=50,b=20))
st.plotly_chart(fig4, use_container_width=True)
