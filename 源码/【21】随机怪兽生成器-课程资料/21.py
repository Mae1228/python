''''''
'''
len(数据)：获取列表和字符串的长度
列表：存储多个元素，元素可以是列表
mylist[index]——访问列表中的元素；
mylist[index][index]——访问嵌套列表中的元素。
list.pop(index)方法用于移除列表中的一个元素，再返回该元素的值。
                index是要移除元素的索引值，如果不填写index，则默认移除最后一个元素。
交换变量的值：一、a,b=b,a
             二、t=a
                 a=b
                 b=t

'''
'''实践一'''
# import random
# mylist=[1, 45, 'a', 'fd', 3, 's']
# x=random.randint(0,len(mylist)-1)


'''实践二'''
# import random
# names=['时空魔神', '海底猿人', '植物怪兽', '火山怪鸟', '刺客超兽']
# where=['猪圈', '厕所里', '房顶上', '办公室']
# doing=['引起大规模停电', '抄作业', '喜极而泣', '偷西瓜', '玩火自焚', '倒立狂奔']
# n=random.randint(0,len(names)-1)
# w=random.randint(0,len(where)-1)
# d=random.randint(0,len(doing)-1)
# print(names[n],'在',where[w],doing[d])


'''实践三'''
# mylist= [ ['codemao',5 ],['列表',2],0]
# print(mylist[0][1],mylist[1][1],mylist[2],mylist[0][0])


'''移出列表元素'''
# mylist = [['阿短' , '编程猫', '绿豆'], '绿豆',['阿短','编程猫']]
# x = mylist[0].pop(2)
# y = mylist.pop(2)
# print(x,y)
# print(mylist)


'''实践四'''
# mylist= [ ['codemao' , 5 ], ['列表' , 2],0  ]
# mylist[0].pop()
# mylist[0].pop()
# mylist[1].pop(1)
# mylist.pop()
# print(mylist)


'''交换变量的值'''
# a=3
# b=7
# a,b=b,a
# print('a、b的值分别为：',a,b)


'''随机怪兽生成器'''
# import random
# mylist = [['时空魔神', '海底猿人', '植物怪兽', '火山怪鸟', '刺客超兽'],
#           ['猪圈', '厕所里', '房顶上', '办公室'],
#           ['引起大规模停电', '抄作业', '喜极而泣', '偷西瓜', '玩火自焚', '倒立狂奔']]
# temp=[[],[],[]]
# while True:
#     if len(mylist[0])!=0 and len(mylist[1])!=0 and len(mylist[2])!=0:
#         a=input('***Press Enter***见证怪兽的时刻到了:')
#         if a=='':
#             n=random.randint(0,len(mylist[0])-1)#随机索引
#             w=random.randint(0,len(mylist[1])-1)
#             d=random.randint(0,len(mylist[2])-1)
#             x=mylist[0].pop(n)#删除对应的文字，防止重复
#             temp[0].append(x)
#             y = mylist[1].pop(w)
#             temp[1].append(y)
#             z = mylist[2].pop(d)
#             temp[2].append(z)
#             print(x,'在',y,z)
#         else:
#             break
#     else:
#         if len(mylist[0])==0:
#             mylist[0],temp[0]=temp[0],mylist[0]
#         if len(mylist[1])==0:
#             mylist[1],temp[1]=temp[1],mylist[1]
#         if len(mylist[2])==0:
#             mylist[2],temp[2]=temp[2],mylist[2]


'''---------------------------------------------------------------------------------'''

