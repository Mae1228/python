'''神秘逻辑——练习二'''

# 反向输出字符串
def myreverse(s):
    if s == '':
        return ''
    else:
        return myreverse(s[1:])+s[0]

msg =  input('请输入字符串：')
print(myreverse(msg)) 

