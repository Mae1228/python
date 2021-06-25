import random
print('开始猜数字游戏！')
a=random.randint(0,100)      #谜底
print(a)
i=1     #循环次数
xiao=0
da=100
while i<4:
    number=int(input('第'+str(i)+'次('+str(xiao)+'-'+str(da)+')：'))
    if a==number:
        print('恭喜，猜对了！')
        break
    elif number>a:
        if number//10*10>a:
            da=number//10*10
        else:
            da=(number//10+1)*10
        print('不对，猜大了！')
    elif number<a:
        if (number//10+1)*10<a:
            xiao=(number//10+1)*10
        else:
            xiao = number//10*10
        print('不对，猜小了！')
    i+=1
else:
    print('正确数字是'+str(a)+'，没有机会了！')