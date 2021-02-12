import requests
from lxml import etree
from fake_useragent import UserAgent
import re

class MzbSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers = {'User-Agent':UserAgent().random}

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text

        return html

    def xpath_func(self, html, x):
        p = etree.HTML(html)
        r_list = p.xpath(x)

        return r_list

    def parse_html(self):
        # 1、提取最新月份的href
        html = self.get_html(url=self.url)
        x = '//table/tr[1]/td[2]/a/@href'
        href_list = self.xpath_func(html, x)
        detail_url = 'http://www.mca.gov.cn' + href_list[0]
        # 获取具体数据的函数
        self.get_data(detail_url)

    def get_data(self, detail_url):
        # 从detail_html中提取真实的JS跳转后的链接
        detail_html = self.get_html(url=detail_url)
        regex = 'window.location.href="(.*?)"'
        pattern = re.compile(regex, re.S)
        really_url = pattern.findall(detail_html)[0].strip()
        # 获取具体数据的函数,因为我有了js跳转之后的url地址
        self.get_really_data(really_url)

    def get_really_data(self, really_url):
        really_html = self.get_html(url=really_url)
        really_xpath = '//tr[@height=19]'
        tr_list = self.xpath_func(really_html, really_xpath)
        print(tr_list)
        for tr in tr_list:
            item = {}
            item['code'] = tr.xpath('./td[2]/text() | ./td[2]/span/text()')[0].strip()
            item['name'] = tr.xpath('./td[3]/text()')[0].strip()
            print(item)

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()






