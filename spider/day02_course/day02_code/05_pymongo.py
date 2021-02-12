"""
库: maoyandb
集合: maoyanset
插入一条文档: {'name':'喜剧之王', 'star':'张柏芝', 'time':'1995-01-01'}
"""
import pymongo

# 1、先连接到数据库: 创建数据库连接对象
conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
# 2、创建库对象
db = conn['maoyandb']
# 3、创建集合对象
myset = db['maoyanset']
# 4、插入文档
myset.insert_one({'name':'西游记之女儿国','star':'赵丽颖','time':'2019-01-01'})





















