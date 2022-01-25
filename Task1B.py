# This file prints a list of types (station name, town, distance) for the 10 closest
# and the 10 furthest stations from the Cambridge City Centre

from floodsystem.systemdata import build_station_list 
from geo import stations_by_distance 

# Build a list of stations 
stations = build_station_list()

# Create the require list
x = stations_by_distance(stations,(52.2053,0.1218))

print(x[:10])
