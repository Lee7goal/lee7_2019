# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/24 15:22'
__author__ = 'lee7goal'
import requests
import time
from pymongo import MongoClient
from bs4 import BeautifulSoup as bs

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
    r = requests.get(link, headers=headers)
    html = r.text
    # html = html.decode('utf-8')
    soup = bs(html, 'lxml')

    return soup


def parse_one_page(post_list):
    data_list = []
    for post in post_list:
        try:
            # 获取排名
            num = post.find(name='span', attrs={'class', 'n'}).get_text().strip().replace(' ','')
            # 获取游戏名称
            name = post.find(name='a', attrs={'class', 'name'}).get_text().strip().replace(' ','')
            # 获取游戏标签
            label = post.find(name='td', attrs={'class', 'type'}).get_text().strip().replace(' ','')
            # 获取游戏状态
            stage = post.find(name='span', attrs={'class', 'p'}).get_text().strip().replace(' ','')
            #  获取游戏热度
            hot_point = post.find(name='td', attrs={'class', 'hottr hot'}).get_text().strip().replace(' ','')
            # 传递到data_list
            data_list.append([num, name, label, stage, hot_point])
        except AttributeError:
            continue
    # return
    return data_list

# jiuyou_post = MongoAPI("localhost", 27017, "9you", "leader_board")
with open('leaderBoard.txt', 'w') as f:
    for i in range(1, 6):
        link = 'http://www.9game.cn/xyrb/' + str(i) + '_0/'
        soup = get_one_page(link)
        post_list = soup.find(name='div', attrs={'class', 'box-text'}).find_all('tr')
        data_list = parse_one_page(post_list)
        for each in data_list:
            f.write(each[0])
            f.write(" ")
            f.write(each[1])
            f.write(" ")
            f.write(each[2])
            f.write(" ")
            f.write(each[3])
            f.write(" ")
            f.write(each[4])
            f.write("\r\n")
        #     jiuyou_post.add({
        #         "排名": each[0],
        #         "名称": each[1],
        #         "类型": each[2],
        #         "阶段": each[3],
        #         "热度": each[4]
        #     })
        time.sleep(2)
        print("第 %d 页获取完成，休息两秒后进行下一页" % i)
