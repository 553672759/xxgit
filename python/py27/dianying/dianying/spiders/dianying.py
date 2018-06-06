# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Request, Rule
from dianying.items import DianyingItem
# scrapy crawl spidertieba -o items.json



class dianying(scrapy.Spider):
    name = "dianying"
    allowed_domains = ["www.dy2018.com"]
    url = "https://www.dy2018.com/i/"
    start_urls = [url+"98000.html"]

    def parse(self,response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        for i in range(95000,99318):
            url = "https://www.dy2018.com/i/" + str(i) + ".html"
            print str(i) + '...open'
            yield scrapy.spiders.Request(url=url, callback=self.parse_do)

    def parse_do(self, response):

        item = DianyingItem()
        #取得链接
        #link=response.xpath('//*[@id="Zoom"]/table[2]/tbody/tr/td/a/@href').extract()
        link = response.xpath('//*[@id="Zoom"]//a/text()').extract()
        print("zzzzzzzz=")
        print link
        if(len(link)==0):
             print "1...begin"
             link = response.xpath('//*[@id="Zoom"]/table[1]/tbody/tr/td/anchor/a/text()').extract()
             print link
             print('1...over')
        if(not len(link) == 0):
            video_link=""
            for i in link:
                print "i========="+i
                video_link+= i
                video_link += "##"
            item['video_link'] = video_link
            item['video_name'] = response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[6]/div[1]/h1/text()').extract()[0]
            imglink = response.xpath('//*[@id="Zoom"]/p[1]/img/@src').extract()
            item['image_urls'] = imglink
            if(not len(imglink) == 0):
                item['video_img'] = imglink[0].split('/')[-1]
            print 'will yield...'
            yield item



