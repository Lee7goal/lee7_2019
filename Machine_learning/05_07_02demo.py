# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/7 12:37'
__author__ = 'lee7goal'
# strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
# print([x.upper() for x in strings if len(x) > 2])
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x.__float__() for tup in some_tuples for x in tup]
print(flattened)
flattened2 = [[x for x in tup] for tup in some_tuples]
print(tuple(flattened2))