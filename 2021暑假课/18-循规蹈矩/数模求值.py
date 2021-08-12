#一个数模3剩2，模5剩3，模7剩2，求这个数
num=9
while num<1000:
    if num%3==2:
        if num%5==3:
            if num%7==2:
                print('一个数模3剩2，模5剩3，模7剩2，这个数是：',num)
                break
    num+=1



















