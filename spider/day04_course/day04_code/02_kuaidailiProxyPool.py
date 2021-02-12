import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import random

class KuaiProxyPool:
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.test_url = 'http://httpbin.org/get'

    def get_html(self, url):
        """功能函数1: 发请求获取html"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')

        return html

    def get_proxy(self, url):
        """爬虫逻辑函数"""
        html = self.get_html(url=url)
        p = etree.HTML(html)
        # 基准xpath,匹配所有的tr节点对象列表
        tr_list = p.xpath('//table/tbody/tr')
        for tr in tr_list:
            ip_list = tr.xpath('./td[1]/text()')
            ip = ip_list[0].strip() if ip_list else None
            port_list = tr.xpath('./td[2]/text()')
            port = port_list[0].strip() if port_list else None
            if ip and port:
                self.test_proxy(ip, port)
                time.sleep(random.uniform(0, 1))

    def test_proxy(self, ip, port):
        """测试一个代理IP是否可用"""
        proxies = {
            'http' : 'http://{}:{}'.format(ip, port),
            'https': 'https://{}:{}'.format(ip, port),
        }
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, timeout=3)
            if resp.status_code == 200:
                print(ip, port, '可用')
            else:
                print(ip, port, '不可用')
        except:
            print(ip, port, '不可用')

    def run(self):
        for page in range(1, 1001):
            page_url = self.url.format(page)
            self.get_proxy(url=page_url)

if __name__ == '__main__':
    spider = KuaiProxyPool()
    spider.run()

























