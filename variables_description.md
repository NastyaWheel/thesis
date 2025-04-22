# Feature Descriptions

## Raw XML Features

- `REGION` _[binary]_: Region where the traffic accident occurred.
- `DATE` _[datetime]_: Date when the traffic accident occurred.
- `TIME` _[datetime]_: Time of the accident.
- `ID` _[numeric]_: Unique identifier of the accident.
- `TYPE` _[categorical]_: Type of road traffic accident.
- `n_VEHICLES` _[numeric]_: Number of vehicles involved in the accident.
- `n_PARTICIPANTS` _[numeric]_: Number of participants involved in the accident (drivers, pedestrians, etc.).
- `n_DEATHS` _[numeric]_: Number of fatalities in the accident.
- `n_INJURED` _[numeric]_: Number of people injured in the accident.
- `COORD_L` _[numeric]_: Latitude of the accident location.
- `COORD_W` _[numeric]_: Longitude of the accident location.
- `NP` _[categorical]_: Human settlement (town/village) near the accident.
- `road_name` _[categorical]_: Name of the road where the accident occurred.
- `road_rank` _[categorical]_: Road significance (e.g., primary, secondary).
- `road_category` _[categorical]_: Road category (e.g., federal, regional, etc.).
- `road_km` _[numeric]_: Kilometer mark of the road where the accident occurred.
- `road_m` _[numeric]_: Meter mark of the road where the accident occurred.
- `road_defects` _[categorical]_: Road network maintenance defects (transport-operational condition issues).
- `adj_objects` _[categorical]_: Road network objects located near the accident scene.
- `site_objects` _[categorical]_: Road network objects directly at the accident site.
- `road_surface` _[categorical]_: Road surface condition at the time of the accident.
- `traffic_changes` _[categorical]_: Information about changes in traffic organization.
- `cause_factors` _[categorical]_: Factors that influenced the accident (e.g., weather conditions, road defects).
- `weather` _[categorical]_: Weather conditions during the accident.
- `lighting` _[categorical]_: Lighting conditions at the accident location.

## Derived/Aggregated Features

- `vehicle_failure` _[binary]_: Vehicle had technical failures during the accident.
- `non_private_vehicle` _[binary]_: A non-private vehicle was involved in the accident.
- `russian_vehicle` _[binary]_: A Russian-made vehicle was involved in the accident.
- `white_vehicle` _[binary]_: A white vehicle was present at the accident scene.
- `black_vehicle` _[binary]_: A black vehicle was present at the accident scene.
- `colored_vehicle` _[binary]_: A vehicle of other color was present at the accident scene.
- `drunk_driver` _[binary]_: A driver was found to be intoxicated.
- `female_driver` _[binary]_: A female driver participated in the accident.
- `escaped` _[binary]_: A participant or pedestrian fled the accident scene.
- `no_seatbelt_injury` _[binary]_: At least one injured participant was not wearing a seatbelt.
- `n_drunk` _[numeric]_: Total number of intoxicated participants.
- `n_children` _[numeric]_: Total number of child passengers using restraints.
- `n_cyclists` _[numeric]_: Total number of cyclists involved.
- `n_pedestrians` _[numeric]_: Total number of pedestrians involved.
- `vehicle_age_min` _[numeric]_: Minimum vehicle age among all vehicles in the accident.
- `vehicle_age_max` _[numeric]_: Maximum vehicle age among all vehicles in the accident.
- `vehicle_age_avg` _[numeric]_: Average vehicle age among all vehicles in the accident.
- `n_class_a` _[numeric]_: Number of A-class vehicles involved.
- `n_class_b` _[numeric]_: Number of B-class vehicles involved.
- `n_class_c` _[numeric]_: Number of C-class vehicles involved.
- `n_class_d` _[numeric]_: Number of D-class vehicles involved.
- `n_class_e` _[numeric]_: Number of E-class vehicles involved.
- `n_class_s` _[numeric]_: Number of S-class vehicles involved.
- `n_front_drive` _[numeric]_: Number of vehicles with front-wheel drive.
- `n_rear_drive` _[numeric]_: Number of vehicles with rear-wheel drive.
- `n_4wd` _[numeric]_: Number of vehicles with all-wheel drive.
- `n_guilty` _[numeric]_: Total number of guilty objects (vehicles or pedestrians).
- `guilty_share` _[numeric]_: Proportion of guilty objects to total vehicles.
- `n_fatal_violations` _[numeric]_: Number of unique violations committed by guilty parties.
- `guilty_exp_avg` _[numeric]_: Average experience (in years) of guilty drivers.
- `exp_avg` _[numeric]_: Average driving experience of all drivers in the accident.
- `violations` _[multilabel]_: Set of all violations (both fatal and concomitant) in the accident.
- `injury_severity` _[multilabel]_: Set of all injury severities in the accident.

## Derived Features During Work


