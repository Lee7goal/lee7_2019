# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/7 0007 17:13'
__author__ = 'Lee7'
"""
同步就是协同步调
互斥锁---当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制
能够保证当我运行时，共享数据你动不了
mutex = threading.Lock()  # 创建锁
mutex.acquire()  # 锁定
mutex.release()  # 释放
"""

import threading
import time


# 定义一个全局变量
g_num = 0
lenth = len(threading.enumerate())


def test1(num):
    global g_num
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前，已经被上锁，那么此时会堵塞，知道锁被解开
    mutex.acquire()
    for i in range(num):
        g_num += 1
        # time.sleep(1)
    mutex.release()  # 解锁
    print("-----in test1 g_num=%d-----" % g_num)
    # print("当前线程数量为 %d " % lenth)


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
        # time.sleep(1)
    mutex.release()  # 解锁
    print("-----in test2 g_num=%d-----" % g_num)
    # print("当前线程数量为 %d " % lenth)


mutex = threading.Lock()  # 创建一个互斥锁，默认没有上锁


def main():
    a = threading.Thread(target=test1, args=(1000000,))
    b = threading.Thread(target=test2, args=(1000000,))

    a.start()
    b.start()

    time.sleep(1)
    print("-----in main Thread g_num = %d-----" % g_num)


if __name__ == "__main__":
    main()

