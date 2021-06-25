'''我的自创函数-成果包'''

#模拟range()函数基础功能
def myrange(start, stop, step = 1):
    res = []
    while start < stop:
        res.append(start)
        start += step
    return res
#生成0-15自然序列
for x in myrange(0, 16):
    print(x)
#生成2-16偶数序列
for x in myrange(2, 17, 2):
    print(x)
