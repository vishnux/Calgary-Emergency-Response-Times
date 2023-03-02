import streamlit as st
# import folium
# from streamlit_folium import st_folium
# import geopandas as gpd

# # Load the shapefile using geopandas

# df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
# shapefile = gpd.read_file("clipped-to-calgary.shp")

# m = shapefile.explore()
# for idx, row in df_fire.iterrows():
#     folium.Marker(location=[row["LAT"], row["LON"]]).add_to(m)
# st_data = st_folium(m, width=725)import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd

st.set_page_config(layout="wide")
st.title("")
st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)#color: red;

# Load data into a pandas dataframe
#data = pd.read_csv("fire_station_data.csv")
df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
#df_ems = pd.read_excel("EMS_Stations.xlsx")

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")

# center on Liberty Bell, add marker
#m = folium.Map(tiles='OpenStreetMap',zoom_start=160)
m = shapefile.explore()
for idx, row in df_fire.iterrows():
    folium.Marker(location=[row["LAT"], row["LON"]], icon=folium.Icon(icon="circle", prefix='fa', color='blue')).add_to(m)#, row["LON"]], popup=row["Name"]
st_data = st_folium(m, width=725)
shapefile.explore()
