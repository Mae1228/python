'''练习1成果包——假期倒计时'''
'''
完成假期和考试天数倒计时小程序。
设定：考试日期和放假日期
输出：今天的日期和星期
	考试倒计时天数
	放假倒计时天数
'''
from datetime import date
a = date.today()
week = date.isoweekday(a)
print('今天是：'+str(a)+' 星期：'+str(week))
b = date(2020, 6, 28)
c = date(2020, 7, 1)
res1 = (b - a).days
res2 = (c - a).days
print('距离考试还有：'+str(res1)+'天')
print('距离暑假还有：'+str(res2)+'天')

