''''''
'''
函数：一段命名的代码，可以实现某一些功能，我们通过调用函数即可执行相应代码
内置函数：print()、input()、range()
定义函数：以def开头定义函数
          自定义函数名应该避开python中的保留字，如if、True、and等------help('keywords')
          函数中的代码块里至少有一条语句。
          格式：def 函数名():
位置参数：调用函数时，按照定义函数的参数数量和位置（顺序）传入的参数
          格式：def 函数名(参数a，参数b):
返回值：函数返回的值，即返回值。
        return语句用于退出函数并返回函数的返回值
        return语句可缺省。若缺省则函数返回None
        return语句可以返回变量、常量、表达式
None：它既不是0,也不是False,也不是空字符串。它只是一个空值的对象,也就是一个空的对象,只是没有赋值而已
默认参数：定义函数时，设定了默认值的一个或多个参数，它必须在位置参数后
          调用函数时，可以传递值给默认参数，也可以不传（保留默认值），传默认参数也要按照它们的位置传递
          格式：def 函数名(参数a，参数b，......,参数m=0，参数n=1):


'''
'''实践一'''
# def myfun():
#     print('执行我的第一个函数')
# myfun()



'''位置参数'''
# def myfun(a,b,c):
#     print(c,b,a)
# myfun(1,2,3)



'''实践二'''
# def myadd(a,b):
#     print(a+b)
# myadd(1,2)



'''实践三'''
# def myadd(a,b):
#     return a+b
# res=myadd(1,2)
# print(res)



'''默认参数'''
# def myfun(a,b=2,c=3):
#     print(a,b,c)
# myfun(1,0)



'''项目'''
# def myrange(start,stop,step=1):
#     res=[]
#     while start<stop:
#         res.append(start)
#         start+=step
#     return res
# for i in myrange(0,16):
#     print(i)
# for j in myrange(2,17,2):
#     print(j)


'''-------------------------------------------------------------------------------'''




