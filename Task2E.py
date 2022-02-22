### This file produces plots of the water levels for different stations 

from floodsystem.stationdata import * 
from floodsystem.datafetcher import * 
from floodsystem.flood import * 
from floodsystem.plot import * 
from floodsystem.station import *
import datetime 

# Create Empty List
highest_risk_stations_measure_id = []

# Build a list of stations 
stations = build_station_list() 

# Refresh to obtain the latest information and add to list 
update_water_levels(stations)

# Obtain list of stations that have the highest levels 
highest_risk_stations = stations_highest_rel_level(stations,6)

# Take data from the past 10 days 
dt = 10 

# Cycle through each station in the list and produce the plot 
for entry in highest_risk_stations:
    for station in stations:
        if station.name == "Letcombe Bassett":
            continue 

        if station == entry[0]:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_levels(station, dates, levels)