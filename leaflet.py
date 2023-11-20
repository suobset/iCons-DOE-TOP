import folium
import pandas as pd
from urllib.request import urlopen
import json

# Load GeoJSON data
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Load unemployment data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                 dtype={"fips": str})

# Create a Folium map centered at a location of your choice (e.g., USA center)
map_center = [37.0902, -95.7129]
m = folium.Map(location=map_center, zoom_start=4)

# Add choropleth layer to the map with blue to red color scale
folium.Choropleth(
    geo_data=counties,
    name='choropleth',
    data=df,
    columns=['fips', 'unemp'],
    key_on='feature.id',
    fill_color='RdBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(m)

# Add layer control to toggle visibility
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('./map.html')
