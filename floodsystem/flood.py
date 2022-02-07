"""This module contains a collection of functions related to flood data."""

from floodsystem.stationdata import build_station_list
from floodsystem.station import * 

### TASK 2B 
stations = build_station_list() 

def stations_level_over_threshold(stations, tol): 
    """Returns a list of stations that have a relative water level over the threshold"""