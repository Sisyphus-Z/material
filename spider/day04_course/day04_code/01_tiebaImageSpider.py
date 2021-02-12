import requests
from lxml import etree
from urllib import parse
import time
import random

class TiebaImageSpider:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

    def get_html(self, url):
        """功能函数1: 请求获取html"""
        html = requests.get(url=url, headers=self.headers).content.decode('utf-8', 'ignore')

        return html

    def xpath_func(self, html, x):
        """功能函数2: xpath解析"""
        p = etree.HTML(html)
        r_list = p.xpath(x)

        return r_list

    def parse_html(self, one_url):
        """爬虫逻辑函数"""
        # 一级页面:提取50个帖子的链接
        one_html = self.get_html(url=one_url)
        one_x = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        href_list = self.xpath_func(one_html, one_x)
        for href in href_list[:-1]:
            tlink = 'https://tieba.baidu.com' + href
            # 把tlink这个帖子中所有图片保存到本地
            self.get_images(tlink)

    def get_images(self, tlink):
        """把1个帖子中所有的图片保存到本地"""
        t_html = self.get_html(url=tlink)
        # xpath表达式中的或 | 用法
        t_x = '//img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        img_link_list = self.xpath_func(t_html, t_x)
        for img_link in img_link_list:
            # 保存1张图片到本地
            self.save_image(img_link)
            time.sleep(random.uniform(0, 1))

    def save_image(self, img_link):
        """保存1张图片到本地文件"""
        img_html = requests.get(url=img_link, headers=self.headers).content
        filename = img_link[-10:]
        with open(filename, 'wb') as f:
            f.write(img_html)
        print(filename,'下载成功')

    def run(self):
        """程序入口函数"""
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        params = parse.quote(name)
        for page in range(start, end+1):
            pn = (page - 1) * 50
            page_url = self.url.format(params, pn)
            self.parse_html(page_url)

if __name__ == '__main__':
    spider = TiebaImageSpider()
    spider.run()





































