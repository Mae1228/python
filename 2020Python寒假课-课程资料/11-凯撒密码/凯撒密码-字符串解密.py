#凯撒密码程序
message=input('输入一个要解密的字符串：')
message=message.upper()
output=''
for letter in message:
    if letter.isupper():#判断letter是字母，不是其他值
        # 将字符串转换成ASCII码，数字移动13个顺位
        value = ord(letter) - 13
        # 将新的加密的数字转换成字符
        letter = chr(value)
        if not letter.isupper():#超出字母表
            value=value+26
            # 将新的加密的数字转换成字符
            letter = chr(value)
        output=output+letter
    else:
        print('输入错误！')
        break
else:
    print("解密后的字符串结果是：",output)




