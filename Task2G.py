### This file uses existing implmentations to decide which regions are at the
### highest risk of flooding.

from floodsystem.analysis import * 
from floodsystem.datafetcher import * 
from floodsystem.stationdata import * 
import datetime

stations = build_station_list()
update_water_levels(stations)

dt = 5
p = 4

severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []


for station in stations:
   #fetch measure levels
   dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))

   if type(station.relative_water_level()) == type(None):
       continue 
                                        
   elif station.relative_water_level() > 1.5:
      severe_risk.append(station.name)
                                        
   elif station.relative_water_level() > 1 and rising_check(dates, levels, p) == True:
      severe_risk.append(station.name)
                                        
   elif station.relative_water_level() > 1:
      high_risk.append(station.name)
                                        
   elif station.relative_water_level() > 0.5 and rising_check(dates, levels, p) == True:
      high_risk.append(station.name)
                                        
   elif station.relative_water_level() > 0.5:
      moderate_risk.append(station.name)
                                        
   elif station.relative_water_level() > 0 and rising_check(dates, levels, p) == True:
      moderate_risk.append(station.name)
                                        
   elif station.relative_water_level() <= 0:
      low_risk.append(station.name)
     


  
