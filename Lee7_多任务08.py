# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/7 0007 16:37'
__author__ = 'Lee7'
import threading
import time


def test1(temp):
    temp.append(33)
    print("-----in test1 g_nums=%s-----" % str(g_nums))


def test2(temp):
    temp.remove(33)
    print("-----in test2 g_nums=%s-----" % str(g_nums))


g_nums = [11, 22]


def main():
    """验证多线程之间共享全局变量"""
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用函数的时候，传递什么数据过去
    a = threading.Thread(target=test1, args=(g_nums,))
    b = threading.Thread(target=test2, args=(g_nums,))

    a.start()
    time.sleep(5)
    b.start()
    time.sleep(5)

    print("-----in main Thread g_nums = %s-----" % str(g_nums))


if __name__ == "__main__":
    main()

