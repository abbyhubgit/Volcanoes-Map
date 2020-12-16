import folium
import pandas

# use pandas to import Volcanoes.txt as dataframe
data = pandas.read_csv("Volcanoes.txt")
# save LAT and LON values into lists: 
lat = list(data["LAT"])
lon = list(data["LON"])  
elev = list(data["ELEV"])
names = list(data["NAME"])

# elevation < 1000 : green marker
# elevation [1000, 3000] : orange marker
# elevetion > 3000 : red marker
def choose_color(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el <= 3000:
        return 'orange'
    else:
        return 'red'

# create map 
map = folium.Map(location = [33.22, -96.68], zoom_start = 10, tiles = "Stamen Terrain")

# save features into feature group (optional - for organizing purposes)
features = folium.FeatureGroup(name="My Map")
for lt, ln, el, name in zip(lat, lon, elev, names):
    features.add_child(folium.Marker(location=[lt, ln], popup= name + ' ' + str(el)+'m', icon=folium.Icon(color=choose_color(el))))

# add features to map 
map.add_child(features)
map.save("Map1.html")
