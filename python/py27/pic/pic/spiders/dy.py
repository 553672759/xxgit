# -*- coding: utf-8 -*-
import scrapy
from pic.items import VideoItem
import sys

class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['dy2018.com']
    url = "https://www.dy2018.com/i/"
    start_urls = [url + "98000.html"]

    def parse(self, response):

        for i in range(98900,98950):
            url = "https://www.dy2018.com/i/" + str(i) + ".html"
            print str(i) + '...open'
            yield scrapy.spiders.Request(url=url, callback=self.parse_do)

    def parse_do(self, response):
        item = VideoItem()
        link = response.xpath('//*[@id="Zoom"]/table[2]/tbody/tr/td/a/@href').extract()
        # print "link====="+str(len(link))
        if (not len(link) == 0):
            item['video_link'] = link
            item['video_name'] = response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[6]/div[1]/h1/text()').extract()[0]
            imglink = response.xpath('//*[@id="Zoom"]/p[1]/img/@src').extract()
            item['image_urls'] = imglink
            i= imglink[-36:]
            item['video_img'] =i

            yield item