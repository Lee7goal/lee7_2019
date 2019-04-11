# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 16:09'
__author__ = 'Lee7'

"""
需求：写一个判断是否符合变量名的文件
:* 匹配前一个字符出现0或者无限次，可有可无
:+ 匹配前一个字符出现1次或者无限次，至少有一次
:? 匹配前一个字符出现1次或者0次，即要么有1次要么没有
:{m} 匹配前一个字符出现m次
:{m,n} 匹配前一个字符出现m到n次
"""
import re


def main():
    names = ["age", "_age", "2age", "age2", "a_age", "age_1_", "age!", "a#123"]
    for name in names:
        # ret = re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', name)
        # 正则规范(r'^XXXXXXX$',"")
        ret = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name)
        if ret:
            print("变量名%s符合要求" % name)
        else:
            print("变量名%s非法" % name)


if __name__ == "__main__":
    main()

