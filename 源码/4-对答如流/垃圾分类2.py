'''练习2成果包——垃圾分类v2.0'''
'''
自行完善垃圾分类的判断
分类：
1.有害：锂电池
2.可回收：作业纸、塑料、电池
3.厨余：鱼骨、炒米饭、鸡蛋壳
4.其它：大棒骨、渣土、污染纸
根据以上提示的垃圾分类方式，制作垃圾分类提示小帮手，输入要扔的垃圾，给出判定类型
如:
Input:
请输入要丢弃的垃圾：电池
Output:
可回收垃圾
'''

rubbish1 = '锂电池'
rubbish2 = '作业纸、塑料、电池'
rubbish3 = '鱼骨、炒米饭、鸡蛋壳'
rubbish4 = '大棒骨、渣土、污染纸'
message = input('请输入要丢弃的垃圾：')
if message in rubbish2:
    print('可回收垃圾')
elif message in rubbish1:
    print('有害垃圾')
elif message in rubbish3:
    print('厨余垃圾')
elif message in rubbish4:
    print('其他垃圾')
