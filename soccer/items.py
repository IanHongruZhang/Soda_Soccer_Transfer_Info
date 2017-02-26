# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoccerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #转会日期
    transfer_date = scrapy.Field()
    #转会类型
    transfer_model = scrapy.Field()
    #转会费
    transfer_fee = scrapy.Field()
    #转会球员名字
    transfer_name = scrapy.Field()
    #转入俱乐部
    transfer_from = scrapy.Field()
    #转出俱乐部
    transfer_to = scrapy.Field()


