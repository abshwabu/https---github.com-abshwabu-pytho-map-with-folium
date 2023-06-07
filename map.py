import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])

map = folium.Map(location=[8.9806, 38.7578],zoom_start=12,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')
for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup='AA',icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('map.html')