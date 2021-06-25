'''练习1成果包——静夜思v1.0'''
'''
当前文件夹中有一文件“静夜思.txt”，其中包含一首诗文。
编写程序，将诗文排版成要求的样式，并写入新文件“静夜思v1.0.txt”中。
'''

with open('静夜思.txt') as f0:
    data = f0.read()
with open('静夜思v1.0.txt', 'w') as f1:
    datalist = data.split(' ') #以空格符进行分隔
    print(datalist)
    for i in datalist:
        f1.write(i)     
        f1.write('\n')      #添加换行符






