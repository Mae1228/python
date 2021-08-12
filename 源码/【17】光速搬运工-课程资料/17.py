''''''
'''
文件操作：1、打开文件：f=open('文件路径及名称','打开模式',encoding='utf-8')
                      1、b：二进制模式--------图片、音频
                      2、t：文本模式-------默认
                      3、r：读取文件-------默认
                      4、w：写入文件，若文件存在则覆盖原有数据写入；若文件不存在则新建文件
                      5、a：写入，如果文件存在则在末尾追加；若文件不存在则新建文件进行写入
          2、读/写文件（传入值都是str类型）：1、读文件：s=f.read()--------将数据存为一个字符串
                        2、写文件：f.write('数据')-------写入字符串数据
          3、关闭文件：f.close()
open()与close()成对使用
with语句能够在文件使用后快速关闭文件
with open()=open()+close()
with语句格式：with open('文件路径及文件名','打开模式') as 变量:
绝对路径：总是从根文件夹开始，Window 系统中以盘符（C：、D：）作为根文件夹，而OSX或者Linux系统中以/作为根文件夹。
相对路径：指的是文件相对于当前工作目录所在的位置。（其中 .\ 就表示当前所在目录）
    注意：我们常用’/‘来表示相对路径，’\‘来表示绝对路径，上面的路径里\\是转义的意思。
        此外，网页网址和linux、unix系统下一般都用’/‘。
utf-8：以8位为一个编码单位的可变长编码；编码规则。
'''
'''实践一'''
# f=open('学习日记.txt','r')
# f.close()
# f=open('房子.png','br')
# f.close()
# f=open('房子.png','wb')
# f.close()
# f=open('学习日记.txt','a')
# f.close()


'''实践二'''
# f=open('自传.txt','w')
# f.write('我喜欢学Python')
# f.close()
# f=open('自传.txt','r')
# s=f.read()
# print(s)
# f.close()


'''光速搬运工'''
# with open('房子.png','br') as t:
#     pic=t.read()
# with open('房子1.png','bw') as t1:
#     t1.write(pic)


'''---------------------------------------------------------------'''















