from dash import html

from figures.quadrant import quadrant_momentum
from figures.prisutveckling import pris_utveckling
from figures.rum import rum_utveckling
from figures.table import table

title = html.H1("Sverige", style={
    "font-size": "36px",
    "color": "#fff",
    "width" : "100%",
    "padding" : "10px",
    "text-align": "center",
    "margin-bottom": "10px",
    "margin-top": "10px"
})

bostadratten = html.Div([
    title,
    pris_utveckling,
    rum_utveckling,
    quadrant_momentum,
    # table,
        
    ], style={
        "display": "flex",
        "justify-content": "space-around",
        "flex-wrap" : "wrap",  
        "align-items": "flex-start",       
        "width": "85%",
        "margin-left": "15%",
        "box-sizing": "border-box"
})
