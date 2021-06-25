''''''
'''
\t：制表符，对齐表格数据的各列
    是字符串，在引号里面使用
str.center(字符串总宽度，填充字符)：返回一个居中的原字符串
                                    默认填充字符为空格

'''
'''练习1'''
# list3=[1,3,3,1]
# list4=[]
# for j in range(len(list3)):
#     if j==0:
#         list4.append(1)
#     else:
#         list4.append(list3[j]+list3[j-1])
# list4.append(1)
# print(list4)


'''练习2'''
# lis=[]
# for i in range(9):
#     if i==0:
#         lis.append([1])
#     elif i==1:
#         lis.append([1,1])
#     else:
#         li=[]
#         for j in range(len(lis[i-1])):
#             if j==0:
#                 li.append(1)
#             else:
#                 li.append(lis[i-1][j]+lis[i-1][j-1])
#         li.append(1)
#         lis.append(li)
# for i in lis:
#     print(i)


'''制表符\t'''
# print('张三  李四  王五  ')
# print('158cm  175cm  187cm  ')
# print('张三\t李四\t王五\t')
# print('158cm\t175cm\t187cm\t')


'''练习3'''
# lis=[]
# for i in range(9):
#     if i==0:
#         lis.append([1])
#     elif i==1:
#         lis.append([1,1])
#     else:
#         li=[]
#         for j in range(len(lis[i-1])):
#             if j==0:
#                 li.append(1)
#             else:
#                 li.append(lis[i-1][j]+lis[i-1][j-1])
#         li.append(1)
#         lis.append(li)
# for i in lis:
#     s=''
#     for j in i:
#         s+=str(j)+'\t'
#     print(s)


'''字符串的center方法'''
# test='12345678901234567890'
# print(test)
# print(test.center(30))
# print(test.center(30,'*'))


'''练习4'''
# lis=[]
# for i in range(9):
#     if i==0:
#         lis.append([1])
#     elif i==1:
#         lis.append([1,1])
#     else:
#         li=[]
#         for j in range(len(lis[i-1])):
#             if j==0:
#                 li.append(1)
#             else:
#                 li.append(lis[i-1][j]+lis[i-1][j-1])
#         li.append(1)
#         lis.append(li)
# for i in lis:
#     s=''
#     for j in i:
#         s+=str(j)+'   '
#     print(s.center(60))


'''-------------------------------------------------------------'''











































































