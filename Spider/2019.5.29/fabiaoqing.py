# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/29 9:32'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
import urllib.request

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

for i in range(1, 940):
    link = 'https://fabiaoqing.com/bqb/lists/type/hot/page/' + str(i) + '.html'
    r = requests.get(url=link, headers=headers)
    r.encoding = 'utf-8'
    html = r.text
    soup = bs(html, 'lxml')
    # print(soup)

    img_url_list = soup.find_all(name='div', attrs={'class','bqppdiv'})
    # print(img_url_list)
    for img_url in img_url_list:
        get_url = img_url.find('img').get('data-original')
        get_name = img_url.find(name='p').get_text().strip().replace('\n', '')
        file_name = 'bqb\\' + get_name.split('-',2)[0] + '.jpg'
        html2 = requests.get(get_url)
        with open(file_name, 'wb') as img:
            img.write(html2.content)
