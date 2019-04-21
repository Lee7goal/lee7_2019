# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/21 0021 12:03'
__author__ = 'Lee7'


class Foo:

    def __init__(self, name):
        self.name = name
        self.country = '中国'

    def ord_func(self):
        """定义实例方法，至少有一个self参数"""
        print('实例方法')

    @classmethod
    def class_func(cls):
        """定义类方法，至少有一个cls参数"""
        print('类方法')

    @staticmethod
    def static_func():
        """定义静态方法，去默认参数"""
        print('静态方法')


f = Foo('四川')
# 调用实例方法
f.ord_func()
print(f.name)
print(f.country)
# 调用类方法
Foo.class_func()


# 调用静态方法
Foo.static_func()
