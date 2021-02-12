"""
向京东官网发请求,获取响应内容
"""
import requests

# 向网站发起请求,得到响应对象
resp = requests.get(url='https://www.jd.com/')
# 属性1: text 获取响应内容-字符串
html = resp.text
# 属性2: content 获取响应内容-字节串(bytes),主要用于抓取图片、音频、视频、文件...
html = resp.content
# 属性3: status_code  HTTP响应码
code = resp.status_code
# 属性4: url  返回实际数据的URL地址
url = resp.url























