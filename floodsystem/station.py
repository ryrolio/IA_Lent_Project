# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    #### TASK 1F #### 

    def typical_range_consistent(self): 
        """This method reports whether or not the Monitoring Station has a results for the high & low range data"""
        return type(self.typical_range) == tuple 

    #### TASK 2B #### 
    def relative_water_level(self):
        """This method reports the latest water level as a fraction of the typical range; if not available, reports none"""

        if self.latest_level is None or self.typical_range is None:
            return None 
        else: 
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])

def inconsistent_typical_range_stations(stations):
    """Given a list of stations, this returns a list of stations that have inconsistent data""" 

    inconsistent_station_list = [] 

    for station in stations: 
        if station.typical_range_consistent() == False:
            inconsistent_station_list.append(station)
    
    return inconsistent_station_list 
