# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/16 11:56'
__author__ = 'lee7goal'
import pandas as pd
import matplotlib.pyplot as plt
from math import exp


# get the data
target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

# read the data of abalone and set the data first line
abalone = pd.read_csv(target_url, header=None, prefix="V")
# ['性'，'长度'，'直径'，'身高'，'整体重量'，'去壳重量'，'内脏重量'，'壳重量'，'戒指']
abalone.columns = [
    'Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings'
]

#get summary to use for scaling
summary = abalone.describe()
minRings = summary.iloc[3, 7]
maxRings = summary.iloc[7, 7]
nrows = len(abalone.index)

for i in range(nrows):
    # plot rows of data as if they were series data
    dataRow = abalone.iloc[i, 1:8]
    labelColor = (abalone.iloc[i, 8] - minRings) / (maxRings - minRings)
    dataRow.plot(color=plt.cm.RdYlBu(labelColor), alpha=0.5)

plt.xlabel("Attribute Index")
plt.ylabel("Attribute Values")
plt.show()

# renormalize using mean and standard variation, then compress
# with logit function
meanRings = summary.iloc[1, 7]
sdRings = summary.iloc[2, 7]

for i in range(nrows):
    # plot rows of data as if they were series data
    dataRow = abalone.iloc[i, 1:8]
    normTarget = (abalone.iloc[i, 8] - meanRings)/sdRings
    labelColor = 1.0/(1.0 + exp(-normTarget))
    dataRow.plot(color=plt.cm.RdYlBu(labelColor), alpha=0.5)

plt.xlabel("Attribute Index")
plt.ylabel("Attribute Values")
plt.show()