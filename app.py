import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Load the shapefile using geopandas

#df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
shapefile = gpd.read_file("clipped-to-calgary.shp")

m = shapefile.explore()
for idx, row in df_fire.iterrows():
    folium.Marker(location=[row["LAT"], row["LON"]], icon=folium.Icon(icon="circle", prefix='fa', color='blue')).add_to(m)
st_data = st_folium(m, width=725)
