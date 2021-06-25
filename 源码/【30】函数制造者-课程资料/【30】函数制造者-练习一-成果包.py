'''函数制造者-练习一'''

tpl = (1, 4, -5, 64, 78, 12, 0, 3, 3.5, 3)
# 定义最大值函数
def mymax(x):
    m = x[0]
    for i in x:
        if i > m:
            m = i
    return m
# 调用最大值函数
res = mymax(tpl)
print('最大值是：'+str(res))
