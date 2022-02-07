from floodsystem.stationdata import build_station_list
from floodsystem.station import * 

# Build a list of stations 
stations = build_station_list()

list_of_inconsistent_stations = inconsistent_typical_range_stations(stations)

# Extract only the names of the stations 
names_of_inconsistent_stations = []

for station in list_of_inconsistent_stations:
    names_of_inconsistent_stations.append(station.name)

names_of_inconsistent_stations.sort()

print(names_of_inconsistent_stations)