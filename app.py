import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")

# center on Liberty Bell, add marker
#m = folium.Map(tiles='OpenStreetMap',zoom_start=160)
m = shapefile.explore()
# folium.Marker(
#      [114.0719, 51.0447]
# ).add_to(m)
#folium.GeoJson(shapefile).add_to(m)
# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
shapefile.explore()

