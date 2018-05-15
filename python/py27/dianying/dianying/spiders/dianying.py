# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Request, Rule
from dianying.items import DianyingItem
# scrapy crawl spidertieba -o items.json



class dianying(CrawlSpider):
    name = "dianying"
    allowed_domains = ["www.dy2018.com"]
    rules=(
        Rule(LinkExtractor(allow=r"/i/d+$"),callback="parse_dy",follow=True),
    )


    def start_requests(self):
        www = "https://www.dy2018.com/i/"
        for i in range(98000, 98050):
            url = www + str(i) + ".html"
            yield Request(url=url,callback=self.parse)

    def parse_dy(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        sel = Selector(response)
        print
        items = DianyingItem()
        #取得名字
        a = sel.xpath('//*[@id="header"]/div/div[3]/div[2]/div[6]/div[1]/h1/text()').extract()[0]
        items['name'] = a
        #取得链接
        link=sel.xpath('//*[@id="Zoom"]/table[2]/tbody/tr/td/a/@href').extract()
        if(not link == 0):
            items['link'] =link
            yield items



