'''杨辉三角金字塔v1.0'''
res = []
#绘制前九行的杨辉三角列表
for x in range(9):
    #前两行，分别为[1], [1, 1]
    if x == 0:
        res.append([1])
    elif x == 1:
        res.append([1, 1])
    #从第三行起，根据上一行确定本行内容
    else:
        #定义一个列表l，存放每行的数据
        l=[]
        l.append(1)
        for y in range(1,len(res[x - 1])):
            l.append(res[x - 1][y] + res[x - 1][y - 1])
        l.append(1)
        #每次循环把列表l添加到res列表中
        res.append(l)
#打印前九行杨辉三角列表
for x in res:
    print(x)
