# demo01_numpy.py  
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(ary, type(ary))

# ndarray的运算
print(ary + ary)
print(ary * 3)
print(ary == 3)

# 对象的创建：
ary = np.array([[1,2,3],[4,5,6]])
print(ary, ary.shape)

b = np.arange(1, 11)
print(b)

c = np.zeros(10)
d = np.ones((2,5), dtype='float32')
print(c)
print(d)

print(np.ones(5) / 5)

print(np.ones_like(ary))
print(np.zeros_like(ary))

# ndarray属性的基本操作
ary = np.arange(1, 9)
# 维度
print(ary, ary.shape)
ary.shape = (2, 2, 2)
print(ary, ary.shape)
# 类型
print(ary, ary.dtype)
#ary.dtype = 'float32'
ary = ary.astype('float32') # 原数组不会变化，应该接收返回值数组
print(ary, ary.dtype)
# size
print(ary.size, len(ary))
# 索引
print(ary[0])
print(ary[0][0])
print(ary[0][0][0])
print(ary[1,1,0])

for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i,j,k])


