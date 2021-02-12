"""
    打开浏览器,输入百度
"""
from selenium import webdriver

# 1、创建浏览器对象 - 打开浏览器
driver = webdriver.Chrome()
# 浏览器窗口最大化
driver.maximize_window()
driver.get(url='http://www.baidu.com/')

# page_source: 查看HTML结构源码
html = driver.page_source

print(driver.page_source.find('ssssssssssssssss'))





















