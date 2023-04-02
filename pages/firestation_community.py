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
#df_fire_avgtimes = pd.read_csv("FireStation_avgtimes_Community.csv")
df_avgtimes_fire = pd.read_csv("FireStation_avgtimes_Community.csv")

# Load the shapefile using geopandas
shapefile = gpd.read_file("communities_to_fsa.shp")

# Join shapefile with df_avgtime_fire on Community code
df_avgtimes_fire = shapefile.merge(df_fire_avgtime, left_on="name", right_on="Community")
df_avgtimes_fire["Avg_time"] = df_avgtimes_fire["Avg_time"].round(2)
# Sort data by highest response time per Community to lowest
df_avgtimes_fire = df_avgtimes_fire.sort_values(by=['Avg_time'], ascending=[False])
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
    tooltip=folium.GeoJsonTooltip(fields=["Community", "Avg_time"], aliases=["Community", "Avg Response Time(min)"], sticky=False),
    highlight_function=lambda x: {
        "weight": 4,
        "fillOpacity": 0.9,
    },
    name="Average Response Time (s)"
).add_to(m)

# Add the legend to the map
color_scale.add_to(m)
folium.LayerControl().add_to(m)

# col1, col2,col3 = st.columns((0.5,1,0.5))#gap="large"

# with col1:
#     # Add some vertical space between the graphs
#     st.write("")  

# with col2:
#     # Render the map in Streamlit        
#     st_data = st_folium(m, width=825, height=600)
    
# with col3:
#     # Add some vertical space between the graphs
#     st.write("")

# col1, col2,col3 = st.columns((1,0.1,1))#gap="large"

# #df_avgtimes_fire["Avg_time"] = df_avgtimes_fire["Avg_time"].round(2)

# with col1:
#      # Show a bar chart of the average response times by Community
#      st.write("## Average Response Time by Forward Sortation Area (Community)")
#      st.write('''
#      In the event of an emergency, **T3S** and **T1X** are the Communitys with the lowest coverage, potentially leaving those areas vulnerable and in need of 
#      additional support. \n
#      The following bar chart shows the average response times by Forward Sortation Area (Community) in minutes. ''')
#      fig_bar = px.bar(df_avgtimes_fire, x='Community', y='Avg_time', labels={'Community':'Forward Sortation Area', 'Avg_time':'Average Response Time (mins)'})
#      fig_bar.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
#      fig_bar.update_layout(title_text='Average Emergency Response Times by Community')
#      fig_bar.add_hline(y=6, line_dash="dash", line_color="red",
#               annotation_text="Target",annotation_font_color="red")
#      st.plotly_chart(fig_bar, use_container_width=True)


# with col2:
#     # Add some vertical space between the graphs
#     st.write("")

# with col3:
#     st.write("## Response Time Distribution by Forward Sortation Area (Community)")
#     st.write('''
#     An impressive **95%** of our Communitys consistently meet our response time target of **6 minutes**, with over **60%** achieving an 
#     even quicker response time of **2-3 minutes**.
#     \n
#     The following histogram shows the distribution of response times in minutes. ''')
#     #bins = st.slider("Select the number of bins", min_value=5, max_value=50, value=20)
#     fig_hist = px.histogram(df_avgtimes_fire, x='Avg_time', nbins=20, labels={'Avg_time':'Average Response Time (mins)'})
#     fig_hist.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
#     fig_hist.update_layout(title_text='Distribution of Emergency Response Times',yaxis_title = 'Count')
#     fig_hist.add_vline(x=6, line_dash="dash", line_color="red",
#               annotation_text="Target",annotation_font_color="red")
#     st.plotly_chart(fig_hist, use_container_width=True)

    
# with st.expander("What is an Community?"):
#     st.write("""
#         A forward sortation area [Community](https://ised-isde.canada.ca/site/office-superintendent-bankruptcy/en/statistics-and-research/forward-sortation-area-fsa-and-north-american-industry-classification-naics-reports/forward-sortation-area-definition) 
#         is a way to designate a geographical unit based on the first three characters 
#              in a Canadian postal code. All postal codes that start with the same three characters—for example, 
#              K1A—are together considered an FSA.
#     """)    
