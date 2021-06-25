#凯撒密码程序
letter=input('输入一个要加密的字母：')
letter=letter.upper()
if letter.isupper():
    # 将字符串转换成ASCII码，数字移动13个顺位
    value = ord(letter) + 13
    # 将新的加密的数字转换成字符
    letter = chr(value)
    if not letter.isupper():
        value=value-26
        # 将新的加密的数字转换成字符
        letter = chr(value)
    print("加密后的字母结果是：",letter)
else:
    print('输入错误！')




# #凯撒密码-单字母加密流程
# #利用input获取键盘输入一个字母赋值给word
# word=input("请输入一个要加密的字母")
# #使用upper()内置方法将获取的字母转换为大写字母,ps标点符号则不会进行转换
# word=word.upper()
# #使用isupper（）内置方法判断是否为大写字母，不是的话就不进行转换
# if  word.isupper():
#     #利用ord（）获取字母的ASCII码，并前移3位数，赋值给变量value
#     value=ord(word)-3
#     #利用chr()将ASCII码转化为字母，并赋值给word
#     word=chr(value)
#     #判断word是否为大写字母
#     if not word.isupper():
#         #如果不是，将上一步获取的value的ASCII码后移26位
#         value=value+26
#         #将移动后的value用chr()转化为字母，赋值给word
#         word=chr(value)
#     #转化完成，输出转化后结果word的内容
#     print("凯撒密码加密后结果是：",word)