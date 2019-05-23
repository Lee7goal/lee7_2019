# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 15:56'
__author__ = 'lee7goal'
import threading
import time

# 为线程定义一个函数
class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print("starting " + self.name)
        print_time(self.name, self.delay)
        print("Exiting " + self.name)

def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        print(threadName, time.ctime())
        count += 1

threads = []
# 创建线程
thread1 = MyThread("Thread-1", 1)
thread2 = MyThread("Thread-2", 2)
# 开始线程
thread1.start()
thread2.start()
# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
# 等待所有线程完成
for t in threads:
    t.join()

print("Exist main Thread")
