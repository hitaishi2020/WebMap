import folium
import pandas

map_details = pandas.read_csv("original.txt")

latitude = map_details["LAT"]
longitude = map_details["LON"]

map = folium.Map(location=[38.98249085413869, -94.67612947504763],zoom_start=5,tiles="Stamen Terrain")
fgv = folium.FeatureGroup("My Map of USA Volcanoes")

fgv.add_child(folium.Marker(location=[38.98249085413869, -94.67612947504763],tooltip="Hi!",icon=folium.Icon(color='red',),popup = "pop",))

for la,lo in zip(latitude,longitude):
    fgv.add_child(folium.CircleMarker(location=[la,lo],radius = 6,popup="Volcono eruption record",fill_color='blue',color='grey',fill_opacity=0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read()
,style_function =lambda x: {'fillColor':'blue' if x['properties']['POP2005'] < 10000000 else 'red'})) 


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("volcanoMap.html")