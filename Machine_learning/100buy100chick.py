# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/13 10:58'
__author__ = 'lee7goal'

money = 100
x_value = 5  # 公鸡的价钱
y_value = 3  # 母鸡的价钱
z_value = 1/3  # 小鸡的价钱

for x in range(21):
    for y in range(34):
        z = (money - x_value * x - y_value * y) / z_value
        if x + y + z == 100:
            print("公鸡买%d只,母鸡买%d只,小鸡买%d只" % (x, y, z))
