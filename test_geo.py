### This file is the Unit Test for the geo.py module 

import string
from tokenize import String
from typing import List, Set, Tuple
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list 
import random 

#### TASK 1B: Check that the outputs are of the correct type and value 
def test_stations_by_distance(): 
    """Check that the outputs of stations_by_distance are of the correct type and value"""

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
    for n in range(0,len(X)-1):
        assert X[n+1][1] >= X[n][1] 

### TASK 1C: Check that the outputs are of the correct type and are ordered properly
def test_stations_within_radius(): 
    """Check that the outputs of stations_within_radius are of the correct type"""
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
    for n in range(0,len(X)-1):
        assert X[n+1] >= X[n]

### TASK 1D: Check that the outputs are of the correct type and are ordered properly 
def test_rivers_with_station(): 
    """Check that the outputs of rivers_with_station are of the correct type"""
    stations = build_station_list() 
    # Obtain output 
    X = rivers_with_station(stations)

    # Check that the output is of the correct type 
    assert type(X) == Set 

    # Check that every entry in the set is of the correct type 
    for n in range(0,len(X)-1):
        assert type(X[n]) == String 

    # The output should not contain duplicate entries 
    for entry in X:
        if X.count(entry) > 1:           # Frequency Counter 
            raise ValueError("There are duplicate entries in the output")

def test_stations_by_river(): 
    """Check that the outputs of stations_by_river are of the correct type and value"""
    stations = build_station_list() 

    # Obtain output 
    X = stations_by_river(stations)

    # Check the output type
    assert type(X) == dict 

    # We know that the River Cam is in Cambridge 
    assert "Cambridge" in X["River Cam"]
            
### TASK 1E: Check that the outputs are of the correct type and are ordered properly
def test_rivers_by_station_number():
     """Check that the outputs of rivers_by_station_number are of the correct type"""
     
     stations = build_station_list() 
     N = random.randint(1,1000)
     
     # Obtain output 
     X = rivers_by_station_number(stations, N)
     
     # Check the type of the output
     assert type(X) == list 

     #Check that the list is of length N or longer 
     assert len(X) >=N
     
     # Check that the list is in alphabetical order 
     for n in range(0,len(X)-1):
         assert X[n+1][1] >= X[n][1]