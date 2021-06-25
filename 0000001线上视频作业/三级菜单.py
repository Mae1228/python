# d={
#     '海南省':
#         {
#             '海口市':['美兰区','海甸岛','秀英区'],
#             '三亚市':['sanya1','sanya2','sanya3','snaya4'],
#             '文昌市':['文城','迈号','东郊','重兴']
#         },
#     '黑龙江省':
#         {
#             '哈尔滨市':['南岗区','和平大街','太阳岛'],
#             '绥化市':['绥化1','绥化2','绥化3','绥化4'],
#             '齐齐哈尔市':['齐齐哈尔1','齐齐哈尔2','齐齐哈尔3','齐齐哈尔4']
#         },
#     '广州省':
#         {
#             '广东市':['广东1','广东2','广东3'],
#             '深圳市':['深圳1','深圳2','深圳3','深圳4'],
#             '珠海市':['珠海1','珠海2','珠海3','珠海4']
#         }
# }
#
# print('welcome third class menu')
# tuic=True
# biao=1
# while tuic:
#     if biao==1:
#         while 1:
#             sheng_list=[]
#             for v,i in enumerate(d.keys(),1):
#                 print(v,'>>>>>',i)
#                 sheng_list.append(i)
#             chioce1=input('【省份】请输入您的选择：0退出，1查看下一级')
#             if chioce1.isdigit():
#                 chioce1=int(chioce1)
#                 if chioce1==0:
#                     tuic=False
#                     break
#                 elif chioce1==1:
#                         sheng = input('【省份】请输入你要查看省份的选项：')
#                         if sheng.isdigit():
#                             sheng = int(sheng)
#                             if sheng > 0 and sheng <= len(sheng_list):
#                                 biao=2
#                                 break
#                             else:
#                                 pass
#                         else:
#                             pass
#                 else:
#                     pass
#             else:
#                 pass
#
#     if biao==2:
#         while 1:
#             shi_list = []
#             for v, i in enumerate(d[sheng_list[sheng - 1]].keys(), 1):
#                 print(v, '>>>>>', i)
#                 shi_list.append(i)
#             chioce2 = input('【市级】请输入您的选择：0退出，1查看下一级，2返回上一级')
#             if chioce2.isdigit():
#                 chioce2 = int(chioce2)
#                 if chioce2 == 0:
#                     tuic = False
#                     break
#                 elif chioce2 == 1:
#                     shi = input('【市级】请输入你要查看的市：')
#                     if shi.isdigit():
#                         shi = int(shi)
#                         if shi > 0 and shi <= len(shi_list):
#                             biao=3
#                             break
#                         else:
#                             pass
#                     else:
#                         pass
#                 elif chioce2 == 2:
#                     biao=1
#                     break
#             else:
#                 pass
#
#     if biao==3:
#         while 1:
#             for i in d[sheng_list[sheng - 1]].items():
#                 if shi_list[shi - 1] == i[0]:
#                     for m, n in enumerate(i[1], 1):
#                         print(m, '>>>>', n)
#                     break
#             chioce3 = input('【乡镇】请输入您的选择：0退出，2返回上一级')
#             if chioce3.isdigit():
#                 chioce3 = int(chioce3)
#                 if chioce3 == 0:
#                     tuic = False
#                     break
#                 elif chioce3 == 2:
#                     biao=2
#                     break
#                 else:
#                     pass
#             else:
#                 pass











menu={
    '海南省':
        {
            '海口市':{
                '美兰区':{
                    '白坡里':{},
                    '仙迹林':{},
                    '南立交大桥':{}
                },
                '海甸岛':{},
                '秀英区':{}
            },
            '三亚市':{
                'sanya1':{},
                'sanya2':{},
                'sanya3':{},
                'snaya4':{}
            },
            '文昌市':{
                '文城':{},
                '迈号':{},
                '东郊':{},
                '重兴':{}
            }
        },
    '黑龙江省':
        {
            '哈尔滨市':{
                '南岗区':{},
                '和平大街':{},
                '太阳岛':{}
                },
            '绥化市':{
                '绥化1':{},
                '绥化2':{},
                '绥化3':{},
                '绥化4':{}
            },
            '齐齐哈尔市':{
                '齐齐哈尔1':{},
                '齐齐哈尔2':{},
                '齐齐哈尔3':{},
                '齐齐哈尔4':{}
            }
        },
    '广州省':
        {
            '广东市':{
                '广东1':{},
                '广东2':{},
                '广东3':{}
            },
            '深圳市':{
                '深圳1':{},
                '深圳2':{},
                '深圳3':{},
                '深圳4':{}
            },
            '珠海市':{
                '珠海1':{},
                '珠海2':{},
                '珠海3':{},
                '珠海4':{}
            }
        }
}
current_layer=menu
# parent_layer=menu
parent_list=[]
while True:
    for key in current_layer:
        print(key)
    choice=input('>>>').strip()
    if len(choice)==0:continue
    if choice in current_layer:
        # parent_layer=current_layer
        parent_list.append(current_layer)
        current_layer=current_layer[choice]
    elif choice=='b':
        # current_layer=parent_layer
        if parent_list:
            current_layer=parent_list.pop()
    else:
        print('无此项')