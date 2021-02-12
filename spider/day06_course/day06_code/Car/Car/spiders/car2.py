# -*- coding: utf-8 -*-
import scrapy
from ..items import CarItem

class CarSpider(scrapy.Spider):
    name = 'car2'
    allowed_domains = ['www.guazi.com']
    # 1、去掉start_urls
    # 2、重写start_requests()方法
    def start_requests(self):
        """生成所有要抓取的URL地址,一次性交给调度器入队列"""
        for i in range(1, 7):
            url = 'https://www.guazi.com/bj/buy/o{}/#bread'.format(i)
            yield scrapy.Request(url=url, callback=self.detail_page)

    def detail_page(self, response):
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









