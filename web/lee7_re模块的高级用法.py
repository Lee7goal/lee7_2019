# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 17:48'
__author__ = 'Lee7'
import re
"""
match：从头开始匹配
search: 不会从头匹配，但是匹配到一个符合的就接受到了
findall: 找到所有的search
sub: 能够替换所有替换的数字
split: 切割字符串并返回一个列表
"""
ret1 = re.search(r'\d+', "总阅读量为 9654").group()
print(ret1)

ret2 = re.match(r'\d+', "总阅读量为 9654")
print(ret2)

night_num = 9654-3524-4096
ret3 = re.findall(r'\d+', "总阅读量为 9654,早晨阅读量为 3524，下午阅读量为 4096 ，余下 %d 为晚间阅读量" % night_num)
print(ret3[0], ret3[1], ret3[2], ret3[3])

ret4 = re.sub(r'\d+', '998', "python = 997, c++ = 1024")
print(ret4)


def add(temp):
    str_num = temp.group()
    num = int(str_num) + 1
    return str(num)


ret5 = re.sub(r'\d+', add, "python = 997")
print(ret5)
ret5 = re.sub(r'\d+', add, "python = 99")
print(ret5)

ret6 = re.split(r':| ', "info:xiaozhang 33 shandong")
print(ret6)
