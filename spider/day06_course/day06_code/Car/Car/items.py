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

    # 相当于: {'name':'', 'price':'', 'href':''}








