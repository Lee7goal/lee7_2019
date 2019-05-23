# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 16:21'
__author__ = 'lee7goal'
import threading
import requests
import time

link_list = []
with open('alexa.txt', 'r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link_1st = eachone.split('\t')[1]
        link = link_1st.replace('\n', ' ')
        link_list.append(link)

start = time.time()
# 为线程定义一个函数
class MyThread(threading.Thread):
    def __init__(self, name, link_range):
        threading.Thread.__init__(self)
        self.name = name
        self.link_range = link_range
    def run(self):
        print("starting " + self.name)
        crawler(self.name, self.link_range)
        print("Exiting " + self.name)

def crawler(threadName, link_range):
    for i in range(link_range[0], link_range[1] + 1):
        try:
            r = requests.get(link_list[i].strip(), timeout=20)
            print(threadName, r.status_code, link_list[i])
        except Exception as e:
            print(threadName, "Error: ", e)

thread_list = []
link_range_list = [(0, 200), (201, 400), (401, 600), (601, 800), (801, 1000)]

# 创建进程
for i in range(1,6):
    thread = MyThread("Thread--" + str(i), link_range_list[i-1])
    thread.start()
    thread_list.append(thread)

# 等待所有进程完成
for thread in thread_list:
    thread.join()

end = time.time()
print('简单的多线程爬虫总共花了 %f 秒时间' % (end - start))