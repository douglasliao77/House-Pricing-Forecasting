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
from figures.rum import rum_utveckling
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


table = html.Div(
    dash_table.DataTable(
        columns=columns,
        data=df.to_dict('records'),
        merge_duplicate_headers=True,
    
        style_table={
            'minWidth': '100%',  
            'overflowX': 'auto',  
        },
        
        style_cell={
            'padding': '5px',
            'textAlign': 'center',
            'border': '1px solid #444',    
            'fontFamily': 'Arial, sans-serif',
            'color': 'white',             
            'backgroundColor': '#1e1e1e',  
            'minWidth': '100px',  
            'width': '100px',    
            'maxWidth': '200px'   
        },

        style_header={
            'textAlign': 'center',
            'fontWeight': 'bold',
            'backgroundColor': '#2b2b2b',
            'color': 'white',
        },

        style_data_conditional=[
            {'if': {'row_index': 0}, 'borderBottom': '3px solid black'},
        ],
        
        style_header_conditional=[
            {'if': {'column_id': columns[1]['id']}, 'borderRight': '3px solid black'}
        ],

        style_cell_conditional=[
            {'if': {'column_id': columns[4]['id']}, 'borderRight': '3px solid black'},
            {'if': {'column_id': columns[0]['id']}, 'borderRight': '3px solid black'},
            {
                'if': {'column_id': columns[0]['id']},
                'position': 'sticky',
                'left': 0,
                'backgroundColor': '#2b2b2b',
                'zIndex': 2,
            }
        ]
    ),
    style={
        'overflowX': 'auto',  
        'padding': '20px',
        'width': '70%',      
        'maxWidth': '100vw', 
        'marginLeft': '0',
        'marginRight': 'auto',
    }
)