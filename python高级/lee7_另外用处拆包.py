# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/20 0020 21:38'
__author__ = 'Lee7'


def demo2(a, b, *args, **kwargs):
    print("-----")
    print(a)
    print(b)


def demo(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

    demo2(a, b, *args, **kwargs)


demo(2, 200, 28525, name="老王", age=16)
