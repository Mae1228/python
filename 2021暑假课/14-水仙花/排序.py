'''
输入多个数字（以空格隔开），并且把这些数字降序或者升序排序

'''
a=input('请输入多个数字：')
num=a.split(' ')
sj=input('升序（1）还是降序（2）：')
px=[]
for i in range(len(num)):
    m = int(num[0])
    if sj == '1':
        for i in num:
            i=int(i)
            if i<m:
                m=i
    elif sj=='2':
        for i in num:
            i=int(i)
            if i>m:
                m=i
    else:
        print('输入错误，无法排序，程序停止')
        break
    px.append(m)
    num.remove(str(m))
else:
    print(px)















