# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/20 13:50'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
from requests import RequestException
import json


def get_one_page(url):
    try:
        headers = {
            'host': 'cd.5i5j.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
    # 如果返回值正常 则为200 则对返回数据进行解析
        if response.status_code == 200:
            return response.text
        return response.status_code
    except RequestException:
        return '接受数据有误，考虑是否被限制'


def parse_one_page(html):
    soup = bs(html, 'lxml')
    house_info = soup.find_all(name='div', attrs={'class': 'listCon'})
    for house in house_info:
        try:
            # 1.房子的标题
            title = house.find(name='h3', attrs={'class': 'listTit'}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # 2.户型
            hx = house.find(name='i', attrs={'class': 'i_01'}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # 3.房子位置
            local = house.find(name='a', attrs={'target': '_blank'}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # 4.房子价格
            price = house.find(name='p', attrs={'class': 'redC'}).get_text().strip().replace(' ','').replace("\n\t\t\t\t\t\t\t\t\t", "、")
            # 5.出租方式
            ways = house.find(name='p').get_text().strip().replace(' ','').replace("\n\n", "、")
            yield {
                "房名": title,
                "户型": hx,
                "房子位置": local,
                "价格": price,
                "出租方式": ways,
            }
        except Exception:
            print("出现了异常情况，正在紧急撤离....")
            continue

url = 'https://cd.5i5j.com/zufang/n1/'  # 分析域名 cd 代表成都 n2代表第二页
html = get_one_page(url)
infos = parse_one_page(html)
for info in infos:
    print(info)
