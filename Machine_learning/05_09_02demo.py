# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/9 16:29'
__author__ = 'lee7goal'
import numpy as np

np.random.seed(2018)
nd11 = np.random.random([10])

# 获取指定位置的数据 获取第四个元素
print('-'*30)
print(nd11[3])

# 截取一段距离
print('-'*30)
print(nd11[3:6])

# 截取固定间隔的距离
print('-'*30)
print(nd11[1:6:2])

# 截取倒序取数
print('-'*30)
print(nd11[::-1])

# 截取一个多维数组的一个区域内的数据
print('-'*30)
nd12 = np.arange(25).reshape([5, 5])
print(nd12)
print(nd12[1:3, 1:3])

# 截取一个多维数组中，数值在一个值域之内的数据
print('-'*30)
print(nd12[(nd12 > 3) & (nd12 <10)])

# 截取多维数组中，指定的行，如读取数据2，3行
print('-'*30)
print(nd12[[1,2]])  # 或nd12[1:3,:]

# 截取多维数组，指定的列,如2，3列
print('-'*30)
print(nd12[:, 1:3])
