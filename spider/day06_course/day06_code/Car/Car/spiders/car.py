# -*- coding: utf-8 -*-
import scrapy
from ..items import CarItem

class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['www.guazi.com']
    # start_urls: 改为了第一页的url地址
    start_urls = ['https://www.guazi.com/bj/buy/o1/#bread']
    o = 1

    def parse(self, response):
        """提取第一页的所有数据"""
        # 基准xpath: 匹配汽车信息的li节点对象列表
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            # 在给 items.py 中的 CarItem类 做实例化
            item = CarItem()
            item['name'] = li.xpath('./a/@title').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['href'] = li.xpath('./a/@href').get()

            yield item

        # 生成下一页的URL地址，交给调度器入队列
        if self.o <= 5:
            self.o += 1
            next_page_url = 'https://www.guazi.com/bj/buy/o{}/#bread'.format(self.o)
            yield scrapy.Request(url=next_page_url, callback=self.parse)












