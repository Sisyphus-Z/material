from threading import Thread

# def f1():
#     print('看不见你的笑我怎么睡的着')
#
# t_list = []
# for i in range(5):
#     t = Thread(target=f1)
#     t.start()
#
# for t in t_list:
#     t.join()

from threading import Lock

n = 5000
lock = Lock()

def f1():
    global n
    for i in range(1000000):
        lock.acquire()
        n += 1
        lock.release()

def f2():
    global n
    for i in range(1000000):
        lock.acquire()
        n -= 1
        lock.release()

t1 = Thread(target=f1)
t1.start()

t2 = Thread(target=f2)
t2.start()

t1.join()
t2.join()

print(n)

"""
一次 加1 和 减1 操作 （正常）
x = n + 1    # x=5001
n = x        # n=5001
x = n - 1    # x=5000
n = x        # n=5000


一次 加1 和 减1 操作 （不正常）
x = n + 1     # x=5001
x = n - 1     # x=4999
n = x         # n=4999
n = x         # n=4999
"""















