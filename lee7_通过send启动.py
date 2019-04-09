# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/9 0009 21:42'
__author__ = 'Lee7'


def creat_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a  # 把a的值暂停
        print("------>ret", ret)
        a, b = b, a + b
        current_num += 1


obj = creat_num(11)
# ret = obj.send(None)   # send一般不会放到第一次启动生成器，如果非要这么左，传递None
ret = next(obj)
print(ret)

# send里面的数据会传递给yield，当作yield的结果，然后ret保存这个结果
# send的结果是下一次调用yield时后面的值
ret = obj.send("哈哈")
print(ret)
