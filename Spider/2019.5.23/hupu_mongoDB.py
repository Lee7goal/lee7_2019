# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 10:29'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs
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

def get_page(link):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    r = requests.get(url=link, headers=headers)
    html = r.content
    html = html.decode('utf-8')
    soup = bs(html, 'lxml')
    return soup

def get_data(post_list):
    data_list = []
    for post in post_list:
        # 帖子主题
        title = post.find(name='a', attrs={'class', 'truetit'}).get_text().strip().replace(' ', '')
        # 作者
        author = post.find(name='a', attrs={'class', 'aulink'}).get_text().strip().replace(' ', '')
        # 创建主题日期
        crea_date = post.find(name='div', attrs={'class', 'author box'}).get_text().strip().replace(' ', '').replace(
            '\n\n', '').replace(author, '')
        # 回复浏览数量
        rep_bro = post.find(name='span', attrs={'class', 'ansour box'}).get_text().strip().replace(' ', '').replace(
            u'\xa0', '')
        # 最后回复人
        last_user = post.find(name='span', attrs={'class', 'endauthor'}).get_text().strip().replace(' ', '')

        data_list.append([title, author, crea_date, rep_bro, last_user])
    return data_list


hupu_post = MongoAPI("localhost", 27017,"hupu", "post")
for i in range(1, 101):
    link = 'https://bbs.hupu.com/bxj-' + str(i)
    soup = get_page(link)
    post_list = soup.find(name='ul', attrs={'class', 'for-list'}).find_all('li')
    data_list = get_data(post_list)
    for each in data_list:
        hupu_post.add({
            "title": each[0],
            "author": each[1],
            "crea_date": each[2],
            "rep_bro": each[3],
            "last_user": each[4]
        })
    time.sleep(3)
    print("第 %d 页获取完成，休息三秒后进行下一页" % i)


