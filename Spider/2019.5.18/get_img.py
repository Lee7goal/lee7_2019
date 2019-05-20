# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/20 12:24'
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
    house_info = soup.find_all(name="div", attrs={'class': 'content__list--item'})
    for house in house_info:
        try:
            # 房子标题
            name = house.find(name="a", attrs={'target':"_blank"}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # 房子价格
            price = house.find(name="span", attrs={'class':'content__list--item-price'}).get_text().strip().replace(' ','').replace("\n\n", "、")
            # 房子规格
            des = house.find(name='p', attrs={'class': 'content__list--item--des'})
            # 发布时间
            show_time = house.find(name='p', attrs={'class': 'content__list--item--time oneline'})
            # 文章图片
            jpg_url = house.find(name="img").get('src')
            yield {
                "name": name,
                "price":price,
                "des": des,
                "show_time": show_time,
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
    with open('The house info.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'https://cd.lianjia.com/zufang/' + str(offset) + '/#contentList'
    html = get_one_page(url)
    # 返回的是一个字典
    title_dict = parse_one_page(html)
    for title in title_dict:
        print(title)
        # write_to_file(title)


if __name__ == '__main__':
    # 创建进程池，加快爬取速度
    pool = Pool()
    # 进程池的映射方法,第一个参数传入函数,第二个传入参数,用生成器生成了一个步长为25，循环20次列表
    pool.map(main, [i for i in range(20)])
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
