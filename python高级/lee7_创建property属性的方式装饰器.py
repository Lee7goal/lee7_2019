# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/21 0021 21:21'
__author__ = 'Lee7'


class Goods:
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

# ########## 调用 ##########


obj = Goods()
print(obj.price)  # 自动执行@property修饰的price方法，并获取方法的返回值
obj.price = 200  # 自动执行@price.setter修饰的price方法，并将123赋值给方法的参数
print(obj.price)
del obj.price  # 自动执行@price.deleter修饰的price方法

