num = int(input('请输入一个任意整数,我将计算出从2到这个数字之间的所有素数:'))

#哥德巴赫猜想挑战包
a = []
for j in range(2, num):
    flag = 1     # flag等于1时是素数，等于0时不是素数
    i = 2
    while i < j:
        if j % i == 0:
            flag = 0
            break
        else:
            i += 1
    if flag == 1:
        print(j)
        a.append(j)

n2 = int(input('输入一个正偶数：'))


for i in a:
    for j in a:
        ans = i+j
        if ans == n2:
            print(i,j)



