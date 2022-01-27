from floodsystem.geo import rivers_with_station 
from floodsystem.stationdata import build_station_list 

# Build a list of stations 
stations = build_station_list()

# How many rivers contain at least one monitoring system? 
set_of_rivers = rivers_with_station(stations)
print("There are {} rivers with a station(s).".format(len(set_of_rivers)))

# Convert back into a list, since a set does not support indexing 
list_of_rivers = list(set_of_rivers)
sorted_list_of_rivers = sorted(list_of_rivers)
print(sorted_list_of_rivers[:10])