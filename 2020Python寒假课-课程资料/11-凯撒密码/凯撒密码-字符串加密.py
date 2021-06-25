#凯撒密码程序
message=input('输入一个要加密的字符串：')
message=message.upper()
output=''
for letter in message:
    if letter.isupper():#判断letter是字母，不是其他值
        # 将字符串转换成ASCII码，数字移动13个顺位
        value = ord(letter) + 13
        # 将新的加密的数字转换成字符
        letter = chr(value)
        if not letter.isupper():#超出字母表
            value=value-26
            # 将新的加密的数字转换成字符
            letter = chr(value)
        output=output+letter
    else:
        print('输入错误！')
        break
else:
    print("加密后的字符串结果是：",output)




# #凯撒密码-字符串加密
# #利用input获取键盘输入一个字符串赋值给message
# message=input("请输入一个要解密的字符串:")
# #利用upper（）将message字符串内容全部转化为大写字母
# message=message.upper()
# #新建字符串变量output，并赋值为空字符串“”,接收加密后的空字符串
# output=" "
# #利用for循环，依次将message的字母赋值给word，并且处理
# for word in message:
#     #判断是否为大写字母，不是得话就不进行转换
#     if word.isupper():
#         #利用ord()获取字母的ASCII码，并前移13位数，赋值给变量value
#         value=ord(word)+3
#         #利用chr()将ASCII码转化为字母，并赋值给word
#         word=chr(value)
#         #判断word是否为大写字母
#         if not word.isupper():
#             #如果不是，将上一步获取的value的ASCII码后移26位（一个字母表）
#             value=value-26
#             #将移动后的value用chr()转化为字母，赋值给word
#             word=chr(value)
#         #将转换后的字母，拼接到字符串output中
#         output=output+word
# #字符串转换完成，打印出转换后结果output
# print("凯撒密码加密后结果是：",output)