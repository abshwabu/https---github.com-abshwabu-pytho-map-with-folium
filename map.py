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

fgv = folium.FeatureGroup(name='Volcanos')



for lt,ln,name,el in zip(lat,lon,names,elv):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=name +'\n'+str(el)+'m',radius=6,fill_color=color(el),color='grey',fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),style_function=lambda x: {'fillColor':'blue' if x['properties']['POP2005']<30000000 else 'orange' if 30000000 <= x['properties']['POP2005'] <= 50000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save('map.html')