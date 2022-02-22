### This file is the Unit Test for the analysis.py module 

import matplotlib
import pytest
import math
import numpy as np
from floodsystem.analysis import *

def test_polyfit(): 
    # Number of Data Points 
    N = 20

    # Create a set of dates 
    x = np.linspace(10000, 10005, N)
    dates = matplotlib.dates.date2num(x) 

    # The water levels must follow a known function, x^4 
    levels0 = np.linspace(0,20,N)
    levels = levels0**4 

    # Obtain outputs of the polyfit function 
    function, shift = polyfit(x, levels, 4) 

    assert type(function) == np.poly1d
    assert type(shift) == np.float64