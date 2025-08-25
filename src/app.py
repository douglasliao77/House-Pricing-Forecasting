import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
from layout import get_layout, accent 
from pages.bostadsratten import bostadratten

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True
)

dcc.Dropdown(
    id="period-selector",
    options=[
        {"label": "3 månader", "value": "3m"},
        {"label": "12 månader", "value": "12m"},
    ],
    value="3m",  # default
    clearable=False,
    style={"width": "200px"}
)


app.layout = html.Div([
    get_layout(), 
    bostadratten
])

if __name__ == "__main__":
    app.run(debug=True)
