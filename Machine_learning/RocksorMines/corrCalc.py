# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/15 10:48'
__author__ = 'lee7goal'
import pandas as pd
from pandas import DataFrame
from math import sqrt

# get the data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
print("Get the data finished!")

# calculate correlations between real-valued attribute
dataRow2 = rocksVMines.iloc[1, 0:60]
dataRow3 = rocksVMines.iloc[2, 0:60]
dataRow21 = rocksVMines.iloc[20, 0:60]

mean2, mean3, mean21 = 0.0, 0.0, 0.0
numElt = len(dataRow2)
for i in range(numElt):
    mean2 += dataRow2[i]/numElt
    mean3 += dataRow3[i]/numElt
    mean21 += dataRow21[i]/numElt

var2, var3, var21 = 0.0, 0.0, 0.0
for i in range(numElt):
    var2 += (dataRow2[i] - mean2) * (dataRow2[i] - mean2)/numElt
    var3 += (dataRow3[i] - mean3) * (dataRow3[i] - mean3)/numElt
    var21 += (dataRow21[i] - mean21) * (dataRow21[i] - mean21)/numElt

corr23, corr221 = 0.0, 0.0
for i in range(numElt):
    corr23 += (dataRow2[i] - mean2) * (dataRow3[i] - mean3) / (sqrt(var2*var3) * numElt)
    corr221 += (dataRow2[i] - mean2) * (dataRow21[i] - mean21) / (sqrt(var2*var21) * numElt)

# compare 2 to 3
print(corr23)

# compare 2 to 21
print(corr221)