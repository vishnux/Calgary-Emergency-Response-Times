import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd

st.set_page_config(layout="wide")
st.title("")
st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)#color: red;

df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")

m = shapefile.explore()
for idx, row in df_fire.iterrows():
    folium.Marker(location=[row["LAT"], row["LON"]], popup=row["Name"]).add_to(m)#, row["LON"]], 
st_data = st_folium(m, width=725)
shapefile.explore()
