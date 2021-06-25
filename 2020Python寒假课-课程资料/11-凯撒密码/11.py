''''''
'''
ASCII码：美国标准信息交换码（英文、数字、符号）----------Unicode（中文）
ord(字符)：把字符返回对应的 ASCII 数值，或者 Unicode 数值------内置函数
chr(ASCII码)：返回值是当前整数对应的 ASCII 字符-------内置函数
str.upper()：字符串中所有的字母都变成大写
str.isupper()：判断字符串中的所有字母是否全是大写，返回T或F
str.lower()：字符串中所有的字母都变成小写
str.islower()：判断字符串中的所有字母是否全是小写，返回T或F
str.swapcase()：字符串中的大小写相互转换
str.capitalize()：将字符串的第一个字母变成大写,其他字母变小写
str.title()：返回"标题化"的字符串,就是说所有单词都是以大写开始
'''
'''字母加密'''
# a=input('请输入要加密字母：')
# a=a.upper()
# if a.isupper():
#     a_v=ord(a)+3
#     a=chr(a_v)
#     if not a.isupper():
#         a_v-=26
#         a=chr(a_v)
#     print('加密后的字母结果是：',a)
# else:
#     print('输入错误！请输入字母')


'''字符串加密'''
# a1=input('请输入要加密字符串：')
# a1=a1.upper()
# b=''
# for a in a1:
#     if a.isupper():
#         a_v=ord(a)+3
#         a=chr(a_v)
#         if not a.isupper():
#             a_v-=26
#             a=chr(a_v)
#         b+=a
#     else:
#         print('输入错误！请输入字符串')
#         break
# else:
#     print('加密后的字符串结果是：',b)


'''字符串解密'''
# a1=input('请输入要解密字符串：')
# a1=a1.upper()
# b=''
# for a in a1:
#     if a.isupper():
#         a_v=ord(a)-3
#         a=chr(a_v)
#         if not a.isupper():
#             a_v+=26
#             a=chr(a_v)
#         b+=a
#     else:
#         print('输入错误！请输入字符串')
#         break
# else:
#     print('解密后的字符串结果是：',b)


















