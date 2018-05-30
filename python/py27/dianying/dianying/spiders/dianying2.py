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
    i=98000
    url = "https://www.dy2018.com/i/"
    start_urls = [url+str(i)+".html"]

    def parse(self,response):
        for i in range(98000,98050):
            url = "https://www.dy2018.com/i/" + str(i) + ".html"
            print str(i) + '...open'
            yield scrapy.spiders.Request(url=url, callback=self.parse_do)

    def parse_do(self, response):
        items = DianyingItem()
        #取得链接
        link=response.xpath('//*[@id="Zoom"]/table[2]/tbody/tr/td/a/@href').extract()
        if(not len(link) == 0):
            items['link'] =link
            # 取得名字
            items['name'] = response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[6]/div[1]/h1/text()').extract()[0]
            items['image_urls'] = response.xpath('//*[@id="Zoom"]/p[1]/img/@src').extract()
            yield items



