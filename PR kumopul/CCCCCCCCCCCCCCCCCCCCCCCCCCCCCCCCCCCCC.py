import datetime
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
import calendar

# yeahhh i just import everything :D
DATAAAAAA = pd.read_csv(r"E:\BINUS\Every meeting file\File CompSci\week 12\PR kumopul\aa.csv") 
print(pd.isnull(DATAAAAAA).sum())

New_DATAAAAAA = DATAAAAAA.fillna(0)

print(pd.isnull(New_DATAAAAAA).sum())
days = []
steps = []
for a in New_DATAAAAAA['date'].unique():
    days.append(a)
    steps.append(New_DATAAAAAA.loc[DATAAAAAA['date']==a, 'steps'].sum())

data_plot = pd.DataFrame({'Days':days, 'Steps':steps})

Thefinaldata = data_plot.plot.bar(x='Days', y='Steps', width=0.1 , color='r')
plt.title('Total Number of Steps Per Day')
plt.xlabel('Days')
plt.ylabel('Steps')
plt.show()
