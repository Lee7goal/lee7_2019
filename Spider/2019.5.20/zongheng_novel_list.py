# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/20 17:12'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
from requests import RequestException
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
    listes_info = soup.find_all(name='li', attrs={'class', 'col-4'})
    for listes in listes_info:
        # 章节链接
        li_url = listes.find(name='a').get('href')
        # 章节名称
        li_name = listes.find(name='a').get_text().strip().replace(' ','').replace("\n\n", "、")
        yield {
            "章节名": li_name,
            "章节链接": li_url
        }

# 写入文件中
def write_to_file(content):
    # 如果不加ensure_ascii=False,中文会变成ascii编码格式
    with open('list_url.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main():
    novel_id = input("请输入书籍编号:\r\n")
    url = 'http://book.zongheng.com/showchapter/{}.html'.format(novel_id)  # 解析 list 章节目录页面 后面是书籍编号
    html = get_the_novel_list(url)
    book_info = parse_the_list(html)
    for book in book_info:
        # print(book)
        write_to_file(book)


if __name__ == '__main__':
    main()