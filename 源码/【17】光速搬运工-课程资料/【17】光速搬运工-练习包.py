'''光速搬运工-练习包'''

# 实践1
# 只读打开文本
f = open('学习日记.txt','r')
# 只读打开二进制
f = open('房子.png','rb')
# (覆盖)写入模式打开二进制
f = open('房子.png','wb')
# 追加写入文本
f = open('学习日记.txt','a')


# 实践2
f = open('B:\\自传.txt','w')
f.write('我喜欢学Python')
f.close()
f = open('B:\\自传.txt', 'r')
s = f.read()
print(s)
f.close()


