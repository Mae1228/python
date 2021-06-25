'''练习4成果包——智能体重秤'''
'''
智能体重秤
计算公式：
男士标准体重 = 身高 - 100 
女士标准体重 = 身高 - 110 
注：与标准体重相差3kg以内均算标准
根据以上提示制作智能体重秤，分别输入性别、体重、身高，给出判断结果
如
例1:
Input:
请输入您的性别：男
请输入您的体重：65
请输入您的身高：178
Output:
您的体重非常标准！
例2:
Input:
请输入您的性别：女
请输入您的体重：50
请输入您的身高：165
Output:
您需要补充营养!
例2:
Input:
请输入您的性别：男
请输入您的体重：50
请输入您的身高：165
Output:
您需要减肥了!
'''

gender = input('请输入您的性别:')
weight = int(input('请输入您的体重（kg）:'))
height = int(input('请输入您的身高（cm）:'))
d = 0
if gender == '男':
    d = weight - (height - 100)
    if d > 3:
        print('您需要减肥了!')
    elif d < -3:
        print('您需要补充营养!')
    else:
        print('您的体重非常标准！')
if gender == '女':
    d = weight - (height - 110)
    if d > 3:
        print('您需要减肥了!')
    elif d < -3:
        print('您需要补充营养!')
    else:
        print('您的体重非常标准！')


