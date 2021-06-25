'''无限的质数-阶段2'''

#搜索一定范围内的所有质数
head = int(input('请输入起始数：'))
tail = int(input('请输入终止数：'))
for i in range(head, tail + 1):
    check = 0
    for j in range(2, i):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        print(i)

