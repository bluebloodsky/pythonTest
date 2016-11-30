# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LasvitSpider(CrawlSpider):
    name = 'lasvit'
    allowed_domains = ['lasvit.com']
    start_urls = ['http://lasvit.com/']

    rules = (
        Rule(LinkExtractor(allow='.*'), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
