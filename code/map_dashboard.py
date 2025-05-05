'''
map_dashboard.py
'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import branca.colormap as cm

# Constants
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min value for color scale
VMAX = 5000                 # max value for color scale

# Load the dataset
df = pd.read_csv('./cache/top_locations_mappable.csv')

# Create a color scale based on fine amount
colormap = cm.LinearColormap(colors=["yellow", "red"], vmin=VMIN, vmax=VMAX)
colormap.caption = "Total Fine Amount"

# Create folium map
m = folium.Map(location=CUSE, zoom_start=ZOOM, tiles="CartoDB positron")

# Add each location as a circle
for _, row in df.iterrows():
    folium.CircleMarker(
        location=(row['lat'], row['lon']),
        radius=6,
        color=colormap(row['amount']),
        fill=True,
        fill_opacity=0.7,
        popup=f"{row['location']}<br>Total: ${row['amount']:,.0f}"
    ).add_to(m)

# Add color scale to map
colormap.add_to(m)

# Render the map in Streamlit
st.title("💸 Syracuse Parking Tickets Heatmap")
st.markdown("Locations with $1,000+ in fines are shown. Circle color reflects total fine amount.")

sf.st_folium(m, width=800, height=600)
