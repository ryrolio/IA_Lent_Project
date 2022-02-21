### This file produces plots the best fit polynomial for the top 5 stations, going back 2 days, polynomial degree 4

import datetime
from floodsystem.stationdata import *
from floodsystem.datafetcher import *
from floodsystem.plot import *
from floodsystem.analysis import *
from floodsystem.flood import *
	
stations = build_station_list()
update_water_levels(stations)

#Get the top 5 stations with the highest water level
highest_wl_stations = stations_highest_rel_level(stations, 5)
dt = 5

#Find data for the 5 stations and then plot the data using the 2F function polyfit
for item in highest_wl_stations:
    for station in stations:
        if station == item[0]:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_level_with_fit(station.name, dates, levels,4)