# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class Scrapy01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhilianItem(scrapy.Item):
    jobName = Field()
    jobSalary = Field()
    jobExp = Field()
    jobEdu = Field()
    jobFuli = Field()
    jobCompany = Field()
    jobProperty = Field()
    jobScale = Field()
    jobRequire = Field()
    jobAddress = Field()
    jobCompanyIntro = Field()