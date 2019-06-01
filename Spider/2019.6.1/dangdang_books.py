# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/6/1 15:30'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool
import json

def get_page(link):
    # link = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-' + str([i for i in range(1,26)])
    # 定制headers
    headers = {
        'Referer': 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    res = requests.get(link)
    res.encoding = 'gbk'
    html = res.text
    return html

def parse_page(html):
    soup = bs(html, 'lxml')
    book_info = soup.find(name='ul', attrs={'class', 'bang_list clearfix bang_list_mode'}).find_all('li')
    for book in book_info:
        # <div class="list_num red">1.</div>
        list_num = book.find(name='div').get_text().strip().replace('\n','').replace(' ','')
        # <div class="name"><a href="http://product.dangdang.com/23761145.html" target="_blank" title="人间失格（日本小说家太宰治的自传体小说）">人间失格（日本小说家太宰治的自传体小说）</a></div>
        name = book.find(name='div', attrs={'class', 'name'}).get_text().strip().replace('\n','').replace(' ','')
        #  <span class="tuijian">100%推荐</span>
        tuijian = book.find(name='span', attrs={'class', 'tuijian'}).get_text().strip().replace('\n','').replace(' ','')
        #  <div class="publisher_info">（日）<a href="http://search.dangdang.com/?key=太宰治" title="（日）太宰治　著，杨伟　译" target="_blank">太宰治</a>　著，<a href="http://search.dangdang.com/?key=杨伟" title="（日）太宰治　著，杨伟　译" target="_blank">杨伟</a>　译</div>
        pub_info = book.find(name='div', attrs={'class', 'publisher_info'}).get_text().strip().replace('\n','').replace(' ','')
        # <span class="price_n">¥21.00</span>
        # <span class="price_r">¥25.00</span>
        price_now = book.find(name='span', attrs={'class', 'price_n'}).get_text().strip().replace('\n','').replace(' ','')
        # <span class="price_s">8.4折</span>
        sale_per = book.find(name='span', attrs={'class', 'price_s'}).get_text().strip().replace('\n','').replace(' ','')
        yield {
            '书籍编号': list_num,
            '书名': name,
            '推荐率': tuijian,
            '作者': pub_info,
            '现价': price_now,
            '打折': sale_per
        }

def main(offset):
    link = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-' + str(offset)
    html = get_page(link)
    book_list = parse_page(html)
    with open('当当网现推书籍.json', 'w') as f:
        for book in book_list:
            book_obj = json.dumps(book)
            f.write(book_obj)
            f.write("\n")
        print('已下载一页数据...请等待')


if __name__ == '__main__':
    print('任务开始执行')
    print('任务执行中......')
    pool = Pool()
    pool.map(main, [i for i in range(1, 26)])
    pool.close()
    pool.join()
