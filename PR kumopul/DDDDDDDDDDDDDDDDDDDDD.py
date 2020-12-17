import datetime
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
import calendar

DATAAAAAA = pd.read_csv(r"E:\BINUS\Every meeting file\File CompSci\week 12\PR kumopul\aa.csv") 

def Theday(date): 
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    the_date = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    if calendar.day_name[the_date] in weekdays:
        return 'weekday'
    else:
        return 'weekend'

DATAAAAAA['day'] = DATAAAAAA['date'].apply(Theday)

interval = []
steps_weekday = []
steps_weekend = []
for a in DATAAAAAA['interval'].unique():
    interval.append(a)
    steps_weekday.append(DATAAAAAA.loc[(DATAAAAAA['interval']==a) & (DATAAAAAA['day']=='weekday'), 'steps'].dropna().mean())
    steps_weekend.append(DATAAAAAA.loc[(DATAAAAAA['interval']==a) & (DATAAAAAA['day']=='weekend'), 'steps'].dropna().mean())

datafile = pd.DataFrame({'Interval':interval, 'Weekday': steps_weekday,'Weekend':steps_weekend})

datafile.plot(x ='Interval', kind = 'line')
plt.title('AVrg 5min/steps')
plt.ylabel('Steps')
plt.show()