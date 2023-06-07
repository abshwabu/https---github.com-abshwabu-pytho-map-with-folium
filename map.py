import folium

map = folium.Map(location=[8.9806, 38.7578],zoom_start=12,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')
for coordinates in [[8.9806,38.7578],[8.9806,38.7578]]:
    fg.add_child(folium.Marker(location=coordinates,popup='AA',icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('map.html')