#闰到何时
years=input('请输入一个四位数年份：')
years=int(years)
if years%4==0 and years%100!=0:
    print(years,'是闰年')
elif years%400==0:
    print(years,'是闰年')
else:
    print(years,'不是闰年，一年只有365天')













