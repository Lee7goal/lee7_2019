# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 16:33'
__author__ = 'Lee7'
import re
import requests
import os
"""
题目要求：
匹配出163的邮箱地址，且@符号之前有4-20位
"""


def main():
    email = input("请输入邮箱地址")
    # 如果在正则表达式中需要用到了某些普通的字符，比如.比如？等，仅仅需要在他们钱棉捻加一个反斜杠进行转义
    # 实际情况下，厂家应该会直接将@XXX.com固定死
    ret = re.match(r'^[a-zA-Z0-9_]{4,20}@163\.com$', email)
    if ret:
        print("%s 注册成功" % ret.group())
    else:
        print("%s不符合注册要求" % email)


if __name__ == "__main__":
    main()
