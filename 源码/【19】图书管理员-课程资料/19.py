''''''
'''
列表：Python中的一种数据类型，通常用于按照一定顺序存储多个或者一组数据
序列：字符串、range、列表
创建列表：用一对方括号把数据项全部括起来，逗号将每个数据项分隔开，将整个列表赋值给一个变量
列表中的元素可以是不同的数据类型
创建空列表：空列表内没有任何内容
列表是一种序列，可以使用for循环进行遍历
索引：是序列中元素的位置编号，也叫下标
        正向索引：0~长度-1
        反向索引：-1~-长度
切片：用于截取序列中指定区间的元素值
        格式：list[开始:结束:步长]--------跟range差不多
列表是可以修改的，Python中提供了很多操作列表的内置方法        
append() 方法用于在列表末尾添加新的数据
remove() 方法用于移除列表中某个值的第一个匹配项。
         没有匹配项会报错
      


'''
'''实践一'''
# s=['c','o','d','e','m','a','o']
# for i in s:
#     print(i)


'''实践二'''
# s = 'hello codemao'
# print(s[8])
# print(s[6:10:1])
# print(s[0:len(s):2])


'''实践三'''
# s = 'hello codemao !'
# mylist=[]
# for i in s:
#     if i!=' ':
#         mylist.append(i)
# mylist.remove('!')
# print(mylist)

'''挑战'''
# list=['哈利波特','流浪地球','封神演义','三国演义','红楼梦','西游记','水浒传']
# while True:
#     print('end:结束管理图书 0：展示书单 1：借书 2：还书 3:查询借书记录')
#     do=input('你好！要图书助手帮你做什么:')
#     if do=='end':
#         break
#     elif do=='0':
#         print('目前有图书:')
#         for i in list:
#             if '#' not in i:
#                 print(i)
#     elif do=='1':
#         j_book=input('要借哪本书:')
#         if j_book in list:
#             print('好的，马上帮您办理借书！')
#             j_people=input('请登记借书人姓名:')
#             print('借书成功！')
#             list.remove(j_book)
#             list.append(j_book+'#'+j_people)
#         else:
#             print('没有此书或此书已被借走！')
#     elif do=='2':
#         h_book=input('要还哪本书:')
#         h_people=input('请核对借书人:')
#         if h_book+'#'+h_people in list:
#             print('还书成功！')
#             list.remove(i)
#             list.append(h_book)
#         else:
#             print('请检查书名或借书人信息是否正确！')
#     elif do=='3':
#         c_people=input('请输入借书人：')
#         print('你借走的书籍有：')
#         for i in list:
#             if '#'+c_people in i:
#                 if '#'+c_people == i[i.index('#')::]:
#                     print(i[:i.index('#')])



'''----------------------------------------------------------------------'''




































