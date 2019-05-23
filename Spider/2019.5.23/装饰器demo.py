# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 17:15'
__author__ = 'lee7goal'
from threading import Thread

#多线程异步方法执行封装
def demo(func):
    def wrapper(*args, **kwargs):
        thr = Thread(target = func, args = args, kwargs = kwargs)
        thr.start()
    return wrapper
@demo
def get_data(num):
    print("--------线程开始--------------")
    for x in range(num):
        pass
for x in range(1000000):
    get_data(1000000)