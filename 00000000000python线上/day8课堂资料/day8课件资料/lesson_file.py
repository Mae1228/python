#__author:  Administrator
#date:  2016/8/26

############################基本流程
#能调用方法的一定是对象
# li=[1,2,3]
# li.append('2')
# 'asc'.capitalize()

# import time
#三种基本的操作模式 r(只可读) w（只可写） a（追加）
#流程：1 创建文件对象 2 调用文件方法进行操作  3 关闭文件

# f=open('小重山2','r',encoding='utf8')
# f.write()#报错

# data=f.read(5)
# print(data)
# f.write('\nhello world \n')
# f.write('alex')
#
#注意：if not close,数据会缓存，而不是磁盘！
# time.sleep(30)
# f.close()




################################具体操作方法

# f=open('小重山','a',encoding='utf8')

# print(f.read(5))
# print(f.read(5))# 注意 ：汉字在这里占一个单位（in Py3）

# a=f.readline()
# print(a)

# print(f.readline())
# print(f.readline())#无论是read()还是readline(),光标会发生位置变化

# print(f.readlines())#['昨夜寒蛩不住鸣。\n', '惊回千里梦，已三更。\n', '起来独自绕阶行。\n', '人悄悄，帘外月胧明。\n', '白首为功名，旧山松竹老，阻归程。\n', '欲将心事付瑶琴。\n', '知音少，弦断有谁听。']



#实例打印文件

# data=f.readlines()#注意及时关闭文件
# f.close()

# number = 0
# for i in data:
#     number += 1

#     if number == 6:
#         i = ''.join([i.strip(), 'iiiii'])  # 取代万恶的+
#     print(i.strip())
# f.close()

##########对于大数据文件，要用以下方式（the best way）：
# number=0
# for i in f:#这是for内部将f对象做成一个迭代器，用一行去一行。
#     number+=1
#     if number == 6:
#         i = ''.join([i.strip(), 'iiiii'])  # 取代万恶的+
#     #     print(i.strip())
#     print(i.strip())



# print(f.tell())#  取出光标位置
# print(f.read(2))
# print(f.tell())
#
# f.seek(0)#  移动光标到指定的位置
# print(f.read(4))

#flush():同步吧将数据从缓存转移到磁盘上去
##进度条实例
# import sys,time
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.1)


#print的flush
# import sys,time
# for i in range(30):
#
#     print('*',end='',flush=True)
#
#     time.sleep(0.1)
# f=open('小重山','r',encoding='utf8')


#truncate（）：截断数据(不能在r模式下)
#在w模式下：先清空，再写，再截断
#在a模式下：直接将指定位置后的内容截断
# f.truncate(5)
# f.write('hello world')
# f.truncate(5)
# f.close()


##### r+, w+, a+

# r+:光标默认在0位置，最后位置开始写
# w+:先清空，再写读
# a+:光标默认在最后位置


# f=open('小重山','r+',encoding='utf8')
# print(f.tell())
# print(f.readline())
# f.write('岳飞')
# print(f.tell())
# f.seek(0)
# print(f.readline())
# f.close()

# 终极问题 如何在磁盘修改文件
# 常规思路，由于磁盘存储机制不能完成
# number=0
# for line in f:
#     number+=1
#     if number==3:
#         f.write('alex')


#只能采取重新创建一个文件的思路
# f_read=open('小重山','r',encoding='utf8')
# f_write = open('小重山2','w',encoding='utf8')

# number=0
# for line in f_read:
#     number+=1
#     if number==5:
#         line=''.join([line.strip(),'alex\n'])
#         # line='hello 岳飞\n'
#     f_write.write(line)
#
#
# f_read.close()
# f_write.close()


######作业涉及方法
# a=str({'beijing':{'1':111}})
# print(type(a))
# print(a)#     '{'beijing':{'1':111}}'
# a=eval(a)
# print(type(a))
# print(a['beijing'])

# f=open('log', 'r')
# f.readline()
# f.read()
# f.close()

# with open('log', 'r') as f:
#     f.readline()
#     f.read()
# print('hello')

#with 同时管理多个文件对象
# with open('log1','r') as f_read, open('log2','w') as f_write:
#     for line in f_read:
#         f_write.write(line)































