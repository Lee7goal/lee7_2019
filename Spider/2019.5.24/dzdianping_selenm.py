# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/24 12:59'
__author__ = 'lee7goal'

# for i in range(1, 100):
#     link = 'http://www.dianping.com/chengdu/ch10/p{}'.format(i)
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get('http://www.9game.cn/xyrb/')
# http://www.dianping.com/chengdu/ch10/p1
element = driver.find_element_by_css_selector('td')
print(element.get_attribute('value'))
driver.quit()