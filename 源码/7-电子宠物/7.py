''''''
'''
数据类型：字符串str     数字类型：整数int   浮点float    布尔类型（True，False）
算数运算符7：+，-，*，/（返回浮点）,**（幂运算）,//（向下取整），%（取余数，返回整数类型）
赋值运算符8：=，+=，-=，/=,//=,**=,%=,*=
逻辑运算符3：and（与），or（或）；not（非）
真：True     假：False
比较运算符6：>  >=  <  <=  ==  !=
成员运算符2：in
查看数据类型：type（）
input默认返回类型：字符串str
+在两种数据类型的用法：字符串：拼接       数字类型：加号
数据类型转换：转成int：纯数字的字符串（没有小数点）    转成float：数字的字符串（有小数点）
输入：input        输入的内容给变量接收
变量的命名：不能以数字开头，由字母，数字，_,组成
输出：print
分支结构：单分支if。。。     双分支if。。。else。。。   多分支：if。。。elif。。。else。。。（无数个elif）
拼接：+：只能是字符串和字符串拼接，没有空格     “，”：可以是字符串和数字进行拼接，有空格（取消空格sep="）
缩进：一个Tab     4个空格
while循环：计算机做重复的内容
死循环：while True:    （不知道次数的循环）
跳出循环：break    （只能在循环体里面使用）
导入随机库：import random
随机产生整数：random.randint(小,大)---------包头包尾
注释：1.单行注释：# (Ctrl+?)       2.多行注释：三对单引号：''''''   三对双引号：""""""
'''



'''打印π'''
# import math
# print(math.pi)





'''实践一'''
# a=1
# while a<=10:
#     print(a)
#     a+=1
# print('kkkk')


'''实践二'''
# a=1
# while True:
#     print(a)
#     if a==10:
#         break
#     a+=1
# print('hhhhhh')

'''小金鱼'''
# import random#导入随机库
# name='hhhhhhhh'
# eggs=0#总产卵量
# t=100#体力值
# print('小金鱼'+name+'陪你玩！')
# while True:
#     a=input('要小金鱼'+name+'做什么：')
#     if t>150:
#         print('饱死了')
#         break
#     if t<=0:
#         print('饿死了')
#         break
#     if a=='eat':
#         t+=random.randint(12,18)#体力值增加：随机
#         print('什么东西，真香')
#     elif a=='lay':
#         t-=random.randint(18,23)#体力值减少：随机
#         egg=random.randint(10,15)#这时候的产卵量:随机
#         eggs+=egg#总产卵量
#         print('产下了'+str(egg)+'颗卵')
#     else:
#         print(name+'不知道什么意思')
# print('产卵总数：',eggs,sep='')


# random.randint(1,10)

'''------------------------------------------------------------------------------------'''




















'''
输入错误，请输入不大于100的分数
满分
优秀
良好
中等
及格
不及格
输入错误，请输入不小于0的分数
'''




