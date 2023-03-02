import streamlit as st
import pandas as pd
import json
from datetime import date
from urllib.request import urlopen
import time
import altair as alt
import folium
import geopandas as gpd

shapefile = gpd.read_file("clipped-to-calgary.shp",SHAPE_RESTORE_SHX = 'YES')
print(shapefile)
