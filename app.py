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
# for idx, row in df_fire.iterrows():
#     folium.Marker(location=[row["LAT"], row["LON"]], popup=row["NAME"]).add_to(m)#, row["LON"]], 
# st_data = st_folium(m, width=725)
# shapefile.explore()

for index, row in df_fire.iterrows():
    folium.CircleMarker(
        location=[row["LAT"], row["LON"]],
        radius=2,
        fill=True,
        fill_color="red",
        fill_opacity=1,
        color="red",
        opacity=1,
        weight=1
    ).add_to(m)

# Add the shapefile to the map
folium.GeoJson(shapefile,style_function=lambda x: {'fillColor': 'lightblue', 'color': 'black', 'weight': 2, 'fillOpacity': 0.01}).add_to(m)

# Render the map in Streamlit
st_data = st_folium(m, width=725, height=450)
