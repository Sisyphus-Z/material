"""
    豆瓣图书top250抓取
"""
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
import pymongo

class DoubanBookSpider:
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'
        # 创建3个对象
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['doubandb']
        self.myset = self.db['doubanset']

    def get_html(self, url):
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).content.decode('utf-8','ignore')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """lxml+xpath解析提取数据"""
        p = etree.HTML(html)
        table_list = p.xpath('//table')
        for table in table_list:
            item = {}
            name_list = table.xpath('.//div[@class="pl2"]/a/@title')
            item['name'] = name_list[0].strip() if name_list else None

            info_list = table.xpath('.//p[@class="pl"]/text()')
            info_list = info_list[0].split('/')
            if len(info_list) >= 4:
                item['price'] = info_list[-1].strip()
                item['year'] = info_list[-2].strip()
                item['shop'] = info_list[-3].strip()
                item['author'] = ' '.join(info_list[:-3])
            else:
                item['price'] = item['year'] = item['shop'] = item['author'] = None

            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            item['score'] = score_list[0].strip() if score_list else None

            commit_list = table.xpath('.//span[@class="pl"]/text()')
            item['commit'] = commit_list[0][1:-1].strip()[:-3] if commit_list else None

            comment_list = table.xpath('.//span[@class="inq"]/text()')
            item['comment'] = comment_list[0].strip() if comment_list else None

            print(item)
            self.myset.insert_one(item)

    def run(self):
        for page in range(1, 11):
            start = (page - 1) * 25
            page_url = self.url.format(start)
            self.get_html(url=page_url)
            # 控制频率
            time.sleep(random.uniform(1,3))

if __name__ == '__main__':
    spider = DoubanBookSpider()
    spider.run()






















