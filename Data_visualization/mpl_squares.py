# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/7 13:58'
__author__ = 'lee7goal'
import matplotlib.pyplot as plt

"""绘制简单的折线图"""
squares = [i**2 for i in range(11) if i <= 10]
input_value = [i for i in range(11) if i <= 10]
plt.plot(input_value, squares, linewidth=5)
# set the pic_tittle and the label
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
# set the tick_params size
plt.tick_params(axis='both', width=2, colors='blue', labelsize=14)
plt.show()
