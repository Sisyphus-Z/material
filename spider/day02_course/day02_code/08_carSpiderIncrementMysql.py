"""
汽车之家二级页面数据抓取 - MySQL实现增量爬虫
create database cardb charset utf8;
use cardb;
create table request_finger(
finger char(32)
)charset=utf8;
"""
import requests
import re
import time
import random
from fake_useragent import UserAgent
import pymongo
import pymysql
from hashlib import md5
import sys

class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'
        # mongodb三个对象 - 实现数据存储
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['cardb']
        self.myset = self.db['carset']
        # mysql两个对象 - 实现增量
        self.mydb = pymysql.connect('localhost', 'root', '123456', 'cardb', charset='utf8')
        self.cur = self.mydb.cursor()

    def get_html(self, url):
        """功能函数1: 发请求获取到html"""
        headers = { 'User-Agent': UserAgent().random }
        # ignore: 解码过程中遇到不识别的字符直接忽略
        # UnicodeDecodeError: gb2312 code cannot decode character ...
        html = requests.get(url=url, headers=headers).content.decode('gb2312', 'ignore')

        return html

    def re_func(self, regex, html):
        """功能函数2: 正则解析"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    def md5_url(self, url):
        """功能函数3: 对url地址进行md5加密函数"""
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def is_spider(self, car_finger):
        """判断car_finger在表中是否存在"""
        sel = 'select * from request_finger where finger=%s'
        self.cur.execute(sel, [car_finger])
        # result: 要么是空元组  要么是非空元组
        result = self.cur.fetchall()
        if not result:
            return True
        return False

    def parse_html(self, one_url):
        """爬虫逻辑函数"""
        one_html = self.get_html(url=one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        # href_list: [ '/declar/xx','/declar/xx', .... ]
        href_list = self.re_func(one_regex, one_html)
        for href in href_list:
            two_url = 'https://www.che168.com' + href
            car_finger = self.md5_url(url=two_url)
            # is_spider()返回值:True,说明之前没抓取过（指纹表中不存在此条记录）
            # 返回值为False,说明之前已经抓取过了（指纹表中已经存在此条记录）
            if self.is_spider(car_finger):
                self.get_one_car_info(two_url)
                # 控制抓取频率: uniform(0, 1) 生成0到1之间的浮点数
                time.sleep(random.uniform(0, 2))
                # 抓完之后把指纹存入指纹表
                ins = 'insert into request_finger values(%s)'
                self.cur.execute(ins, [car_finger])
                self.mydb.commit()
            else:
                sys.exit('更新完成')

    def get_one_car_info(self, two_url):
        """获取一辆汽车的具体数据"""
        two_html = self.get_html(url=two_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b>'
        # car_info_list: [('BJD','2万公里','2016年6月','自动 / 20L','北京','2000万'),]
        car_info_list = self.re_func(two_regex, two_html)
        item = {}
        # 名字 + 行驶里程 + 上牌时间
        item['name'] = car_info_list[0][0].strip()
        item['km'] = car_info_list[0][1].strip()
        item['year'] = car_info_list[0][2].strip()
        # 类别 + 排量
        item['type'] = car_info_list[0][3].split('/')[0].strip()
        item['displace'] = car_info_list[0][3].split('/')[1].strip()
        # 地址 + 价格
        item['city'] = car_info_list[0][4].strip()
        item['price'] = car_info_list[0][5].strip()

        print(item)
        # 存入mongodb数据库
        self.myset.insert_one(item)

    def run(self):
        for page in range(1, 3):
            page_url = self.url.format(page)
            self.parse_html(page_url)

if __name__ == '__main__':
    spider = CarSpider()
    spider.run()

































