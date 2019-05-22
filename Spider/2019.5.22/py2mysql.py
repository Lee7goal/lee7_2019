# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/22 15:39'
__author__ = 'lee7goal'
import MySQLdb


conn = MySQLdb.connect(host='localhost', user='root', passwd='lee7goal', db='scraping')
cur = conn.cursor()
cur.execute("INSERT INTO urls(url, content) VALUES('www.baidu.com', 'This is content.')")
cur.close()
conn.commit()
conn.close()