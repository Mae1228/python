'''闰年计算器-练习5'''

#闰年计算器：结合逻辑运算，减少嵌套
year = input('请输入年份：')
#year变量调用和重新赋值
year = int(year)
#判断语句
if year % 400 == 0:
    print(year, '年是世纪闰年', sep='')
elif year % 4 == 0 and year % 100 != 0:
    print(year, '年是普通闰年', sep='')
else:
    print(year, '年不是闰年', sep='')


