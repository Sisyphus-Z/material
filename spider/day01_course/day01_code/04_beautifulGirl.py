"""
把赵丽颖图片保存到本地
"""
import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596617772589&di=3ae05eaa1f0f5bf6aee44734bde16921&imgtype=0&src=http%3A%2F%2Fimg.ylq.com%2F2016%2F0411%2F20160411085540352.png'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
# 1、请求获取bytes数据类型
html = requests.get(url=url, headers=headers).content

# 2、将图片保存到本地
with open('girl.jpg', 'wb') as f:
    f.write(html)

















