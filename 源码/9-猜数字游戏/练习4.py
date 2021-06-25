'''练习4'''

#调用随机库
import random

number = random.randint(1, 10)
i = 1
print('开始猜数字小游戏吧！')
print(number)
while i <= 3:
    #变量灵活使用
    send = '第' + str(i) + '次：'
    message = int(input(send))
    if message == number:
        print('恭喜！猜对了！')
        break
    elif message > number:
        print('不对，猜大了哦')
    elif message < number:
        print('不对，猜小了哦')
    i += 1
#while循环的else结构使用
else:
    print('正确数字是' + str(number) + ',没有机会了...')