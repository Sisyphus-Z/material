"""
猫眼电影top100数据抓取
流程:
    1、右键 - 查看网页源代码 - 搜索关键字是否存在
    2、存在的情况下，查看URL地址的规律
    3、尝试写正则表达式
    4、写代码
"""
import requests
import time
import random
from lxml import etree

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'Cookie' : '__mta=146701579.1596764111175.1596793240236.1596849950241.12; uuid_n_v=v1; uuid=3874F860D84E11EABF2811F0086C462EE17B71210148427B88FD81F76AE3254F; _lxsdk_cuid=173c68ec014c8-0ea3158fd846cb-3c634103-100200-173c68ec01571; _lxsdk=3874F860D84E11EABF2811F0086C462EE17B71210148427B88FD81F76AE3254F; mojo-uuid=ce74c1869b6a9e60f819699b37ff8527; _csrf=9286414242fce42b033f2791933f3b14e946bc471ab15766d5129f10fb1ecbf1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1596764111,1596793228,1596849942; __mta=146701579.1596764111175.1596793240236.1596849943865.12; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1596849950; _lxsdk_s=173cc099055-d18-0ba-62e%7C%7C1',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

    def get_html(self, url):
        """请求"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """lxml+xpath提取数据"""
        p = etree.HTML(html)
        # 1、基准xpath，匹配每个电影的dd节点对象列表
        # dd_list: [<element dd at xxx>, <element dd at xxx>, ...]
        dd_list = p.xpath('//dl/dd')
        for dd in dd_list:
            item = {}
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()')[0]
            item['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0]

            print(item)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(url=page_url)
            # 控制频率
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()





















