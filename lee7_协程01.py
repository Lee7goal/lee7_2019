# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/8 0008 21:33'
__author__ = 'Lee7'
from collections import Iterable
from collections import Iterator
from time import sleep


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象成为一个可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老万")
classmate.add("王五")
classmate.add("张山")
classmate.add("白无迹")

print("判断classmate是否是可以迭代的对象", isinstance(classmate, Iterable))

classmate_iterator = iter(classmate)
print("判断classmate_iterator是否是迭代器", isinstance(classmate_iterator, Iterator))


# print(next(classmate_iterator))
for i in classmate:
    print(i)
    sleep(2)

