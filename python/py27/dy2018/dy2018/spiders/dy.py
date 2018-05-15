# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders  import  CrawlSpider,Request,Rule
from scrapy.linkextractors import LinkExtractor
from dy2018.items import Dy2018Item

class DySpider(CrawlSpider):
    name = 'dy'
    allowed_domains = ['dy2018.com']
    start_urls = ['http://dy2018.com/']
    rules = (
        Rule(LinkExtractor(allow=r"/i/d+$"), callback="parse_dy", follow=True),
    )

    def start_requests(self):
        for i in  range(98550,98560):
            url="https://www.dy2018.com/i/"+str(i)+".html"
            #print "url==="+url
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        item=Dy2018Item()
        item['title']=response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[6]/div[1]/h1/text()').extract()[0]
        item['link']=response.xpath('//*[@id="Zoom"]/table[2]/tbody/tr/td/a/@href').extract()
        item["image_urls"]=response.xpath('//*[@id="Zoom"]/p[1]/img/@src').extract()[0]
        print item['image_urls']
        #print item['link']
        yield item
