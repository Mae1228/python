'''三角形公式大师——成果包'''
#判断是否是三角形
def triangle_check(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        return True
    else:
        return False

# 计算三角形周长和面积
def triangle_area(a, b, c):
    #计算三角形周长
    C = a + b + c
    # 计算三角形面积
    p = C / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    S = round(S, 1)
    return C, S

#三角形类型判断
def triangle_sort(a, b, c):
    if a == b == c:
        return '等边三角形'
    elif a == b or a == c or b == c:
        return '等腰三角形'
    elif a**2+b**2 == c**2 or b**2+c**2 == a**2 or a**2+c**2 == b**2:
        return '直角三角形'
    else:
        return '普通三角形'

# 定义主函数
def triangle(a,b,c):
    #调用函数triangle_check()判断是否是三角形
    if triangle_check(a, b, c): 
        #调用函数triangle_area()计算周长和面积     
        C = triangle_area(a, b, c)[0]
        S = triangle_area(a, b, c)[1]
        #调用函数triangle_sort()判断三角形类型
        T = triangle_sort(a, b, c)
        return C, S, T
    else:
        return '不是三角形'

#例子测试
print(triangle(5, 5, 5))
print(triangle(2, 2, 3))
print(triangle(3, 4, 5))
print(triangle(3, 5, 6))
print(triangle(1, 2, 3))
