'''练习3成果包——绝句v1.0'''
'''
当前文件夹中有一文件“绝句.txt”，其中包含一首诗文。
编写程序，去除文件中的空行，并写入新文件“绝句v1.0.txt”中。
'''

with open('绝句.txt', 'r') as f0:
    u=f0.readlines()
with open('绝句v1.0.txt', 'w') as f1:
    for i in u:
        if i!='\n':
            f1.write(i)


#方法一：
f0 = open('绝句.txt')
f1 = open('绝句v1.0.txt','w')
for i in f0.readlines():
    if i != '\n':
        f1.write(i)
f0.close()
f1.close()

#方法二：
s = ''
with open('绝句.txt') as f0:
    for i in f0.readlines():
        if i != '\n':
            s +=i
with open('绝句v1.0.txt', 'w') as f1:
    f1.write(s)

#方法三：
with open('绝句.txt') as f0:
    with open('绝句v1.0.txt', 'w') as f1:
        for i in f0.readlines():
            if i != '\n':
                f1.write(i)


