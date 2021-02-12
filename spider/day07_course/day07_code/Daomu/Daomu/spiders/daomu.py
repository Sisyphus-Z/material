# -*- coding: utf-8 -*-
import scrapy
import os
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        """一级页面解析函数: 提取大标题和大链接"""
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            # 创建item对象
            item = DaomuItem()
            parent_title = a.xpath('./text()').get()
            parent_url = a.xpath('./@href').get()
            item['directory'] = './novel/' + parent_title
            # 创建对应目录
            if not os.path.exists(item['directory']):
                os.makedirs(item['directory'])
            # 把详情页链接交给调度器入队列
            yield scrapy.Request(url=parent_url,meta={'meta1':item},callback=self.parse_two_page)

    def parse_two_page(self, response):
        """二级页面解析函数: 提取小标题和小链接"""
        # meta1: {'directory':'./novel/盗墓笔记1:'}
        meta1 = response.meta['meta1']
        article_list = response.xpath('//article')
        for article in article_list:
            # 只要有继续交往调度器的请求,我们就必须创建item对象
            item = DaomuItem()
            item['son_title'] = article.xpath('./a/text()').get()
            son_url = article.xpath('./a/@href').get()
            item['directory'] = meta1['directory']

            yield scrapy.Request(
                url=son_url,
                meta={'item':item},
                callback=self.parse_three_page
            )

    def parse_three_page(self, response):
        """三级页面解析函数: 提取具体小说内容"""
        item = response.meta['item']
        # extract()之后p_list: ['段落1','段落2','段落3', ... ...]
        p_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['content'] = '\n'.join(p_list)

        # 至此,一条完整的数据提取完成，交给管道文件处理
        yield item

























