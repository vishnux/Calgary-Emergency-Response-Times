import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd

st.set_page_config(layout="wide")
st.title("")
st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)

df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
df_avgtime_fire = pd.read_csv("FireStation_avgtimes.csv")

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")

# Join shapefile with df_avgtime_fire on FSA code
df_avgtimes_fire = shapefile.merge(df_avgtime_fire, left_on="cfsauid", right_on="FSA")

# Define color scale
color_scale = folium.LinearColormap(
    colors=["blue", "green", "yellow", "red"],
    index=[0, 2, 4, 6, df_avgtimes_fire["Avg_time"].max()],
    vmin=0,
    vmax=df_avgtimes_fire["Avg_time"].max(),
    caption="Average Response Time (Minutes)",
)

# Create a map
m = folium.Map(location=[51.0447,-114.0719], zoom_start=10)

for index, row in df_fire.iterrows():
    folium.CircleMarker(
        location=[row["LAT"], row["LON"]],
        popup=row["NAME"],
        tooltip=row["NAME"],
        radius=2,
        fill=True,
        fill_color="red",
        fill_opacity=1,
        icon=folium.Icon(color="red"),
        color="red",
        opacity=1,
        weight=1
    ).add_to(m)

# Add the shapefile with color ranges to the map
folium.GeoJson(
    df_avgtimes_fire,
    style_function=lambda x: {
        "fillColor": color_scale(x["properties"]["Avg_time"]),
        "color": "black",
        "weight": 2,
        "fillOpacity": 0.6,
    },
    tooltip=folium.GeoJsonTooltip(fields=["cfsauid", "Avg_time"], aliases=["FSA", "Avg Response Time(min)"], sticky=False),
    highlight_function=lambda x: {
        "weight": 4,
        "fillOpacity": 0.9,
    },
    name="Average Response Time (min)"
).add_to(m)

# Add the legend to the map
color_scale.add_to(m)
folium.LayerControl().add_to(m)

# Search Bar for FSA
fsa_search = st.sidebar.text_input("Search for FSA:")
if fsa_search:
    fsa_data = df_avgtime_fire[df_avgtime_fire["FSA"].str.contains(fsa_search)]
    for index, row in fsa_data.iterrows():
        folium.Marker(
            location=[row["LAT"], row["LON"]],
            popup=row["NAME"],
            tooltip=row["NAME"],
            icon=folium.Icon(color="green", icon="info-sign"),
        ).add_to(m)

# Render the map in Streamlit
st_data = st_folium(m, width=725, height=550)


# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium
# import geopandas as gpd

# st.set_page_config(layout="wide")
# st.title("")
# st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)

# df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
# df_avgtime_fire = pd.read_csv("FireStation_avgtimes.csv")

# # Load the shapefile using geopandas
# shapefile = gpd.read_file("clipped-to-calgary.shp")

# # Join shapefile with df_avgtime_fire on FSA code
# df_avgtimes_fire = shapefile.merge(df_avgtime_fire, left_on="cfsauid", right_on="FSA")

# # Define color scale
# color_scale = folium.LinearColormap(
#     colors=["blue", "green", "yellow", "red"],
#     index=[0, 2, 5, 8, df_avgtimes_fire["Avg_time"].max()],
#     vmin=0,
#     vmax=df_avgtimes_fire["Avg_time"].max(),
#     caption="Average Response Time (Seconds)",
# )

# # Create a map
# m = folium.Map(location=[51.0447,-114.0719], zoom_start=10)

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

# # Add the shapefile with color ranges to the map
# folium.GeoJson(
#     df_avgtimes_fire,
#     style_function=lambda x: {
#         "fillColor": color_scale(x["properties"]["Avg_time"]),
#         "color": "black",
#         "weight": 2,
#         "fillOpacity": 0.6,
#     },
#     tooltip=folium.GeoJsonTooltip(fields=["cfsauid", "Avg_time"], aliases=["FSA", "Avg Response Time(min)"], sticky=False),
#     highlight_function=lambda x: {
#         "weight": 4,
#         "fillOpacity": 0.9,
#     },
#     name="Average Response Time (s)"
# ).add_to(m)

# # Add the legend to the map
# color_scale.add_to(m)
# folium.LayerControl().add_to(m)

# # Search Bar for FSA
# fsa_search = st.sidebar.text_input("Search for FSA:")
# if fsa_search:
#     fsa_data = df_avgtime_fire[df_avgtime_fire["FSA"].str.contains(fsa_search)]
#     for index, row in fsa_data.iterrows():
#         folium.Marker(
#             location=[row["LAT"], row["LON"]],
#             popup=row["NAME"],
#             tooltip=row["NAME"],
#             icon=folium.Icon(color="green", icon="info-sign"),
#         ).add_to(m)

# # Render the map in Streamlit
# st_data = st_folium(m, width=725, height=550)



#TEST 

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

# #START

# import streamlit as st
# import pandas as pd
# import folium
# from streamlit_folium import st_folium
# import geopandas as gpd

# st.set_page_config(layout="wide")
# st.title("")
# st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)#color: red;

# df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
# df_avgtime_fire = pd.read_csv("FireStation_avgtimes.csv")

# # Load the shapefile using geopandas
# shapefile = gpd.read_file("clipped-to-calgary.shp")

# # Create a map
# m = folium.Map(location=[51.0447,-114.0719], zoom_start=11)

# # #Add the fire stations as markers with popups
# # for index, row in df_fire.iterrows():
# #     folium.Marker(
# #         location=[row["LAT"], row["LON"]],
# #         popup=row["NAME"],
# #         tooltip=row["NAME"],
# #         icon=folium.Icon(color="red")
# #     ).add_to(m)
    
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


# # Add the shapefile to the map
# folium.GeoJson(
#     shapefile,
#     style_function=lambda x: {'fillColor': 'lightblue', 'color': 'black', 'weight': 2, 'fillOpacity': 0.01},
#     tooltip=folium.GeoJsonTooltip(fields=['cfsauid'], labels=False, sticky=False)
# ).add_to(m)

# # Define color ranges for FSAs
# color_ranges = {
#     "0-2 mins": "green",
#     "2-4 mins": "yellow",
#     "5+ mins": "red"
# }

# # Add FSAs to the map with popup showing FSA code and average response time
# for index, row in df_avgtime_fire.iterrows():
#     fsa = row["FSA"]
#     avg_time = row["Avg_time"]
    
#     # Define color based on response time range
#     if avg_time < 2:
#         color = color_ranges["0-2 mins"]
#     elif avg_time < 4:
#         color = color_ranges["2-4 mins"]
#     else:
#         color = color_ranges["5+ mins"]
    
#     # Find the FSA in the shapefile and add to the map
#     fsa_shape = shapefile[shapefile["cfsauid"] == fsa]
#     if not fsa_shape.empty:
#         folium.GeoJson(
#             fsa_shape.to_json(),
#             style_function=lambda x: {'fillColor': color, 'color': 'black', 'weight': 2, 'fillOpacity': 0.7},
#             tooltip=f"FSA {fsa}<br>Avg Response Time: {avg_time:.2f} mins"
#         ).add_to(m)

# #Search Bar for FSA
# fsa_search = st.sidebar.text_input("Search for FSA:")
# if fsa_search:
#     fsa_data = df_avgtime_fire[df_avgtime_fire["FSA"].str.contains(fsa_search)]
#     for index, row in fsa_data.iterrows():
#         folium.Marker(
#             location=[row["LAT"], row["LON"]],
#             popup=row["NAME"],
#             tooltip=row["NAME"],
#             icon=folium.Icon(color="green", icon="info-sign"),
#         ).add_to(m)


# # Add a legend to the map
# legend_html = '''
#      <div style="position: fixed; 
#                  bottom: 50px; left: 50px; width: 120px; height: 110px; 
#                  border:2px solid grey; z-index:9999; font-size:14px;
#                  background-color:white;
#                  ">
#          &nbsp; Fire Stations &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i><br>
#          &nbsp; Forward Sortation Areas &nbsp; <i class="fa fa-map fa-2x" style="color:lightblue"></i>
#      </div>
#      '''
# m.get_root().html.add_child(folium.Element(legend_html))

# # Render the map in Streamlit
# st_data = st_folium(m, width=725, height=450)

# #END

