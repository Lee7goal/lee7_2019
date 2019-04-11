# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 11:50'
__author__ = 'Lee7'
from gevent import monkey
import gevent
import random
import time

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码转换为gevent中自己实现的模块


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


gevent.joinall([
    gevent.spawn(coroutine_work, "work1"),
    gevent.spawn(coroutine_work, "work2")
])
