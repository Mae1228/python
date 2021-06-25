''''''
'''
质数：质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数
标记位：数值没有意义，表示一种状态
for循环的嵌套：外循环每执行一次，内循环完成执行一遍，然后继续执行外循环（内循环是外循环的一部分）
for。。。else。。。：for循环正常结束后（无break）执行else语句；for循环提前结束后执行其他语句

'''
'''判断一个数是否是质数：标记位'''
# number=int(input('input a number:'))
# biaoji=0
# for i in range(2,number):
#     if number%i==0:
#         biaoji=1
# if biaoji==0:
#     print(number,'yes')
# else:
#     print(number, 'no')



'''输出一个范围内的所有质数：标记位'''
# number1=int(input('input a number1:'))
# number2=int(input('input a number2:'))
# for j in range(number1,number2+1):
#     biaoji=0
#     for i in range(2,j):
#         if j%i==0:
#             biaoji=1
#     if biaoji==0:
#         print(j)



'''输出一个范围内的所有质数：for。。。else。。。'''
# number1=int(input('input a number1:'))
# number2=int(input('input a number2:'))
# for j in range(number1,number2+1):
#     for i in range(2,j):
#         if j%i==0:
#             break
#     else:
#         print(j)


'''输出一个范围内的所有质数：while。。。else。。。'''
# n1=int(input('input a number1:'))
# n2=int(input('input a number2:'))
# while n1<=n2:
#     i=2
#     while i<n1:
#         if n1%i==0:
#             break
#         i+=1
#     else:
#         print(n1)
#     n1+=1



'''----------------------------------------------------------------------------------------------'''





a1=int(input('请输入开始数：'))
a2=int(input('请输入结束数：'))
for j in range(a1,a2+1,1):
    for i in range(2,j,1):#2 3 4 5 6
        if j%i==0:
            break
    else:
        print(j,'是质数')



# a=int(input('请输入一个数：'))
# for i in range(2,a,1):#2 3 4 5 6
#     if a%i==0:
#         print(a,'不是质数')
#         break
# else:
#     print(a,'是质数')







