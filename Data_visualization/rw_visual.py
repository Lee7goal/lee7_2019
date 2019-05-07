# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/7 17:48'
__author__ = 'lee7goal'
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # create a Instance to draw points
    rw = RandomWalk(50000)
    rw.fill_walk()
    # set the pic size
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.get_cmap('Blues'), edgecolors='none', s=15)
    # point the start point and end point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make more walk? (y/n)\r\n:")
    if keep_running == "n":
        break

