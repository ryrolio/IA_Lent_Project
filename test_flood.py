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
    assert stations_level_over_threshold(stations,1e8) == [] 

    # If the tolerance is zero, there is at least one output 
    assert stations_level_over_threshold(stations,0) != []

### TASK 2C: Check that the outputs are reasonable.
def test_stations_highest_rel_level(): 
    """Check that the outputs of stations_highest_rel_level are of the correct type"""

    # Create stations and a list of stations 
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (0, 0)
    trange = (1, 10)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Define the relative levels for each station using the average
    s1.latest_level = (trange[0] + trange[1]) / 2 
    s2.latest_level = 0.5 * (trange[0] + trange[1]) / 2  

    # List of stations
    stations = [s1, s2] 

    # Obtain output 
    list_stations_highest_rel_level = stations_highest_rel_level(stations,1)

    # The list should only have one entry: 
    assert len(list_stations_highest_rel_level) == 1 