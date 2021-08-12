'''
有四个数字：1、2、3、4，能组成多少个互不相同且五重复数字的三位数？各是多少？


'''
count=0     #计数器
for i in range(1,5):    #百位的数字可以是1，2，3，4
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:  #百位 十位 个位的数字不重复
                count+=1                #符合条件计数器就+1
                print(i*100+j*10+k)         #打印符合条件的三位数
print('一共有',count,'种可能性',sep='')










