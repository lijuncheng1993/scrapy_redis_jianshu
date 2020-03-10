# -*- coding: utf-8 -*-
import scrapy
# from ..items import JianshuItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    # allowed_domains = ['dddd']
    start_urls = ['https://www.jianshu.com/p/05c9f97ddc13']

    # https://www.jianshu.com/p/05c9f97ddc13
    # https://www.jianshu.com/p/75f27d77b4d0

    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/.*?'), callback='parse', follow=True),
    )

    def parse(self, response):
        print(response.url, '------------')
        item = {}
        return item
