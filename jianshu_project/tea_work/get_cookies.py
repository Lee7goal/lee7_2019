# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/9/7 0007 22:14'
__author__ = 'Lee7'
from selenium import webdriver
from PIL import Image
from io import BytesIO
import base64
import time
import json

def get_cookies():

    link = 'https://data.bytedance.com/'
    brow = webdriver.Firefox()
    brow.get(link)

    account = 'liqigao@52wanh5.com'                  #input('请输入邮箱地址:\n')
    password = 'lee7goal@@##'                        #input('请输入密码:\n')

    account_input = brow.find_element_by_id('account')
    password_input = brow.find_element_by_id('password')
    captcha_input = brow.find_element_by_id('captcha')

    account_input.send_keys(account)
    password_input.send_keys(password)
    time.sleep(2)

    captcha_img = brow.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div[2]/div/img').get_attribute('src')
    img_url = captcha_img.split(',')[-1]

    binary_img_data = base64.b64decode(img_url)
    file_like = BytesIO(binary_img_data)
    img = Image.open(file_like)
    img.show()

    img_value = input('请输入验证码:\n')
    captcha_input.send_keys(img_value)
    brow.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/button').click()

    time.sleep(2)

    cookie = brow.get_cookies()
    jsoncookies = json.dumps(cookie)
    with open('bytedance.json', 'w') as f:
        f.write(jsoncookies)

    print("获取cookie免登陆完成，执行下一步......")