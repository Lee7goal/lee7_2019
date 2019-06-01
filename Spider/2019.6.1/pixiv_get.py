# coding=utf-8
# Version:3.7.3
# Tools:Pycharm
__date__ = ' 2019/6/1 11:24'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs
import json

def get_page(link):
    # 定义头部
    headers = {
        'Referer': 'https://www.google.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    res = requests.get(url=link, headers=headers)
    res.encoding = 'utf-8'
    html = res.text
    return html

def parse_page(html):
    soup = bs(html, 'lxml')
    movie_list = soup.find(name='ol', attrs={'class', 'grid_view'}).find_all('li')
    for movie in movie_list:
        num = movie.find(name='div', attrs={'class', 'pic'}).get_text().replace('\n','')
        name = movie.find(name='span', attrs={'class', 'title'}).get_text()
        actor_time = movie.find(name='p', attrs={'class', ''}).get_text().strip().replace('\n', '').replace(' ','').replace('\xa0', '')
        rating_num = movie.find(name='span', attrs={'class', 'rating_num'}).get_text()
        star_info = movie.find(name='div', attrs={'class', 'star'}).get_text().replace('\n', '').replace(rating_num,'')
        inq = movie.find(name='span', attrs={'class', 'inq'}).get_text()

        yield {
            '排名': num,
            '影名': name,
            '导演信息': actor_time,
            '评分': rating_num,
            '评分人数':star_info,
            '一句话介绍': inq
        }

for offset in range(0,250,25):
    link = 'https://movie.douban.com/top250?start=' + str(offset)
    html = get_page(link)
    book_info = parse_page(html)
    with open('豆瓣电影.json', 'w') as file:
        for info in book_info:
            jsobj = json.dumps(info)
            file.write(jsobj)
        print('写入完毕~')