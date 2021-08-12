#水仙花-拆数
#获得数字
num=int(input('请输入一个小于8位的数字：'))
#获取位数
w=0
i=1
while i<10000000:
    i*=10
    w+=1
    if num<i:
        print(num,'是',w,'位数')
        break
print('over')













