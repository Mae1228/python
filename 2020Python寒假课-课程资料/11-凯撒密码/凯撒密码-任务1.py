#凯撒密码程序
letter=input('输入一个要加密的字母：')
#将字符串转换成ASCII码，数字移动13个顺位
value=ord(letter)+13
#将新的加密的数字转换成字符
letter=chr(value)
print('加密后的字母结果是：',letter)
# exit=input('按下回车键，离开源码世界......')
