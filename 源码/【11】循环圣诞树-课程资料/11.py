''''''
'''
*在不同数据类型下的使用：在字符串：倍数     在数字类型：乘号
遍历：逐个访问
序列：一组数据
遍历序列：逐个访问一组数据的每个元素
for循环：已知循环次数的循环，常用来遍历
while循环：未知循环次数的循环，符合条件就行，很少用来遍历
for循环：for 变量 in 序列：
range()方法：start:默认为0    stop：不包括stop本身    step：步长，默认为1
'''
'''while循环实现圣诞树'''
# number=int(input('please input a number :'))
# i=1
# while i<=number:
#     print(' '*(number-i)+'*'*(i*2-1))
#     i+=1
# j=1
# while j<=number//2:
#     print(' '*(number-2)+'*'*3)
#     j+=1


'''for循环实现圣诞树'''
# number=int(input('please input a number :'))
# for i in range(1,number+1):
#     print(' '*(number-i)+'*'*(i*2-1))
# for j in range(1,number//2+1,):
#     print(' '*(number-2)+'*'*3)


'''挑战：for循环实现分层圣诞树'''
# number=int(input('please input a number :'))
# y=1
# for i in range(1,number+1):
#     print(' '*(number-y)+'*'*(y*2-1))
#     if i%5==0:
#         y-=2
#     else:
#         y+=1
# for j in range(1,number//2+1,):
#     print(' '*(number-2)+'*'*3)



'''范围内的水仙花数：使用for循环'''
# a1=int(input('input a number1:'))
# a2=int(input('input a number2:'))
# for a1 in range(a1,a2+1):
#     #判断a1是不是水仙花数
#     s=0
#     astr=str(a1)
#     for i in range(len(astr)):
#         s+=int(astr[i])**3
#     if s==a1:
#         print(a1,'yes')


'''----------------------------------------------------------------------------------------------'''
















