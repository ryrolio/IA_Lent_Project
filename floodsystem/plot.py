"""This module plots real-time data obtained from various stations"""

from matplotlib import *
import matplotlib.pyplot as plt 
import datetime
import numpy as np 
from floodsystem.analysis import *
from floodsystem.station import * 
from floodsystem.stationdata import * 
from floodsystem.datafetcher import * 

### TASK 2E
def plot_water_levels(station, dates, levels):
    """Plots the water levels for a particular station over a range of dates"""

    # Obtain y-axis data 
    high_level = [station.typical_range[1]]*len(dates) 
    low_level = [station.typical_range[0]]*len(dates)

    # Plot the data 
    plt.plot(dates, levels, label = "Water Level")
    plt.plot(dates, high_level, label = "Typical High Level")
    plt.plot(dates, low_level, label = "Typical Low Level")

    # Add labels/title/legend 
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.legend()
    plt.xticks(rotation = 45) 
    plt.title(station.name + " Water Level")
    plt.tight_layout() 

    return plt.show()

### TASK 2F 
def plot_water_level_with_fit(station, dates, levels, p): 
    """Plots the water level data and the least square fit polynomial for any station"""

    # Obtain x-axis data 
    time = matplotlib.dates.date2num(dates) 

    # Obtain the polynomial and initial shift 
    function, offset = polyfit(dates, levels, p)

    high_level = [station.typical_range[1]]*len(dates) 
    low_level = [station.typical_range[0]]*len(dates) 

    # Show the graph of the polynomial fit 
    plt.plot(dates, function(offset - time), label = "Best Fit Curve")

    # Show the graph of the actual water levels 
    plt.plot(dates, high_level, label = "Typical High Level")
    plt.plot(dates, low_level, label = "Typical Low Level")

    # Add labels/title/legend 
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation = 45)
    plt.title(station.name + " Water Level")
    plt.tight_layout() 

    plt.show() 