"""
猫眼电影top100数据抓取 - csv文件
流程:
    1、在 __init__ 中打开文件,并初始化写入对象
    2、在 save_html() 中数据存入
    3、在 run() 所有数据写入完成后，关闭文件
"""
import requests
import re
import time
import random
import csv

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'Cookie' : '__mta=176010909.1596620334596.1596764128202.1596764132799.11; uuid_n_v=v1; uuid=783FE7C0D6FF11EABDA91DE1C2FF63054B79E3644FC040D0BDD1512287BA416B; _csrf=38a08e8489c4ebe0eed75c3005cf00ee39c826e562a0feb680efa4d16e2cbf02; _lxsdk_cuid=173bdfce115c8-032a2bd594d29c-31760856-100200-173bdfce115c8; _lxsdk=783FE7C0D6FF11EABDA91DE1C2FF63054B79E3644FC040D0BDD1512287BA416B; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1596620333; mojo-uuid=062aaeb785e8e3d4241c9f12edbbc9ef; __mta=176010909.1596620334596.1596620334596.1596620336452.2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1596764133; _lxsdk_s=173c6c1e71f-19d-091-027%7C%7C1',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        # 打开文件 + 初始化写入对象
        self.f = open('maoyan.csv', 'w', newline='')
        self.writer = csv.writer(self.f)

    def get_html(self, url):
        """请求"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """正则提取数据"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        # r_list: [('大圣娶亲','周星驰','1993-01-01'),(),...()]
        r_list = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        for rt in r_list:
            li = [
                rt[0].strip(),
                rt[1].strip(),
                rt[2].strip()
            ]
            self.writer.writerow(li)
            print(li)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(url=page_url)
            # 控制频率
            time.sleep(random.randint(1,2))
        # 关闭文件
        self.f.close()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()





















