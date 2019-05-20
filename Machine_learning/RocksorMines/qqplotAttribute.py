# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 15:29'
__author__ = 'lee7goal'
import urllib.request
import pylab
import scipy.stats as stats


# get the data
print("get the data")

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar"
              ".all-data")

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


stats.probplot(colData, dist='norm', plot=pylab)
pylab.show()
