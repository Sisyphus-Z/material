"""
    selenium操作鼠标
"""
from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains
import time

# 1、打开浏览器,输入百度
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='http://www.baidu.com/')

# 2、找到右上角 设置 节点
set_node = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')

# 3、鼠标移动到右上角的 设置 节点
ActionChains(driver).move_to_element(to_element=set_node).perform()

# 重要: 给页面元素的加载预留时间
time.sleep(0.5)

# 4、找到 高级搜索 节点,并点击
driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[2]').click()





























