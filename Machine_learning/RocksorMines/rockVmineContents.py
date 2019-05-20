# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 13:53'
__author__ = 'lee7goal'
import urllib.request
import sys
# file_name = 'sonar.all-data'
# with open(file_name) as f:
#     data = f.read()

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)

xList = []
labels = []
for line in data:
    # split on comma
    row = line.strip().split(b',')
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])


type_info = [0] * 3
colcounts = []

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type_info[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type_info[1] += 1
            else:
                type_info[2] += 1

    colcounts.append(type_info)
    type_info = [0] * 3

print("Col\tNumber\tStrings\tOther\n")
icol = 0
for types in colcounts:
    print("{}\t\t{}\t\t{}\t\t{}\n".format(str(icol), str(types[0]), str(types[1]), str(types[2])))
    icol += 1
