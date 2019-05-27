# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/27 13:09'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
from pymongo import MongoClient
import time


class MongoAPI():
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = MongoClient(host=self.db_ip, port=self.db_port)
        self.db =  self.conn[self.db_name]
        self.table = self.db[self.table_name]

    def get_one(self,query):
        return self.table.find_one(query, projection={"_id": False})

    def get_all(self, query):
        return self.table.find(query)

    def add(self, kv_dict):
        return self.table.insert(kv_dict)

    def delete(self, query):
        return self.table.delete_many(query)

    def check_exist(self,query):
        ret = self.table.find_one(query)
        return ret is not None
    # 如果没有会新建
    def update(self, query, kv_dict):
        self.table.update_one(query, {
            '$set': kv_dict
        }, upsert=True)

def get_one_page(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    try:
        res = requests.get(link, headers=headers)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            soup = bs(res.text, 'lxml')
            return soup
        else:
            return res.status_code + 'Error'
    except:
        return None

def parse_page(job_list):

    get_job_list = []

    for job in job_list:
        # 工作区域
        # 职位名称
        job_name = job.find(name='h3').get_text().strip().replace(' ','')
        # 工作地点
        job_local = job.find(name='span', attrs={'class', 'add'}).get_text().strip().replace(' ','')
        # 发布时间
        job_time = job.find(name='span', attrs={'class', 'format-time'}).get_text().strip().replace(' ','')
        # 薪资
        job_money = job.find(name='span', attrs={'class', 'money'}).get_text().strip().replace(' ','')
        # 职业要求
        job_need = job.find(name='div', attrs={'class', 'li_b_l'}).get_text().strip().replace(' ','').replace('\n', '').replace(job_money, '')
        # 公司简介(因为是始终解决不了工作标签的问题i于是我就直接replace了content)
        com_content = job.find(name='div', attrs={'class', 'li_b_r'}).get_text().strip().replace(' ','')
        # 工作标签
        job_labels = job.find(name='div', attrs={'class', 'list_item_bot'}).get_text().replace('\n', ' ').replace(com_content, '')
        # 公司区域
        # 公司名称
        com_name = job.find(name='div', attrs={'class', 'company_name'}).get_text().strip().replace(' ','')
        # 公司介绍
        com_des = job.find(name='div', attrs={'class', 'industry'}).get_text().strip().replace(' ','').replace('\n\n', '')
        # 公司logo url
        com_logo_url = job.find(name='img').get('src')
        get_job_list.append([job_name, job_local, job_time, job_money, job_need, job_labels, com_name, com_des, com_content, com_logo_url])
    return get_job_list

lagou_job_list = MongoAPI('localhost', 27017, 'lagou', 'job')
# 多爬取几页的信息
for i in range(1,31):
    # 确定link
    link = 'https://www.lagou.com/zhaopin/youxicehua/2/?filterOption=' + str(i)
    # 解析
    soup = get_one_page(link)
    # 先找块
    job_list = soup.find_all(name='li', attrs={'class', 'con_list_item default_list'})
    # 在块里把所需内容获取到
    data_list = parse_page(job_list)
    for each in data_list:
        lagou_job_list.add({
            "工作名称": each[0],
            "工作地点": each[1],
            "发布时间": each[2],
            "薪资": each[3],
            "工作要求": each[4],
            "工作标签": each[5],
            "公司名称": each[6],
            "公司简介": each[7],
            "公司福利": each[8]
        })
    time.sleep(3)
    print("第 %d 页获取完成，休息三秒后进行下一页" % i)