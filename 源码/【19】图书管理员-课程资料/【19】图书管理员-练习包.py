'''图书管理员-练习包'''

# 实践1
mylist = ['c','o','d','e','m','a','o']
for i in mylist:
    print(i)


# 实践2
s = 'hello codemao'
# 1小题
print(s[8])
# 2小题
print(s[6:10:1])
# 3小题
print(s[0:14:2])
stop = len(s)
print(s[0:stop:2])


# 实践3
s = 'hello codemao !'
mylist = []
for i in s:
    if i != ' ':
        mylist.append(i)
mylist.remove('!')
print(mylist)


