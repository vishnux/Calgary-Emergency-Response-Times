import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("")
st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)

df_fire = pd.read_excel("Fire_Stations_wcoordinates.xlsx")
df_avgtime_fire = pd.read_csv("FireStation_avgtimes.csv")

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")

# Join shapefile with df_avgtime_fire on FSA code
df_avgtimes_fire = shapefile.merge(df_avgtime_fire, left_on="cfsauid", right_on="FSA")
df_avgtimes_fire["Avg_time"] = df_avgtimes_fire["Avg_time"].round(2)
# Sort data by highest response time per FSA to lowest
df_avgtimes_fire = df_avgtime_fires.sort_values(by=['Avg_time'], ascending=[False])
# Define color scale
color_scale = folium.LinearColormap(
    colors=["blue", "green", "yellow", "red"],
    index=[0, 2, 5, df_avgtimes_fire["Avg_time"].max()],
    vmin=0,
    vmax=df_avgtimes_fire["Avg_time"].max(),
    caption="Average Response Time (Seconds)",
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
    tooltip=folium.GeoJsonTooltip(fields=["FSA", "Avg_time"], aliases=["FSA", "Avg Response Time(min)"], sticky=False),
    highlight_function=lambda x: {
        "weight": 4,
        "fillOpacity": 0.9,
    },
    name="Average Response Time (s)"
).add_to(m)

# Add the legend to the map
color_scale.add_to(m)
folium.LayerControl().add_to(m)

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

col1, col2,col3 = st.columns((0.5,1,0.5))#gap="large"

with col1:
    # Add some vertical space between the graphs
    st.write("")  

with col2:
    # Render the map in Streamlit        
    st_data = st_folium(m, width=825, height=650)
    
with col3:
    # Add some vertical space between the graphs
    st.write("")

col1, col2,col3 = st.columns((1,0.1,1))#gap="large"

#df_avgtimes_fire["Avg_time"] = df_avgtimes_fire["Avg_time"].round(2)

with col1:
     # Show a bar chart of the average response times by FSA
     st.write("## Average Response Time by Forward Sortation Area (FSA)")
     st.write("The following bar chart shows the average response times by Forward Sortation Area (FSA) in minutes. You can hover over the bars to see the exact values.")
     fig_bar = px.bar(df_avgtimes_fire, x='FSA', y='Avg_time', labels={'FSA':'Forward Sortation Area', 'Avg_time':'Average Response Time (mins)'})
     fig_bar.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
     fig_bar.update_layout(title_text='Average Emergency Response Times by FSA')
     fig_bar.add_hline(y=6, line_dash="dash", line_color="red",
              annotation_text="Target",annotation_font_color="red")
     st.plotly_chart(fig_bar, use_container_width=True)


with col2:
    # Add some vertical space between the graphs
    st.write("")

with col3:
    st.write("## Response Time Distribution by Forward Sortation Area (FSA)")
    st.write('''
    An impressive **95%** of our FSAs consistently meet our response time target of **6 minutes**, with over **60%** achieving an 
    even quicker response time of **2-3 minutes**.
    \n
    The following histogram shows the distribution of response times in minutes. ''')
    #bins = st.slider("Select the number of bins", min_value=5, max_value=50, value=20)
    fig_hist = px.histogram(df_avgtimes_fire, x='Avg_time', nbins=20, labels={'Avg_time':'Average Response Time (mins)'})
    fig_hist.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
    fig_hist.update_layout(title_text='Distribution of Emergency Response Times',yaxis_title = 'Count')
    fig_hist.add_vline(x=6, line_dash="dash", line_color="red",
              annotation_text="Target",annotation_font_color="red")
    st.plotly_chart(fig_hist, use_container_width=True)

    
with st.expander("What is an FSA?"):
    st.write("""
        A forward sortation area [FSA](https://ised-isde.canada.ca/site/office-superintendent-bankruptcy/en/statistics-and-research/forward-sortation-area-fsa-and-north-american-industry-classification-naics-reports/forward-sortation-area-definition) 
        is a way to designate a geographical unit based on the first three characters 
             in a Canadian postal code. All postal codes that start with the same three characters—for example, 
             K1A—are together considered an FSA.
    """)    

# with st.expander("See explanation"):
#     st.write("""
#         The chart above shows some numbers I picked for you.
#         I rolled actual dice for these, so they're *guaranteed* to
#         be random.
#     """)
    
# # Show a bar chart of the average response times by FSA
# fig = px.bar(df_avgtime_fire, x='FSA', y='Avg_time', labels={'FSA':'Forward Sortation Area', 'Avg_time':'Average Response Time (mins)'})
# st.plotly_chart(fig)

# # Show a scatter plot of the response times by FSA
# fig2 = px.scatter(df_avgtime_fire, x='FSA', y='Avg_time', labels={'FSA':'Forward Sortation Area', 'Avg_time':'Response Time (mins)'})
# st.plotly_chart(fig2)

# # Show the distribution of the response times
# fig3 = px.histogram(df_avgtime_fire, x='Avg_time', nbins=20, labels={'Avg_time':'Response Time (mins)'})
# st.plotly_chart(fig3)





# Show a scatter plot of the response times by FSA

#st.write("The following scatter plot shows the distribution of response times by Forward Sortation Area (FSA) in minutes. You can hover over the dots to see the exact values.")

# fig_scatter = px.scatter(df_avgtime_fire, x='FSA', y='Avg_time', labels={'FSA':'Forward Sortation Area', 'Avg_time':'Response Time (mins)'}, trendline='ols')
# fig_scatter.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
# fig_scatter.update_layout(title_text='Distribution of Emergency Response Times by FSA')
# st.plotly_chart(fig_scatter)

# Show the distribution of the response times
#st.write("## Distribution of Response Times")



# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write(' ')

# with col2:
#     # Render the map in Streamlit
#     st_data_2 = st_folium(m, width=825, height=550)

# with col3:
#     st.write(' ')        
        

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

