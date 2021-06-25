'''杨辉三角完形挑战-工程包'''
#杨辉三角单行生成
#前三行
# list0 = [1]
# list1 = [1, 1]
# list2 = [1, 2, 1]
#第四行
list3 = [1, 3, 3, 1]
#第五行
list4 = []
#根据第四行，生成第五行

    #每行第一个元素是1，直接加到空列表里

    #从每行第二个元素开始，按规律进行计算

#每行最后一个元素是1，直接加到列表末尾

#打印第五行
print(list4)

'''杨辉三角金字塔v1.0-工程包'''
res = []
# 绘制前九行的杨辉三角列表
for x in range(9):
    # 前两行，分别为[1], [1, 1]
    if x == 0:
        res.append([1])
    elif x == 1:
        res.append([1, 1])
    # 从第三行起，根据上一行确定本行内容
    else:
# 定义一个列表l，存放每行的数据

# 每次循环把列表l添加到res列表中

# 打印前九行杨辉三角列表


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


'''杨辉三角金字塔v3.0-工程包'''
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

