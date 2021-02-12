def f1():
    for i in range(2):
        yield i


g = f1()
print(next(g))
print(next(g))

# 1、进程  线程  协程(纤程、微线程)
# 2、yield语句就是实现协程的关键字
# 3、实现协程的模块: gevent greelet

# def f1():
#     xxxx
#     yield xxx
#
# def f2():
#     xxxx
#     yield xxx
#
# def f3():
#     xxxx
#     yield xxx














