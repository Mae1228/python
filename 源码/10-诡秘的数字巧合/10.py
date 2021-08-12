'''10-诡秘的数字巧合'''
'''
获取字符串的长度：len(str)
字符串索引：正向索引（递增）：0------（长度-1）       反向索引（递减）：-1------（-长度）
幂运算：（底数）**（指数）
while循环的嵌套：先执行内循环，内循环结束后才能执行外循环
break：只能跳出离他最近的循环
'''
'''
水仙花：判断一个数是否是水仙花
'''
# a=int(input('qingshuruyigeshu:'))
# astr=str(a)
# i=0
# s=0
# while i<len(astr):
#     s+=int(astr[i])**3
#     i+=1
# if s==a:
#     print('shui')
# else:
#     print('no')

'''
水仙花：一个范围内的所有水仙花：双重循环
'''
# a=int(input('qingshuruyigeshu:'))
# b=int(input('qingshuruyigeshu:'))
#
# bstr=str(b)
# while a<=b:
#     astr = str(a)
#     i=0
#     s=0
#     while i<len(astr):
#         s+=int(astr[i])**3
#         i+=1
#     if s==a:
#         print(str(a)+'shui')
#     # else:
#     #     print('no')
#     a+=1

'''
回文数：使用while     else
'''
# a=int(input('input a number:'))
# astr=str(a)
# t=0
# w=len(astr)-1
# while t<=w:
#     if astr[t]!=astr[w]:
#         print('no')
#         break
#     t+=1
#     w-=1
# else:
#     print('yes')

'''
回文数：使用while True
'''
# a=int(input('input a number:'))
# astr=str(a)
# t=0
# w=len(astr)-1
# while True:
#     if astr[t]!=astr[w]:
#         print('no')
#         break
#     if t>=w:
#         print('yes')
#         break
#     t+=1
#     w-=1

'''
回文数正着数和倒着数都一样
'''
# a=int(input('input a number:'))
# astr=str(a)
# bstr=''
# i=len(astr)-1
# while i>=0:
#     bstr+=astr[i]
#     # print(bstr+'-----'+astr)
#     i-=1
# if bstr==astr:
#     print('yes')
# else:
#     print('no')



'''----------------------------------------------------------------------------------'''


























# a=int(input('输入数字：'))
# astr=str(a)
# t=0
# w=len(astr)-1
# while t<w:
#     if astr[t]!=astr[w]:
#         print(a,'不是回文数')
#         break
#     t+=1
#     w-=1
# else:
#     print(a,'是回文数')






