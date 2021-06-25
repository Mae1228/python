'''自助点单机-挑战包'''
'''
	阿短家的小区附近开了一家快餐店，由于物美价廉，每天来吃饭的人都很多，老板发现这人一多收银成了个难题。
于是，善良的阿短决定帮老板制作一个自助收点单小程序，可以帮助客人快速点单以及计算出应该支付的价格。
	请你一起来协助阿短完成这个任务吧。

店里售卖的东西如下：
10元：汉堡,鸡肉卷,牛肉面,三明治
6元：薯条,沙拉,花生米,可乐,柠檬茶,紫菜汤
客户每次可以任选三种，也可直接选择套餐。
套餐如下：
套餐1：汉堡,薯条,可乐
套餐2：鸡肉卷,沙拉,柠檬茶
'''

#套餐及售卖食物信息
meal1 = '汉堡,薯条,可乐'
meal2 = '鸡肉卷,沙拉,柠檬茶'
food10 = '汉堡,鸡肉卷,牛肉面,三明治'
food6 = '薯条,沙拉,花生米,可乐,柠檬茶,紫菜汤'

#自助点单机
msg1 = input('是否选择套餐(y/n):')
if msg1 == 'y':
    msg2 = input('请选择套餐:')
    if msg2 == '1':
        print(meal1, '共20元')
    elif msg2 == '2':
        print(meal2, '共20元')
else:
    money = 0
    free = ''
    msg2 = input('请选择菜品1:')
    msg3 = input('请选择菜品2:')
    msg4 = input('请选择菜品3:')
    #判断是否是套餐1
    if msg2 in meal1 and msg3 in meal1 and msg4 in meal1:
        print(meal1, '共20元')
    #判断是否是套餐2
    elif msg2 in meal2 and msg3 in meal2 and msg4 in meal4:
        print(meal2, '共20元')
    #原来的部分
    else:
        free += msg2 + ','
        free += msg3 + ','
        free += msg4
        if msg2 in food10:
            money += 10
        else:
            money += 6
        if msg3 in food10:
            money += 10
        else:
            money += 6
        if msg4 in food10:
            money += 10
        else:
            money += 6
        print(free, '共', money, '元')
