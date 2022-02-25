### This file prints the towns at which the flood risk is low/moderate/high/severe: 

from floodsystem.stationdata import *
from floodsystem.analysis import * 

# Obtain list of stations 
stations = build_station_list()
update_water_levels(stations)

# Create and show list of classified towns
all_towns = risk_ranking_of_stations(stations) 

severe_towns = all_towns[0] 
print("Towns at SEVERE Risk: {} Town(s): {} etc.".format(len(severe_towns), severe_towns[0:5]))

high_towns = all_towns[1]
print("Towns at HIGH Risk: {} Town(s): {} etc.".format(len(high_towns), high_towns[0:5])) 

moderate_towns = all_towns[2]
print("Towns at MODERATE Risk: {} Town(s): {} etc.".format(len(moderate_towns), moderate_towns[0:5]))

low_towns = all_towns[3]
print("Towns at LOW Risk: {} Town(s): {} etc.".format(len(low_towns), low_towns[0:5]))