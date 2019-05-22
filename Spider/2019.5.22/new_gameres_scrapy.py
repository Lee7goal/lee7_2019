# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/22 17:37'
__author__ = 'lee7goal'
import MySQLdb
import requests
from bs4 import BeautifulSoup as bs

# 连接数据库
conn = MySQLdb.connect(host='localhost', user='root', passwd='lee7goal', db='scraping', charset='utf8')
cur = conn.cursor()

# 选取link
link = 'https://www.gameres.com'

# 设置headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

# 开始你的BS4操作
response = requests.get(link, headers=headers)
soup = bs(response.text, 'lxml')
title_list = soup.find_all(name='article', attrs={'class', 'feed-item'})

# 先在循环外部把表建了 妈的 又把自己坑了一次
cur.execute("CREATE TABLE new_urls(id int not null AUTO_INCREMENT,url varchar(1000) not null,title varchar(4000) not null,content VARCHAR (10000) not NULL ,created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY(id))")

for all_ele in title_list:
    name = all_ele.find('h3').get_text().strip().replace(' ','').replace('\n\n        ','')
    url = 'https://www.gameres.com' + all_ele.find('a').get('href')
    content = all_ele.find('p').get_text().strip().replace(' ','').replace('\n\n        ','')
    # 数据库 添加操作
    cur.execute("INSERT INTO new_urls(url, title, content) VALUES('%s', '%s', '%s')" % (url, name, content))

# 最后记得关闭数据库连接
cur.close()
conn.commit()
conn.close()