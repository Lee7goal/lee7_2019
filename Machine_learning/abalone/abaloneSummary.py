# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/15 11:00'
__author__ = 'lee7goal'
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt


# get the data
target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

# read the data of abalone and set the data first line
abalone = pd.read_csv(target_url, header=None, prefix="V")
# ['性'，'长度'，'直径'，'身高'，'整体重量'，'去壳重量'，'内脏重量'，'壳重量'，'戒指']
abalone.columns = [
    'Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings'
]

print(abalone.head())
print(abalone.tail())

# print summary of data frame
summary = abalone.describe()
print(summary)

# box plot the real-valued attributes
# convert to array for plot routine
array = abalone.iloc[:, 1:9].values
boxplot(array)
plt.xlabel("Attribute Index")
plt.ylabel("Quartile Ranges")
show()


# the last column (rings) is out of scale with the rest
#  - remove and replot
array2 = abalone.iloc[:, 1:8].values
boxplot(array2)
plt.xlabel("Attribute Index")
plt.ylabel("Quartile Ranges")
show()


# removing is okay but renormalizing the variables generalizes better.
# renormalize columns to zero mean and unit standard deviation
# this is a common normalization and desirable for other operations
#  (like k-means clustering or k-nearest neighbors
abaloneNormalized = abalone.iloc[:, 1:9]
for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    abaloneNormalized.iloc[:, i:(i + 1)] = (
                                                  abaloneNormalized.iloc[:, i:(i + 1)] - mean) / sd


array3 = abaloneNormalized.values
boxplot(array3)
plt.xlabel("Attribute Index")
plt.ylabel("Quartile Ranges - Normalized ")
print(abalone)
show()
