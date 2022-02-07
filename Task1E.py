### This file prints the N rivers with the greatest number of stations
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list 


# Build a list of stations 
stations = build_station_list()

print(rivers_by_station_number(stations,9))
