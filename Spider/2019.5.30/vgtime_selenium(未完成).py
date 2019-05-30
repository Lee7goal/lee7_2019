# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/30 9:54'
__author__ = 'lee7goal'
from selenium import webdriver
from pyquery import PyQuery as pq
import time

link = 'http://www.vgtime.com/topic/index.jhtml'

# 新建浏览器进程
brow = webdriver.Chrome()
# 将浏览器放大
# brow.maximize_window()
# 打开网页
brow.get(link)
# 解析网页
html = brow.page_source
doc = pq(html)
list_source = doc('.vg_list li.news').items()

# 获取文章主页并拼接新的url
for info in list_source:
    source_data = {
        'url': info.find('a').attr('href')
    }

    sour_brow = webdriver.Chrome()
    sour_brow.get('http://www.vgtime.com' + source_data['url'])
    time.sleep(1)
    sour_html = sour_brow.page_source
    sour_doc = pq(sour_html)
    art_source = sour_doc('.vg_main article').items()
    for art in art_source:
        art_data = {
            '文章标题': art.find('.art_tit').text(),
            '编辑': art.find('.color').text(),
            '发布时间': art.find('.time_box').text(),
            '引言': art.find('.abstract').text(),
            '内容': art.find('.p').text()
        }
        print(art_data)
    sour_brow.close()

# 关闭浏览器
brow.close()