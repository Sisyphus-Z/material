# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    # 汽车名称、价格、链接
    name = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
    # 行驶里程、排量、变速箱
    km = scrapy.Field()
    displace = scrapy.Field()
    typ = scrapy.Field()









