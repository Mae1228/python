'''杨辉三角金字塔v2.0-工程包'''
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
#利用制表符调整打印格式

