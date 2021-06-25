'''神秘逻辑-练习三'''

'''猴子每天吃一半再多吃一个，吃到第十天再想吃的时
候，发现只剩一下一个了，求最开始多少个'''
# 猴子吃香蕉函数
def monkey(day) :
	# 倒数第day天
	if day == 1 :
		return 1
	else :
		# 推给倒数第day-1天
		return (monkey(day - 1) + 1) * 2

d = int(input('请输入今天是第几天：'))
print(monkey(d))	
