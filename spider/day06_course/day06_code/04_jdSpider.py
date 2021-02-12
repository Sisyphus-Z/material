"""
    selenium爬取京东 爬虫书 商品数据
"""
from selenium import webdriver
import time
import pymongo

class JdSpider:
    def __init__(self):
        self.url = 'https://www.jd.com/'
        # 无界面模式
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        # 打开网站
        self.driver.get(url=self.url)
        # 搜索框节点  搜索按钮 两个节点
        self.driver.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
        self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        # 给页面跳转|加载预留时间
        time.sleep(1)
        # mongodb数据库
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['jddb']
        self.myset = self.db['jdset']

    def parse_html(self):
        """拉进度条到最底部,休眠,提取数据"""
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        # 休眠,给页面元素加载预留时间
        time.sleep(2)
        # 提取数据
        li_list = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            item = {}
            try:
                item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]/strong').text
                item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a').text
                item['comment'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text
                item['shop'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]/a').text
                print(item)
                self.myset.insert_one(item)
            except:
                pass

    def run(self):
        while True:
            self.parse_html()
            # 八个大字: 没有找到,返回-1
            if self.driver.page_source.find('pn-next disabled') == -1:
                self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
                # 休眠
                time.sleep(1)
            else:
                self.driver.quit()
                break

if __name__ == '__main__':
    spider = JdSpider()
    spider.run()


































