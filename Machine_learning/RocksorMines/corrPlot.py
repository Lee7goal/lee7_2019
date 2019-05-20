# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 16:12'
__author__ = 'lee7goal'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

# get the data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
print("Get the data finished!")

# calculate correlations between real-valued attributes
dataRow2 = rocksVMines.iloc[1, 0:60]
dataRow3 = rocksVMines.iloc[2, 0:60]

plt.scatter(dataRow2, dataRow3)

# set the scatter settings
plt.xlabel("2nd Attributes")
plt.ylabel("3rd Attributes")
plt.show()

# a e.g for 2 to 21 compare
dataRow21 = rocksVMines.iloc[20, 0:60]
plt.scatter(dataRow2, dataRow21)

plt.xlabel("2nd Attributes")
plt.ylabel("21st Attributes")
plt.show()

