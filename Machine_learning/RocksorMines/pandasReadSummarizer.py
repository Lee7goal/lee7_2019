# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 15:40'
__author__ = 'lee7goal'
import pandas as pd


# get the data
print("get the data")

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

# print the head and tail of the data frame
print(rocksVMines.head())
print(rocksVMines.tail())

# print the summary of data frame
summary = rocksVMines.describe()
print(summary)
