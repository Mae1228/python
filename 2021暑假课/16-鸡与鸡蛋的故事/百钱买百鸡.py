#基础解法：循环嵌套
#设小鸡的购买数为x，母鸡购买数为y，公鸡购买数为z
'''
小鸡每只5毛，母鸡每只2元，公鸡每只3元。求百元可以有几种购买方式？

'''
count=0
for x in range(0,101):
    for y in range(0,101):
        for z in range(0,101):
            if x*0.5+y*2+z*3==100 and x+y+z==100:
                print('小鸡：',x,'只，母鸡：',y,'只，公鸡：',z,'只')
            count+=1
print('程序运行的次数：',count)








