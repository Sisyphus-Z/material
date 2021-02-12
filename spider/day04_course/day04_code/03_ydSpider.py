"""
有道翻译破解
思路:
    1、F12刷新页面抓包
    2、Network-XHR-Preview找到了具体返回数据的网络数据包
    3、分析此数据包
       3.1> Headers-General 找到了 Request URL (post的地址)
       3.2> Headers-Requests Headers(请求头)
       3.3> Form Data 找到了Form表单的数据
    4、发现Form表单数据有加密
       4.1> 页面执行行为,分析对比加密的数据
       4.2> 找到相关JS，并分析查看JS代码（可能用到断点调试）
       4.3> Python按照相同的加密方式实现一遍
"""
import requests
import time
from hashlib import md5
import random

class YdSpider:
    def __init__(self):
        # post_url:一定要为F12抓包抓到的地址
        self.post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            # Cookie Referer User-Agent 检查频率最高的
            "Cookie": "OUTFOX_SEARCH_USER_ID=969922199@10.108.160.100; JSESSIONID=aaaT2kNDhaW8ia9pNCwpx; OUTFOX_SEARCH_USER_ID_NCOO=1913004122.8620024; ___rl__test__cookies=1597030696050",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }

    def get_ts_salt_sign(self, word):
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        # sign:
        string = "fanyideskweb" + word + salt + "]BjuETDhU)zqSxf-=B#7m"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    def attack_yd(self, word):
        ts, salt, sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": ts,
            "bv": "94ef9c063d6b2a801fab916722d70203",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # .json(): 直接把json格式的字符串 转为 Python数据类型
        html = requests.post(url=self.post_url, data=data, headers=self.headers).json()
        result = html['translateResult'][0][0]['tgt']

        return result

    def run(self):
        word = input('请输入要翻译的单词:')
        print(self.attack_yd(word))

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()









