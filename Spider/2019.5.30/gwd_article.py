# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/30 15:08'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

link = 'https://gameinstitute.qq.com/community/plan?order_by=hot'

r = requests.get(url=link, headers=headers)
r.encoding = 'utf-8'
html = r.text
soup = bs(html, 'lxml')
arc_list = soup.find_all('h4')
for info in arc_list:
    arc_url = info.find(name='a', attrs={'class', 'link'}).get('href')
    res = requests.get(url=arc_url, headers=headers)
    res.encoding = 'utf-8'
    res_html = res.text
    res_soup = bs(res_html, 'lxml')
    title = res_soup.find('title').get_text()
    author = res_soup.find(name='span', attrs={'class','name'}).get_text()
    content = res_soup.find(name='div', attrs={'class','art-cnt tigskin ck-content'}).get_text()
    print(title)
    print('\r\n')
    print("作者：", author)
    print(content)
    print("------"*25)
