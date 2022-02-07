# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#### TASK 1B ####

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

#### TASK 1C #### 

def stations_within_radius(stations, centre, r):

    """Returns a list of all stations within a radius of a specified geographic coordinate."""

    # Initialise a List

    list = []

    #build list with stations and their respective distances to centre

    stations_distance_list = stations_by_distance(stations,centre)

    for tup in stations_distance_list:

        # Use distance from station to a given coordinate given by function stations_by_distance

        distance = tup[1]

        if distance < r:

            #Add to list if distance is less than r

            list.append(tup[0])

    return list

#### TASK 1D ####

def rivers_with_station(stations):
    """Returns a container of river names with stations, without any duplicating entries"""

    # Initialise a list
    list_of_rivers = []

    # First create a list of all the rivers associated with each station 
    for station in stations:
        list_of_rivers.append(station.river)
    
    set_of_rivers = set(list_of_rivers)

    return set_of_rivers 

def stations_within_radius(stations, centre, r):
    """Returns a list of all stations within a radius of a specified geographic coordinate."""
    # Initialise a List 
    list = []
    #build list with stations and their respective distances to centre
    stations_distance_list = stations_by_distance(stations,centre)
    for tup in stations_distance_list: 
        # Use distance from station to a given coordinate given by function stations_by_distance 
        distance = tup[1]
        if distance < r:
            #Add to list if distance is less than r
            list.append(tup[0])
    return list


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

#### TASK 1E ####

def rivers_by_station_number(stations, N):
    """Gives a list of N rivers with the greatest number of monitoring stations"""
    list = []
    dictionary = stations_by_river(stations)
    for river in dictionary:
        n = len(dictionary[river])
        tup = (river, n)
        list.append(tup)
    sorted_list = sorted_by_key(list,1,1)
    N_list = sorted_by_key(list,1,1)[:N]
    x = 0
    while sorted_list[N+x] == sorted_list[N]:
        N_list.append(sorted_list[N+x])
        x +=1
    return N_list
