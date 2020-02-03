# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/8/29 14:43'
__author__ = 'lee7goal'
from jianshu_artic_url import *
from jianshu_artic_content import *



if __name__ == '__main__':
    start = time.time()
    print("程序开始执行，请耐心等待...")

    get_article_url()
    get_art_content()

    print("总共耗时 %.2f 秒，获取了 %d 篇文章" % (time.time() - start,len(os.listdir('./')) - 7))
    print(os.listdir('./'))
