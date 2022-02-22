### This file is the Unit Test for the plot.py module 

import datetime
from distutils.command.build import build
from turtle import update 
from floodsystem.plot import * 
from floodsystem.datafetcher import * 
from floodsystem.stationdata import * 

# Task 2E: Use the sample dates provided in order to test whether the function produces a viable graph 
def test_plot_water_levels():
    """Check that the output of plot_water_levels is correct"""
    # Obtain lists of all stations 
    stations = build_station_list()
    update_water_levels(stations)

    # Obtain one stations from the list of stations: e.g. Cam 
    for station in stations:
        if station.name == "Cam":
            station_Cambridge = station

    assert station_Cambridge 

    # Obtain sample data
    dates = [datetime.datetime(2016, 12, 30), datetime.datetime(2016, 12, 31), datetime.datetime(2017, 1, 1), datetime.datetime(2017, 1, 2), datetime.datetime(2017, 1, 3), datetime.datetime(2017, 1, 4), datetime.datetime(2017, 1, 5)]
    
    levels = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    # Obtain output plot 
    plot_water_levels(station_Cambridge, dates, levels)

# Task 2F 
def test_plot_water_levels_with_fit(): 
    """Check that the output of plot_water_levels_with_fit is correct"""

    # Obtain a list of all stations
    stations = build_station_list()
    update_water_levels(stations) 

    # Obtain data from Cam
    for station in stations:
        if station.name == "Cam": 
            station_Cambridge = station 
    
    assert station_Cambridge 

    # Obtain sample data
    dates = [datetime.datetime(2016, 12, 30), datetime.datetime(2016, 12, 31), datetime.datetime(2017, 1, 1), datetime.datetime(2017, 1, 2), datetime.datetime(2017, 1, 3), datetime.datetime(2017, 1, 4), datetime.datetime(2017, 1, 5)]
    
    levels = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    # Degree of the polynomial required 
    p = 4 

    # Obtain output plot 
    plot_water_level_with_fit(station_Cambridge, dates, levels, p)