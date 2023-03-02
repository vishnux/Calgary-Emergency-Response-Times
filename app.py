import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd

shapefile = gpd.read_file("clipped-to-calgary.shp",SHAPE_RESTORE_SHX = 'YES')

choropleth = folium.Choropleth(
        geo_data='data/us-state-boundaries.geojson',
        data=shapefile,
        columns=('cfsauid'),
        key_on='feature.properties.name',
        line_opacity=0.8,
        highlight=True
    )
choropleth.geojson.add_to(map)
