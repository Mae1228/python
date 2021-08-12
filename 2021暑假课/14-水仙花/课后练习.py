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
#补充拆数代码，输入每一位上的值
divisor=1
n=0
#获取最高位除数
while n<w-1:
    divisor*=10
    n+=1
#分解每个数字
while divisor>0:
    print(num//divisor%10,end=',')
    divisor//=10












