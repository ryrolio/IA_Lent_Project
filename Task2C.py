### This file prints the N rivers with the highest relative levels 
from floodsystem.flood import *
from floodsystem.stationdata import * 

# Build a list of stations 
stations = build_station_list() 

# Refresh to obtain the latest information and add to list 
update_water_levels(stations)

# Obtain output list 
list_of_stations_with_highest_level = stations_highest_rel_level(stations, 10)

# Show the output list: 
for station, level in list_of_stations_with_highest_level:
    print("{},{}".format(station.name, level))