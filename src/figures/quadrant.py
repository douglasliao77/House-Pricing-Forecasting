import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math
from dash.dependencies import Input, Output

BASE_PATH = "data/bostadsratter/"

df2 = pd.read_excel(
    BASE_PATH + "Svensk Mäklarstatistik Tabell Riket.xlsx",
    header=1 
)

df_3m = df2[['Områden', 'Medelpris kr', 'Prisutveckling (%)']].copy()
df_12m = df2[['Områden', 'Medelpris kr.1', 'Prisutveckling (%).1']].copy()

# Rename columns for clarity
df_3m.columns = ['Områden', 'Medelpris', 'Prisutveckling']
df_12m.columns = ['Områden', 'Medelpris', 'Prisutveckling']

# Add period column
df_3m['Period'] = '3 månader'
df_12m['Period'] = '12 månader'

df_quadrant = pd.DataFrame({
    'Områden': df_3m['Områden'],
    'Medelpris_3M': df_3m['Medelpris'],
    'Prisutveckling_3M': df_3m['Prisutveckling'],
    'Medelpris_12M': df_12m['Medelpris'],
    'Prisutveckling_12M': df_12m['Prisutveckling']
})

# Create the quadrant chart
fig3 = px.scatter(
    df_quadrant,
    x='Prisutveckling_12M',
    y='Prisutveckling_3M',
    size='Medelpris_3M',  # size by recent Medelpris
    color='Prisutveckling_3M',  # color by recent growth
    hover_name='Områden',
    text='Områden',
    size_max=60,
    color_continuous_scale='RdYlGn',
    labels={
        'Prisutveckling_12M': '12 månaders prisutveckling (%)',
        'Prisutveckling_3M': '3 månaders prisutveckling (%)'
    },
    title='3M vs 12M Prisutveckling per Län (Bubble size = Medelpris)'
)

# Add quadrant lines at 0%
fig3.add_shape(type="line", x0=0, x1=0,
              y0=df_quadrant['Prisutveckling_3M'].min(),
              y1=df_quadrant['Prisutveckling_3M'].max(),
              line=dict(color='black', dash='dash'))

fig3.add_shape(type="line", y0=0, y1=0,
              x0=df_quadrant['Prisutveckling_12M'].min(),
              x1=df_quadrant['Prisutveckling_12M'].max(),
              line=dict(color='black', dash='dash'))

# Improve text readability
fig3.update_traces(textposition='top center', textfont=dict(size=12))
fig3.update_layout(
    title={
        'text': "3 vs 12 månader Prisutveckling",
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis=dict(showgrid=False, color="#FFFFFF"),
    yaxis=dict(showgrid=False, color="#FFFFFF"),
    plot_bgcolor="#1F1F1F",
    paper_bgcolor="#1F1F1F",
    font=dict(family="Arial", size=14, color="#FFFFFF"),
)

quadrant_momentum = html.Div([
    dcc.Graph(figure=fig3)
    ], style={
        "flex": "1 1 45%",
        "height" : "600px",  
        "min-width": "500px",
        "padding": "20px",
        "border-radius": "10px",
    })