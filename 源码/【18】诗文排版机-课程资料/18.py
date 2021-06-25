''''''
'''
split() 方法：可以将一个字符串按照指定的分隔符分成多个子串。
              格式：str.split(sep,maxsplit)
                    str：要进行分割的字符串
                    sep：分隔符，可以包含多个字符。
                    maxsplit：可选，用于指定分割次数，子串的个数最多为maxsplit+1，
                              如若不指定，则分割次数没有限制。
转义字符：\
反斜杠：\\
双引号：\"
单引号：\'
换行：\n
回车：\r   输出回到本行行首，结果可能会将这一行之前的输出覆盖掉
横向制表符：\t    在终端和文件中的输出显示相当于按下键盘TAB键效果
文件读写方法：1、读：read()：一次性读取全部内容
                    readline()：读取一整行，包括"\n"字符
                    readlines()：读取所有行并返回列表
              2、写：write()：将字符串写入文件，返回的是写入的字符长度。
                     writelines()：向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''
''' 练习一'''
# with open('B:\\jingyesi.txt','r') as f:
#     j=f.read()
# with open('B:\\j.txt', 'w') as ff:
#     for i in j.split(' '):
#         ff.write(i+'\n')


''' 练习二  '''
# with open('B:\\j.txt', 'r') as f:
#     j=f.readline()
#     jj=f.read()
# with open('B:\\jj.txt','w') as ff:
#     ff.write('  '+j)
#     ff.write('唐代 '+jj)
#     print(ff.write(j))


''' 练习三  '''
# with open('B:\\jueju.txt', 'r') as f:
#     u=f.readlines()
# with open('B:\\u.txt', 'w') as ff:
#     for i in u:
#         if i!='\n':
#             ff.write(i)




'''--------------------------------------------------------------------------------------------------------------'''





















