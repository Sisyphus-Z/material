import requests
from lxml import etree

# 帖子链接，想要提取帖子中视频的链接
url = 'https://tieba.baidu.com/p/6868131252'
headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
p = etree.HTML(html)
# 以响应内容为准来写xpath或者正则表达式
src_list = p.xpath('//div[@class="video_src_wrapper"]/embed/@data-video')

html = requests.get(url=src_list[0], headers=headers).content
with open('颖火虫.mp4', 'wb') as f:
    f.write(html)






