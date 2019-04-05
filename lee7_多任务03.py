# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/6 0006 21:48'
__author__ = 'Lee7'

import threading
import time

print("猜猜我在哪里执行1")


def saysorry():
    print("亲爱的，我错了，我再也不敢了")
    time.sleep(1)


print("猜猜我在哪里执行2")


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saysorry)
        t.start()
