# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 14:27'
__author__ = 'lee7goal'
import urllib.request
import numpy as np

# get the data
print("get the data")

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)

# arrange data into list for labels and list of lists for attributes
print("arrange data into list for labels and list of lists for attributes")
print("-"*60)
xList = []
labels = []

for line in data:
    # split the comma
    row = line.strip().split(b',')
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type_info = [0] * 3
colCounts = []

# generate summary statistics for column 3 (e.g.)
print("-"*60)
print("generate summary statistics for column 3 (e.g.)")
col = 3
colData = []

for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)

print("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t ' + str(colsd) + "\n")

# calculate quantile boundaries
print("calculate quantile boundaries")
print("-"*60)
ntiles = 4
percentBdry = []

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, (i*100)/ntiles))

print("Boundaries for 4 Equal Percentiles ")
print(percentBdry)

# run again with 10 equal intervals
print("run again with 10 equal intervals")
print("-"*60)
ntiles = 10
percentBdry = []

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, (i*100)/ntiles))

print("Boundaries for 10 Equal Percentiles ")
print(percentBdry)

#The last column contains categorical variables
print("The last column contains categorical variables")
print("-"*60)
col = 60
colData = []
for row in xList:
    colData.append(row[col])

unique = set(colData)
print("Unique Label Values ")
print(unique)

# count up the number of elements having each value
print("count up the number of elements having each value")
print("-"*60)
catDict = dict(zip(list(unique), range(len(unique))))
catCount = [0] * 2

for elt in colData:
    catCount[catDict[elt]] += 1
print("Counts for Each Value of Categorical Label ")
print(list(unique))
print(catCount)