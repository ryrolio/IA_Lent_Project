"""This module contains a collection of functions related to flood data."""

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation 

### TASK 2B 
def stations_level_over_threshold(stations, tol): 
    """Returns a list of stations that have a relative water level over the threshold"""
    
    stations = build_station_list() 

    # Initialise a List
    list_of_stations = [] 

    # Run through the list of stations and extract stations that satisfy the requirement
    for station in stations: 
        # Obtain the relative level for the station
        relative_level = station.relative_water_level() 

        # Handle consistent and inconsistent water levels 
        if relative_level == None:
            continue 
        else: 
            if relative_level > tol:
                list_of_stations.append((station, station.relative_water_level()))
    
    return list_of_stations 