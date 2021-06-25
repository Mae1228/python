'''练习2'''
import random
a=random.randint(1,10)
print('开始猜数字游戏吧！')
print(a)
i=1
while i<=3:
    number = int(input('请输入一个数：'))
    if number==a:
        print('恭喜，猜对了！')
        break
    else:
        print('猜错了，请重新输入')
    i+=1