import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Define a SessionState class to manage the selected page
class SessionState:
    def __init__(self):
        self.page = "executive_summary"

# Create an instance of SessionState
session_state = SessionState()

# Optional -- adds the title and icon to the current page
# add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("executive_summary", "Executive Summary", "📈"),
        Page("pages/1_🌍_Fire_Station_-_FSA_level.py", "Fire_Station_-_FSA_level"),
        Page("pages/2_🛒_Fire_Station_-_Community_level.py", "Fire_Station_-_Community_level","🛒"),
        Page("pages/3_🪙_EMS_-_FSA_level.py", "EMS_-_FSA_level"),
        Page("pages/4_💸_EMS_-_Community_level.py", "EMS_-_Community_level"),
    ]
)

# Define the content of the executive summary page
if session_state.page == "executive_summary":
    st.title("Calgary Emergency Response Time Analysis - Executive Summary")
    st.write("This executive summary provides a concise overview of the key findings and the importance of the project.")
    st.write("## Introduction")
    st.write("The Calgary Emergency Response Time Analysis project conducted an in-depth assessment of emergency response times in the city of Calgary. Our primary goal was to evaluate the efficiency and effectiveness of emergency services, a critical factor in ensuring public safety and well-being.")
    st.write("## Key Findings")
    st.write("1. **Fire Station - FSA:** In the event of an emergency, FSAs with postal codes T3S, T1X, and T3P exhibit the lowest coverage, potentially leaving those areas vulnerable and in need of additional support. Remarkably, 91% of FSAs consistently meet the response time target of 6 minutes, with over 60% achieving an even quicker response time of 2-3 minutes.")
    st.write("2. **Fire Station - Community:** For community-level emergency response, areas like Glacier Ridge, Keystone Hills, Twin Hills, and Pegasus have shown lower coverage levels, raising concerns about their vulnerability. Nevertheless, an impressive 93% of communities consistently meet the response time target of 7 minutes, with over 75% achieving an even quicker response time of 2-5 minutes.")
    st.write("3. **EMS - FSA:** In terms of EMS response times, FSAs with postal codes T1X, T3S, T2X, and T2Y are identified as having the lowest coverage. While 88% of FSAs consistently meet the response time target of 8 minutes and 59 seconds, more than 45% achieve an even quicker response time of 3-4 minutes.")
    st.write("4. **EMS - Community:** When analyzing community-level EMS responses, communities like Glacier Ridge, Legacy, Hotchkiss, and Wolf Willow are identified as having suboptimal coverage levels, potentially rendering them vulnerable. It is concerning that over 14% of communities fail to meet the response time target of 8 minutes and 59 seconds.")
    st.write("## Importance of the Project")
    st.write("This research is of paramount importance as it directly impacts public safety and has the potential to save lives. By critically evaluating and improving emergency response times, we aim to create a safer and more resilient community for all residents of Calgary. The insights gained from this study can inform policy decisions, resource allocation, and training programs to enhance overall emergency response capabilities in the city. Ensuring that vulnerable areas receive timely and effective emergency services is crucial for public well-being.")
