# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/9 11:56'
__author__ = 'Lee7'
class Fibonacci(object):
    def __init__(self,all_num):
        self.all_nums = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1
        self.list_num = list()

    def __iter__(self):
        """如果想要一个对象成为一个可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < self.all_nums:
            ret = self.a
            self.a,self.b = self.b,self.a + self.b
            self.list_num.append(ret)
            self.current_num += 1
            return self.list_num
        else:
            raise StopIteration

fibo = Fibonacci(5.6)

for num in fibo:
    print(num)

