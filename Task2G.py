### This file prints the towns at which the flood risk is low/moderate/high/severe: 

from floodsystem.stationdata import *
from floodsystem.analysis import * 

# Obtain list of stations 
stations = build_station_list()
update_water_levels(stations)

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
   if station.name == "Letcombe Bassett":
      continue 

   if type(station.relative_water_level()) != type(None):
      if float(station.relative_water_level()) >= 1.5 and float(rising_check(station, 4)) > 0:      
         # Classed as 'severe': high relative level and rising levels 
         severe_risk_towns.append(station.town) 
      
      elif float(station.relative_water_level()) >= 1.5 and float(rising_check(station, 4)) <= 0:    
         # Classed as 'high': high relative levels but levels are not rising
         high_risk_towns.append(station.town) 
      
      elif 0.75 <= float(station.relative_water_level()) < 1.5:  # Classed as 'moderate' 
         moderate_risk_towns.append(station.town) 
      
      elif float(station.relative_water_level()) < 0.75:     # Classed as 'low' 
         low_risk_towns.append(station.town)
  
# Return the final output 
all_towns = [severe_risk_towns, high_risk_towns, moderate_risk_towns, low_risk_towns]

severe_towns = all_towns[0] 
print("Towns at SEVERE Risk: {} Town(s): {} etc.".format(len(severe_towns), severe_towns[0:5]))

high_towns = all_towns[1]
print("Towns at HIGH Risk: {} Town(s): {} etc.".format(len(high_towns), high_towns[0:5])) 

moderate_towns = all_towns[2]
print("Towns at MODERATE Risk: {} Town(s): {} etc.".format(len(moderate_towns), moderate_towns[0:5]))

low_towns = all_towns[3]
print("Towns at LOW Risk: {} Town(s): {} etc.".format(len(low_towns), low_towns[0:5]))