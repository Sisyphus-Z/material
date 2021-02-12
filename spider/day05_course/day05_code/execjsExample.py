# 模块安装: sudo pip3 install pyexecjs
# 安装nodejs: sudo apt-get install nodejs

import execjs

with open('translate.js', 'r') as f:
    js_code = f.read()


execjs_object = execjs.compile(js_code)
result = execjs_object.eval('e("tiger")')

print(result)







