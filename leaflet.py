# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:59:36 2023

@author: kushd
"""

import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from folium import plugins
from folium.plugins import HeatMap
import geopandas as gpd
from shapely.geometry import Point

data1 = pd.read_csv("./data/counties-age.csv")

def geocode_address(address):
  geolocator = Nominatim(user_agent="my_geocoder")
  try:
    location = geolocator.geocode(address)
    if location:
      return location.latitude, location.longitude
    else:
      return None
  except GeocoderTimedOut:
    return geocode_address(address)

data1["Location"] = data1["NAMELSAD"] + ", " + data1["STUSPS"]
data1["Latitude"], data1["Longitude"] = zip(*data1["Location"].apply(geocode_address).dropna())

# Geocode the county names to get coordinates
data1["geometry"] = data1["Location"].apply(geocode_address).apply(Point)
gdf = gpd.GeoDataFrame(data1, geometry="geometry")

# Download U.S. counties shapefile from the Census Bureau
counties_shapefile_url = "https://www2.census.gov/geo/tiger/GENZ2021/shp/cb_2021_us_county_20m.zip"
counties_gdf = gpd.read_file(counties_shapefile_url)

# Merge the county geometries with your data based on county names
merged_gdf = pd.merge(counties_gdf, gdf, left_on="NAME", right_on="Location", how="inner")

# Save the GeoJSON file
merged_gdf.to_file("us-counties.json", driver="GeoJSON")

m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

# Choropleth map
folium.Choropleth(
    geo_data='us-counties.json',  # Replace with the path to a US counties GeoJSON file
    name='choropleth',
    data=data1,
    columns=['Location', 'Population Age 65 and Older'],
    key_on='feature.properties.NAME',  # Use the county name as the key
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population Age 65 and Older',
).add_to(m)

# Display the map
folium.LayerControl().add_to(m)

# Save the map
m.save("choropleth_map.html")