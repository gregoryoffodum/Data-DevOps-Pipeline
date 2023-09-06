import sys
import pandas as pd

weather_all = pd.read_csv('weather_all.csv')
year = sys.argv[1]

if (int(year) in [1996,1997,1998]):
        minimum = weather_all[weather_all['Year'] == int(year)]['Mean Temp (°C)'].min()
        maximum = weather_all[weather_all['Year'] == int(year)]['Mean Temp (°C)'].max()

        print('Min temperature for year is:' + ' ' + str(minimum))
        print('Max temperature for year is:' + ' ' + str(maximum))

else:
        print('Please enter year 1996, 1997 or 1998')

