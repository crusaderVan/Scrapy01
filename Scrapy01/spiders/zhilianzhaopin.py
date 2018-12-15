# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from scrapy.http import Request

from Scrapy01.items import ZhilianItem

class ZhilianzhaopinSpider(scrapy.Spider):
    name = 'zhilianzhaopin'
    allowed_domains = ['zhaopin.com']
    start_urls = []
    for i in range(0, 2):
        startNum = i * 60
        url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(
            startNum) + '&pageSize=60&cityId=531&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3&_v=0.40289009&x-zp-page-request-id=f549042cbcf44187ad0437bb583b162c-1544670110228-733398'
        start_urls.append(url)

    def parse(self, response):
        jsonBody = json.loads(response.body)
        jsonJobs = jsonBody['data']['results']

        for job in jsonJobs:
            job_item = ZhilianItem()
            job_item['jobName'] = job['jobName']
            job_item['jobSalary'] = job['salary']
            job_item['jobExp'] = job['workingExp']['name']
            job_item['jobEdu'] = job['eduLevel']['name']
            job_item['jobFuli'] = ','.join(job['welfare'])
            job_item['jobCompany'] = job['company']['name']
            job_item['jobProperty'] = job['company']['type']['name']
            job_item['jobScale'] = job['company']['size']['name']
            yield Request(response.urljoin(job['positionURL']), callback=self.parse_detail, meta={'job_item' : job_item})

    def parse_detail(self, response):
        job_item = response.meta['job_item']

        pos_ul = response.xpath('//div[@class="pos-ul"]//text()').extract()
        address = response.xpath('//p[@class="add-txt"]//text()').extract()
        company_intro = response.xpath('//div[@class="intro-content"]//text()').extract()

        job_item['jobRequire'] = pos_ul
        job_item['jobAddress'] = address
        job_item['jobCompanyIntro'] = company_intro

        return job_item


