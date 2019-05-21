# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/21 17:22'
__author__ = 'lee7goal'
import json
import random

with open('ip_list.json', 'r') as f:
    ip_json = json.load(f)
    proxies = 'http://' + random.choice(ip_json)


