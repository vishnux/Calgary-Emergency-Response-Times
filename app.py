import streamlit as st
import pandas as pd
import json
from datetime import date
from urllib.request import urlopen
import time
import altair as alt
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap

shapefile = gpd.read_file("clipped-to-calgary.shp",SHAPE_RESTORE_SHX = 'YES')
print(shapefile)

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
