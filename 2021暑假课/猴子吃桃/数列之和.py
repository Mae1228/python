'''

题目: 求1+2!+3!+...+20!的和


'''
# 阶乘：所有小于及等于该数的正整数的积，并且0的阶乘为1。自然数n的阶乘写作n!。

while True:
    num=input('请输入num:')
    if num.isdigit():   #字符串都为数字才能为真，如：3.5为假
        num = int(num)
        if num>1:
            break
        else:
            print('请输入大于1的数字')
    else:
        print('请输入数字')
get_sum=0   #统计和
cheng_ji=1     #记住前一个数的阶乘
for i in range(1,num+1):
    cheng_ji*=i
    get_sum+=cheng_ji
if num>3:
    print('1+2!+3!+...+%d!=%d'%(num,get_sum))
else:
    print('1+...+%d!=%d' % (num, get_sum))












