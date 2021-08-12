tou=int(input('请输入鸡兔头总数：'))
jiao=int(input('请输入鸡兔脚总数：'))
if tou>=0 and jiao>=0:
    for j in range(0,tou+1,1):
        if 2*j+4*(tou-j)==jiao:
            print('鸡的数量是：',j)
            print('兔子的数量是：',tou-j)
            break
    else:
        print('无解，没有该组合')
else:
    print('输入错误')













