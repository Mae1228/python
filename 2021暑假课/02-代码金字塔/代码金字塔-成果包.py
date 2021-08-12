#塔高（行）
height=int(input('请输入代码塔高度：'))
if height<0:
    height=1

# 塔列：通过行下标获取塔列数，行下标从0开始，0代表第1行
def GetCols(rowIndex):
    x=1
    for i in range(rowIndex):
        x+=2
    return x

# 生产指定行列的空二维列表
def Make2List(rows,cols):
    dList=[]
    # 动态扩展二维列表
    for i in range(rows):
        dList.insert(i,[])
        for j in range(cols):
            dList[i].insert(j,[])
    return dList

# 创建列表塔（二维列表）
colMax=GetCols(height-1)#索引从0开始，所以要行高减一
tower=Make2List(height,colMax)
print('塔高：',height,'列：',colMax)

# 设置列表塔
for i in range(height-1,-1,-1):
    blank=height-(i+1)#计算出每行需要空的格数
    for j in range(colMax-blank):
        if j < blank:
            tower[i][j]=' '
        else:
            tower[i][j]='1'

# 遍历列表塔
for i in range(len(tower)):
    for j in range(len(tower[i])):
        if tower[i][j]:
            print(tower[i][j],end=' ')#print的格式化方法，末尾不换行
    print()#此行起到换行的作用






