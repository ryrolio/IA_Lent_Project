### This file uses existing implmentations to decide which regions are at the
### highest risk of flooding.

stations = build_station_list()
update_water_levels(stations)

severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []



for station in stations_level_over_threshold(stations, 1.5):
   if rising_check(stations) = True:
    severe_risk.append((station.name, station.relative_water_level))
   else:
    high_risk.append((station.name, station.relative_water_level))

for station in stations_level_over_threshold(stations, 1):
   if rising_check(stations) = True:
    high_risk.append((station.name, station.relative_water_level))
   else:
    moderate_risk.append((station.name, station.relative_water_level))
    
for station in stations_level_over_threshold(stations, 0.5):
   if rising_check(stations) = True:
    moderate_risk.append((station.name, station.relative_water_level))
   else:
    low_risk.append((station.name, station.relative_water_level))

for station in stations_level_over_threshold(stations, 0):
   if rising_check(stations) = True:
    low_risk.append((station.name, station.relative_water_level))
   else:
    low_risk.append((station.name, station.relative_water_level))

    
s = set(severe_risk)
h = set(high_risk)
m = set(moderate_risk)
l = set(low_risk)

severe_risk = list(s)
high_risk = list(h)
moderate_risk = list(m)
low_risk = list(l)

  
