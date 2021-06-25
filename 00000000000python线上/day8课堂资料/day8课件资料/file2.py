#__author:  Administrator
#date:  2016/8/26


f=open('小重山2','w',encoding='utf8')
print(f.fileno())
f.write('lllll')
f.close()