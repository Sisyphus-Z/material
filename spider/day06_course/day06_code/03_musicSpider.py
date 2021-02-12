"""
    网易云音乐排行榜数据抓取
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='https://music.163.com/#/discover/toplist')

# 切换iframe节点: id 和 name 两个属性值支持直接切换
driver.switch_to.frame('contentFrame')

# 基准xpath
tr_list = driver.find_elements_by_xpath('//table/tbody/tr')
for tr in tr_list:
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text
    item['name'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').replace('\xa0', '')
    item['time'] = tr.find_element_by_xpath('.//span[@class="u-dur "]').text
    item['author'] = tr.find_element_by_xpath('.//div[@class="text"]/span').get_attribute('title')

    print(item)

driver.quit()



























