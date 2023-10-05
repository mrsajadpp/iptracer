import geocoder
import folium
import os

# Display a warning message
print("\n\033[91mWARNING: We do not promote any illegal activities. Use this for educational purposes only - Developed by Sajad pp.\033[0m\n")

# Get user input for the IP address
user_ip = input("Enter an IP address: ")


# Use the geocoder library to get the location of the IP address
g = geocoder.ip(user_ip)
myAddress = g.latlng
print("Location based on IP address:", myAddress)

# Create a directory based on the IP address
directory_name = "_".join(map(str, myAddress))
os.makedirs(directory_name, exist_ok=True)

# Create a map using Folium
myMap = folium.Map(location=myAddress, zoom_start=12)

# Add a circle marker and a regular marker to the map
folium.CircleMarker(location=myAddress, radius=50, popup="You").add_to(myMap)
folium.Marker(myAddress, popup="You").add_to(myMap)

# Save the map as an HTML file within the directory
html_file_path = os.path.join(directory_name, f"{user_ip}.html")
myMap.save(html_file_path)

# Return the URL of the saved HTML file
url = "file://" + os.path.abspath(html_file_path)
print("Map saved as:", url)
