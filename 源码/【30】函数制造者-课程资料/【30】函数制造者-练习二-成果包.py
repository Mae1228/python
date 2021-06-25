'''函数制造者-练习二'''

tpl = (1, 4, -5, 64, 78, 12, 0, 3, 3.5, 3)
# 定义最小值函数
def mymin(x):
    m = x[0]
    for i in x:
        if i < m:
            m = i
    return m
# 调用最小值函数
res = mymin(tpl)
print('最小值是：'+str(res))
