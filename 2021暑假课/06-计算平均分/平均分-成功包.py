# 分数列表化
scoreTotal=[
    [72,80,66,86],
    [70,50,40,60],
    [60,60,82,66]
]
#计算每人总分
name=['小明','小李','小华']
count=0
indxe=0
classScore=0
#遍历全班成绩
for student in scoreTotal:
    for s in student:
        count+=s
    print(name[indxe],'的总分为：',count,'平均分为：',count//len(student))
    indxe+=1
    classScore+=count
    count=0
print('全班总分：',classScore,'全班平均分：',classScore//(len(scoreTotal)*len(scoreTotal[0])))











