#闰到何时
m30=[4,6,9,11]
m31=[1,3,5,7,8,10,12]
year=int(input('请输入年：'))
month=int(input('请输入月：'))
if month==2:
    #闰年：四年一闰，百年不闰，四百年再闰
    if year%4==0 and year%100!=0 or year%400==0:
        print('%s年2月是闰年，有29天'%(year))
    else:
        print('%s年2月是平年，有28天' %(year))
elif month in m30:
    print('%s年%s月有30天'%(year,month))
elif month in m31:
    print('%s年%s月有31天' % (year, month))
else:
    print('月份输入错误')







