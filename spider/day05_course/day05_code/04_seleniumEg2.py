"""
打开浏览器 - 输入百度 - 搜索框输入 赵丽颖 - 点击 百度一下 按钮
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

# 找到搜索框节点,并发送关键字: 赵丽颖
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
# 找到 百度一下 按钮节点,点击
driver.find_element_by_xpath('//*[@id="su"]').click()


# 关闭浏览器
driver.quit()

















