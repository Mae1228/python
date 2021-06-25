'''我的自创函数-挑战包'''

#模拟range()函数基础功能
def myrange(start, stop, step=1):
    res = []
    while start < stop:
        res.append(start)
        start += step
    return res

x = myrange(0, 5)
print(x)
y = range(0, 5)
print(y)