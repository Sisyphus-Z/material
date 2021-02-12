"""
建立私密代理的代理IP池
思路：
    1、提取私密代理
    2、依次测试，把能用的代理IP保存
"""
import requests
import pymysql

class ProxyPool:
    def __init__(self):
        self.api_url = 'http://dps.kdlapi.com/api/getdps/?orderid=999687602367746&num=20&pt=1&sep=1'
        self.test_url = 'http://httpbin.org/get'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # 2个对象
        self.db = pymysql.connect('localhost', 'root', '123456', 'proxydb', charset='utf8')
        self.cur = self.db.cursor()

    def get_proxy(self):
        """获取代理ip并测试"""
        html = requests.get(url=self.api_url, headers=self.headers).content.decode('utf-8', 'ignore')
        # proxy_list: ['1.1.1.1:8888','1.1.1.2:9999',...]
        proxy_list = html.split('\r\n')
        for proxy in proxy_list:
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        """测试一个代理IP是否可用:proxy(1.1.1.1:8888)"""
        ins = 'insert into proxy_tab values(%s,%s)'
        proxies = {
            'http' : 'http://309435365:szayclhp@{}'.format(proxy),
            'https': 'https://309435365:szayclhp@{}'.format(proxy),
        }
        try:
            resp = requests.get(url=self.test_url, proxies=proxies,headers=self.headers, timeout=3)
            if resp.status_code == 200:
                print(proxy,'\033[31m可用\033[0m')
                # 把能用的代理IP存入mysql数据库
                self.cur.execute(ins, proxy.split(':'))
                self.db.commit()
            else:
                print(proxy,'不可用')
        except:
            print(proxy, '不可用')

    def run(self):
        self.get_proxy()

if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()





















