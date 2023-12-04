import folium
import folium.plugins
import pandas as pd
import json
from urllib.request import urlopen

# Read CSV files
actual_odin = pd.read_csv("./data/actual_odin.csv")
predicted_odin = pd.read_csv("./data/predicted_odin.csv")

# Load GeoJSON data for counties
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Load GeoJSON data for states
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    states = json.load(response)

# Create a Folium map centered at an initial location
map_center = [37.7749, -122.4194]  # You can adjust these coordinates
m = folium.Map(location=map_center, zoom_start=10)

# Add actual ODIN choropleth layer to the map
folium.Choropleth(
    geo_data=counties,
    name='Actual ODIN',
    data=actual_odin,
    columns=['FIPS', 'F-VALUES'],  # Update column names
    key_on='feature.id',  # Adjust this according to your GeoJSON structure
    fill_color='PuBuGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='gray',  # Set color for null values
    nan_fill_opacity=0.5,  # Set opacity for null values
    legend_name='Actual ODIN',
    tooltip=folium.GeoJsonTooltip(fields=['name'], labels=False)
).add_to(m)

# Add predicted ODIN choropleth layer to the map
folium.Choropleth(
    geo_data=counties,
    name='Predicted ODIN',
    data=predicted_odin,
    columns=['FIPS', 'F-VALUES'],  # Update column names
    key_on='feature.id',  # Adjust this according to your GeoJSON structure
    fill_color='PuBuGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color='gray',  # Set color for null values
    nan_fill_opacity=0.5,  # Set opacity for null values
    legend_name='Predicted ODIN',
    tooltip=folium.GeoJsonTooltip(fields=['name'], labels=False)
).add_to(m)

# Add state borders with a higher line weight
folium.GeoJson(
    states,
    style_function=lambda feature: {'color': 'black', 'weight': 2}
).add_to(m)

# Add layer control for selecting layers
folium.LayerControl().add_to(m)

# Display the map
m.save('./actual_odin_map.html')
