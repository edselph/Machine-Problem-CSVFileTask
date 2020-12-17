import datetime
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
import calendar

step = pd.read_csv(r"E:\BINUS\Every meeting file\File CompSci\week 12\PR kumopul\aa.csv") 
print(step)

days = []
steps = []
step.dropna()

for a in step["date"].unique():
    days.append(a)
    steps.append(step.loc[step['date']==a, 'steps'].sum())
# step.hist(column="steps") cant use histogram :,D

TheColumndata = pd.DataFrame({'Days':days, 'Steps':steps})
asdasd = TheColumndata.plot.bar(x='Days', y='Steps', width=0.1 , color='r')
plt.title('step/daysssssssss')
plt.xlabel('Days')
plt.ylabel('Steps')
plt.show()

print("report: ")
print(f"Mean: {TheColumndata.mean().item()}")
print(f"Median: {TheColumndata.median().item()}")