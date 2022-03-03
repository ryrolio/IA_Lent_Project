### This file produces plots the best fit polynomial for the top 5 stations, going back 2 days, polynomial degree 4

import datetime
from floodsystem.stationdata import *
from floodsystem.datafetcher import *
from floodsystem.plot import *
from floodsystem.analysis import *
from floodsystem.flood import *
from floodsystem.station import * 

# Build a list of stations 
stations = build_station_list()
update_water_levels(stations)

# Set the degree of the polynomial 
p = 4 

# Set the number of days over which we take data 
dt = 2

# Identify the stations with the highest risk 
stations_highest = stations_highest_rel_level(stations, 6) 

# Plot the graphs for each highest risk station in the list 
for entry in stations_highest: 
    for station in stations:
        if station.name == "Letcombe Bassett":
            continue 

        if station.name == "Whitchurch Main":
            continue 

        if station == entry[0]:
            dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, p)
