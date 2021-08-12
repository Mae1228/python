'''练习2成果包——静夜思v2.0'''
'''
编写程序读取练习1排版后的文件“静夜思v1.0.txt”，将诗文
排版成练习2要求的样式，并写入新文件“静夜思v2.0.txt”中。
'''

#方法一：
with open('静夜思v1.0.txt') as f1:
    data1 = f1.readline()    
    data2 = f1.readline()   
    datas = f1.readlines()
with open('静夜思v2.0.txt', 'w') as f2:
    f2.write("   "+data1)
    f2.write("唐朝 "+data2)
    f2.writelines(datas)  

# #方法二：
# with open('静夜思v1.0.txt') as f1:
#     data1 = f1.readline()
#     data2 = f1.readline()
#     datas = f1.read()
# with open('静夜思v2.0.txt', 'w') as f2:
#     f2.write("   "+data1)
#     f2.write("唐朝 "+data2)
#     f2.write(datas)













