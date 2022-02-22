### This file uses existing implmentations to decide which regions are at the
### highest risk of flooding.

stations = build_station_list()
update_water_levels(stations)

severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []

for station in stations_level_over_threshold(stations, 1.5):
  severe_risk
  
  
