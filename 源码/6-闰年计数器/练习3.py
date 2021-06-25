'''闰年计算器-练习3'''

#闰年计算器：if else 嵌套
year = input('请输入年份：')
#year变量调用和重新赋值
year = int(year)
#判断语句
if year % 100 == 0:  # 判断世纪年
    if year % 400 == 0:  # 判断被400整除的世纪年是闰年
        print(year, '年是世纪闰年', sep='')
    else:
        print(year, '年不是闰年', sep='')
else:
    if year % 4 == 0:  # 判断被4整除的普通年是闰年
        print(year, '年是普通闰年', sep='')
    else:
        print(year, '年不是闰年', sep='')
