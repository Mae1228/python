'''练习1'''
a=6
print('开始猜数字游戏吧！')
while True:
    number=int(input('请输入一个数：'))
    if number==a:
        print('恭喜，猜对了！')
        break
    else:
        print('猜错了，请重新输入')