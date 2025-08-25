import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math
from dash.dependencies import Input, Output
from figures.quadrant import quadrant_momentum
from figures.prisutveckling import pris_utveckling

# -------------------------------
# Read data
# -------------------------------
BASE_PATH = "data/bostadsratter/"

rum = pd.read_csv(BASE_PATH + "rum.csv")
rum = rum.melt(id_vars="Label", var_name="Series", value_name="Value")

df = pd.read_excel(
    BASE_PATH + "Svensk Mäklarstatistik Tabell Riket.xlsx",
)

header_values = [col if not col.startswith("Unnamed") else "" for col in df.columns]
super_headers = {
    "3 månader": range(1, 5),       
    "12 månader": range(5, len(df.columns))  
}

columns = []
for i, col in enumerate(df.columns):
    header_top = ""
    for text, col_range in super_headers.items():
        if i in col_range:
            header_top = text
            break
    columns.append({"name": [header_top], "id": col})


fig2 = px.line(
    rum,
    x="Label",
    y="Value",
    color="Series",
    markers=True     
)

fig2.add_annotation(
    text="källa: Svensk Mäklarstatistik",
    xref="paper", yref="paper",
    x=1, y=1,
    font=dict(color="#CCCCCC", size=12)
)

fig2.update_traces(
    hovertemplate='%{y:.0f} kr/kvm<br>',  # Only show y-value
)
fig2.update_layout(
    title={
        'text': "Kvadratmeterpriser per lägenhetsstorlek",
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    plot_bgcolor="#1F1F1F",
    paper_bgcolor="#1F1F1F",
    font=dict(family="Arial", size=14, color="#FFFFFF"),
    xaxis=dict(showgrid=False, color="#FFFFFF"),
    yaxis=dict(showgrid=False, color="#FFFFFF"),
    hovermode="x unified",
    xaxis_title="",
    yaxis_title="Pris kr/kvm",
)

rum_utveckling = html.Div([
    dcc.Graph(figure=fig2)
    ], style={
        "flex": "1 1 45%",
        "width": "50%",    
        "min-width": "500px",
        "padding": "20px",
        "border-radius": "10px",
    })
