#设消极的购买数为x，母鸡购买数为y，公鸡购买数为z
#设count为变量计算程序运行次数
count=0
for x in range(0,101):
    for y in range(0,51):#极端情况下100元只能买50只母鸡
        for z in range(0,34):#极端情况下100元只能买33只公鸡
            if x*0.5+y*2+z*3==100 and x+y+z==100:
                print('小鸡：',x,'只，母鸡：',y,'只，公鸡：',z,'只')
            count+=1
print('程序运行的次数：',count)












