# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/29 15:09'
__author__ = 'lee7goal'
from selenium import webdriver
import pyquery
import time
from pymongo import MongoClient

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

lianjia_post = MongoAPI("localhost", 27017,"lianjia", "house_info")
brow = webdriver.Chrome()
brow.maximize_window()
brow.get('https://cd.lianjia.com/ershoufang/rs/')
for i in range(1, 101):
    # 解析网页
    html = brow.page_source
    doc = pyquery.PyQuery(html)
    house = doc('.sellListContent li').items()

    for info  in house:
        house_data = {
            '名称': info.find('.title').text(),
            '房源简介': info.find('.houseInfo').text(),
            '地址信息': info.find('.positionInfo').text(),
            '热度信息': info.find('.followInfo').text(),
            '房源价格': info.find('.totalPrice').text(),
            '均价/M^2': info.find('.unitPrice').text(),
            '房源标签': info.find('.tag').text(),
            # '房源链接': info.find('.noresultRecommend img ').attr('href')
        }
        lianjia_post.add({
            '名称': house_data['名称'],
            '房源简介': house_data['房源简介'],
            '地址信息': house_data['地址信息'],
            '热度信息': house_data['热度信息'],
            '房源价格': house_data['房源价格'],
            '均价/M^2': house_data['均价/M^2'],
            '房源标签': house_data['房源标签']
        })

    a = "window.scrollTo(0,800);"
    b = "window.scrollTo(0,1600);"
    c = "window.scrollTo(0,3200);"

    brow.execute_script(a)
    time.sleep(2)

    brow.execute_script(b)
    time.sleep(3)

    brow.execute_script(c)
    time.sleep(2)
    print("数据保存完成，正在跳转下一页")
    next_page_link = brow.find_element_by_link_text('下一页')

    if i < 100:
        next_page_link.click()
    else:
        pass

print("数据已经全部保存，现在退出浏览器")
brow.close()

