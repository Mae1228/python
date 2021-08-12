''''''
'''
max(列表\元组\字符串\字典\集合\......)：求最大值的函数
max(数字1,数字2,......,数字n)：求最大值的函数

min(列表\元组\字符串\字典\集合\......)：求最小值的函数
min(数字1,数字2,......,数字n)：求最小值的函数

sorted(列表\元组\字符串\字典\集合\......)：排序函数
sorted(列表\元组\字符串\字典\集合\......,reverse=True)：排序函数
                                                        reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

round(浮点数\除法表达式\......)：取近似值的函数
round(浮点数\除法表达式\......,保留位数)：取近似值的函数
                                        保留位数默认值位None，即返回最接近传入数值的整数
                                        保留位数表示从小数点位数，默认值为 0。

参数：
    形参：形式参数，定义函数时设置的参数
        位置参数、关键字参数
    实参，实际参数，调用函数时传入的参数

'''

'''练习一'''
# t=(1,4,-5,64,78,12,0,3,3.5,3)
# #定义最大值函数
# def mymax(t):
#     m=t[0]
#     for i in t:
#         if i>m:
#             m=i
#     return m
# #调用最大值函数
# res=mymax(t)
# print('最大值是：'+str(res))


'''求最大值函数max()'''
# lst=[2,4,1]
# x=max(lst)
# print(x)
# x=max(2,4,1)
# print(x)


'''练习二'''
# t=(1,4,-5,64,78,12,0,3,3.5,3)
# #定义最小值函数
# def mymin(t):
#     m=t[0]
#     for i in t:
#         if i<m:
#             m=i
#     return m
# #调用最小值函数
# res=mymin(t)
# print('最大值是：'+str(res))


'''求最小值min()'''
# lst=[2,4,1]
# x=min(lst)
# print(x)
# x=min(2,4,1)
# print(x)


'''练习三'''
# t=(1,4,-5,64,78,12,0,3,3.5,3)
#
# #定义最大值函数
# def mymax(t):
#     m=t[0]
#     for i in t:
#         if i>m:
#             m=i
#     return m
#
# #定义最小值函数
# def mymin(t):
#     m=t[0]
#     for i in t:
#         if i<m:
#             m=i
#     return m
#
# def mysorted(t,reverse=False):
#     newlst=[]
#     lst=list(t)
#     #默认是升序排序
#     if reverse==False:
#         while len(lst)>0:
#             #调用最小值函数
#             res=min(lst)
#             newlst.append(res)
#             lst.remove(res)
#     #降序排序
#     elif reverse==True:
#         while lst:
#             #调用最大值函数
#             res = max(lst)
#             newlst.append(res)
#             lst.remove(res)
#     return newlst
#
# #调用排序函数
# r=mysorted(t)
# print('升序排序：',r)
# r1=mysorted(t,True)
# print('降序排序：',r1)


'''排序函数sorted()'''
# lst=[2,4,1]
# x=sorted(lst,reverse=True)
# print(x)
# x=sorted(lst)
# print(x)


'''练习四'''
# #定义取近似值函数
# def myround(n,s=0):
#     #小数点向后移动s+1位
#     y=int(n*10**(s+1))
#     #取余
#     f=y%10
#     #取整
#     rnd=y//10
#     if f>4:
#         rnd+=1
#     #小数点向前移动s位
#     rnd*=10**(-s)
#     return rnd
#
# #输入小数和位数
# n=float(input('请输入要取近似值的浮点数：'))
# s=int(input('请输入要保留小数点后的位数：'))
# #调用取近似值函数
# res=myround(n,s)
# print(n,'取近似值后的结果是：',res)



'''取近似值函数round()'''
# num=3.14159
# x=round(num,3)
# print(x)
# x=round(num)
# print(x)


