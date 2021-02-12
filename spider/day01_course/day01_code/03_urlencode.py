"""
输入搜索关键字,保存页面到本地文件
"""
import requests
from urllib import parse

# 1、拼接URL地址 : http://www.baidu.com/s?wd=???
keyword = input('请输入搜索关键字:')
params = parse.urlencode( {'wd':keyword} )
url = 'http://www.baidu.com/s?{}'.format(params)

# 2、发请求获取响应
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
html = requests.get(url=url, headers=headers).text

# 3、保存数据
filename = '{}.html'.format(keyword)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)


















