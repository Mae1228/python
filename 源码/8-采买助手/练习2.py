'''练习2成果包——无人售卖机v1.0'''
'''
顾客选择一定整数金额商品后，付款给售卖机，售卖机进行自动收钱和找零。
收钱和找零的面额有：1元、5元、10元、20元、50元。

输入应付金额，然后多次输入付款面额，输入end，付款结束，输出实际收款金额和找零的每张面额。
如：
Input：
输入应付多少：26
收钱：20
收钱：20
收钱：end
实际收款：40
Output：
10
1
1
1
1
'''

pay = int(input('输入应付多少：'))
money = 0
while True:
    gave = input('收钱：')
    if gave == 'end':
        break
    money += int(gave)
print('实际收款：', money, sep='')
change = money - pay
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
