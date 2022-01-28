# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa 
from haversine import haversine, Unit 

def stations_by_distance(stations,p):
    """Returns a list of stations and distances, and sorts them by distance from a given co-ordinate"""

    # Initialise a List 
    list = []

    for station in stations:
        # Calculate distance from each station to the given coordinate
        D = haversine(station.coord,p)

        # Create a list of towns 
        list.append((station.name,D))
    
    return sorted_by_key(list,1)

def rivers_with_station(stations):
    """Returns a container of river names with stations, without any duplicating entries"""

    # Initialise a list
    list_of_rivers = []

    # First create a list of all the rivers associated with each station 
    for station in stations:
        list_of_rivers.append(station.river)
    
    set_of_rivers = set(list_of_rivers)

    return set_of_rivers 

def stations_by_river(stations):
    """Returns a dictionary that maps river names to the list of stations on a river"""
    
    set_of_rivers = rivers_with_station(stations)

    # Initialise a dictionary 
    stations_by_river = {} 

    list_of_stations_along_each_river = [] 

    for riv in set_of_rivers:
        for station in stations: 
            if station.river == riv:
                list_of_stations_along_each_river.append(station.name)
        
        stations_by_river[riv] = list_of_stations_along_each_river
        list_of_stations_along_each_river = []
        
        
    return stations_by_river 