import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path
repo_root = Path(__file__).parent.parent

class DataLoader:
    """Utility class for loading and managing data with caching"""
    @staticmethod 
    @st.cache_data(ttl=3600)
    def load_bostadratter_summary():
        try:
            file_path = repo_root / "data/villor/tabell.xlsx"
            if not file_path.exists():
                st.error(f"File not found: {file_path}")
                return pd.DataFrame()
            
            df = pd.read_excel(file_path, skiprows=1)
            df.columns = [
                "Områden",
                "Antal sålda 3m",
                "Kr/kvm 3m",
                "Medelpris kr 3m",
                "Prisutveckling 3m",
                "Antal sålda 12m",
                "Kr/kvm 12m",
                "Medelpris kr 12m",
                "Prisutveckling 12m"
            ]
            return df
            
        except Exception as e:
            st.error(f"Error loading bostadsratter data: {e}")
            return pd.DataFrame()
        
    @staticmethod 
    @st.cache_data(ttl=3600)
    def load_bostadratter_sales():
        """Load bostadsrätter sales data with normalized columns for Streamlit Cloud"""
        try:
            file_path = repo_root / "data/villor/bostad.xlsx"
            if not file_path.exists():
                st.error(f"File not found: {file_path}")
                return pd.DataFrame()

            df = pd.read_excel(file_path, skiprows=2)

            # Normalize column names: strip spaces and fix Unicode issues
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.normalize('NFC')

            return df

        except Exception as e:
            st.error(f"Error loading bostadsrätter sales data: {e}")
            return pd.DataFrame()


    @staticmethod 
    @st.cache_data(ttl=3600)
    def load_bostadratter_summary():
        try:
            file_path = repo_root / "data/bostadsratter/tabell.xlsx"
            if not file_path.exists():
                st.error(f"File not found: {file_path}")
                return pd.DataFrame()
            
            df = pd.read_excel(file_path, skiprows=1)
            df.columns = [
                "Områden",
                "Antal sålda 3m",
                "Kr/kvm 3m",
                "Medelpris kr 3m",
                "Prisutveckling 3m",
                "Antal sålda 12m",
                "Kr/kvm 12m",
                "Medelpris kr 12m",
                "Prisutveckling 12m"
            ]
            return df
            
        except Exception as e:
            st.error(f"Error loading bostadsratter data: {e}")
            return pd.DataFrame()
    
    @staticmethod 
    @st.cache_data(ttl=3600)
    def load_bostadratter_sales():
        """Load bostadsrätter sales data with normalized columns for Streamlit Cloud"""
        try:
            file_path = repo_root / "data/bostadsratter/bostad.xlsx"
            if not file_path.exists():
                st.error(f"File not found: {file_path}")
                return pd.DataFrame()

            df = pd.read_excel(file_path, skiprows=2)

            # Normalize column names: strip spaces and fix Unicode issues
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.normalize('NFC')

            return df

        except Exception as e:
            st.error(f"Error loading bostadsrätter sales data: {e}")
            return pd.DataFrame()


    @staticmethod 
    @st.cache_data(ttl=3600)
    def load_bostadratter_room_price():
        try:
            file_path = repo_root / "data/bostadsratter/rum.csv"
            if not file_path.exists():
                st.error(f"File not found: {file_path}")
                return pd.DataFrame()
            
            df = pd.read_csv(file_path)
            df = df.melt(id_vars="Datum", var_name="Rooms", value_name="Pris")
            return df
            
        except Exception as e:
            st.error(f"Error loading bostadsratter data: {e}")
            return pd.DataFrame()
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def load_sample_data():
        """Load sample dataset with caching"""
        np.random.seed(42)
        data = {
            'Category': ['A', 'B', 'C', 'D', 'E'] * 20,
            'Value1': np.random.normal(100, 15, 100),
            'Value2': np.random.normal(50, 10, 100),
            'Value3': np.random.normal(200, 30, 100),
            'Date': pd.date_range('2024-01-01', periods=100, freq='D')
        }
        return pd.DataFrame(data)
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def get_metrics():
        """Get sample metrics with caching"""
        return {
            'total_users': 1234,
            'active_users': 890,
            'conversion_rate': 0.23,
            'revenue': 45678.90
        }
    
    @staticmethod
    def clear_cache():
        """Clear all cached data"""
        st.cache_data.clear()