# # -*- coding: utf-8 -*-
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from dy2018.spiders import dy
#
# # 获取settings.py模块的设置
# settings = get_project_settings()
# process = CrawlerProcess(settings=settings)
#
# # 可以添加多个spider
# # process.crawl(Spider1)
# # process.crawl(Spider2)
# process.crawl(dy)
#
# # 启动爬虫，会阻塞，直到爬取完成
# process.start()