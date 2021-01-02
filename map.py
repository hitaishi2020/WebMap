import folium

map = folium.Map(location=[38.98249085413869, -94.67612947504763],zoom_start=10,tiles="Stamen Terrain")

fg = folium.FeatureGroup("My Map features")
fg.add_child(folium.Marker(location=[38.98249085413869, -94.67612947504763],tooltip="Hi!",icon=folium.Icon(color='red'),popup = "pop",))

map.add_child(fg)

map.save("Map1.html")
