# -*- coding: utf-8 -*-
import scrapy


class ZhilianzhaopinSpider(scrapy.Spider):
    name = 'zhilianzhaopin'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
