# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class JianshuPipeline(object):
    def __init__(self):
        self.f=open('test.json','w',encoding='utf-8')
        # client=pymysql.connect(host='127.0.0.1',port=3306,user='admin',password='Root110qwe',database='jianshu',charset='utf8')
        # self.cursor=self.client.cursor()

    def process_item(self, item, spider):
        # sql语句 item就是要储存数据
        # sql='insert into table_name value($s,$s,$s,$s)'
        # self.cursor.execute(sql,[item.get('title'),item.get('author')])
        self.f.write(str(item) + '\n')
        return item

    def close_spider(self,spider):
        # 在spider关闭的时候执行
        self.f.close()