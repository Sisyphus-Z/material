"""
    selenium模拟登录qq邮箱 - iframe
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://mail.qq.com/')

# 1、切换iframe
iframe_node = driver.find_element_by_id('login_frame')
driver.switch_to.frame(iframe_node)

# 2、寻找节点: QQ号  密码  登录按钮
driver.find_element_by_xpath('//*[@id="u"]').send_keys('11111121')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('32322321')
driver.find_element_by_xpath('//*[@id="login_button"]').click()


















