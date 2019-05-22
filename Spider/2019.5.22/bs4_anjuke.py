# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/22 11:19'
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
    house_list = soup.find_all(name='div', attrs={'class', 'zu-itemmod'})
    for house in house_list:
        try:
            # 房间标题名
            name = house.find(name='a').get_text().strip().replace(' ','').replace('\n\n', '')
            # 房间图片
            img_url = house.find(name='img', attrs={'class', 'thumbnail'}).get('src')
            # 房间地址
            local = house.find(name='address', attrs={'class', 'details-item'}).get_text().strip().replace(' ','').replace('\n\n', '')
            # 房间价格
            price = house.find(name='address', attrs={'class', 'details-item'}).get_text().strip().replace(' ','').replace('\n\n', '')
            # 房间标签
            label = house.find(name='p', attrs={'class', 'details-item bot-tag'}).get_text().strip().replace(' ','').replace('\n\n', '')
            yield {
                '房名': name,
                '房图': img_url,
                '房地址': local,
                '房价': price,
                '房间标签': label
            }
        except Exception:
            print("出现了异常情况，正在紧急撤离....")
            continue

def write_to_file(content):
    # 如果不加ensure_ascii=False,中文会变成ascii编码格式
    with open('house_info.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main():
    for i in range(1, 11):
        url = 'https://cd.zu.anjuke.com/ditie/dt20-s2291-p'  + str(i) # 解析 list 章节目录页面 后面是书籍编号
        html = get_one_page(url)
        house_total_info = parse_one_page(html)
        for house_total in house_total_info:
            write_to_file(house_total)


if __name__ == '__main__':
    main()

