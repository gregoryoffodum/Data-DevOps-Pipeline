#!/bin/bash

for year in `seq 2016 2018`;do for month in `seq 1 12`;do wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5051&Year=${year}&Month=${month}&Day=14&timeframe=3&submit= Download+Data" ;done;done

