# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # 思考: 你在pipelines中需要哪些数据？
    # pipelines.py: with open(filename, 'w') as f:
    # filename: ./novel/盗墓笔记1/血尸.txt
    # 需要: 存储目录、小标题、小说内容
    directory = scrapy.Field()
    son_title = scrapy.Field()
    content = scrapy.Field()











