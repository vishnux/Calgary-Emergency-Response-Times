import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
# add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        # Adding app.py as the first page (executive summary)
        Page("app.py", "Calgary Emergency Response Time Analysis", "📈"),
        Page("pages/1_🌍_Fire_Station_-_FSA_level.py", "Fire_Station_-_FSA_level"),
        Page("pages/2_🛒_Fire_Station_-_Community_level.py", "Fire_Station_-_Community_level","🛒"),
        Page("pages/3_🪙_EMS_-_FSA_level.py", "EMS_-_FSA_level"),
        Page("pages/4_💸_EMS_-_Community_level.py", "EMS_-_Community_level"),
    ]
)

# Define the content of the executive summary page (app.py)
if st.session_state.page == "app.py":
    st.title("Calgary Emergency Response Time Analysis")
    st.write("## Introduction")
    st.write("The Calgary Emergency Response Time Analysis project undertakes a comprehensive analysis of the response times exhibited by Emergency Services in the city of Calgary. The primary objective of this research is to gain a deeper understanding of the efficiency and effectiveness of emergency responses, which are critical factors in ensuring public safety and well-being.")
    st.write("The collected data is subjected to rigorous statistical analysis to identify patterns, trends, and any potential areas of improvement. By examining response times across different types of emergencies and geographic locations, we aim to identify factors that may influence the speed and quality of emergency service delivery.")
    st.write("The findings of this study hold significant implications for both Emergency Services personnel and decision-makers within the city. The insights gained can inform policy decisions, resource allocation, and training programs to enhance the overall emergency response capabilities in Calgary.")
    st.write("It is essential to underscore the importance of this research as it directly impacts public safety and has the potential to save lives. By critically evaluating and improving emergency response times, we strive to create a safer and more resilient community for all residents of Calgary.")
    st.write("We acknowledge the limitations of the study, including potential data constraints and external factors that may influence response times.")
    st.write("In conclusion, this research endeavors to contribute valuable insights into the realm of Emergency Services response times in Calgary. By shedding light on the efficiency and effectiveness of emergency responses, we seek to foster a culture of continuous improvement in emergency service delivery, ultimately benefiting the citizens and ensuring the city's preparedness for unforeseen emergencies.")



