# demo02_dtype.py  numpy的数据类型
import numpy as np

data=[('zs', [90, 80, 85], 15),
        ('ls', [92, 81, 83], 16),
        ('ww', [95, 85, 95], 15)]

# 创建ndarray时，指定dtype
ary = np.array(data, dtype='U2, 3int32, int32')
print(ary[0])
print(ary['f0'])

# 第二种设置dtype的方式
ary = np.array(data, dtype=[('name', 'str', 2), 
                        ('scores', 'int32', 3), 
                        ('age', 'int32', 1)])
print(ary)
print(ary['age'])

# 第三种设置dtype的方式
ary = np.array(data, dtype={
    'names':['name', 'scores', 'age'],
    'formats':['U2', '3int32', 'float64']
})
print(ary[1]['age'])
print(ary['age'].mean())   # ndarray.mean() 返回平均值

# 测试日期数据
f = np.array(['2011', '2012-01-01', 
              '2013-01-01 01:01:01','2011-02-01'])
dates = f.astype('M8[D]')
print(dates, dates.dtype)

d = dates[0] - dates[-1]
print(d, type(d))