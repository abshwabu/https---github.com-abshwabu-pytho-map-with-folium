import folium

map = folium.Map(location=[8.9806, 38.7578],zoom_start=12,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')

fg.add_child(folium.Marker(location=[8.9806,38.7578],popup='AA',icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('map.html')