# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/6 0006 22:06'
__author__ = 'Lee7'
import threading
from time import sleep, ctime


def sing():
    """唱歌五秒钟"""
    for i in range(5):
        print("我一路向北，离开有鱼的季节")
        sleep(1)


def dance():
    """跳舞三秒钟"""
    for i in range(3):
        print("鸡你太美")
        sleep(1)


if __name__ == "__main__":
    print("-----开始-----:%s" % ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()
    while True:
        lenth = len(threading.enumerate())  # 当前程序存在的所有线程
        # print(threading.enumerate())
        print("当前运行的线程为 %d" % lenth)
        if lenth <= 1:
            break

        sleep(0.5)
