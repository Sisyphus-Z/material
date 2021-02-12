"""
猫眼电影top100数据抓取 - MYSQL数据库
流程:
    1、在 __init__当中连接数据库
    2、在 save_html() 中存入数据
    3、在 run()函数中 断开数据库链接
"""
import requests
import re
import time
import random
import pymysql

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'Cookie' : '__mta=146701579.1596764111175.1596764120480.1596764123646.5; uuid_n_v=v1; uuid=3874F860D84E11EABF2811F0086C462EE17B71210148427B88FD81F76AE3254F; _csrf=6a841a43819af0d789743e23e05c8e7f5e227d59d9953cd757deb08d8adfbdf1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1596764111; _lxsdk_cuid=173c68ec014c8-0ea3158fd846cb-3c634103-100200-173c68ec01571; _lxsdk=3874F860D84E11EABF2811F0086C462EE17B71210148427B88FD81F76AE3254F; mojo-uuid=ce74c1869b6a9e60f819699b37ff8527; mojo-session-id={"id":"2a89fd1a8b7bda5eccbfc1e59611aeb7","time":1596764110954}; __mta=146701579.1596764111175.1596764111175.1596764112202.2; mojo-trace-id=8; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1596764124; _lxsdk_s=173c68ead38-30d-a54-777%7C%7C13',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        # 创建数据库连接对象和游标对象
        self.db = pymysql.connect('localhost', 'root', '123456', 'maoyandb', charset='utf8')
        self.cur = self.db.cursor()

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
        # rt: ('大圣娶亲','周星驰','1993-01-01')
        ins = 'insert into maoyantab values(%s,%s,%s)'
        for rt in r_list:
            li = [
                rt[0].strip(),
                rt[1].strip(),
                rt[2].strip()
            ]
            self.cur.execute(ins, li)
            self.db.commit()
            print(li)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(url=page_url)
            # 控制频率
            time.sleep(random.randint(1,2))
        # 所有页的数据抓取完成后,断开数据库连接
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()





















