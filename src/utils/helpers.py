import streamlit as st
import pandas as pd
import numpy as np

def load_css():
    """Load custom CSS styles"""
    st.markdown("""
    <style>
    .stTitle {
        text-align: center !important;
        margin-bottom: 2rem !important;
    }

    .sidebar-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 1rem;
        color: white;
    }
    

    .stButton button {
        width: 100%;
        border-radius: 8px;
        border: none;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    }
    </style>
    """, unsafe_allow_html=True)

def get_sidebar_style():
    """Return sidebar specific styles"""
    return """
    <style>
    .css-1d391kg { /* Sidebar background */
        background: linear-gradient(180deg, #2c3e50 0%, #3498db 100%);
    }
    
    .sidebar .sidebar-content {
        background: transparent !important;
    }
    
    .stRadio div label {
        color: white !important;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    
    .stRadio div label:hover {
        background-color: rgba(255, 255, 255, 0.1) !important;
    }
    
    .stRadio div [data-testid="stMarkdownContainer"] {
        color: white !important;
    }
    </style>
    """

def get_sample_data():
    """Generate sample data for demonstration"""
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(100, 1000, size=30),
        'Users': np.random.randint(50, 500, size=30),
        'Revenue': np.random.uniform(1000, 10000, size=30)
    }).set_index('Date')
    
    return data

def format_currency(value):
    """Format number as currency"""
    return f"${value:,.2f}"

def plotly_title(fig, title, title_size=20, title_color=None, font_family='Arial'):
    """
    Center the title of a Plotly figure
    
    Parameters:
    - fig: Plotly figure object
    - title: Title text
    - title_size: Font size (default: 20)
    - title_color: Color for the title (optional)
    - font_family: Font family (default: 'Arial')
    
    Returns:
    - Updated Plotly figure with centered title
    """
    title_config = {
        'text': title,
        'x': 0.5,
        'xanchor': 'center',
        'font': {
            'size': title_size,
            'family': font_family
        }
    }
    if title_color:
        title_config['font']['color'] = title_color
    
    fig.update_layout(title=title_config)
    return fig

def add_source(fig, source_text="Källa: Svensk Mäklarstatistik"):
    """
    Adds a source annotation below the chart.

    Parameters:
    - fig: Plotly figure
    - source_text: text to show
    - y_offset: vertical offset (negative moves below x-axis)
    """
    fig.add_annotation(
        text=source_text,
        xref="paper",
        yref="paper",
        x=1,
        y=1,
        showarrow=False,
        font=dict(size=12, color="gray"),
        align="left"
    )
    return fig

def style_tabs():
    st.markdown("""
        <style>
            /* Make tab list full width */
            .stTabs [data-baseweb="tab-list"] {
                width: 100% !important;
                display: flex !important;
            }

            /* Make each tab stretch equally */
            .stTabs [data-baseweb="tab"] {
                flex-grow: 1 !important;
                text-align: center;
                height: 50px;
                white-space: pre-wrap;
                border-radius: 4px 4px 0px 0px;
                padding-top: 10px;
                padding-bottom: 10px;
                margin: 0 2px; /* small gap between tabs */
            }
        </style>
    """, unsafe_allow_html=True)
