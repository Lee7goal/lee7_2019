# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/7 0007 12:29'
__author__ = 'Lee7'

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        self.register()
        self.login()

    @staticmethod
    def login():

        for j in range(5):
            print("登陆中...")

    @staticmethod
    def register():
        print("开始注册")


if __name__ == "__main__":
    t = MyThread()

    t.start()
    for i in range(5):
        lenth = len(threading.enumerate())
        print("现在的进程数量为 %d" % lenth)
        time.sleep(1)


