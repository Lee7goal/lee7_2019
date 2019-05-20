# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/20 16:23'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
from requests import RequestException
import re
import json



# 获取章节列表先
def get_the_novel_list(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return '未知错误' + response.status_code
    except RequestException:
        return "找不到源文件"

def parse_the_list(html):
    soup = bs(html, 'lxml')
    listes_info = soup.find_all(name='div', attrs={'class', 'reader_box'})
    for listes in listes_info:
        # 章节名
        li_name = listes.find(name='div', attrs={'class', 'title_txtbox'}).get_text().strip().replace(' ','').replace("\n\n", "、")
        # 内容
        li_content = listes.find(name='div', attrs={'class', 'content'}).get_text().strip().replace(' ','').replace("\n\n", "、")
        yield {
            "章节名": li_name,
            "内容": li_content
        }

def write_to_file(content):
    # 如果不加ensure_ascii=False,中文会变成ascii编码格式
    with open('novel.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main():
    with open('list_url.txt','r', encoding='utf-8') as f:
        url_str = f.read()
    href_all = re.findall(r'http://(.*?).html', url_str)
    for use_url in href_all:
        url = 'http://' + use_url + '.html'  # 解析 list 章节目录页面 后面是书籍编号
        html = get_the_novel_list(url)
        book_info = parse_the_list(html)
        for book in book_info:
            write_to_file(book)


if __name__ == '__main__':
    main()