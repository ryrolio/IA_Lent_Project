# This file prints a list of the stations within 10km of the Cambridge city centre 
# in alphabetical order

from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

# Build a list of stations 
stations = build_station_list()

# Create the required list
x = stations_within_radius(stations, (52.2053,0.1218), 10)

print(sorted(x))