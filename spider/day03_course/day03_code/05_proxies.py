"""
    免费代理ip测试
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
proxies = {
    'http' : 'http://113.195.152.190:9999',
    'https': 'https://113.195.152.190:9999'
}
html = requests.get(url=url, proxies=proxies, headers=headers).text
# 确认方法: 查看html中的origin中的IP地址是哪个
print(html)

















