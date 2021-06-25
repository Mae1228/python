print('判断您的成绩水平')
a=int(input('请输入一个数字：'))
if a>100:
    print('输入错误，请输入不大于100的分数')
elif a==100:
    print('满分')
elif a>=90:
    print('优秀')
elif a>=80:
    print('良好')
elif a>=70:
    print('中等')
elif a>=60:
    print('及格')
elif a>=0:
    print('不及格')
elif a<0:
    print('输入错误，请输入不小于0的分数')
