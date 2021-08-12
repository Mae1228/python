#任意正整数累加求和
num=int(input('请输入一个正整数：'))
if num>0:
    sum=0
    for x in range(num+1):
        sum+=x
    print(sum)
else:
    print('输入有误')


















