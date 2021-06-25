'''杨辉三角金字塔v3.0'''
res = []
for x in range(9):
    if x == 0:
        res.append([1])
    elif x == 1:
        res.append([1, 1])
    else:
        l = []
        for y in range(len(res[x - 1])):
            if y == 0:
                l.append(1)
            else:
                l.append(res[x - 1][y] + res[x - 1][y - 1])
        l.append(1)
        res.append(l)
#使用center()函数调整输出造型
for x in res:
    ret = ''
    for y in x:
        ret += (str(y) + '   ')
    print(ret.center(60))
