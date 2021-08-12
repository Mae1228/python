'''
在六一儿童节的歌舞比赛上，共有5个评委给参赛选手进行评分。来帮忙评委进行评分。
你能帮他完成这个程序吗？
输入：输入5个整数（0到100之间，包括0和100），用空格隔开
输出：五个整数的平均分，四舍五入到整数部分
'''
a=input('输入5个整数：')
score=a.split(' ')
sum=0
for i in score:
    sum+=int(i)
pj=sum/5
# pj10=pj*10
# ys=pj10%10
# zs=int(pj10//10)
# if ys>=5:
#     zs+=1
#     print('平均分数是',zs)
# else:
#     print('平均分数是',zs)
print(round(pj))







