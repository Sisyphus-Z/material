"""
1、输入贴吧名称: 赵丽颖吧
2、输入起始页: 1
3、输入终止页: 2
4、保存到本地文件：赵丽颖吧_第1页.html、赵丽颖吧_第2页.html
"""
import requests
from urllib import parse
import time
import random

class BaiduSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}

    def get_html(self, url):
        """请求功能函数: 发请求获取响应内容html"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def parse_html(self):
        """解析功能函数: 解析提取数据(此案例不用)"""
        pass

    def save_html(self, filename, html):
        """数据处理函数"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def run(self):
        """程序入口函数: 整体的逻辑调控"""
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        # 编码（quote)
        params = parse.quote(name)
        for page in range(start, end+1):
            pn = (page - 1) * 50
            page_url = self.url.format(params, pn)
            # 请求 + 解析 + 数据处理
            html = self.get_html(url=page_url)
            filename = '{}_第{}页.html'.format(name, page)
            self.save_html(filename, html)
            print('第%d页抓取完成' % page)
            # 控制数据抓取的频率
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()



















