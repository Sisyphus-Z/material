"""
豆瓣电影电影信息数据抓取
思路:
    1、右键-查看网页源代码，搜索关键字，发现电影数据不存在！！
    2、F12抓包，刷新页面并滚动鼠标滑轮
    3、通过XHR中, Preview预览锁定返回具体数据的网络数据包
    4、点开 Headers, General->Request URL(返回实际数据的json地址)
    5、点开 Query String Parameters 查看查询参数的规律
       5.1> 查询参数中只有 start 的值在变, 0 20 40 60 ...
"""
import requests
import time
import random
from fake_useragent import UserAgent
import json
import re

class DoubanSpider:
    def __init__(self):
        # url: F12抓包抓到的 Headers-General-Request URL
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        # 打开文件
        self.f = open('douban.json', 'w')
        self.all_list = []

    def get_html(self, url):
        """请求功能函数"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).text

        return html

    def parse_html(self, url):
        # 提示: html = json.loads(html)
        # html: [{}, {}, {}, ...{}]
        html = json.loads(self.get_html(url=url))
        for one_film_dict in html:
            item = {}
            item['rank'] = one_film_dict['rank']
            item['name'] = one_film_dict['title']
            item['score'] = one_film_dict['score']
            item['time'] = one_film_dict['release_date']
            print(item)
            # 把item字典添加到 self.all_list 中，用于 json.dump()
            self.all_list.append(item)

    def get_all_type_dict(self):
        """获取所有类别以及对应的type的值的字典"""
        all_type_url = 'https://movie.douban.com/chart'
        all_type_html = self.get_html(url=all_type_url)
        regex = '<span><a href=".*?type_name=(.*?)&type=(.*?)&interval_id=100:90&action=">'
        pattern = re.compile(regex, re.S)
        # r_list: [('剧情','5'),('喜剧','24'),('爱情','13')...]
        r_list = pattern.findall(all_type_html)
        all_type_dict = {}
        for r in r_list:
            all_type_dict[r[0]] = r[1]

        return all_type_dict

    def get_total(self, typ):
        """获取某个类别下电影的总数量"""
        total_url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(typ)
        total_html = json.loads(self.get_html(url=total_url))
        total = total_html['total']

        return total

    def run(self):
        all_type_dict = self.get_all_type_dict()
        # 根据用户输入的t拿到t类别下对应的 type 的值 {'剧情':'5', '喜剧':'24',...}
        menu = ''
        for k in all_type_dict:
            menu = menu + k + '|'
        print(menu)
        t = input('请输入电影类别:')
        # total: 获取某个类别下电影的总数量
        total = self.get_total(all_type_dict[t])
        for start in range(0, total, 20):
            page_url = self.url.format(all_type_dict[t], start)
            self.parse_html(url=page_url)
            # 控制频率
            time.sleep(random.uniform(0,2))

        # 所有数据抓取完成后，保存到douban.json文件中
        json.dump(self.all_list, self.f, ensure_ascii=False)
        self.f.close()

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()















