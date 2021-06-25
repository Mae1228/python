'''猜数字游戏-挑战包'''
'''stamp:标记修改点,本文共有4个标记'''

import random
number = random.randint(0, 100)
i = 1
#stamp1:设置start和end记录猜测的结果
start = 0
end = 100
print('开始猜数字小游戏吧！')
print(number)
while i <= 3:
    #stamp2:修改猜数字游戏提示
    send = '第' + str(i) + '次(' + str(start) + '-' + str(end) + '):'
    message = int(input(send))
    if message == number:
        print('恭喜！猜对了！')
        break
    elif message > number:
        print('不对，猜大了哦')
        #stamp3:修改范围
        end = message
    elif message < number:
        print('不对，猜小了哦')
        #stamp4:修改范围
        start = message
    i += 1
else:
    print('正确数字是' + str(number) + ',没有机会了...')