#确定层数
k=10
# 创建记录数值的列表
a=[]

#创建k+k的二维列表，并且用0填充占位
for i in range(k):
    a.append([])
    for j in range(k):
        a[i].append(0)

# 前两行
for i in range(k):
    a[i][0]=1
    a[i][i]=1

#第三行开始：根据杨辉三角的特点，第三行开始每个数等于它上方两数之和
for i in range(2,k):
    for j in range(1,i):
        a[i][j]=a[i-1][j-1]+a[i-1][j]

# 依次打印每一个元素，记得格式化输出
for i in range(k):
    for j in range(i+1):
        print(a[i][j],end=' ')
    print()#换行的作用











