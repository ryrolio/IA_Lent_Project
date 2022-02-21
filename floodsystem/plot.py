"""This module plots real-time data obtained from various stations"""

import matplotlib 
import matplotlib.pyplot as plt 
import datetime
import numpy as np 
from floodsystem.analysis import *

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
    """Plots the water level data and best fit polynomial"""
    float_dates = matplotlib.dates.date2num(dates)

    shift_dates = []

    for i in range(len(float_dates)):
        shift_dates.append(float_dates[i] - float_dates[0])
  
    coefficient = np.polyfit(shift_dates, levels, p)
  
    poly = np.poly1d(coefficient)
    
    # Plot original data points
    plt.plot(shift_dates, levels, '.')

    # Obtain x-axis of polynomial 
    x = np.linspace(shift_dates[0],shift_dates[-1],50)
    
    # Obtain y-axis data 
    high_level = [station.typical_range[1]]*len(x) 
    low_level = [station.typical_range[0]]*len(x)

    # Plot the data 
    plt.plot(x, poly(x - x[0]), label = "Best Fit Curve")
    plt.plot(x, high_level, label = "Typical High Level")
    plt.plot(x, low_level, label = "Typical Low Level")

    # Add labels/title/legend 
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.legend()
    plt.xticks(rotation = 45) 
    plt.title(station.name + " Water Level")
    plt.tight_layout() 

    return plt.show()
    
