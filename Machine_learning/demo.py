# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/15 14:33'
__author__ = 'lee7goal'
import csv
import numpy as np
import matplotlib.pyplot as plt

def readData():
    x = []
    y = []
    with open('Housing.csv') as f:
        rdr = csv.reader(f)
        # Skip the header row
        next(rdr)
        # Read x and y
        for line in rdr:
            xline = [1.0]
            for s in line[:-1]:
                xline.append(float(s))
            x.append(xline)
            y.append(float(line[-1]))
    return x, y


X0, y0 = readData()
# Convert all but the last 10 rows of the raw data to numpy arrays
d = len(X0)-10
X = np.array(X0[:d])
y = np.transpose(np.array([y0[:d]]))

# Compute beta
Xt = np.transpose(X)
XtX = np.dot(Xt, X)
Xty = np.dot(Xt, y)
beta = np.linalg.solve(XtX, Xty)
print(beta)

# 可视化
predictions = list()
actuals = list()
# Make predictions for the last 10 rows in the data set
for data, actual in zip(X0[d:], y0[d:]):
    x = np.array([data])
    prediction = np.dot(x, beta)
    actuals.append(actual)
    predictions.append(prediction[0, 0])
    print('prediction = '+str(prediction[0, 0])+' actual = '+str(actual))
a = [i for i in range(1, 11)]
plt.plot(a, predictions, label='预测趋势')
plt.plot(a, actuals, label='实际趋势')

plt.show()