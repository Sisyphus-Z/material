"""
    小米应用商店多线程抓取
"""
import requests
import json
from threading import Thread,Lock
from queue import Queue
import time
from fake_useragent import UserAgent

class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.q = Queue()
        self.lock = Lock()

    def url_in(self):
        """先让URL地址入队列"""
        for page in range(67):
            page_url = self.url.format(page)
            # 瞬间产生67个URL地址,入队列
            self.q.put(page_url)

    def get_html(self, url):
        """功能函数"""
        headers = {'User-Agent':UserAgent().random}
        html = requests.get(url=url, headers=headers).text

        return html

    def parse_html(self):
        """线程事件函数: 请求+解析+数据处理"""
        while True:
            # 加锁
            self.lock.acquire()
            if not self.q.empty():
                page_url = self.q.get()
                # 释放锁
                self.lock.release()
                html = json.loads(self.get_html(url=page_url))
                for one_app_dict in html['data']:
                    item = {}
                    item['app_name'] = one_app_dict['displayName']
                    item['app_link'] = one_app_dict['packageName']
                    print(item)
            else:
                # 释放锁
                self.lock.release()
                break

    def run(self):
        # URL地址入队列
        self.url_in()
        # 创建多线程
        t_list = []
        for i in range(5):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()

if __name__ == '__main__':
    start_time = time.time()
    spider = XiaomiSpider()
    spider.run()
    end_time = time.time()
    print('time:%.2f' % (end_time - start_time))
























