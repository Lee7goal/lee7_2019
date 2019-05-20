# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/15 10:56'
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
corMat = DataFrame(rocksVMines.corr())

# visualize correlations using heatmap
plt.pcolor(corMat)
plt.show()
