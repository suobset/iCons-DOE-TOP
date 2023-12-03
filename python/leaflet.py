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

#popup html
popup_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        <style>
            /* Tooltip container */
            .tooltip {
                position: relative;
                display: inline-block;
                border-bottom: 1px dotted black; 
            }

            /* Tooltip text */
            .tooltip .tooltiptext {
                visibility: hidden;
                width: 120px;
                background-color: black;
                color: #fff;
                text-align: center;
                padding: 5px 0;
                border-radius: 6px;
                
                /* Position the tooltip text*/
                position: absolute;
                z-index: 1;
            }

            /* Show the tooltip text when you mouse over the tooltip container */
            .tooltip:hover .tooltiptext {
                visibility: visible;
            }
        </style>
    </head>
    <body>
        <h1>Overburdenned Index = some_number</h1>
        <div class="tooltip">
            <button class="button" style="display: flex;" onmouseover="showPopup()" onmouseout="hidePopup()">
                <i class="fa fa-question-circle" aria-hidden="true"></i>
                <span class="tooltiptext">Tooltip text</span>
            </button>
        </div>
       
    </body>
    </html>
'''


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
    legend_name='Unemployment Rate (%)',
    highlight=True,
    popup= folium.Popup(popup_html),
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
    legend_name='Education Attainment',
    highlight=True,  
    popup= folium.Popup(popup_html),
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
    legend_name='Health Index',
    highlight=True,  
    popup= folium.Popup(popup_html),
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
    legend_name='Social Vulnerability Index',
    highlight=True,  
    popup= folium.Popup(popup_html),
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
    legend_name='Housing Index',
    highlight=True,  
    popup= folium.Popup(popup_html),
).add_to(m)

# Add layer control to toggle visibility
folium.LayerControl().add_to(m)

# Move the zoom control to the center left
folium.plugins.MiniMap(toggle_display=True, position='bottomleft').add_to(m)

# Save the map as an HTML file
m.save('./map.html')
