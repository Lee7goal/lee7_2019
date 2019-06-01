# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/6/1 17:10'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool


def get_page(link):
    #  定制headers
    headers = {
        'Referer': 'https://www.qiushibaike.com/text/page/1/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    res = requests.get(link, headers=headers)
    res.encoding = 'utf-8'
    html = res.text
    return html

def parse_page(html):
    soup = bs(html, 'lxml')
    content_list = soup.find(name='div', attrs={'class', 'col1'}).find_all(name='div', attrs={'class', 'content'})
    for content in content_list:
        text = content.find('span').get_text().strip().replace('\n','').replace(' ','')
        yield {
            '每日一笑':text
        }

def main(offset):
    link = 'https://www.qiushibaike.com/text/page/' + str(offset) + '/'
    html = get_page(link)
    text_list = parse_page(html)
    for text in text_list:
        print(text.values())


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1,14)])
    pool.close()
    pool.join()