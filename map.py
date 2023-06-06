import folium

map = folium.Map(location=[8.9806, 38.7578],zoom_start=2,tiles = "Stamen Terrain")

map.add_child(folium.Marker(location=[8.9806,38.7578],popup='AA',icon=folium.Icon(color='green')))

map.save('map.html')