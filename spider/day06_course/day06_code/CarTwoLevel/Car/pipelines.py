# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CarPipeline(object):
    def process_item(self, item, spider):
        # 处理爬虫交过来的item数据
        print(item['name'], item['price'], item['href'])

        return item









