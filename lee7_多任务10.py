# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/7 0007 18:24'
__author__ = 'Lee7'


import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()


class MyThread1(threading.Thread):
    def run(self):
        # 对mutex上锁
        mutexA.acquire()

        # 对上锁后，延时1秒，等待另外哪个线程，把B上锁
        print(self.name+'-----do1-----up-----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name+'-----do1-----down-----')
        mutexB.release()

        # 对A解锁
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexB上锁
        mutexB.acquire()

        # 对上锁后，延时1秒，等待另外哪个线程，把A上锁
        print(self.name + '-----do1-----up-----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexA已经被另外的线程抢先上锁了
        mutexA.acquire()
        print(self.name + '-----do1-----down-----')
        mutexA.release()

        # 对B解锁
        mutexB.release()


if __name__ == "__main__":
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()

"""
避免死锁的方式：
1.程序设计师要尽量避免
2.添加超时时间
"""