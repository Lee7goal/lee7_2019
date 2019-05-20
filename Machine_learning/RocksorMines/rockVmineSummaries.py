# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 13:28'
__author__ = 'lee7goal'
"""采集数据"""
import urllib.request


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)
# content = data.read().decode('utf-8', 'ignore')
#
# with open('sonar.all-data', 'w') as get_data:
#     get_data.write(content)

xList = []
labels = []

for line in data:
    # split the comma
    row = line.strip().split(b",")
    xList.append(row)

print("Number of Rows of Data = " + str(len(xList)))
print("Number of Columns of Data = " + str(len(xList[1])))


