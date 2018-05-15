# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Dy2018Pipeline(object):
    def process_item(self, item, spider):
        IMAGES_STORE = '/path/to/valid/dir'
        ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
        return item
