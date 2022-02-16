"""Unit test for the flood module"""

from floodsystem.flood import *
from floodsystem.station import * 

### TASK 2B: Check that the outputs are of the correct type and are ordered properly  
def test_stations_level_over_threshold(): 
    """Check that the outputs of stations_level_over_threshold are of the correct type"""
    
    # Obtain a list of stations 
    stations = build_station_list() 
    update_water_levels(stations)

    # If the tolerance is set to a high number, there should be no output 
    assert stations_level_over_threshold(stations,1e6) == [] 

    # If the tolerance is zero, there is at least one output 
    assert stations_level_over_threshold(stations,0) != []