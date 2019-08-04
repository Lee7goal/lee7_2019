# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/8/4 0004 11:16'
__author__ = 'Lee7'
import pymongo
import requests
from bs4 import BeautifulSoup as bs
import os

client = pymongo.MongoClient('localhost', 27017)
zcool = client['zcool摄影大全']
album_info = zcool['专辑网页url']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

for album in album_info.find():
    album_name = album['专辑名称']
    album_link = album['专辑地址']

    try:
        if 'event' in album_link:
            continue
        else:
            path = "D:\\zcool摄影\\" + str(album_name) + "\\"
            os.makedirs(path)
            res = requests.get(url=album_link, headers=headers)
            soup = bs(res.text, 'lxml')
            img_list = soup.select('div.work-show-box > div > img')
            num = 0
            for img in img_list:
                img_url = img.get('src').replace('@1280w_1l_0o_100sh.jpg','')               # 还没想好有什么较好的解决方式不是原图就不是原图吧
                img_data = requests.get(img_url).content
                num += 1
                with open(path + str(num) + '.jpg','wb') as f:
                    f.write(img_data)
    except Exception as err:
        print(err)
        continue


