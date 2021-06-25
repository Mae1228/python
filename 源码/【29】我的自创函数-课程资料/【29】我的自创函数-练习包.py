'''我的自创函数-练习包'''

#自定义函数基本构成语句
def myfunc():
    print('执行我的第一个函数')

myfunc()

#自定义函数———位置参数
def myadd(a, b):
    print(a + b)

myadd(100, 33)

#自定义函数———返回值
def myadd(a,b):
    return a + b

res = myadd(100,33)
print(res)

