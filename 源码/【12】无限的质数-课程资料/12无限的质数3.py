'''无限的质数-阶段3'''

#搜索一定范围内的所有质数
head = int(input('请输入起始数：'))
tail = int(input('请输入终止数：'))
for i in range(head, tail + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
