import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['NAME'])

map = folium.Map(location=[48.7767982, -121.810997],zoom_start=12,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')
for lt,ln,name in zip(lat,lon,names):
    fg.add_child(folium.Marker(location=[lt,ln],popup=name,icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('map.html')