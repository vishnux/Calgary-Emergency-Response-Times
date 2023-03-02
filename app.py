# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium
# import geopandas as gpd

# shapefile = gpd.read_file("clipped-to-calgary.shp")

# choropleth = folium.Choropleth(
#         geo_data='clipped-to-calgary.shp',
#         data=shapefile,
#         columns=('cfsauid'),
#         key_on='feature.properties.name',
#         line_opacity=0.8,
#         highlight=True
#     )
# choropleth.geojson.add_to(map)
# st_map = st_folium(map, width=700, height=450)

import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")

# # Create a folium map centered on Calgary
# map = folium.Map(location=[51.0447, -114.0719], zoom_start=10)

# # Add the shapefile as a choropleth layer to the map
# folium.Choropleth(
#     geo_data=shapefile,
#     name='choropleth',
#     data=shapefile,
#     columns=['cfsauid','prname'],
#     key_on='feature.properties.cfsauid',
#     fill_color='YlGn',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name='CFSAs'
# ).add_to(map)

# # Add the folium map to Streamlit using the st_folium wrapper function
# st_map = st_folium(map, width=700, height=450)

# # Display the map on Streamlit
# st_map

import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(zoom_start=16)
# folium.Marker(
#     [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
# ).add_to(m)
folium.GeoJson(shapefile).add_to(m)
# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)


