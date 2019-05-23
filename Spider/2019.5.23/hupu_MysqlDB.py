# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 13:56'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs
import csv
import MySQLdb
"""
整体思路
1.先试着获取数据  : 完成
2.检查数据没有问题了再导库
3.然后导csv文件
4.写一个新文件进行关键词统计
"""

# 连接数据库
conn = MySQLdb.connect(host='localhost', user='root', passwd='lee7goal', db='scraping', charset='utf8')
cur = conn.cursor()

# 确定link
link = 'https://bbs.hupu.com/bxj'
# 定义headers以及数据获取
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
print("进程开始...")
response = requests.get(link, headers=headers)
response.encoding='utf-8'

# 查看需求并创建新tables
sql_create = """CREATE TABLE hupu_info(
id INT NOT NULL  AUTO_INCREMENT, 
title VARCHAR (1000) NOT NULL ,
author VARCHAR (100) NOT  NULL ,
crea_date VARCHAR(1000) NOT NULL ,
rep_bro  VARCHAR (1000) NOT NULL ,
last_user VARCHAR (1000) NOT NULL , 
created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(id)
)
"""
cur.execute(sql_create)
print("创建 table 完成...")

print('开始主线程资源获取...')
# print(html) 已经确认可以收到信息
soup = bs(response.text, 'lxml')
all_post = soup.find(name='ul', attrs={'class', 'for-list'}).find_all('li')
# 在循环外先打开csv
with open('hupu_topic.csv', 'a+', encoding='gbk', newline='') as csv_label:
    for info in all_post:
        # 帖子主题
        title  = info.find(name='a', attrs={'class', 'truetit'}).get_text().strip().replace(' ','')
        # 作者
        author = info.find(name='a', attrs={'class', 'aulink'}).get_text().strip().replace(' ','')
        # 创建主题日期
        crea_date = info.find(name='div', attrs={'class', 'author box'}).get_text().strip().replace(' ','').replace('\n\n', '').replace(author, '')
        # 回复浏览数量
        rep_bro = info.find(name='span', attrs={'class', 'ansour box'}).get_text().strip().replace(' ','').replace(u'\xa0', '')
        # 最后回复人
        last_user = info.find(name='span', attrs={'class', 'endauthor'}).get_text().strip().replace(' ','')
        # 最后回复日期
        # last_date = None
        # 数据库 添加操作
        cur.execute(
            "INSERT INTO hupu_info(title, author, crea_date,rep_bro,last_user) VALUES('%s', '%s', '%s', '%s', '%s')" %
            (title, author, crea_date, rep_bro, last_user))
        # csv 添加导入
        line = [title, author, crea_date, rep_bro, last_user]
        w = csv.writer(csv_label)
        w.writerow(line)
        del line
        print('一次主线程完成...')
print('任务完成')
# 最后记得关闭数据库
print('关闭数据库中...')
cur.close()
conn.commit()
conn.close()