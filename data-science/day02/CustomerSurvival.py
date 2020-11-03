# CustomrSurvival.py   中国联通用户流失情况分析
import numpy as np

# 加载数据
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

# 统计流失用户与未流失用户的占比
loss_data = data[data['loss']==1]
unloss_data = data[data['loss']==0]
print('流失用户比例：', len(loss_data) / len(data))
print('未流失用户比例：', len(unloss_data) / len(data))

# 分析一下额外通话时长
print('流失用户剩余通话时长（平均）：', 
        loss_data['extra_time'].mean())
print('未流失用户剩余通话时长（平均）：', 
        unloss_data['extra_time'].mean())

# 分析一下额外流量
print('流失用户剩余流量（平均）：', 
        loss_data['extra_flow'].mean())
print('未流失用户剩余流量（平均）：', 
        unloss_data['extra_flow'].mean())

# 分析套餐类型   pack_type
types = set(data['pack_type'])
print("套餐类型:", types)
for type in types:
    # 获取每种类型的数据量，看一下占比
    sub_data = data[data['pack_type']==type]
    print('type:', type, ', 占比：', len(sub_data)/len(data))
    loss_data = sub_data[sub_data['loss']==1]
    unloss_data = sub_data[sub_data['loss']==0]
    print('  流失用户占比:', len(loss_data)/len(sub_data))
    print('  未流失用户占比:', len(unloss_data)/len(sub_data))

# 分析套餐改变行为对流失率的影响 pack_change
types = set(data['pack_change'])
print("套餐改变行为:", types)
for type in types:
    # 获取每种类型的数据量，看一下占比
    sub_data = data[data['pack_change']==type]
    print('type:', type, ', 占比：', len(sub_data)/len(data))
    loss_data = sub_data[sub_data['loss']==1]
    unloss_data = sub_data[sub_data['loss']==0]
    print('  流失用户占比:', len(loss_data)/len(sub_data))
    print('  未流失用户占比:', len(unloss_data)/len(sub_data))

# 分析关联购买 asso_pur 与 集团用户 group_user 对流失率的影响
types = set(data['asso_pur'])
print("关联购买行为:", types)
for type in types:
    # 获取每种类型的数据量，看一下占比
    sub_data = data[data['asso_pur']==type]
    print('type:', type, ', 占比：', len(sub_data)/len(data))
    loss_data = sub_data[sub_data['loss']==1]
    unloss_data = sub_data[sub_data['loss']==0]
    print('  流失用户占比:', len(loss_data)/len(sub_data))
    print('  未流失用户占比:', len(unloss_data)/len(sub_data))

types = set(data['group_user'])
print("集团用户:", types)
for type in types:
    # 获取每种类型的数据量，看一下占比
    sub_data = data[data['group_user']==type]
    print('type:', type, ', 占比：', len(sub_data)/len(data))
    loss_data = sub_data[sub_data['loss']==1]
    unloss_data = sub_data[sub_data['loss']==0]
    print('  流失用户占比:', len(loss_data)/len(sub_data))
    print('  未流失用户占比:', len(unloss_data)/len(sub_data))

