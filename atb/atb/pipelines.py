# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class AtbPipeline(object):

    def __init__(self):
        self.Client = pymongo.MongoClient()
        self.DB = self.Client['atbDBv1']
        self.TB = self.DB['atbTBv1']





    def process_item(self, item, spider):

        dict_item = dict(item)
        self.TB.insert(dict_item)
        self.Client.close()
        return item
