import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd

shapefile = gpd.read_file("clipped-to-calgary.shp",SHAPE_RESTORE_SHX = 'YES')

map = folium.Map(location=[38, -96.5], zoom_start=4, scrollWheelZoom=False, tiles='CartoDB positron')
    
choropleth = folium.Choropleth(
        geo_data='clipped-to-calgary.shp',
        #data=df,
        #columns=('State Name', 'State Total Reports Quarter'),
        key_on='feature.properties.name',
        line_opacity=0.8,
        highlight=True
)
choropleth.geojson.add_to(map)
