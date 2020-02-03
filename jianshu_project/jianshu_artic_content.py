# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/8/29 14:38'
__author__ = 'lee7goal'
import csv
import os
import requests
from bs4 import BeautifulSoup as bs


def get_art_content():
    # 先制定好爬虫头部headers
    headers = {
        'Referer': 'https://www.jianshu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    # 先读取另一个功能模块文件得到的url数据并添加到本地列表

    article_list = []

    with open('jianshu_data.csv', 'r') as csv_file:
        csv_read = csv.reader(csv_file)
        for art in csv_read:
            if csv_read.line_num == 1:
                continue
            else:
                article_list.append(art[1])
    # 去重
    article_list = list(set(article_list))
    # 开始从本地列表读取目标网址进行二次内容提取 内容包括文章标题、文章作者(提供转载地址以及作者)、文章内容、文章图集
    for url in article_list:
        # 一次完整的数据获取
        link = url
        res = requests.get(url=link, headers=headers)
        res.encoding = 'utf-8'
        soup = bs(res.text, 'lxml')

        # 文章标题
        title = soup.find('h1').get_text().replace('|', '')
        # 作者内容
        # author = soup.select('div.author > div > span > a')[0].text
        # 文章内容
        # content = soup.find(name='div', attrs={'class', 'show-content'}).text.replace('\n', '')
        content = soup.find('article').text.replace('\n', '')
        # 图片内容
        pic_list = []
        # f_pic = soup.find(name='div', attrs={'class', 'show-content'}).find_all('img')
        f_pic = soup.find('article').find_all('img')
        for i in f_pic:
            pic_list.append(i.get('data-original-src'))
        # 创建文件夹
        os.mkdir('./project/' + title)
        # 导入文本内容
        path = './project/' + title + '/content.txt'
        with open(path, 'w+', encoding='utf-8') as f:
            f.writelines(title + '\n')
            # f.writelines(author)
            f.writelines(__date__ + '\n')
            f.writelines(content)
        # 下载图片
        for num, img in enumerate(pic_list):
            url = 'http:' + img
            img_path = './project/' + title + '/' + str(num) + '.jpg'
            with open(img_path, 'wb+') as img_file:
                req = requests.get(url)
                img_file.write(req.content)


get_art_content()