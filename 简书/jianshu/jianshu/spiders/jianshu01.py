# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider,RedisSpider
from ..items import JianshuItem




# class Jianshu01Spider(CrawlSpider):
class Jianshu01Spider(RedisCrawlSpider):
    name = 'jianshu01'
    # allowed_domains = ['dddd']
    # start_urls = ['https://www.jianshu.com/p/05c9f97ddc13']
    redis_key = 'jianshu:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i=JianshuItem()
        item = {}

        item['title'] = response.xpath('//h1/text()').extract_first()

        item['author'] = response.xpath('//span[@class="_22gUMi"]/text()').extract_first()

        item['timing'] = response.xpath('//time/text()').extract_first()

        # item['read_num'] = re.findall(r'<span>阅读 (\d+)</span>',response.text)[0]

        return item
