#初始化列表
platform=[1,1,1,2,2,2,2,3,3,4,4,4,4,4,5,5,5,5,5,5,5]
#记录平台中每个数字出现的数量，更新新数字时归0
count=1
#记录列表中平台最大值
value=platform[0]
#记录列表中平台最大值的平台长度
max=0

#匹配
def compare(count,data):
    global value#声明全局变量
    global max#声明全局变量
    #此平台数字比原先平台数字长，则刷新max值
    if count>max:
        value=data
        max=count

#列表长度
platformLen=len(platform)
#遍历列表而非取出列表中每个元素的值
for i in range(platformLen):
    if i+1==platformLen:
        print(platform[i],'在平台中的长度：',count)
        compare(count, platform[i])
    elif platform[i]==platform[i+1]:
        count+=1
    else:
        print(platform[i-1],'在平台中的长度：',count)
        compare(count,platform[i])
        count=1
print('总结：平台数字最长值是[',value,']它的长度为：',max)




