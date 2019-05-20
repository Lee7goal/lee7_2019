# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 18:03'
__author__ = 'lee7goal'
import pandas as pd
import matplotlib.pyplot as plt
from  pandas import DataFrame
from random import uniform

# get the data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
print("Get the data finished!")

# change the targets to numeric value
target = []
for i in range(208):
    # assign 0 or 1 target values based on "M" or "R" labels
    if rocksVMines.iat[i, 60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

# plot 35th attribute
dataRow = rocksVMines.iloc[0:208, 35]
plt.scatter(dataRow, target)
plt.xlabel("Attribute Value")
plt.ylabel("Target Value")
plt.show()

"""
To improve the visualization, this version dithers the points a little
and makes them somewhat transparent 
"""
target = [] 
for i in range(208):
    # assign 0 or 1 target value based on "M" or "R" labels and add some dither
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))

# plot 35th attribute with semi-opaque points
dataRow = rocksVMines.iloc[0:208, 35]
plt.scatter(dataRow, target, alpha=0.5, s=120)
plt.xlabel("Attribute Value")
plt.ylabel("Target Value")
plt.show()
