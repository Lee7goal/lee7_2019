# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/16 12:11'
__author__ = 'lee7goal'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
# read abalone data
abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height',
                   'Whole weight', 'Shucked weight',
                   'Viscera weight', 'Shell weight', 'Rings']
# calculate correlation matrix
corMat = DataFrame(abalone.iloc[:, 1:9].corr())
# print correlation matrix
print(corMat)
# visualize correlations using heatmap
plt.pcolor(corMat)
plt.show()
