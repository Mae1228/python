'''
题目: 猴子吃桃问题:猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

'''
#逆序思维

# 假设第一天有x1个桃子，第二天有x2个桃子
# x1-(x1/2+1)=x2---------x1=2*(x2+1)
jt=1    #定义第10天的桃子数
qt=0    #定义第9天的桃子数
#第九天的桃子数=（第十天的桃子数+1）*2
for i in range(9,0,-1):
    qt=2*(jt+1)
    jt=qt
    print('第%d天的桃子数量为：%d'%(i,qt))


'''第二种写法'''
# peach=1     #定义第10天的桃子数
# #第九天的桃子数=（第十天的桃子数+1）*2
# for i in range(10,1,-1):
#     peach=(peach+1)*2
#     print('第%d天的桃子数量为：%d'%(i-1,peach))
