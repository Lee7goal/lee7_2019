# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 13:01'
__author__ = 'Lee7'
import re

# 使用match方法进行匹配操作
result = re.match(r'[hH]ello', "hello,world")  # 正则表达式，要匹配的字符串

# 如果上一步匹配到数据，可以使用group方法来提取数据
print(result.group())
