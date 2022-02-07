### This file prints the name of each station with a relative level greater than a threshold 

from floodsystem.flood import *
from floodsystem.stationdata import * 

# Build a list of stations 
stations = build_station_list() 

# Refresh to obtain the latest information and add to list 
update_water_levels(stations)

# Obtain output list 
list_of_stations_above_tol = stations_level_over_threshold(stations, 0.8)

# Show the output list: 
for station, level in list_of_stations_above_tol:
    print("{},{}".format(station.name, level))
