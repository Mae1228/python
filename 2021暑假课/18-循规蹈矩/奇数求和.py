#打印范围内奇数求和
num1=int(input('请输入起始数字：'))
num2=int(input('请输入终止数字：'))
sum=0
for i in range(num1,num2+1,1):
    if i%2!=0:
        sum+=i
print(num1,'到',num2,'以内的奇数之和：',sum)














