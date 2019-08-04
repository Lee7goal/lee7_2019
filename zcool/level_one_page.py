# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/8/3 0003 23:41'
__author__ = 'Lee7'
import requests
from bs4 import BeautifulSoup as bs
import pymongo

client = pymongo.MongoClient('localhost',27017)
zcool = client['zcool摄影大全']
class_url = zcool['类别网页url']

link = 'https://www.zcool.com.cn/discover/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

html = requests.get(link)
soup = bs(html.text, 'lxml')
links = soup.select('ul.classify-select-list > li > div > a')

for link in links:
    page_url = link.get('href')[:-1]
    print(page_url)
    link_name = link.get_text()
    class_data = {
        '类别':link_name,
        '页面链接':page_url
    }
    class_url.insert_one(class_data)