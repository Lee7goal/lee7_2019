# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/18 9:45'
__author__ = 'lee7goal'
from bs4 import BeautifulSoup as bs
import requests
from requests import RequestException
import json
from multiprocessing import Pool

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


def parse_one_page(html):
    soup = bs(html, 'lxml')
    titles_info = soup.find_all(name="div", attrs={'class': 'contentdiv'})
    for titles in titles_info:
        try:
            # 文章标题
            name = titles.find(name="h1", attrs={'class':"article-title"}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # print(name)
            # 文章内容
            content = titles.find(name="td", attrs={'class':'t_f'}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # 文章图片
            jpg_url = titles.find(name="img").get('src')
            yield {
                "name": name,
                "content":content,
                # "mean_price":mean_price,
                "jpg_url": jpg_url,
                # "get_points": get_points,
                # "local": local
            }
        except Exception:
            print("出现了异常情况，正在紧急撤离....")
            continue


def write_to_file(content):
    # 如果不加ensure_ascii=False,中文会变成ascii编码格式
    with open('gameres_spider.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'https://www.gameres.com/' + str(offset) + '.html'
    html = get_one_page(url)
    # 返回的是一个字典
    title_dict = parse_one_page(html)
    for title in title_dict:
        # print(title)
        write_to_file(title)


if __name__ == '__main__':
    # 创建进程池，加快爬取速度
    pool = Pool()
    # 进程池的映射方法,第一个参数传入函数,第二个传入参数,用生成器生成了一个步长为25，循环20次列表
    pool.map(main, [i for i in range(800000,840000)])
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
