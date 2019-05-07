# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/7 17:33'
__author__ = 'lee7goal'
from random import choice


class RandomWalk:
    """a class to create random walk data"""

    def __init__(self, num_points=5000):
        """initialization random walk attributes"""
        self.num_points = num_points
        """the all ran-walk is start with(0,0)"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """count all of the ran-walk points"""
        # ran-walk while length is formulate
        while len(self.x_values) < self.num_points:
            # choice the path and distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3,  4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # never situ ran-walk
            if x_step == 0 and y_step == 0:
                continue
            # count next points(x,y)
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
