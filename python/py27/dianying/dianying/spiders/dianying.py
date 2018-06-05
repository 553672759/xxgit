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
        for i in range(91875,91880):
            url = "https://www.dy2018.com/i/" + str(i) + ".html"
            print str(i) + '...open'
            yield scrapy.spiders.Request(url=url, callback=self.parse_do)

    def parse_do(self, response):
        item = DianyingItem()
        #取得链接
        link=response.xpath('//*[@id="Zoom"]/table[2]/tbody/tr/td/a/@href').extract()
        print link
        if(len(link)==0):
            print "22222222"
            link=response.xpath('//*[@id="Zoom"]/table/tbody/tr/td/anchor/a/@').extract()
            print link
        if(not len(link) == 0):

            item['video_link'] = link
            item['video_name'] = response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[6]/div[1]/h1/text()').extract()[0]
            # imglink = response.xpath('//*[@id="Zoom"]/p[1]/img/@src').extract()
            #
            # item['video_img'] = imglink[0].split('/')[-1]
            # print "=====" + item['video_img']

            yield item



