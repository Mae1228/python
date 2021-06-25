'''练习3成果包——回文数'''
'''
编写程序帮助阿短来判定一个正整数是否为回文数。

输入一个三位以上的正整数，输出是否为回文数提示信息。
如：
Input：
输入数字：12121
Output：
12121 是回文数
'''

# #回文数判断方法一：
number = int(input('输入数字：'))
numberStr = str(number)
newStr = ''
i = len(numberStr) - 1
#使用循环，将numberStr倒序放入newStr中
while i >= 0:
    newStr += numberStr[i]
    i -= 1
    # print(newStr,'---',numberStr)
if newStr == numberStr:
    print(number, '是回文数')
else:
    print(number, '不是回文数')


# #回文数判断方法二(1)
# number = int(input('输入数字：'))
# numberStr = str(number)
# head = 0
# tail = len(numberStr) - 1
# #使用循环，比较相对应的头和尾数字是否相同
# while True:
#     if numberStr[head] != numberStr[tail]:
#         print(number, '不是回文数')
#         break
#     head += 1  # 头标志向后移
#     tail -= 1  # 尾标志向前移
#     if head >= tail:
#         print(number, '是回文数')
#         break


# #回文数判断方法二(2):while...else...
# number = int(input('输入数字：'))
# numberStr = str(number)
# head = 0
# tail = len(numberStr) - 1
# #使用循环，比较相对应的头和尾数字是否相同
# while head<=tail:
#     if numberStr[head] != numberStr[tail]:
#         print(number, '不是回文数')
#         break
#     head += 1  # 头标志向后移
#     tail -= 1  # 尾标志向前移
# else:
#     print(number, '是回文数')
