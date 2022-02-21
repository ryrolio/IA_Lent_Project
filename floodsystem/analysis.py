"""This module contains functions relating to function fitting"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = matplotlib.dates.date2num(dates)

def polyfit(dates, levels, p):
  """Given the water level time history, the function computes a least-squares fit of a polynomial of degree p to water level data, returning a tuple of the polynomial object and any shift of the time axis"""
  
  # Create set of 10 data points on interval (1000, 1002)
  dates = x = np.linspace(10000, 10002, 10)
  y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

  # Using shifted x values, find coefficient of best-fit
  # polynomial f(x) of degree 4
  p_coeff = np.polyfit(x - x[0], y, 4)

  # Convert coefficient into a polynomial that can be evaluated
  # e.g. poly(0.3)
  poly = np.poly1d(p_coeff)

  poly, d0 = polyfit(dates, levels, 3)



