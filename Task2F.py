### This file produces plots the best fit polynomial for the top 5 stations, going back 2 days, polynomial degree 4

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import floodsystem.plot as plot
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
	
stations = build_station_list()
update_water_levels(stations)

#Get the top 5 stations with the highest water level
highest_wl_stations = stations_highest_rel_level(stations, 5)
dt = 5

#Find data for the 5 stations and then plot the data using the 2F function polyfit
for item in highest_wl_stations:
    for station in stations:
        if station.name == item[0]:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            print((polyfit(dates, levels, 4)))
            plot.plot_water_level_with_fit(station.name, dates, levels, 4)

