import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd

shapefile = gpd.read_file("clipped-to-calgary.shp")

choropleth = folium.Choropleth(
        geo_data='clipped-to-calgary.shp',
        data=shapefile,
        columns=['cfsauid'],
        key_on='feature.properties.name',
        line_opacity=0.8,
        highlight=True
    )
choropleth.geojson.add_to(map)
st_map = st_folium(map, width=700, height=450)
