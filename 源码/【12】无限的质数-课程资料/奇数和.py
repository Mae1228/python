''''''
'''for循环'''
a1=int(input('请输入开始数字：'))
a2=int(input('请输入结束数字：'))
sum=0
for i in range(a1,a2+1):
    if i%2==1:
        sum+=i
print(a1,'到',a2,'间奇数和为：',sum,sep='')