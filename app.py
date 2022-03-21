import streamlit as st
import pandas as pd

def main():
    st.set_page_config(
    layout="wide",
    page_title="Gait Analysis",
    page_icon = "🧠")

    @st.cache()
    def get_sheet_names(excel_path):
        return pd.ExcelFile(excel_path).sheet_names
    
    @st.cache()
    def read_data_from_file(excel_path, sheet_name):
        return pd.read_excel(excel_path, sheet_name=sheet_name, skiprows=2)
    
    @st.cache()
    def clean_data_simple(df):
        df["PERSON"] = df["PERSON"].ffill().astype(int)
        df["TRIAL"] = df["TRIAL"].ffill().astype(int)
        return df
    
    """
    ## 🧠 👣 Gait Analysis
    """
    
    excel_path = "ignoredFiles/powerband_orginial.xlsx"
    sheet_names = get_sheet_names(excel_path)
    
    sheet_name = st.selectbox("Select a sheet", options=sheet_names[:-1], index=0)
    
    df = read_data_from_file(excel_path, sheet_name)
    df = clean_data_simple(df)
    
    st.write(df)
    
    
    
    
    

if __name__ == '__main__':
    main()