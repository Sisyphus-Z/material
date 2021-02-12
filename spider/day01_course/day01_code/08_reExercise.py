import re

html = """
<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>
    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>
<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small white rabbit white and white
    </p>
</div>
"""
regex = '<div class="animal">.*?<a title="(.*?)".*?<p class="content">(.*?)</p>'
pattern = re.compile(regex, re.S)
r_list = pattern.findall(html)
for rt in r_list:
    print('动物名称:',rt[0])
    print('动物描述:',rt[1].strip())
    print('*' * 50)











