import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['NAME'])
elv = list(data['ELEV'])

def color(elve):
    if elve < 1000:
        return 'green'
    elif 1000 <= elve <3000:
        return 'orange'
    else:
        return 'red' 


map = folium.Map(location=[48.7767982, -121.810997],zoom_start=6,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')
for lt,ln,name,el in zip(lat,lon,names,elv):
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=name +'\n'+str(el)+'m',icon=folium.Icon(color=color(el))))

map.add_child(fg)

map.save('map.html')