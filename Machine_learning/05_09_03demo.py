# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/9 18:01'
__author__ = 'lee7goal'
import numpy as np
from numpy import random as nr


a = np.arange(1, 10, dtype=int)
c1 = nr.choice(a, size=(2, 2))  # size指定输出数组形状
c2 = nr.choice(a, size=(2, 2), replace=False)  # replace缺省为Ture，即可重复抽取

# 下式中参数p指定每个元素对应的抽取概率，默认为每个元素被抽取的概率相同
c3 = nr.choice(a, size=(2, 2), p=a / np.sum(a))
print("随机可重复抽取")
print(c1)
print("-"*50)
print("随机但不重复抽取")
print(c2)
print("-"*50)
print("随机但按照制度概率抽取:")
print(c3)
print("-"*50)
