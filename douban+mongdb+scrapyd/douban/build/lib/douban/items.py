# -*- coding: utf-8 -*-
import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名
    title = scrapy.Field()
    # 基本信息
    bd = scrapy.Field()
    # 评分
    star = scrapy.Field()
    # 简介
    quote = scrapy.Field()