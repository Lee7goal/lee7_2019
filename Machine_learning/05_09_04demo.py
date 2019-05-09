# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/9 18:23'
__author__ = 'lee7goal'
import numpy as np


nd14 = np.arange(9).reshape([3, 3])
# 矩阵转置
np.transpose(nd14)
# 矩阵乘法运算
a = np.arange(12).reshape([3, 4])
b = np.arange(8).reshape([4, 2])
print(a)
print("-"*50)
print(b)
print("-"*50)
print(a.dot(b))
# 求矩阵的迹
print(a.trace())
# 计算矩阵行列式
np.linalg.det(nd14)
# 计算逆矩阵
c = np.random.random([3, 3])
print(np.linalg.solve(c, np.eye(3)))
