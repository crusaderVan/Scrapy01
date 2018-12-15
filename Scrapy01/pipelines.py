# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
from Scrapy01.utils import ScrapyUtils

class ZhilianzhaopinPipeline(object):

    def __init__(self):
        '''
        initialize the object
        '''
        self.spider = None
        self.count = 1

    def open_spider(self, spider):
        self.wb = Workbook()
        self.ws = self.wb.active
        # 设置表头
        self.ws.append(['序号', '职位名称', '薪资', '工作经验', '学历',
                        '福利特色', '公司名称', '公司性质' ,'公司规模',
                        '职位要求', '公司地址', '公司简介'])
    def process_item(self, item, spider):
        # 去掉空行
        item = ScrapyUtils.item_processor(item)
        # 插入文件
        line = [self.count, item['jobName'], item['jobSalary'], item['jobExp'], item['jobEdu'], item['jobFuli'],
                item['jobCompany'], item['jobProperty'], item['jobScale'], item['jobRequire'], item['jobAddress'],
                item['jobCompanyIntro']]
        self.ws.append(line)
        self.count = self.count + 1
        return item

    def close_spider(self, spider):
        self.wb.save('E:\PythonProject\Scrapy01\Scrapy01\output\zhilianzhaopin01.xlsx')
        self.wb.close()


