# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/7 0007 16:22'
__author__ = 'Lee7'
import threading
import time


# 定义一个全局变量
g_num = 100
lenth = len(threading.enumerate())


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
        # time.sleep(1)
        print("-----in test1 g_num=%d-----" % g_num)
    # print("当前线程数量为 %d " % lenth)


def test2(num):
    # global g_num
    # for i in range(num):
    #     g_num += 1
    #     time.sleep(1)
    print("-----in test2 g_num=%d-----" % g_num)
    # print("当前线程数量为 %d " % lenth)


def main():
    a = threading.Thread(target=test1, args=(5,))
    b = threading.Thread(target=test2, args=(5,))

    a.start()
    time.sleep(5)
    print("当前线程数量为 %d " % lenth)
    b.start()
    time.sleep(5)
    print("当前线程数量为 %d " % lenth)
    # time.sleep(5)
    print("-----in main Thread g_num = %d-----" % g_num)
    print("当前线程数量为 %d " % lenth)


if __name__ == "__main__":
    main()
