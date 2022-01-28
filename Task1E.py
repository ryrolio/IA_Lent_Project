from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import rivers_with_station 
from floodsystem.stationdata import build_station_list 
from floodsystem.geo import stations_by_river 

# Build a list of stations 
stations = build_station_list()

print(rivers_by_station_number(stations,11))
