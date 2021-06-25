'''函数制造者-练习三'''

tpl = (1, 4, -5, 64, 78, 12, 0, 3, 3.5, 3)

# 最大值函数
def mymax(x):
    m = x[0]
    for i in x:
        if i > m:
            m = i
    return m
    
# 最小值函数
def mymin(x):
    m = x[0]
    for i in x:
        if i < m:
            m = i
    return m

# 定义排序函数
def mysorted(y, reverse=False):
    y = list(y)
    # 结果列表
    s = []
    # 默认升序排序
    if reverse == False:
        while y:
            # 调用最小值函数
            m = mymin(y)
            y.remove(m)
            s.append(m)
    # 降序排序
    else:
        while y:
            # 调用最大值函数
            m = mymax(y)
            y.remove(m)
            s.append(m)
    return s

# 调用排序函数
res1 = mysorted(tpl)
res2 = mysorted(tpl, True)
print('升序排列：'+str(res1))
print('降序排列：'+str(res2))

