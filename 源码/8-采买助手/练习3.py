'''练习3成果包——无人售卖机v2.0'''
'''
顾客选择一定整数金额商品后，付款给售卖机，售卖机进行自动收钱和找零。
收钱和找零的面额有：1元、5元、10元、20元、50元。

输入应付金额，然后多次输入付款面额，输入end，付款结束，输出要找零的面额和其张数。
如：
Input：
输入应付多少：26
收钱：20
收钱：20
收钱：end
实际收款：40
Output：
10元 x 1
1元 x 4
'''

pay = int(input('输入应付多少：'))
money = 0
m1 = m5 = m10 = m20 = m50 = 0
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
        m50 += 1
        change -= 50
    elif change >= 20:
        m20 += 1
        change -= 20
    elif change >= 10:
        m10 += 1
        change -= 10
    elif change >= 5:
        m5 += 1
        change -= 5
    elif change >= 1:
        m1 += 1
        change -= 1
if m50 != 0:
    print('50元 x', m50)
if m20 != 0:
    print('20元 x', m20)
if m10 != 0:
    print('10元 x', m10)
if m5 != 0:
    print('5元 x', m5)
if m1 != 0:
    print('1元 x', m1)
