#demo05_slice.py  索引操作
import numpy as np
a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])  # 1 2 3
print(a[3:6])   # 4 5 6
print(a[6:])  # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])  # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])  # 3 6 9

# 高维数组的切片
a = a.reshape(3, 3)
print(a)
print(a[:2, :2])
print(a[::2, ::2])

# 研究一下掩码：
a = np.arange(1, 10)
mask = [True, False, True, False, True, False, True, False, True]
print(a[mask])
# a[mask] = 10
# print(a)
# 输出1~100以内3的倍数
a = np.arange(1, 100)
print(a[a%3==0])
print(a[(a%3==0) & (a%7==0)])

# 索引掩码：
p = np.array(['Mi', 'Apple', 'Huawei', 'Oppo', 'Vivo'])
prices = [0, 4, 3, 2, 1, 2,2,2,2,2,2,2]
print(p[prices])