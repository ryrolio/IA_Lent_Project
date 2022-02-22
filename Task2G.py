### This file uses existing implmentations to decide which regions are at the
### highest risk of flooding.

stations = build_station_list()
update_water_levels(stations)

severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []

for station in stations:
   if station.relative_water_level() > 1.5:
      severe_risk.append((station.name, station.relative_water_level()))
   elif station.relative_water_level() > 1 and rising_check(stations) == True:
      severe_risk.append((station.name, station.relative_water_level()))
   elif station.relative_water_level() > 1:
      high_risk.append((station.name, station.relative_water_level()))
   elif station.relative_water_level() > 0.5 and rising_check(stations) == True:
      high_risk.append((station.name, station.relative_water_level()))
   elif station.relative_water_level() > 0.5:
      moderate_risk.append((station.name, station.relative_water_level()))
   elif station.relative_water_level() > 0 and rising_check(stations) == True:
      moderate_risk.append((station.name, station.relative_water_level()))
   elif station.relative_water_level() <= 0:
      low_risk.append((station.name, station.relative_water_level()))
     


  
