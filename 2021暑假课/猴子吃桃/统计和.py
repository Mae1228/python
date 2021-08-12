'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
如2+22+222+2222+22222（此时共有5个数相加），几个数相加有键盘控制


'''
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# join()方法语法：str.join(要连接的元素序列)
#返回通过指定字符连接序列中元素后生成的新字符串。
a=int(input('请输入数字：'))      #层数
count=int(input('请输入相加的个数：'))
get_sum=0   #统计和
l=[]
for i in range(1,count+1):
    num=int(str(a)*i)   #字符串的*代表复制
    get_sum += num
    l.append(str(num))      #为了使用join方法拼接打印出来
print(str(get_sum)+'='+'+'.join(l))


