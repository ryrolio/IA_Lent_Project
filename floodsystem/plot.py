"""This module plots real-time data obtained from various stations"""

import matplotlib 
import matplotlib.pyplot as plt 
from datetime import datetime, timedelta 
import numpy as np 

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
    plt.ylabel("water Level (m)")
    plt.legend()
    plt.xticks(rotation = 45) 
    plt.title(station.name + " Water Level")
    plt.tight_layout() 

    plt.show()
 
### TASK 2F
def plot_water_level_with_fit(station, dates, levels, p):
