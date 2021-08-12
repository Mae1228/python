'''
题目：一个数如果恰好等于它的因子之和，这个数称为“完数”。
例如6=1+2+3，编程找出范围内的所有完数


'''
a1=int(input(' 请输入开始数字：'))
a2=int(input(' 请输入终止数字：'))
for i in range(a1,a2+1,1):
    num_list=[]
    for j in range(1,i):
        if i%j==0:
            num_list.append(j)
    num_list_str=[]
    if sum(num_list)==i:
        for k in num_list:
            num_list_str.append(str(k))
        str1='+'.join(num_list_str)
        print(i,'=',str1,sep='')









