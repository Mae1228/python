''''''
'''九九乘法表'''
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='   ')
    print()


print()

'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
# print('有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？')
# for i in range(1,5):
#     for j in range(1,5):
#         for x in range(1,5):
#             if i!=j and i!=x and j!=x:
#                 print(i*100+j*10+x)

''''''
a=int(input('请输入行数：'))
for i in range(1,a+1):
    if i<=a//2:
        print("*"*i)
    elif i>a//2:
        print("*"*(a+1-i))

