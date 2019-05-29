# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/5/29 15:00'
__author__ = 'lee7goal'
import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    # 'Cookie': '_zap=d2f03a7c-ef9b-41bd-b2b0-7a390cc6796c; d_c0="ALClzjaoPQ6PTgx_leq3RsMorK0-qmg2Z0w=|1537435905"; tst=r; __gads=ID=7217b7319a6c9ac3:T=1558673177:S=ALNI_MaEcuDUxhcxR5dyDgxybWqv3TAJxg; q_c1=aa8c26afd2144c9f938049d9fa76397b|1558673182000|1537435921000; _xsrf=6108bc04-f5d5-4813-bce8-884a724b946f; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; capsion_ticket="2|1:0|10:1559113218|14:capsion_ticket|44:MGI0NWUyYzkwODI5NDE1NWI4ODQ3ZTNkNjM4YzhhOGY=|21a417826b491419573848f6fc27dcd60ab4c6afdf5534e8cb8d83911acdce30"; z_c0="2|1:0|10:1559113226|4:z_c0|92:Mi4xOU1qWUFRQUFBQUFBc0tYT05xZzlEaVlBQUFCZ0FsVk5DbnpiWFFEOU5NeC1WR0pvMm42NzhiV1lhTzJvQWNSNHRB|e74169e3eac4c556b4cbb047271925e17b9805b8384871832aa4e82f83c9a9ea"'
}
link = 'https://www.zhihu.com/people/li-si-han-97/activities'
r = requests.get(url=link, headers=headers)
r.encoding = 'utf-8'
html = r.text
soup = bs(html, 'lxml')
print(soup)