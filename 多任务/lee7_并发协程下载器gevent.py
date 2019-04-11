# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/11 12:04'
__author__ = 'Lee7'
import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()


def dl(img_name, img_url):

    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(dl, '1.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/04/01/6707439_20190401000838_small.jpg'),
        gevent.spawn(dl, '2.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/04/05/866405_20190405135436_small.jpg'),
        gevent.spawn(dl, '3.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/03/19/4531142_20190319181313_small.jpg'),
    ])
    print("下载成功")


if __name__ == "__main__":
    main()
