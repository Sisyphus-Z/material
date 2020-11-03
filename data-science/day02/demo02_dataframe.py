# demo02_dataFrame.py  DataFrame示例
import numpy as np
import pandas as pd

df = pd.DataFrame()
print(df)
# 通过列表创建DataFrame
ary = np.array([1,2,3,4,5])
df = pd.DataFrame(ary)
print(df, df.shape)
data = [ ['Alex',10],['Bob',12],('Clarke',13) ]
df = pd.DataFrame(data, index=['s1', 's2', 's3'], 
                    columns=['Name', 'Age'])
print(df)

# 通过字典创建DataFrame
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],
        'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
print(df)
# 细节
data = {'Name':pd.Series(['Tom','Jack','Steve','Ricky']),
        'Age':pd.Series([28,34,29], index=[1,2,3]) }
df = pd.DataFrame(data)
print(df)
print(df.index)
print(df.columns)
print(df.head(2))  # 头两行
print(df.tail(2))  # 后两行


# 列的访问
print('-' * 40)
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([1, 3, 4], index=['a', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print(df[df.columns[:-1]])

# 列的添加
print(df)
df['four'] = pd.Series([15,43,12],index=['a','d','c'])
print(df)

# 列的删除
print(df.drop(['three', 'four'], axis=1))

# 行的访问
print(df)
print(df.loc['b'])
print(df.loc[['b','c']])
print(df.loc['b':'d'])
print(df.iloc[1])
print(df.iloc[[1, 2]])
print(df.iloc[1:])

# 行的添加
print(df)
# 向df中添加一行 
newdf = pd.DataFrame([[10, 20, 30, 40]],columns=df.columns)
df = df.append(newdf)
print(df)

# 行的删除 drop  axis=0
print(df.drop([0, 'd'], axis=0))

print('-' * 40)
# 读取上午的电信用户数据，
# 把pack_type, extra_flow, loss存入dataFrame, 获取前5行数据
with open('CustomerSurvival.csv', 'r') as f:
    data = []
    for i, line in enumerate(f.readlines()):
        row = tuple(line[:-1].split(','))
        data.append(row)
    # 转成ndarray
    data = np.array(data, dtype={
        'names':['index','pack_type','extra_time',
            'extra_flow','pack_change','contract',
            'asso_pur','group_user','use_month','loss'],
        'formats':['i4','i4','f8','f8','i4',
                   'i4','i4','i4','i4','i4']
    })

data = pd.DataFrame(data).head(10)
print(data)
# 瘦身： 只需要pack_type, extra_time, loss
sub_data = data[['pack_type', 'extra_time', 'loss']]
# 追加一列：extra_flow
sub_data['extra_flow'] = data['extra_flow']
# 选择所有未流失的数据行
sub_data = sub_data[sub_data['loss']!=1]
print(sub_data)
sub_data['extra_flow'][9] = 0
print(sub_data)

# 复合索引 
print('-' * 40)
# 生成一组(6,3)的随机数。要求服从期望=85，标准差=3的正态分布。
data = np.floor(np.random.normal(85, 3, (6,3)))
df = pd.DataFrame(data)
print(df)
# 设置行级标签索引为复合索引
index = [('A', 'M'), ('A', 'F'), ('B', 'M'), 
        ('B', 'F'), ('C', 'M'), ('C', 'F')]
df.index = pd.MultiIndex.from_tuples(index)
print(df)
columns = [('score','math'), ('score','reading'), 
            ('score', 'writing')]
df.columns = pd.MultiIndex.from_tuples(columns)
print(df)
# C班男生的信息：
print(df.loc['C','M'])
print(df.loc[['A', 'C']])
# 访问复合索引列
print(df['score','writing'])