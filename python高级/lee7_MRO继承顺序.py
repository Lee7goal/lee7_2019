# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/20 0020 19:56'
__author__ = 'Lee7'


class Parent:
    def __init__(self, name, *args, **kwargs):
        print("Parent开始被调用")
        self.name = name
        print("Parent停止被调用")


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son1开始被调用")
        self.age = age
        super().__init__(name, *args, **kwargs)
        print("Son1停止被调用")


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print("Son2开始被调用")
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print("Son2停止被调用")


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson开始被调用")
        super().__init__(name, age, gender)
        print("Grandson停止被调用")


print(Grandson.__mro__)
grandson = Grandson("小王", 15, '男')

print('姓名', grandson.name)
print('年龄', grandson.age)
print('性别', grandson.gender)

print("*****多继承使用类名.__init__发生的状态*****")
