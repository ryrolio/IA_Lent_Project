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

def risk_ranking_of_stations(stations): 
  """Task 2G, given a list of stations, this function sorts the stations into low/medium/high/severe"""
  # Obtain a list of unique towns 
  town_list0 = [] 

  for station in stations: 
    town_list0.append(station.town) 
    town_list = list(set(town_list0)) 
  
  # Initialise Ranking Lists 
  low_risk_towns = [] 
  moderate_risk_towns = [] 
  high_risk_towns = [] 
  severe_risk_towns = [] 

  # Sort based on flood risk 
  for station in stations: 
    if type(station.relative_water_level()) != type(None):
      if float(station.relative_water_level()) >= 2:      # Classed as 'severe' 
        severe_risk_towns.append(station.town) 

      elif 1.5 <= float(station.relative_water_level()) < 2.0:    # Classed as 'high' 
        high_risk_towns.append(station.town) 

      elif 1.0 <= float(station.relative_water_level()) < 1.5:  # Classed as 'moderate' 
        moderate_risk_towns.append(station.town) 
      
      elif float(station.relative_water_level()) < 1.0:     # Classed as 'low' 
        low_risk_towns.append(station.town)
  
  # Return the final output 
  classified_towns_by_risk = [severe_risk_towns, high_risk_towns, moderate_risk_towns, low_risk_towns]

  return classified_towns_by_risk 