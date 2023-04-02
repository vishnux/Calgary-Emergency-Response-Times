import streamlit as st
import pandas as pd
import folium

st.markdown("<h1 style='text-align: center;'>Calgary Fire Station Response Lag Time Analysis</h1>", unsafe_allow_html=True)

df_ems = pd.read_excel("EMS_Stations_wcoordinates.xlsx")
df_ems_avgtime = pd.read_csv("ems_avgtimes.csv")
df_ems_avgtime = pd.read_csv("ems_avgtimes_Community.csv")

# Load the shapefile using geopandas
shapefile = gpd.read_file("clipped-to-calgary.shp")
shapefile = gpd.read_file("communities_to_fsa.shp")

# Join shapefile with df_avgtime_fire on FSA code
df_avgtimes_ems = shapefile.merge(df_ems_avgtime, left_on="cfsauid", right_on="FSA")
# Join shapefile with df_avgtime_fire on Community code
df_avgtimes_ems = shapefile.merge(df_ems_avgtime, left_on="name", right_on="Community")
df_avgtimes_ems["Avg_time"] = df_avgtimes_ems["Avg_time"].round(2)
# Sort data by highest response time per FSA to lowest
# Sort data by highest response time per Community to lowest
df_avgtimes_ems = df_avgtimes_ems.sort_values(by=['Avg_time'], ascending=[False])
# Define color scale
color_scale = folium.LinearColormap(

        "weight": 2,
        "fillOpacity": 0.6,
    },
    tooltip=folium.GeoJsonTooltip(fields=["FSA", "Avg_time"], aliases=["FSA", "Avg Response Time(min)"], sticky=False),
    tooltip=folium.GeoJsonTooltip(fields=["Community", "Avg_time"], aliases=["Community", "Avg Response Time(min)"], sticky=False),
    highlight_function=lambda x: {
        "weight": 4,
        "fillOpacity": 0.9,

color_scale.add_to(m)
folium.LayerControl().add_to(m)

# # Search Bar for FSA
# fsa_search = st.sidebar.text_input("Search for FSA:")
# if fsa_search:
#     fsa_data = df_avgtime_fire[df_avgtime_fire["FSA"].str.contains(fsa_search)]
#     for index, row in fsa_data.iterrows():
# # Search Bar for Community
# Community_search = st.sidebar.text_input("Search for Community:")
# if Community_search:
#     Community_data = df_avgtime_fire[df_avgtime_fire["Community"].str.contains(Community_search)]
#     for index, row in Community_data.iterrows():
#         folium.Marker(
#             location=[row["LAT"], row["LON"]],
#             popup=row["NAME"],

#df_avgtimes_ems["Avg_time"] = df_avgtimes_ems["Avg_time"].round(2)

with col1:
     # Show a bar chart of the average response times by FSA
     st.write("## Average Response Time by Forward Sortation Area (FSA)")
     # Show a bar chart of the average response times by Community
     st.write("## Average Response Time by Community (Community)")
     st.write('''
     In the event of an emergency, **T3S** and **T1X** are the FSAs with the lowest coverage, potentially leaving those areas vulnerable and in need of 
     In the event of an emergency, **T3S** and **T1X** are the communities with the lowest coverage, potentially leaving those areas vulnerable and in need of 
     additional support. \n
     The following bar chart shows the average response times by Forward Sortation Area (FSA) in minutes. ''')
     fig_bar = px.bar(df_avgtimes_ems, x='FSA', y='Avg_time', labels={'FSA':'Forward Sortation Area', 'Avg_time':'Average Response Time (mins)'})
     The following bar chart shows the average response times by Community (Community) in minutes. ''')
     fig_bar = px.bar(df_avgtimes_ems, x='Community', y='Avg_time', labels={'Community':'Community', 'Avg_time':'Average Response Time (mins)'})
     fig_bar.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
     fig_bar.update_layout(title_text='Average Emergency Response Times by FSA')
     fig_bar.update_layout(title_text='Average Emergency Response Times by Community')
     fig_bar.add_hline(y=6, line_dash="dash", line_color="red",
              annotation_text="Target",annotation_font_color="red")
     st.plotly_chart(fig_bar, use_container_width=True)

    st.write("")

with col3:
    st.write("## Response Time Distribution by Forward Sortation Area (FSA)")
    st.write("## Response Time Distribution by Community (Community)")
    st.write('''
    An impressive **95%** of our FSAs consistently meet our response time target of **6 minutes**, with over **60%** achieving an 
    An impressive **95%** of our Communitys consistently meet our response time target of **6 minutes**, with over **60%** achieving an 
    even quicker response time of **2-3 minutes**.
    \n
    The following histogram shows the distribution of response times in minutes. ''')

    st.plotly_chart(fig_hist, use_container_width=True)


with st.expander("What is an FSA?"):
with st.expander("What is an Community?"):
    st.write("""
        A forward sortation area [FSA](https://ised-isde.canada.ca/site/office-superintendent-bankruptcy/en/statistics-and-research/forward-sortation-area-fsa-and-north-american-industry-classification-naics-reports/forward-sortation-area-definition) 
        A forward sortation area [Community](https://ised-isde.canada.ca/site/office-superintendent-bankruptcy/en/statistics-and-research/forward-sortation-area-Community-and-north-american-industry-classification-naics-reports/forward-sortation-area-definition) 
        is a way to designate a geographical unit based on the first three characters 
             in a Canadian postal code. All postal codes that start with the same three characters—for example, 
             K1A—are together considered an FSA.
             K1A—are together considered an Community.
    """)    
