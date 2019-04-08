# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/8 12:09'
__author__ = 'Lee7'
import threading
import time
import multiprocessing
import os
def dl_from_web(q):
    """下载数据"""
    data = [11,22,33,44,55]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)
    print("----下载器已经下载完成并存入队列----")
def analysis_data(q):
    """数据处理"""
    # 从队列中获取数据
    waitting_analysis_data = list()
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():
            break
    # 模拟数据处理
    print(waitting_analysis_data)
def main():
    """Queue队列先进先出，栈先进后出"""
    # 1.创建一个队列
    q = multiprocessing.Queue(5)

    # 2.创建多个进程，将队列的引用当作实参传递
    p1 = multiprocessing.Process(target=dl_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))

    p1.start()
    p2.start()
if __name__ == "__main__":
    main()