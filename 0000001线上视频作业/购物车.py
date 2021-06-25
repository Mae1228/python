# list_sp=['apple','mac book','python book','coffee','bicyle']
# list_price=[5000,9000,60,23,1500]
# list_sell=[]
# salary=int(input('请输入您的工资：'))
# for i in list_sp:
#     for j in list_price:
#         if list_sp.index(i) == list_price.index(j):
#             print(list_sp.index(i) + 1, '.', end='')
#             print(i,j,sep='\t')
# while True:
#     choice1=input('请输入你要购买的选项：')
#     if choice1=='quit':
#         print('您购买一下商品如下：')
#         biaoh=1
#         for i in list_sell:
#             print(biaoh, '.', end='')
#             print(i,list_price[list_sp.index(i)],sep='\t')
#             biaoh+=1
#         print('您的余额为：',salary)
#         print('欢迎下次光临')
#         break
#     choice=int(choice1)
#     if choice>=1 and choice<=5:
#         if salary<list_price[choice-1]:
#             print('余额不足',salary-list_price[choice-1])
#         else:
#             salary -= list_price[choice - 1]
#             list_sell.append(list_sp[choice-1])
#             print('已加入',list_sp[choice-1],'到购物车里面，当前余额为：',salary)
#     else:
#         print('没有该序号，请重新输入序号')




list_sp=[('iphone',5000),('ipad pro',6000),('python book',150),('mac book',10000),('coffe',30)]
save_monye=input('请输入您的金钱：')
shopping_car=[]
if save_monye.isdigit():
    save_monye=int(save_monye)
    while True:
        for i,v in enumerate(list_sp,1):
            print(i,'<<<<<<<<<<',v)
        choice=input('请输入商品序号：')
        if choice.isdigit():
            choice=int(choice)
            if choice>0 and choice<=len(list_sp):
                sp_money=list_sp[choice-1][1]
                if save_monye<sp_money:
                    print('余额不足,还差%d元才能购买此商品'%(sp_money-save_monye))
                else:
                    save_monye-=sp_money
                    for i in shopping_car:
                        if i[:2]==list(list_sp[choice-1]):
                            shopping_car[shopping_car.index(i)][2]+=1
                            break
                    else:
                        sp=list(list_sp[choice-1])
                        sp.append(1)
                        shopping_car.append(sp)
                    print('您已经添加%s到购物车里面，还剩下%d元'%(list_sp[choice-1][0],save_monye))
            else:
                print('请输入正确序号')

        elif choice=='q':
            print('--------------您已购买商品如下---------------')
            for i,v in enumerate(shopping_car,1):
                print('%d<<<<<<<购买%s，数量为%d，花了%d元'%(i,v[0],v[2],v[1]*v[2]))
            print('您还剩余%d元,欢迎下次光临'%save_monye)
            break
        else:
            print('请输入正确的内容')
else:
    print('请输入正确的金钱')