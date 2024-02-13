import folium
import folium.plugins
import pandas as pd
import json
from urllib.request import urlopen
import numpy as np
from folium.plugins import MiniMap

# Read CSV files
actual_odin = pd.read_csv("../data/actual_odin.csv")
predicted_odin = pd.read_csv("../data/predicted_odin.csv")
predicted_complete = pd.read_csv("../data/predicted_complete.csv")
all_odin = pd.read_csv("../data/main/all_ODIN_3.csv")

# Load GeoJSON data for counties
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Load GeoJSON data for states
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    states = json.load(response)

# Set the center to the geographical center of the United States
map_center = [39.8283, -98.5795]
m = folium.Map(location=map_center, zoom_start=4)

# Create a new DataFrame without values over 1.2
act_filtered_dataframe = actual_odin[actual_odin['F-VALUES'] <= 0.1]

# Create a new column for fill_color based on the condition
act_filtered_dataframe['fill_color'] = act_filtered_dataframe['F-VALUES']

# Add actual ODIN choropleth layer to the map
folium.Choropleth(
    geo_data=counties,
    name='Actual ODIN (Higher = More Overburden)',
    data=act_filtered_dataframe,
    columns=['FIPS', 'F-VALUES'],  # Update column names
    key_on='feature.id',  # Adjust this according to your GeoJSON structure
    fill_color='RdBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='pink',  # Set color for null values
    nan_fill_opacity=0.5,  # Set opacity for null values
    legend_name='Actual ODIN',
    tooltip=folium.GeoJsonTooltip(fields=['name'], labels=False)
).add_to(m)

# Create a new DataFrame without values over 1.2
filtered_dataframe = predicted_complete[predicted_complete['F-VALUES'] <= 0.1]

# Create a new column for fill_color based on the condition
filtered_dataframe['fill_color'] = filtered_dataframe['F-VALUES']

# Add predicted ODIN choropleth layer to the map
folium.Choropleth(
    geo_data=counties,
    name='Predicted ODIN Power Burden',
    data=filtered_dataframe,
    columns=['FIPS', 'F-VALUES'],  # Update column names
    key_on='feature.id',  # Adjust this according to your GeoJSON structure
    fill_color='RdBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='pink',  # Set color for null values
    nan_fill_opacity=0.5,  # Set opacity for null values
    #bins=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
    legend_name='Power Burden',
    tooltip=folium.GeoJsonTooltip(fields=['name'], labels=False)
).add_to(m)

# # Add predicted ODIN choropleth layer to the map
# folium.Choropleth(
#     geo_data=counties,
#     name='Predicted ODIN (Archive)',
#     data=predicted_odin,
#     columns=['FIPS', 'F-VALUES'],  # Update column names
#     key_on='feature.id',  # Adjust this according to your GeoJSON structure
#     fill_color='PuBuGn',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     nan_fill_color='gray',  # Set color for null values
#     nan_fill_opacity=0.5,  # Set opacity for null values
#     legend_name='Predicted ODIN',
#     tooltip=folium.GeoJsonTooltip(fields=['name'], labels=False)
# ).add_to(m)

# Add layer control for selecting layers
folium.LayerControl(autoZIndex=True).add_to(m)

# Move the zoom control to the center left
folium.plugins.MiniMap(toggle_display=True, position='bottomleft').add_to(m)

# Display the map
m.save('./odin_same_color.html')
