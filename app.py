# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium
# import geopandas as gpd

# st.set_page_config(layout="wide")
# st.title("")
# st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)#color: red;

# df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")

# # Load the shapefile using geopandas
# shapefile = gpd.read_file("clipped-to-calgary.shp")

# m = shapefile.explore()
# # for idx, row in df_fire.iterrows():
# #     folium.Marker(location=[row["LAT"], row["LON"]], popup=row["NAME"]).add_to(m)#, row["LON"]], 
# # st_data = st_folium(m, width=725)
# # shapefile.explore()

# for index, row in df_fire.iterrows():
#     folium.CircleMarker(
#         location=[row["LAT"], row["LON"]],
#         radius=2,
#         fill=True,
#         fill_color="red",
#         fill_opacity=1,
#         color="red",
#         opacity=1,
#         weight=1
#     ).add_to(m)

# # Add the shapefile to the map
# folium.GeoJson(shapefile,style_function=lambda x: {'fillColor': 'lightblue', 'color': 'black', 'weight': 2, 'fillOpacity': 0.01}).add_to(m)

# # Render the map in Streamlit
# st_data = st_folium(m, width=725, height=450)

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

# Create a map
m = folium.Map(location=[51.0447,-114.0719], zoom_start=11)

# #Add the fire stations as markers with popups
# for index, row in df_fire.iterrows():
#     folium.Marker(
#         location=[row["LAT"], row["LON"]],
#         popup=row["NAME"],
#         tooltip=row["NAME"],
#         icon=folium.Icon(color="red")
#     ).add_to(m)
    
# for index, row in df_fire.iterrows():
#     folium.CircleMarker(
#         location=[row["LAT"], row["LON"]],
#         popup=row["NAME"],
#         tooltip=row["NAME"],
#         radius=2,
#         fill=True,
#         fill_color="red",
#         fill_opacity=1,
#         icon=folium.Icon(color="red"),
#         color="red",
#         opacity=1,
#         weight=1
#     ).add_to(m)

# Add the fire stations as circle markers with popups and labels
for index, row in df_fire.iterrows():
    folium.CircleMarker(
        location=[row["LAT"], row["LON"]],
        popup=row["NAME"],
        radius=2,
        fill=True,
        fill_color="red",
        fill_opacity=1,
        color="red",
        opacity=1,
        weight=1,
        # Add a label to the circle marker
        #tooltip=folium.Popup(row["NAME"], parse_html=True)
    ).add_to(m)


# Add the shapefile to the map
folium.GeoJson(
    shapefile,
    style_function=lambda x: {'fillColor': 'lightblue', 'color': 'black', 'weight': 2, 'fillOpacity': 0.01},
    tooltip=folium.GeoJsonTooltip(fields=['cfsauid'], labels=False, sticky=False)
).add_to(m)

# Add a legend to the map
legend_html = '''
     <div style="position: fixed; 
                 bottom: 50px; left: 50px; width: 120px; height: 110px; 
                 border:2px solid grey; z-index:9999; font-size:14px;
                 background-color:white;
                 ">
         &nbsp; Fire Stations &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i><br>
         &nbsp; Forward Sortation Areas &nbsp; <i class="fa fa-map fa-2x" style="color:lightblue"></i>
     </div>
     '''
m.get_root().html.add_child(folium.Element(legend_html))

# Render the map in Streamlit
st_data = st_folium(m, width=725, height=450)

