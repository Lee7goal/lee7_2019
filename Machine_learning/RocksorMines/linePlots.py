# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 15:58'
__author__ = 'lee7goal'
import pandas as pd
import matplotlib.pyplot as plt

# get the data
print("get the data")

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

for i in range(208):
    # assign color based on "M" or "R" labels
    if rocksVMines.iat[i, 60] == "M":
        pcolor = 'red'
    else:
        pcolor = 'blue'

    # plot rows of data as if they were series data
    dataRow = rocksVMines.iloc[i, 0:60]
    dataRow.plot(color=pcolor)

plt.xlabel("Attributes Index")
plt.ylabel("Attributes Values")
plt.show()
