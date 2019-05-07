# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/7 15:17'
__author__ = 'lee7goal'
"""使用scatter()绘制一个点"""
import matplotlib.pyplot as plt


x_values = list(range(1, 50))
y_values = [i**3 for i in x_values]
plt.scatter(x_values, y_values, c=x_values, cmap=plt.get_cmap('Blues'), edgecolors='none', s=2)
# set title label
plt.title("x2y-pic", fontsize=24)
plt.xlabel("x_value", fontsize=14)
plt.ylabel("y_value", fontsize=14)
# set tick params

# plt.axis([0, 1100, 0, 1100000000])
plt.show()
# plt.savefig('x^32y-pic.png')
