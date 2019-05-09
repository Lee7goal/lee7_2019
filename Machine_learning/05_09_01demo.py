# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/9 16:14'
__author__ = 'lee7goal'
import numpy as np


# create a 3X3 matrix that all number is 0  生成全是0的 3X3矩阵
nd1 = np.zeros([3, 3])

# create a 3x3 matrix that all number is 1 生成全是1的3X3矩阵
nd2 = np.ones([3, 3])

# create a 3x3 matrix 生成3阶的单位矩阵
nd3 = np.eye(3)

# create a 3x3 matrix diag 生成3阶的对角矩阵
nd4 = np.diag([1, 2, 3])

# show all matrix
print(nd1, '\r\n', nd2, '\r\n', nd3, '\r\n', nd4)
np.savetxt(X=nd4, fname='./test2.txt')
nd5 = np.loadtxt('./test2.txt')
print(nd5)