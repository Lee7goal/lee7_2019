# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/18 10:46'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs
import json
from multiprocessing import Pool
from requests import RequestException


# 获取一页的html源码
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        # 如果返回值为200 则返回代码
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析源码，拿到想拿的内容
def parse_one_page(html):
    soup = bs(html, 'lxml')
    """
    分析下面代码：获取书单的序列号，名字，作家，出版时间，评分数
    < div id = "item253261897"  class ="doulist-item" >
    ...
    < span  class ="pos" > 1 < / span >
    < div   class ="post" >
    < a href = "https://book.douban.com/subject/10519369/"  target = "_blank" > < img   width = "100"   
    src = "https://img1.doubanio.com/view/subject/l/public/s8869768.jpg" / > < / a >
    < / div >
    < div   class ="title" >
    < a href = "https://book.douban.com/subject/10519369/"  target = "_blank" > 万物生光辉 < / a >
    < / div >
    < div   class ="abstract" >
    作者: [英]
    吉米 & middot;
    哈利
    < br / > 出版社: 中国城市出版社
    < br / > 出版年: 2012 - 3
    < / div >
    ..
    < / div >
    """
    doulist = soup.find_all(name="div", attrs={'class': 'doulist-item'})
    for book in doulist:
        try:
            # .strip().replace(' ', '').replace("\n\n", "、")：去除空格,将空格缩进,再将\n\n替换掉
            # 书的序号
            seq = book.find(name='span', attrs={'class':'pos'}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # print(seq)
            # 图片url
            jpg_url = book.find(name='img').get('src')
            # print(jpg_url)
            # 书名
            book_name = book.find(name='div', attrs={'class':'title'}).get_text().strip().replace(' ', '').replace("\n\n", "、")
            # print(book_name)
            # 简介
            book_author = book.find(name='div', attrs={'class':'abstract'}).get_text().strip().replace(' ', '').replace("\n\n", "、")
            # print(book_author)
            # 书评
            book_star = book.find(name='blockquote', attrs={'class': 'comment'}).get_text().strip().replace(' ', '').replace("\n\n", "、")
            # print(book_star)
            yield {
                "seq": seq,
                "jpg_url": jpg_url,
                "book_name": book_name,
                "book_author": book_author,
                "book_star": book_star
            }
        except Exception:
            print("出现了异常情况，正在紧急撤离....")
            continue


# 写入文件中
def write_to_file(content):
    # 如果不加ensure_ascii=False,中文会变成ascii编码格式
    with open('books.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    """
    注释下面的主页,因为分析出第一页也可以写成0的形式
    url = 'https://www.douban.com/doulist/1264675/'
    第2页:
    https://www.douban.com/doulist/1264675/?start=25&sort=seq&sub_type=
    第3页:
    https://www.douban.com/doulist/1264675/?start=50&sort=seq&sub_type=
    可以推断如下的第1页：
    https://www.douban.com/doulist/1264675/?start=0&sort=seq&sub_type=
    """
    url = 'https://www.douban.com/doulist/1264675/?start=' + str(offset) + '&sort=seq&sub_type='
    html = get_one_page(url)
    # 返回的是一个字典
    book_dict = parse_one_page(html)
    for content in book_dict:
        print(content)
        write_to_file(content)


if __name__ == '__main__':
    # 创建进程池，加快爬取速度
    pool = Pool()
    # 进程池的映射方法,第一个参数传入函数,第二个传入参数,用生成器生成了一个步长为25，循环20次列表
    pool.map(main, [i * 25 for i in range(20)])
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
