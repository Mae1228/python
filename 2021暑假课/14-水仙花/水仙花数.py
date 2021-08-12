#水仙花
count=0
for num in range(100,1000):
    g=num%10
    s=num//10%10
    b=num//100
    if g*g*g+s*s*s+b*b*b==num:
        print(num,'是水仙花数')
        count+=1
print('1000以内的水仙花数共计：',count,'个')







