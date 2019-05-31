# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/30 15:08'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool

def get_page(link):
    headers = {
        'Referer': 'https://gameinstitute.qq.com/community/plan?order_by=hot',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    r = requests.get(url=link, headers=headers)
    r.encoding = 'utf-8'
    html = r.text
    return html

def parse_page(html, link):
    headers = {
        'Referer': link,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    soup = bs(html, 'lxml')
    arc_list = soup.find_all('h4')
    for info in arc_list:
        arc_url = info.find(name='a', attrs={'class', 'link'}).get('href')
        res = requests.get(url=arc_url, headers=headers)
        res.encoding = 'utf-8'
        res_html = res.text
        res_soup = bs(res_html, 'lxml')
        title = res_soup.find('title').get_text()
        author = res_soup.find(name='span', attrs={'class', 'name'}).get_text()
        content = res_soup.find(name='div', attrs={'class', 'art-cnt tigskin ck-content'}).get_text()
        yield {
            '标题': title,
            '作者': author,
            '内容': content
        }

def main(offset):
    link = 'https://gameinstitute.qq.com/community/plan?order_by=new&page=' + str(offset)

    html = get_page(link)
    arc_dict = parse_page(html, link)
    for arc in arc_dict:
        print(arc)

if __name__ == '__main__':
    # 创建进程池，加快爬取速度
    pool = Pool()
    # 进程池的映射方法,第一个参数传入函数,第二个传入参数,用生成器生成了一个步长为25，循环20次列表
    pool.map(main, [i for i in range(1,85)])
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
