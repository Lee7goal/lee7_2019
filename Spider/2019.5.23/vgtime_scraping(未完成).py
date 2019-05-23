# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/23 9:12'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
import MySQLdb
import csv


# 准备开始数据库的操作
# 连接数据库
conn = MySQLdb.connect(host='localhost', user='root', passwd='lee7goal', db='scraping', charset='utf8')
cur = conn.cursor()

# 先确定link
link = 'http://www.vgtime.com/game/index.jhtml'

# 定义headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# 获取response, (status_code), 和r.text,还有确认网页的charset
print("进程开始......")
response = requests.get(url=link, headers=headers)
response.encoding= 'utf-8'
html = response.text

# 开始解析获得的html
soup = bs(html, 'lxml')
game_list = soup.find(name='ul', attrs={'class', 'game_group_list'}).find_all('li')
print("解析完成...")

# 查看需求并创建新tables
sql_create = """CREATE TABLE vg_time(
id INT NOT NULL  AUTO_INCREMENT, 
game_name VARCHAR (1000) NOT NULL ,
game_point VARCHAR (100) NOT  NULL ,
platform VARCHAR(1000) NOT NULL ,
game_language  VARCHAR (1000) NOT NULL ,
img_url VARCHAR (1000) NOT NULL , 
game_url VARCHAR (1000) NOT NULL ,
created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY(id)
)
"""
cur.execute(sql_create)
print("创建 table 完成...")

print('开始主线程资源获取...')
# 在循环外先打开csv
with open('game_info.csv', 'a+', encoding='gbk', newline='') as csv_label:
    for game in game_list:
        # 获取游戏名称
        name = game.find(name='h2').get_text().strip().replace(' ','').replace('\n\n','')
        # 获取游戏评分
        point = game.find(name='span', attrs={'class', 'game_pf user_pf'}).get_text().strip().replace(' ','').replace('\n\n','')
        # 获取游戏平台
        platform = game.find(name='span', attrs={'class', 'g_rel_l_platform'}).get_text().strip().replace(' ','').replace('\n\n','')
        # 获取游戏语言
        language = game.find(name='span', attrs={'class', 'game_lang'}).get_text().strip().replace(' ','').replace('\n\n','')
        # 获取游戏图片
        img_url = game.find(name='img').get('src')
        # 获取游戏链接
        game_url = 'http://www.vgtime.com/game' + game.find(name='a').get('href')
        # 数据库 添加操作
        cur.execute("INSERT INTO vg_time(game_name, game_point, platform,game_language,img_url,game_url) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (name, point,platform,language,img_url,game_url))
        # csv 添加导入
        line = [name, point, platform, language, img_url, game_url]
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


