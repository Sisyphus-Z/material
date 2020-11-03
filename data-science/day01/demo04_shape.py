# demo04_shape.py 属性测试
import numpy as np

a = np.arange(1, 13)
print(a, a.shape)

# 视图变维
b = a.reshape(2, 6)
a[0] = 999
print(b)
print(b.ravel())
# 复制变维
print(a.flatten())
# 就地变维  (改变a数组本身的维度)
a.shape = (2,2,3)
a.resize(2,2,3)
print(a)