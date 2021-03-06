# This file prints a list of types (station name, town, distance) for the 10 closest
# and the 10 furthest stations from the Cambridge City Centre

from floodsystem.geo import stations_by_distance 
from floodsystem.stationdata import build_station_list 


# Build a list of stations 
stations = build_station_list()

# Create the required list
x = stations_by_distance(stations,(52.2053,0.1218))

# Print the 10 closest stations 
print(x[:10])

# Print the 10 furthest stations
print(x[-10:])