import folium
import folium.plugins
import pandas as pd
from urllib.request import urlopen
import json
import random

# Load GeoJSON data
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Load unemployment data
df_unemployment = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                              dtype={"fips": str})

# Load random educational attainment data (example)
df_education = pd.DataFrame({
    'fips': df_unemployment['fips'],
    'education': [random.uniform(10, 30) for _ in range(len(df_unemployment))]
})

# Load random health data (example)
df_health = pd.DataFrame({
    'fips': df_unemployment['fips'],
    'health': [random.uniform(5, 25) for _ in range(len(df_unemployment))]
})

# Load random social vulnerability index data (example)
df_social_vulnerability = pd.DataFrame({
    'fips': df_unemployment['fips'],
    'social_vulnerability': [random.uniform(0, 1) for _ in range(len(df_unemployment))]
})

# Load random housing data (example)
df_housing = pd.DataFrame({
    'fips': df_unemployment['fips'],
    'housing': [random.uniform(50, 150) for _ in range(len(df_unemployment))]
})

# Create a Folium map centered at a location of your choice (e.g., USA center)
map_center = [37.0902, -95.7129]
m = folium.Map(location=map_center, zoom_start=4, control_scale=True)

# Add unemployment choropleth layer
folium.Choropleth(
    geo_data=counties,
    name='Unemployment Rate',
    data=df_unemployment,
    columns=['fips', 'unemp'],
    key_on='feature.id',
    fill_color='RdBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(m)

# Add education choropleth layer
folium.Choropleth(
    geo_data=counties,
    name='Education Attainment',
    data=df_education,
    columns=['fips', 'education'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Education Attainment'
).add_to(m)

# Add health choropleth layer
folium.Choropleth(
    geo_data=counties,
    name='Health',
    data=df_health,
    columns=['fips', 'health'],
    key_on='feature.id',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Health Index'
).add_to(m)

# Add social vulnerability index choropleth layer
folium.Choropleth(
    geo_data=counties,
    name='Social Vulnerability Index',
    data=df_social_vulnerability,
    columns=['fips', 'social_vulnerability'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Social Vulnerability Index'
).add_to(m)

# Add housing choropleth layer
folium.Choropleth(
    geo_data=counties,
    name='Housing',
    data=df_housing,
    columns=['fips', 'housing'],
    key_on='feature.id',
    fill_color='PuBuGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Housing Index'
).add_to(m)

# Add layer control to toggle visibility
folium.LayerControl().add_to(m)

# Move the zoom control to the center left
folium.plugins.MiniMap(toggle_display=True, position='bottomleft').add_to(m)

# Save the map as an HTML file
m.save('./map.html')
