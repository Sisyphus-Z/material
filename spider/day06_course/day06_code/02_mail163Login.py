"""
    因为iframe节点中id的属性值每次在变,所以我们不能使用id去查找
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://mail.163.com/')
# 切换iframe: xpath表达式要手写
iframe_node = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(iframe_node)

# 用户名 密码 登录
driver.find_element_by_name('email').send_keys('wangweichao_2020')
driver.find_element_by_name('password').send_keys('zhanshen001')
driver.find_element_by_id('dologin').click()













