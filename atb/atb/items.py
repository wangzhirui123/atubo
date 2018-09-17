# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AtbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Class_name = scrapy.Field()
    caption = scrapy.Field()
    keyword = scrapy.Field()
    commpany = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    fixed_phone = scrapy.Field()
    contact_man = scrapy.Field()

