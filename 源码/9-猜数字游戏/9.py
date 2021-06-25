''''''
'''
数据类型：字符串str     数字类型：整数int    浮点float      布尔类型：True和False
算术运算符7：/ （返回浮点类型）  +    -   *    %（求余数，返回int类型）  //(向下取整，返回整数类型)   **（幂运算）
赋值运算符8：=  +=
逻辑运算符3：and（与）：真真为真    or（或）：假假为假    not（非）：真为假，假为真
真、假：True    False
比较运算符6：>    <    ==    >=    <=    !=
成员运算符2：in
查看数据类型：type(数据)
input默认返回类型：字符串
+在两种数据类型中的用法：字符串：拼接      数字类型：加号
数据类型的转换：转成int：纯数字的字符串（无小数点）   转成float：纯数字的字符串（有小数点）
分支结构：单分支：if。。。     双分支：if。。。else。。。     多分支：if。。。elif。。。else。。。（elif有无数个）
拼接：+：没有空格，只能在字符串之间拼接       ，：只能在print()中使用，可以在字符串和数字进行拼接，有空格（取消空格sep="）
缩进：一个Tab    4个空格
循环：while循环
死循环：while True
跳出循环：break    循环体里面使用
跳过本次循环：continue   循环体里面使用
随机库：import random(第一行)
随机产生整数：random.randint(小,大)-----包头包尾
while。。。else。。。（break不执行else语句，正常结束执行else的语句，continue执行else语句）
'''








'''实践一：while循环'''
# a=0
# while a<5:
#     print(a)
#     a+=1



'''实践二：while True'''
# a=0
# while True:
#     if a==5:
#         break
#     print(a)
#     a+=1



'''实践三：'''
# a=0
# while a<5:
#     print(a)
#     a+=1
# else:
#     print('over')
#
#
# a=0
# while True:
#     if a==5:
#         break
#     print(a)
#     a+=1
# else:
#     print('over')



'''实践四'''
# a=0
# while a<5:
#     a+=1
#     if a==3:
#         continue
#     print(a)
# else:
#     print('over')


'''猜数字1'''
# print('start game!')
# b=6
# while True:
#     a=int(input('please input a number:'))
#     if a==b:
#         print('yes')
#         break
#     else:
#         print('no')


'''猜数字2：随机库，次数为3'''
# import random
# print('start game!')
# b=random.randint(0,10)
# print(b)
# i=1
# while i<4:
#     a=int(input('please input a number:'))
#     if a==b:
#         print('yes')
#         break
#     else:
#         print('no')
#     i+=1
# else:
#     # print('no'+str(b)+'change')
#     print('no',b,'change......',sep='')

'''猜数字4：'''
# import random
# print('start game!')
# b=random.randint(0,10)#谜底
# print(b)
# i=1#比较次数
# while i<4:
#     a=int(input('第'+str(i)+'次：'))#用户输入的数
#     if a==b:
#         print('yes')
#         break
#     elif a>b:
#         print('big')
#     elif a<b:
#         print('small')
#     i+=1
# else:
#     # print('no'+str(b)+'change')
#     print('no',b,'change......',sep='')


'''----------------------------------------------------------------------------------------------'''


















