'''闰年计算器-练习4'''

#闰年计算器：if elif else嵌套
year = input('请输入年份：')
#year变量调用和重新赋值
year = int(year)
#判断语句
if year % 400 == 0:  # 世纪年能被400整除的是闰年
    print(year, '年是世纪闰年', sep='')
elif year % 4== 0:  # 普通年不能被100整除且能被4整除且的为闰年
    if year % 100!= 0:
        print(year, '年是普通闰年', sep='')
    else:
        print(year, '年不是闰年', sep='')
else:
    print(year, '年不是闰年', sep='')
