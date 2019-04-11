# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 10:50'
__author__ = 'Lee7'
import gevent
import time


def f1(n):

    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(1)
        gevent.sleep(0.01)


def f2(n):

    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(1)
        gevent.sleep(0.01)


def f3(n):

    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(1)
        gevent.sleep(0.01)


g1 = gevent.spawn(f1, 100)
g2 = gevent.spawn(f2, 100)
g3 = gevent.spawn(f3, 1000)

g1.join()
# time.sleep(100)  # 并不会打断spawn的插入
g2.join()
g3.join()
