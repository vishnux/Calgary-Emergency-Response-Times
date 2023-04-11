import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("pages/1_Fire_Station_-_FSA_level.py", "Fire_Station_-_FSA_level","🌍"),
        #Page("pages/2_Fire_Station_-_Community_level.py", "Fire_Station_-_Community_level","🛒"),
        #Page("pages/3_EMS_-_FSA_level.py", "EMS_-_FSA_level","🪙"),
        #Page("pages/4_EMS_-_Community_level.py", "EMS_-_Community_level","💸"),
    ]
)
