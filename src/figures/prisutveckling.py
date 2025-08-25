import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math
from dash.dependencies import Input, Output

BASE_PATH = "data/bostadsratter/"

BASE_PATH = "data/bostadsratter/"

prisutveckling = pd.read_csv(BASE_PATH + "prisutveckling.csv")

fig1 = px.line(
    prisutveckling, 
    x="Label", 
    y="Pris", 
    markers=True,
    labels={"Value": "Pris (kr/kvm)", "Label": "Tid", "Series": "Serie"},
)

fig1.add_annotation(
    text="källa: Svensk Mäklarstatistik",
    xref="paper", yref="paper",
    x=1, y=1,
    font=dict(color="#CCCCCC", size=12)
)

fig1.update_traces(
    hovertemplate='%{y:.0f} kr<br>', 
)

fig1.update_layout(
    title={
        'text': "Prisutveckling",
        'x':0.5, 
        'xanchor': 'center',
        'yanchor': 'top'
    },
    plot_bgcolor="#1F1F1F",
    paper_bgcolor="#1F1F1F",
    font=dict(family="Arial", size=14, color="#FFFFFF"),
    xaxis=dict(showgrid=False, color="#FFFFFF"),  # No grid
    yaxis=dict(showgrid=False, color="#FFFFFF"),
    xaxis_title="",
    yaxis_title="Pris (SEK)",
    hovermode="x unified",
    legend=dict(
        orientation="h",
        y=-0.2,
        x=0.5,
        xanchor="center"
    )
)

pris_utveckling = html.Div([
    dcc.Graph(figure=fig1)
    ], style={
        "flex": "1 1 45%",
        "width": "50%",  
        "min-width": "500px",  
        "padding": "20px",
        "border-radius": "10px",
    })