import geocoder
import folium

g = geocoder.ip("your ip")
myAddress = g.latlng
print(myAddress)
myMap = folium.Map(location=myAddress, zoom_start=12)
folium.CircleMarker(location=myAddress, radius=50, popup="You").add_to(myMap)
folium.Marker(myAddress, popup="You").add_to(myMap)
myMap.save("mymap.html")
