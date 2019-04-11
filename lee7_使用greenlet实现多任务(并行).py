# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 10:12'
__author__ = 'Lee7'

from greenlet import greenlet
import time


def demo1():
    while True:
        print("-----1-----")
        gr2.switch()
        time.sleep(1)


def demo2():
    while True:
        print("-----2-----")
        gr1.switch()
        time.sleep(1)


gr1 = greenlet(demo1)
gr2 = greenlet(demo2)

gr1.switch()
