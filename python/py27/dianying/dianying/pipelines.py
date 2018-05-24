# -*- coding: utf-8 -*-

from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DianyingPipeline(object):
    def __init__(self):
        host="127.0.0.1"
        port=27017
        dbname='xx'
        sheetname='test'
        client = MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data=dict(item)
        self.post.insert(data)
        return item