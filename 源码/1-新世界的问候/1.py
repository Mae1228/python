''''''
'''
输出：print(内容)
      字母、汉字、符号和数字都要用引号

注释：单行注释：#
      多行注释：三对单引号
                三对双引号

输入：input(提示语)
      
=：赋值，后面赋值给前面

变量：存放数据的容器
      变量名最好不用起重复的
      变量名不能是关键字---------print(help('keywords'))
      变量由下划线、数字、字母、汉字组成，不能以数字开头，通常不用汉字当变量名
      

'''














'''
输出：print(内容)
    内容：字母、汉字、符号必须由引号
输入：input(提示语)
    拿变量进行接收
注释：程序不执行注释的内容，起到提示的作用
    单行注释：#
    多行注释：三对单引号或三对双引号
变量：存储数据的容器
    变量由数字、汉字、字母、_组成，数字不能开头
    变量不能是关键字
拼接：print(内容1,内容2,内容3...,sep='')
    出现空格,以sep=''取消空格
取消换行：print(内容,end='')
      

'''













n=input('输入姓名：')
a=input('输入爱好：')
f=input('输入未来的目标：')
print('姓名：',n,sep='')
print('爱好：',end='')
print(a)
print('未来的目标：',end='')
print(f)



'''
print(内容,end='换行符')：取消换行
print(内容1,内容2,...,sep='间隔符')：逗号进行拼接，取消空格
'''

