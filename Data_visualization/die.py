# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/8 9:03'
__author__ = 'lee7goal'
from random import randint


class Die:
    """is a Die class"""
    def __init__(self, num_sides=6):
        """Die is normal six"""
        self.num_sides = num_sides

    def roll(self):
        """return a 1 to num_sides int"""
        return randint(1, self.num_sides)
