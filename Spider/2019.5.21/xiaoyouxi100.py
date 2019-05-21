# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/21 15:41'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import json
import requests
from requests import RequestException
import random

# 先编写获得一页的函数
def get_one_page(url):
    try:
        with open('ip_list.json', 'r') as f:
            ip_json = json.load(f)
            ip_config = 'http://' + random.choice(ip_json)
            proxies = {'http': ip_config}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        }

        response = requests.get(url=url, headers=headers, proxies=proxies)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        else:
            return response.status_code + "错误"
    except RequestException:
        return '未知的错误'


# 解析网页数据
def parse_one_page(html):
    soup = bs(html, 'lxml')
    game_list = soup.find_all(name='div', attrs={'class', 'col-sm-3 ptd10'})
    for game in game_list:
        try:
            # 游戏名
            name = game.find(name='div', attrs={'class', 'post-title'}).get_text().strip().replace(' ','').replace('\n\n', '')
            # 游戏图片
            img_url = game.find(name='img').get('src')
            # 游戏介绍
            desc = game.find(name='div', attrs={'class', 'post-body'}).get_text().strip().replace(' ','').replace('\n\n', '')
            # 游戏标签
            label = game.find(name='span', attrs={'class', 'badge badge-danger'}).get_text().strip().replace(' ','').replace('\n\n', '')
            yield {
                '游戏名': name,
                '游戏图片': img_url,
                '游戏介绍': desc,
                '游戏标签': label
            }
        except Exception:
            print("出现了异常情况，正在紧急撤离....")
            continue

def write_to_file(content):
    # 如果不加ensure_ascii=False,中文会变成ascii编码格式
    with open('game.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main():
    for i in range(1, 6):
        url = 'https://www.xiaoyouxi100.com/tui/index_' + str(i)+ '.html'  # 解析 list 章节目录页面 后面是书籍编号
        html = get_one_page(url)
        book_info = parse_one_page(html)
        for book in book_info:
            write_to_file(book)


if __name__ == '__main__':
    main()