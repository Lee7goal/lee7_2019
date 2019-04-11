# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 13:16'
__author__ = 'Lee7'

"""
匹配单个字符：
字符         功能
  .            匹配任意一个字符(除了\n)
  []           匹配[]中列举的字符
  \d           匹配数字，即0~9
  \D           匹配非数字
  \s           匹配空白,空格，TAB键
  \S           匹配非空白
  \w           匹配单词字符，即a-z,A-Z,0-9,_
  \W           匹配非单词字符
"""
import re

# 使用match方法进行匹配操作
ret = re.match(r'速度与激情[1-38-9]', "速度与激情8")  # 正则表达式，要匹配的字符串

print(ret)