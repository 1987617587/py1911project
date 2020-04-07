# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs

class JobspiderPipeline(object):


    def __init__(self):
        '''
        初始化，打开csv文件，设置标题行
        '''
        self.file = codecs.open('51jb.csv','w',encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['职业','公司','工作地点','薪资','发布时间'])


    def process_item(self, item, spider):
        self.wr.writerow([item['name'],item['corp'],item['city'],item['salary'],item['pud_date']])
        return item

    def close_spider(self,spider):
        self.file.close()


# 新建管道
class JobspiderMysqlPipeline(object):
    '''
    实现mysql数据的存储
    '''

    def __init__(self):
        '''
        初始化，打开csv文件，设置标题行
        '''
        self.file = codecs.open('51jb.csv','w',encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['职业','公司','工作地点','薪资','发布时间'])


    def process_item(self, item, spider):
        self.wr.writerow([item['name'],item['corp'],item['city'],item['salary'],item['pud_date']])
        return item

    def close_spider(self,spider):
        self.file.close()
