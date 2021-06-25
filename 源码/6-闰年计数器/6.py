a=int(input('请输入年份：'))
if a%400==0:
    print(a,'年是世纪闰年',sep='')
elif a%4==0 and a%100!=0:

        print(a, '年是普通闰年', sep='')

else:
    print(a, '年是ping年', sep='')


















