'''练习1成果包——智慧找零'''
'''
顾客购买了一些商品，共花费了整数金额，但他只有一张一百元的纸币，请编写程序计算出最合适的找零方案。
收银台的货币面额有：1元、5元、10元、20元、50元。

输入应付金额，输出找零的每张面额。
如:
Input：
输入应付多少：26
Output：
50
20
1
1
1
1
'''

pay = int(input('输入应付多少：'))
change = 100 - pay
while True:
    if change == 0:
        break
    if change >= 50:
        print('50')
        change -= 50
    elif change >= 20:
        print('20')
        change -= 20
    elif change >= 10:
        print('10')
        change -= 10
    elif change >= 5:
        print('5')
        change -= 5
    elif change >= 1:
        print('1')
        change -= 1
