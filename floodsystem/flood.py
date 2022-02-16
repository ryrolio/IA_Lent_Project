"""This module contains a collection of functions related to flood data."""

from .stationdata import * 
from .station import MonitoringStation 
from .utils import sorted_by_key

### TASK 2B 
def stations_level_over_threshold(stations, tol): 
    """Returns a list of stations that have a relative water level over the threshold"""
    
    # Initialise a List
    list_of_stations = [] 

    # Run through the list of stations and extract stations that satisfy the requirement
    for station in stations: 
        # Obtain the relative level for the station
        relative_level = station.relative_water_level()

        # Handle consistent and inconsistent water levels 
        if relative_level != None:
            if relative_level > tol:
                list_of_stations.append((station, relative_level)) 
    
    list_of_stations = sorted_by_key(list_of_stations,1,reverse=True)

    return list_of_stations 

### TASK 2C 
def stations_highest_rel_level(stations, N): 
    """Returns a list of the N stations with the highest relative levels"""

    # Produce a list that ranks all the stations by relative level 
    list_of_stations = []

    for station in stations:
        relative_level = station.relative_water_level() 

        if relative_level != None:
            list_of_stations.append((station, relative_level))
    
    list_of_stations = sorted_by_key(list_of_stations,1,reverse=True) 

    # Extract the first N entries 
    return list_of_stations[0:N]