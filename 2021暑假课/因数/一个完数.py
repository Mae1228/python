

a=int(input(' 请输入一个数字：'))
num_list = []
for j in range(1, a):
    if a % j == 0:
        num_list.append(j)
num_list_str=[]
if sum(num_list) == a:
    for i in num_list:
        num_list_str.append(str(i))
    str1 = '+'.join(num_list_str)
    print(a, '=', str1, sep='')
else:
    print('%d不是完数'%a)