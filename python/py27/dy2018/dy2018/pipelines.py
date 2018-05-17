# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Dy2018Pipeline(object):

    def __init__(self):
        self.file=open('imgs.txt','wb')

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def process_item(self, item, spider):
        # url=dict(item)['img_urlr']="\n"
        # self.file.write(url)
        #IMAGES_STORE = '/path/to/valid/dir'
        #ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
        return item
