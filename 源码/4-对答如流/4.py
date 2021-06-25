# # yh='锂电池'
# # khs='作业纸，塑料，电池'
# # message=input('qing:')
# # if message in khs:
# #     print('可回收垃圾')
# # elif message in yh:
# #     print('有害垃圾')
# # else:
# #     print('qita')
# # a=input('qing:')
# # if '骨' in a:
# #     if '大棒骨'==a:
# #         print('qita')
# #     else:
# #         print('厨余')
# # else:
# #     print('zhe')


# s=input('性别：')
# w=input('体重kg：')
# w=int(w)
# h=int(input('身高cm：'))
# if '女'==s:
#     nbiao=h-110
#     d=w-nbiao
#     if d>3:
#         print('pang')
#     elif d<-3:
#         print('shou')
#     else:
#         print('biao')
# else:
#     biao = h - 100
#     d = w - biao
#     if d > 3:
#         print('pang')
#     elif d < -3:
#         print('shou')
#     else:
#         print('biao')
#
#
#
#
#

s=input('请输入您的性别:')
w=int(input('请输入您的体重（kg）:'))
h=int(input('请输入您的身高（cm）:'))
if s=='男':
    d1=w-(h-100)
    if d1<-3:
        print('轻')
    elif d1>3:
        print('zhong')
    else:
        print('biao')
if s=='女':
    d = w - (h - 110)
    if d < -3:
        print('轻')
    elif d > 3:
        print('zhong')
    else:
        print('biao')










