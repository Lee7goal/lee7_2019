# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/9 0009 20:59'
__author__ = 'Lee7'


def creat_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        a, b = b, a + b
        current_num += 1
    return "ok"


obj = creat_num(11)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break


