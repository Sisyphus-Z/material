"""
    有道翻译实现 - selenium
"""
from selenium import webdriver
import time

class YdSpider:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/'
        # 设置无界面
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        # 打开有道翻译首页
        self.driver.get(url=self.url)

    def parse_html(self, word):
        text_node = self.driver.find_element_by_xpath('//*[@id="inputOriginal"]')
        text_node.send_keys(word)
        # 给页面元素加载预留时间
        time.sleep(1)
        result_node = self.driver.find_element_by_xpath('//*[@id="transTarget"]/p/span')
        result = result_node.text

        return result

    def run(self):
        word = input('请输入要翻译的单词：')
        result = self.parse_html(word)
        print(result)
        self.driver.quit()

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()


















