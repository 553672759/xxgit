# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Dy2018Pipeline(object):

    def __init__(self):
        self.file=open('imgs.txt','wb')

    def process_item(self, item, spider):
        # url=dict(item)['img_urlr']="\n"
        # self.file.write(url)
        #IMAGES_STORE = '/path/to/valid/dir'
        #ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
        return item
