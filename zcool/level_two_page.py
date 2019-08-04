# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/8/3 0003 23:54'
__author__ = 'Lee7'
import pymongo
import requests
import time
from bs4 import BeautifulSoup as bs

client = pymongo.MongoClient('localhost',27017)
zcool = client['zcool摄影大全']
class_url = zcool['类别网页url']
album_info = zcool['专辑网页url']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


album_dic = dict()
for class_info in class_url.find():
    album_dic[class_info['类别']] = class_info['页面链接']

num = 0

for name,url in album_dic.items():
    if name == '全部 ':
        continue
    else:
        for page_num in range(1,101):
            res = requests.get(url=url + str(page_num), headers=headers)
            soup = bs(res.text, 'lxml')
            card_list = soup.select('div.work-list-box > div > div.card-info > p > a')
            for card in card_list:
                card_name = card.get('title')
                card_url = card.get('href')
                card_info = {
                    '专辑名称':card_name,
                    '专辑地址':card_url
                }
                album_info.insert_one(card_info)
                num += 1
                print("已完成 %d 次" % num)
                # time.sleep(1)
