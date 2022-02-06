### This file is the Unit Test for the geo.py module 

from typing import List, Tuple
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list 
import random 

#### TASK 1B: Check that the outputs are of the correct type and value 
def test_stations_by_distance(): 
    stations = build_station_list()
    p = (52.2053,0.1218) 
    X = stations_by_distance(stations,p)

    # The output must be a list 
    if type(X) != List:
        raise TypeError("Output is not a list")
    
    # Every entry in the list must be a tuple 
    for entry in X:
        if type(entry) != Tuple:
            raise TypeError("At least one entry in the list is not a tuple")
            break 

    # Check that the list orders each station by distance 
    for n in range(1,len(X)):
        assert X[n+1][1] >= X[n][1] 

### TASK 1C: Check that the outputs are of the correct type and are ordered properly
def test_stations_within_radius(): 
    stations = build_station_list()
    p = (52.2053,0.1218) 

    # We know that there are no stations within a radius of 0 
    assert stations_within_radius(stations,p,0) == []   

    # We know that for any radius, the output list must be in alphabetical order 
    # Choose a random radius 
    R = random.randint(5,10000) 
    # Obtain output list 
    X = stations_within_radius(stations,p,R)
    # Check the type of the output
    assert type(X) == list 
    # Check that the list is in alphabetical order 
    for n in range(1,len(X)):
        assert X[n+1] >= X[n]
