# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/8/29 10:51'
__author__ = 'lee7goal'
from selenium import webdriver
import random
import time
import csv

def get_article_url():

    link = 'https://www.jianshu.com'
    option = webdriver.FirefoxOptions()
    option.headless = True
    brow = webdriver.Firefox(options=option)
    brow.get(link)

    # 第一次进入时要下拉两次
    for a in range(2):
        px = random.randint(10000, 20000)
        js="var q=document.documentElement.scrollTop=" + str(px)
        brow.execute_script(js)
        # print("执行了%d次下拉" % (a + 1))
        time.sleep(2)

    # 然后不知道要点多少次阅读更多 当没有的时候 通过try停止 或者利用if 停止
    for b in range(20):
        try:
            load = brow.find_element_by_class_name('load-more')
            load.click()
            time.sleep(1)
        except:
            # print("执行了 %d 次点击阅读更多" % (b + 1))
            break

    # 然后不能点击阅读更多的时候开始获取文章标题和文章链接
    # 将数据写入到需求的csv中
    with open('jianshu_data.csv', 'a+', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        columns = ['article','href']
        csvwriter.writerow(columns)
        for num in range(1,200):
            try:
                xpath = '/html/body/div[1]/div/div[1]/div[2]/ul/li[' + str(num) + ']/div/a'
                title = brow.find_element_by_xpath(xpath).text
                url = brow.find_element_by_xpath(xpath).get_attribute('href')
                csvwriter.writerow([title,url])
                # print(title)
                # print(url)
                # print("====="*15)
            except:
                # print("获取了 %d 条文章信息" % (num + 1))
                break

    # print("总共耗时 %.2f 秒" % (time.time() - start))


