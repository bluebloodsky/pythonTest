# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LasvitSpider(CrawlSpider):
    name = 'lasvit'
    allowed_domains = ['lasvit.com']
    start_urls = ['http://lasvit.com/']

    rules = (
        Rule(LinkExtractor(allow=r'\.jpg'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'\.png'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
