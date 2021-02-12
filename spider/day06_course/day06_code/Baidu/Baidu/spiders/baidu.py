# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # response: http://www.baidu.com/给我们的响应对象
        # xpath()结果: [<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]
        # extract()结果: ['百度一下,你就知道']
        # extract_first()结果: '百度一下,你就知道'
        # get()结果: '百度一下,你就知道' 等同于 extract_first()
        result = response.xpath('/html/head/title/text()').get()
        print(result)









