import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
# Initialize app with dark theme + Google font
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
accent = "#f58518"
# Full-width top bar
top_bar = html.Div(
    children=[
        html.H2(
            "🏡 Bostadsmarknaden",
            style={
                "color": accent,
                "fontFamily": "'Ubuntu', sans-serif",
                "fontWeight": "bold",
                "margin": "0",
                "padding": "20px 30px"
            }
        )
    ],
    style={
        "width": "100%",
        "backgroundColor": "#1F1F1F",
        "boxShadow": "0 4px 12px rgba(0,0,0,0.3)",
        "position": "sticky",
        "top": "0",
        "zIndex": "1000"
    }
)

sweden_data = {
    'Län': ['Stockholm', 'Skåne', 'Västra Götaland'],
    'Kommun': {
        'Stockholm': ['Stockholm', 'Solna', 'Sundbyberg'],
        'Skåne': ['Malmö', 'Lund', 'Helsingborg'],
        'Västra Götaland': ['Göteborg', 'Borås', 'Trollhättan']
    }
}

# Sidebar filters
sidebar = html.Div([

    dbc.Row([
        dbc.Col(
            html.Div(
                "Bostadsrätt",
                id="card-bostadsratt",
                n_clicks=0,
                style={
                    "textAlign": "center",
                    "fontWeight": "bold",
                    "fontSize": "20px",
                    "cursor": "pointer",
                    "backgroundColor": "#2a2a2a",
                    "border": f"2px solid {accent}",  # selected by default
                    "borderRadius": "10px 0 0 10px",
                    "padding": "15px",
                    "width": "100%",
                }
            ),
            width=6,
            style={"paddingRight": "0px"}
        ),
        dbc.Col(
            html.Div(
                "Villa",
                id="card-villa",
                n_clicks=0,
                style={
                    "textAlign": "center",
                    "fontWeight": "bold",
                    "fontSize": "20px",
                    "cursor": "pointer",
                    "backgroundColor": "#2a2a2a",
                    "border": "2px solid transparent",
                    "borderRadius": "0 10px 10px 0",
                    "padding": "15px",
                    "width": "100%",
                }
            ),
            width=6,
            style={"paddingLeft": "0px"}
        )
    ], style={"marginBottom": "25px"}),

], style={
    "backgroundColor": "#2a2a2a",  
    "padding": "20px 10px",
    "minHeight": "90vh",    
    "color": "#95969A",
    "position": "absolute",
    "top": "10vh",
    "left": "0",
    "width": "20%"
})

# App layout
# Layout
app.layout = html.Div([
    top_bar,
    sidebar ,
    # Hidden div to store the selected type
    html.Div(id="selected-house-type", style={"display": "none"})
])

# Callback to switch selection
@app.callback(
    Output("card-bostadsratt", "style"),
    Output("card-villa", "style"),
    Output("selected-house-type", "children"),
    Input("card-bostadsratt", "n_clicks"),
    Input("card-villa", "n_clicks"),
    State("card-bostadsratt", "style"),
    State("card-villa", "style")
)
def toggle_house_type(bostadsratt_clicks, villa_clicks, style_b, style_v):
    ctx = dash.callback_context
    if not ctx.triggered:
        return style_b, style_v, "bostadsratt"
    
    clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if clicked_id == "card-bostadsratt":
        style_b["border"] = f"2px solid {accent}"
        style_v["border"] = "2px solid transparent"
        selected = "bostadsratt"
    else:
        style_b["border"] = "2px solid transparent"
        style_v["border"] = f"2px solid {accent}"
        selected = "villa"

    return style_b, style_v, selected

if __name__ == "__main__":
    app.run(debug=True)
