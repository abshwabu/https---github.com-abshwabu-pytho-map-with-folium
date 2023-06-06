import folium

map = folium.Map(location=[8.9806, 38.7578],zoom_start=6,tiles = "Stamen Terrain")

map.save('map.html')