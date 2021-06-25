'''练习1成果包——水仙花数v1.0'''
'''
编写程序帮助阿短来判定一个三位整数是否为水仙花数。

输入一个三位整数，输出是否为水仙花数提示信息。
如:
Input：
输入数字：123
Output：
123 不是水仙花数
'''

#判断一个数是不是水仙花数
num = int(input('输入数字:'))
number= str(num)
i = 0  # 循环计数器
daffodil = 0  # 用和原数number来对比的水仙花数
#主循环
while i < len(number):
    daffodil += int(number[i]) ** 3
    i += 1
if int(number) == daffodil:
    print(number, '是水仙花数')
else:
    print(number, '不是水仙花数')


'''for循环实现'''
# #判断一个数是不是水仙花数
# num = int(input('输入数字:'))
# number= str(num)
# daffodil = 0  # 用和原数number来对比的水仙花数
# #主循环
# for i in range(len(number)):
#     daffodil += int(number[i]) ** 3
# if int(number) == daffodil:
#     print(number, '是水仙花数')
# else:
#     print(number, '不是水仙花数')