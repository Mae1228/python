'''无限的质数-阶段1'''

#用for循环判断是否为质数
number = int(input('请输入数字:'))
check = 0
#循环
for i in range(2, number):
    if number % i == 0:
        check = 1
if check == 0:
    print(number, '是质数')
else:
    print(number, '不是质数')



    