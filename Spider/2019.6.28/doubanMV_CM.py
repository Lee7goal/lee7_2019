# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/6/28 19:47'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
import wordcloud
import jieba
from collections import Counter
from os import path


def getonepage(offset):
    link = 'https://movie.douban.com/subject/1291561/comments?start=' + str(offset * 20) + '&limit=20&sort=new_score&status=P'

    headers = {
        'Referer': 'https://movie.douban.com/subject/1291561/?from=showing',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    res = requests.get(url=link, headers=headers)
    res.encoding = 'utf-8'
    html = res.text

    soup = bs(html, 'lxml')

    commit_list = soup.find_all(name='span', attrs={'class', 'short'})
    text = ''
    for commit in commit_list:
        com_content = commit.get_text().replace('\n', '')
        text += com_content

    with open('.//doc/qianxun.txt', 'w', encoding='utf-8') as fw:
        fw.write(text)



