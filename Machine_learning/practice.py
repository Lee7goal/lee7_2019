# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/17 17:06'
__author__ = 'lee7goal'
import urllib.request
import numpy as np

# get the data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = urllib.request.urlopen(url)

xList = list()
labels = list()

for line in data:
    # split the comma
    row = line.strip().split(b',')
    xList.append(row)
nrow = len(xList)
ncol = len(xList[0])

count_type = [0] * 3
col_counts = []

# generate summary statistics for column 3 (e.g.)
col = 3
colData = []

for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)

print("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t ' + str(colsd) + "\n")

ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i * 100 / ntiles))

print("\nBoundaries for 4 Equal Percentiles \n")
print(percentBdry)

# run again with 10 equal intervals
ntiles = 10
percentBdry = []

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i * 100 / ntiles))

print("\nBoundaries for 10 Equal Percentiles \n")
print(percentBdry)

# The last column contains categorical variables
col = 60
colData = []

for row in xList:
    colData.append(str(row[col]))

unique = set(colArray)
print("Unique Label Values \n")
print(unique)

# count up the number of elements having each value
catDict = dict(zip(list(unique), range(len(unique))))
catCount = [0]*2
for elt in colData:
    catCount[catDict[elt]] += 1
print("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)


