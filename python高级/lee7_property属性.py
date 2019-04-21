# coding = utf-8
# Version:Python3.7.3
# Tools:Pycharm 2017.3.2
__date__ = '2019/4/21 0021 20:32'
__author__ = 'Lee7'


# ########## 定义 ##########
class Page:
    def __init__(self, current_page):
        # 用户当前需求的页码
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = ((self.current_page - 1) * self.per_items) + 1
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


class Item:

    def __init__(self, name, item_id):
        self.name = name
        self.item_id = item_id

    @property
    def item_in_page(self):
        if self.item_id > 10:
            if self.item_id % 10 == 0:
                val = (self.item_id - self.item_id % 10)/10 - 1
            else:
                val = (self.item_id - self.item_id % 10) / 10
            return '%s 的位置在本类的 %d 页' % (self.name, val)
        else:
            return "%s 的位置在本类的第 1 页" % self.name


a = Page(15)
b = Item('西瓜', 3)
c = Item('Mac—Air', 36)
d = Item('小米手机9', 60)
print(b.item_in_page)
print(c.item_in_page)
print(d.item_in_page)
