# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 17:21'
__author__ = 'lee7goal'
from multiprocessing import Process,Queue
import time
import requests

link_list = []
with open('alexa.txt', 'r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link_1st = eachone.split('\t')[1]
        link = link_1st.replace('\n', ' ')
        link_list.append(link)

start = time.time()
class MyProcess(Process):
    def __init__(self, q):
        Process.__init__(self)
        self.q = q

    def run(self):
        print("starting ", self.pid)
        while not self.q.empty():
            crawler(self.q)
        print("exiting ", self.pid)

def crawler(q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url, timeout=20)
        print(q.qsize(), r.status_code, url)
    except Exception as e:
        print(q.qsize(), url, "Error: ",e)

if __name__ == '__main__':
    ProcessName = ["Process----1", "Process----2", "Process----3", "Process----4", "Process----5", "Process----6", ]
    workQueue = Queue(1000)

    # 填充队列
    for url in link_list:
        workQueue.put(url.strip())

    for i in range(0,6):
        p = MyProcess(workQueue)
        p.daemon = True
        p.start()
        p.join()

    end = time.time()
    print("Process & Queue 多进程总共花费时间： %f" % (end - start))
    print("Ending....")
