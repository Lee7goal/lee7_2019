# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/9/8 0008 15:37'
__author__ = 'Lee7'
from selenium import webdriver
import json
import time

def get_sub_info(sub_value):

    link = 'https://data.bytedance.com/tea/app/52616/behavior-detail'
    brow = webdriver.Firefox()
    brow.get(link)

    fp = open('bytedance.json','r')
    cookies = json.load(fp)
    fp.close()
    for cookie in cookies:
        brow.add_cookie(cookie)
    brow.refresh()

    sub_id_input = brow.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/span/span/input')
    sub_id_input.send_keys(sub_value)
    brow.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/button').click()

    # 如果有事件显示 则下载用户事件
    time.sleep(3)
    brow.find_element_by_class_name('ant-btn ant-btn-primary').click()
