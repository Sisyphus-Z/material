from selenium import webdriver

# 设置无界面模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# 浏览器最大化
driver.maximize_window()
driver.get('https://maoyan.com/board/4')

def get_one_page():
    # 基准xpath: 匹配所有电影信息的dd节点对象列表
    dd_list = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for dd in dd_list:
        item = {}
        # text属性: 获取当前节点以及子节点和后代节点的文本内容
        info_list = dd.text.split('\n')
        item['rank'] = info_list[0].strip()
        item['name'] = info_list[1].strip()
        item['star'] = info_list[2].strip()
        item['time'] = info_list[3].strip()
        item['score'] = info_list[4].strip()

        print(item)

while True:
    get_one_page()
    # selenium查找节点时，如果找不到会抛出异常
    try:
        driver.find_element_by_link_text('下一页').click()
    except:
        driver.quit()
        break
















