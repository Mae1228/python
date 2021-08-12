#求前n项斐波那契数的值
n=int(input('请输入要求几项？'))
fbi=[]
for i in range(n):
    if i==0 or i==1:#第1，2项 都为1
        fbi.append(1)
    else:
        fbi.append(fbi[i-2]+fbi[i-1])#从第3项开始每项值为前两项值之和
print(fbi)














