'''
两个或多个整数共有的倍数叫做公倍数。
公倍数里最小的那个叫做他们的最小公倍数。
输入两个整数，输出他们的最小公倍数
'''
a1=int(input('请输入第一个数字：'))
a2=int(input('请输入第二个数字：'))
max=0
if a1>a2:
    max=a2
else:
    max=a1
while True:
    if max%a1==0 and max%a2==0:
        print(max)
        break
    max+=1






