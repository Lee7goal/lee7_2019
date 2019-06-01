# coding=utf-8
# Version:3.6.3
# Tools:Pycharm
__date__ = ' 2019/6/1 16:37'
__author__ = 'lee7goal'
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)
