"""This module contains functions relating to function fitting"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import datetime 


def polyfit(dates, levels, p):
  """Given the water level time history, the function computes a least-squares fit of a polynomial of degree p to water level data, returning a tuple of the polynomial object and any shift of the time axis"""
  
  float_dates = matplotlib.dates.date2num(dates)
  
  d0 = float_dates[0]
  shift_dates = []
  for i in range(len(float_dates)):
    shift_dates.append(float_dates[i] - float_dates[0])
  
  coefficient = np.polyfit(shift_dates, levels, p)
  
  poly = np.poly1d(coefficient)
  
  poly_tuple = (poly, d0)

  return poly_tuple 



