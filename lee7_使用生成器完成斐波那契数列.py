# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/9 14:51'
__author__ = 'Lee7'

def creat_num(all_num):
    print("-----1-----")
    a,b = 0,1
    current_num = 0
    while current_num < all_num:
        print("-----2-----")
        yield a  # 如果一个函数中有yield语句 那么这个就不再是函数，而是一个生成器的模板
        print("-----3-----")
        a,b = b,a+b
        current_num += 1
        print("-----4-----")

# 如果在调用creat_num的时候，发现这个函数中有yield，则不是调用函数，而是创建一个生成器对象
obj = creat_num(35)
obj1 = creat_num(36)
result = next(obj)
print(result)
result = next(obj)
print(result)
result = next(obj1)
print(result)
result = next(obj1)
print(result)

# new_list = list()
# for num in obj:
#     new_list.append(num)
# print(new_list)