''''''
'''

'''
'''蒙提霍尔悖论'''
# import random
# doors=[0,0,0]
# yes=random.randint(0,2)
# doors[yes]=1
# choise=int(input('请输入你要选择的门【0、1、2】：'))
# res=doors.pop(choise)#不换门就是判断当下的值是否为1（车）
# for i in range(2):#删除掉选择的门下标，就是防止遍历时打开选择的门
#     if doors[i]==0:
#         doors.pop(i)#删除打开的门，就是为了取到剩余门的值
#         break
# yn=input('是否要换门：')
# if yn=='y':
#     res=doors[0]#换门就是判断当下的值是否为1（车）
# if res==1:
#     print('恭喜')
# else:
#     print('抱歉')


'''蒙提霍尔悖论挑战包'''
# import random
# car=0
# yang=0
# for j in range(1000):
#     doors = [0, 0, 0]
#     yes = random.randint(0, 2)
#     doors[yes] = 1
#     choise = random.randint(0, 2)
#     res = doors.pop(choise)
#     for i in range(2):
#         if doors[i]==0:
#             doors.pop(i)
#             break
#     res=doors[0]
#     if res==1:
#         car+=1
#     else:
#         yang+=1
# print('车和羊数分别是：',car,yang)


'''----------------------------------------------------------------'''


















