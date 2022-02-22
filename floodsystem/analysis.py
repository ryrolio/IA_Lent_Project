"""This module contains functions relating to function fitting"""

import matplotlib 
import numpy as np 
import datetime 

### TASK 2F 
def polyfit(dates, levels, p):
  """Given the water level time history, this function computes the least squares polynomial of degree p"""

  # Convert dates into floats 
  date_floats = matplotlib.dates.date2num(dates) 

  # Obtain date shift 
  d0 = date_floats[0] 

  # Find the coefficients of the best fit polynomial 
  coeff = np.polyfit(d0 - date_floats , levels, p)

  # Convert coefficients into a polynomial 
  poly = np.poly1d(coeff) 

  return poly, d0

###TASK 2G

def rising_check(dates, levels, p):
  """Finds the derivative of the polynomial function found by polyfit, and if the gradient is greater than zero (ie if the water level is rising) returns true"""
  poly, d0 = polyfit(dates, levels, p)
  gradient = np.polyder(poly)
  if gradient > 0:
    return True
  else:
    return False

  
