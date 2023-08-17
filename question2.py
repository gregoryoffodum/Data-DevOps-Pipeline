import sys
import pandas as pd

weather_all = pd.read_csv('weather_all.csv')
year = sys.argv[1]

def percentdiff(yr):
    if (int(year) == 1998):

        diff1 = ((weather_all[weather_all['Year']==1996]['Mean Temp (°C)'].mean())\
                /(weather_all[weather_all['Year']==1997]['Mean Temp (°C)'].mean())) - 1
        
        diff2 = ((weather_all[weather_all['Year']==1996]['Mean Temp (°C)'].mean())\
        /(weather_all[weather_all['Year']==1998]['Mean Temp (°C)'].mean())) - 1

        diff1=diff1.round(2) * 100
        diff2=diff2.round(2) * 100

        print('The percent difference btw avg temperature for year ' + str(year) 
                + ' and other years are: ' + str(diff1) + '%'
                + ' and ' + str(diff2) + '%')
    elif (int(year) == 1997):

        diff1 = ((weather_all[weather_all['Year']==1997]['Mean Temp (°C)'].mean())\
                /(weather_all[weather_all['Year']==1998]['Mean Temp (°C)'].mean())) - 1
        
        diff2 = ((weather_all[weather_all['Year']==1997]['Mean Temp (°C)'].mean())\
        /(weather_all[weather_all['Year']==1996]['Mean Temp (°C)'].mean())) - 1

        diff1=diff1.round(2) * 100
        diff2=diff2.round(2) * 100

        print('The percent difference btw avg temperature for year ' + str(year) 
                + ' and other years are: ' + str(diff1) + '%'
                + ' and ' + str(diff2) + '%')    
    
    elif (int(year) == 1996):

        diff1 = ((weather_all[weather_all['Year']==1998]['Mean Temp (°C)'].mean())\
                /(weather_all[weather_all['Year']==1997]['Mean Temp (°C)'].mean())) - 1
        
        diff2 = ((weather_all[weather_all['Year']==1998]['Mean Temp (°C)'].mean())\
        /(weather_all[weather_all['Year']==1996]['Mean Temp (°C)'].mean())) - 1

        diff1=diff1.round(2) * 100
        diff2=diff2.round(2) * 100

        print('The percent difference btw avg temperature for year ' + str(year) 
                + ' and other years are: ' + str(diff1) + '%'
                + ' and ' + str(diff2) + '%')
    else:   
        print('Please enter year 1996, 1997 or 1998')

percentdiff(year)
