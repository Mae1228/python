import random
#根据玩家属性表，构建出玩家的初始属性
hp=50
hpMax=100
mp=30
mpMax=100
#根据道具映射图，将道具编号添加到列表中
bag=[2,4,1,4,2,1,3,1]
userCode=input('指令：')
if userCode=='open':
    print('背包被打开')
    while True:
        #玩家指令匹配
        userCode=input('指令：')
        if userCode=='quit':
            print('关闭背包')
            break
        elif userCode=='open':
            print('您已经打开背包')
        elif userCode.isdigit()==True:
            # 背包位置验证
            userCodeValue = int(userCode)
            if userCodeValue > 0 and userCodeValue <= len(bag):
                bagIndex = userCodeValue - 1
                # 背包位置转换为道具代码
                prop = bag[bagIndex]
                #使用的道具设置为[-1]
                bag[bagIndex]=-1
                #匹配道具
                if prop==-1:
                    print('此道具已经被使用，请重新选择')
                elif prop==1:
                    hp+=10
                    if hp>hpMax:
                        hp=hpMax
                    print('您使用了一瓶红色药水')
                elif prop==2:
                    mp+=10
                    if mp>mpMax:
                        mp=mpMax
                    print('您使用了一瓶蓝色药水')
                elif prop==3:
                    hp+=10
                    if hp>hpMax:
                        hp=hpMax
                    mp += 10
                    if mp > mpMax:
                        mp = mpMax
                    print('您使用了一瓶绿色药水')
                elif prop==4:
                    print('您使用了一瓶黑色药水')
                    if random.randint(0,1)==0:
                        hp=hpMax
                        print('您太幸运了，健康达到最佳状态')
                    else:
                        hp=1
                        print('您太不幸了，健康达到最低状态')
                print('当前生命值为：',hp,'/',hpMax,'当前法力值为：',mp,'/',mpMax)
            else:
                print('请您输入背包的有效数值[1-8]')














