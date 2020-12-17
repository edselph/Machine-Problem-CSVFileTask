import time
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 

DATAFORSTEP = pd.read_csv(r"E:\BINUS\Every meeting file\File CompSci\week 12\PR kumopul\aa.csv") 

interval = []
steps = []
for A in DATAFORSTEP['interval'].unique():
    interval.append(A)
    steps.append(DATAFORSTEP.loc[DATAFORSTEP['interval']==A, 'steps'].dropna().mean())

B = pd.DataFrame({'Interval':interval, 'Steps':steps})
B.plot.line(x="Interval", y="Steps")
plt.title('Average for 5min/step')
plt.show()