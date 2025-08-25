from dash import html
import dash_bootstrap_components as dbc

def get_layout():
    return html.Div([
        top_bar,
        sidebar
    ])

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

# Sidebar filters
sidebar = html.Div([

    dbc.Row([
    ], style={}),

], style={
    "position" : "fixed",
    "backgroundColor": "#2a2a2a",  
    "padding": "20px 10px",
    "height": "100%",    
    "color": "#95969A",
    "top": "0",
    "left": "0",
    "width": "15%"
})