# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 11:56'
__author__ = 'Lee7'
import gevent
import time
from gevent import monkey

monkey.patch_all()


def f1(n):

    for i in range(n):
        print("我是任务【1】", i)
        time.sleep(0.01)


def f2(n):

    for i in range(n):
        print("我是任务【2】", i)
        time.sleep(0.01)


def f3(n):

    for i in range(n):
        print("我是任务【3】", i)
        time.sleep(0.01)


# gevent.spawn 设置产卵，函数，参数
g1 = gevent.spawn(f1, 100)
g2 = gevent.spawn(f2, 100)
g3 = gevent.spawn(f3, 1000)

# g1.join()
# time.sleep(100)  # 并不会打断spawn的插入
# g2.join()
# g3.join()

gevent.joinall([
    g1, g2, g3
])
