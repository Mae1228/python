'''练习2成果包——水仙花数v2.0'''
'''
编写程序帮助阿短找到全部的水仙花数。查找范围为：100-999。

输入起始数，输入终止数，输出此范围内所有的水仙花数。
如：
Input：
输入起始数：100
输入终止数：999
Output：
153 是水仙花数
370 是水仙花数
371 是水仙花数
407 是水仙花数
'''

#判定一定范围内的水仙花数
head = int(input('输入起始数：'))
tail = int(input('输入终止数：'))
#外层添加主循环，依次处理范围内的每个数
while head <= tail:
    #将从范围内取到的数对应拿出,赋值给变量number
    number = str(head)
    i = 0
    daffodil = 0
    while i < len(number):
        daffodil += int(number[i]) ** 3
        i += 1
    if int(number) == daffodil:
        print(number, '是水仙花数')
    #外层循环中的head处理
    head += 1
