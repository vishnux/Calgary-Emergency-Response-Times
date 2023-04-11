import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("pages/1_🌍_Fire_Station_-_FSA_level.py", "Fire_Station_-_FSA_level",),
        Page("pages/2_🛒_Fire_Station_-_Community_level.py", "2_🛒_Fire_Station_-_Community_level"),
        Page("pages/3_🪙_EMS_-_FSA_level.py", "3_🪙_EMS_-_FSA_level"),
        Page("pages/4_💸_EMS_-_Community_level.py", "4_💸_EMS_-_Community_level"),
    ]
)
