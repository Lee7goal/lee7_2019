# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 16:57'
__author__ = 'lee7goal'
import time
import threading
import requests
import queue as Queue

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
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    def run(self):
        print("starting " + self.name)
        while True:
            try:
                crawler(self.name, self.q)
            except:
                break
        print("Exiting " + self.name)

def crawler(threadName, q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=20)
        print(q.qsize(), threadName, r.status_code, url)
    except Exception as e:
        print(q.qsize(), threadName, url, 'Error:', e)

thread_list = ["Thread---1", "Thread---2", "Thread---3", "Thread---4", "Thread---5"]
workQueue = Queue.Queue(1000)
threads = []
# 创建新线程
for tName in thread_list:
    thread = MyThread(tName, workQueue)
    thread.start()
    threads.append(thread)

# 填充队列
for url in link_list:
    workQueue.put(url.strip())

# 等待所有线程完成
for t in threads:
    t.join()

end = time.time()
print('简单的多线程爬虫总共花了 %f 秒时间' % (end - start))
