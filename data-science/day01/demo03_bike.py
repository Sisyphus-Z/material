# demo03_bike.py  共享单车数据分析
import numpy as np

# 加载数据
with open('../data/bike_day.csv', 'r') as f:
    data = []
    for i, line in enumerate(f.readlines()):
        if i==0:
            header = line[:-1].split(',')
        else:
            data.append(tuple(line[:-1].split(',')))
    # 把data转成ndarray
    data = np.array(data, dtype={
        'names':header,
        'formats':['i4','U15','i4','i4','i4','i4','i4',
            'i4','i4','f8','f8','f8','f8','i4','i4','i4']
    })

# 输出并分析data的维度
print(data.shape)
# 输出前10行数据
print(data[:10])

# 获取周一的数据
print(data[data['weekday']==1])
# 求 节假日天数的占比   holiday
holidays = data[data['holiday']==1]
print(len(holidays) / len(data))
# 求 共享单车使用量>3000辆 的天数占比