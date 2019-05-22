# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/22 17:05'
__author__ = 'lee7goal'
import MySQLdb
import requests
from bs4 import BeautifulSoup as bs

# 连接数据库
conn = MySQLdb.connect(host='localhost', user='root', passwd='lee7goal', db='scraping', charset='utf8')
cur = conn.cursor()
# 选取link
link = 'https://www.gameres.com/'
# 设置headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
# 常规BS4操作
response = requests.get(link, headers=headers)
soup = bs(response.text, 'lxml')
title_list = soup.find_all(name='article', attrs={'class', 'feed-item'})
for title in title_list:
    name = title.find('h3').get_text().strip().replace(' ','').replace('\n\n        ','')
    url = 'https://www.gameres.com' + title.find('a').get('href')
    # 数据库 添加操作 这个百分号坑死我了
    cur.execute("INSERT INTO urls(url, content) VALUES('%s', '%s')" % (url, name))
# 最后记得关闭数据库连接
cur.close()
conn.commit()
conn.close()