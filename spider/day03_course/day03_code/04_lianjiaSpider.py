"""
    链家二手房数据抓取 - 一切以响应内容为主
"""
import requests
from lxml import etree
from fake_useragent import UserAgent

# 向第一页的URL地址发请求,获取响应内容
url = 'https://bj.lianjia.com/ershoufang/'
headers = {'User-Agent':UserAgent().random}
html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')

# xpath解析提取第一页的数据
p = etree.HTML(html)
li_list = p.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
for li in li_list:
    item = {}
    # 名称
    name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
    item['name'] = name_list[0].strip() if name_list else None
    # 地址
    address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
    item['address'] = address_list[0].strip() if address_list else None
    # 信息
    info_list = li.xpath('//div[@class="houseInfo"]/text()')
    item['info'] = info_list[0].strip() if info_list else None
    # 总价
    total_list = li.xpath('.//div[@class="totalPrice"]/span/text()')
    item['total'] = total_list[0].strip() if total_list else None
    # 单价
    unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
    item['unit'] = unit_list[0].strip()[2:-4] if unit_list else None

    print(item)
# 把数据存入MongoDB或者MySQL中


















