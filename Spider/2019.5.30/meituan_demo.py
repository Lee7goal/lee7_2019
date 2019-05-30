# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/30 16:22'
__author__ = 'lee7goal'
import requests
import json
from bs4 import BeautifulSoup as bs

# 定义请求url  这里的start每次多加25 直到250
for i in range(0, 250, 25):
    url = 'https://book.douban.com/top250?start=' + str(i)
    # 定义请求头
    headers = {
        'Referer': 'https://www.google.com/',
        'Host': 'book.douban.com',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    # 定义res

    res = requests.get(url=url, headers=headers)
    res.encoding = 'utf-8'
    html = res.content
    soup = bs(html, 'lxml')
    book_list = soup.find_all(name='table')
    for info in book_list:
        try:
            book_name = info.find(name='div', attrs={'class', 'pl2'}).get_text().strip().replace('\n','').replace(' ','')
            print(book_name)
            book_author = info.find(name='p', attrs={'class', 'pl'}).get_text().strip().replace('\n','')
            print(book_author)
            book_rating = info.find(name='span', attrs={'class', 'rating_nums'}).get_text().strip().replace('\n','')
            rating_num = info.find(name='span', attrs={'class', 'pl'}).get_text().strip().replace('\n','').replace(' ','')
            print(book_rating,"分", rating_num)
            inq = info.find(name='span', attrs={'class', 'inq'}).get_text().strip().replace('\n','')
            print(inq)
            book_img = info.find('img').get('src')
            print(book_img)
            print("-----" * 20)
        except:
            continue
