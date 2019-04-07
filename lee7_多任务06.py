# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/7 0007 14:00'
__author__ = 'Lee7'

num = 100
nums = [11, 22]


def test1():
    global num
    num += 100


def test2():
    nums.append(33)


print(num)
print(nums)

test1()
test2()

print(num)
print(nums)




