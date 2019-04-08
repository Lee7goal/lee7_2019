# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/8 14:39'
__author__ = 'Lee7'
from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpgid()))
    # random.random随机生成0~1的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%.2f" % (t_stop - t_start))

po = Pool(3)  # 定义一个进程池，最大进程数3
for i in range(0,10):
    # pool().apply_async(要调用的目标，(传递目标的参数元祖))
    # 每次循环将会空闲出的子进程去调用目标
    po.apply_async(worker,(i,))
print("-----start-----")
po.close()  # 关闭进程池，关闭后po不再接受
po.join()  # 等待进程池中的子进程执行完close之后新增
print("-----end-----")
