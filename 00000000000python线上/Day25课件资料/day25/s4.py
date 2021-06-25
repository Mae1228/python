#__author:  Administrator
#date:  2016/9/23
"""
class Tearch:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.salary = 1000

class Course:

    def __init__(self, name, cost, tearcher):
        self.name = name
        self.tearcher = tearcher
        self.cost = cost

    def class_up(self):
        self.tearcher.salary += self.cost



t1 = Tearch('李杰' ,8)
t2 = Tearch('烧饼', 9)
t3 = Tearch('豆饼', 10)

c1 = Course('生理课', 1, t1)

print(c1.name)
print(c1.tearcher.age)
print(c1.tearcher.name)
print(c1.tearcher.salary)

c1.class_up()

print(c1.tearcher.salary)
"""

class F1:

    def __init__(self):
        self.name = 123

class F2:

    def __init__(self, a):
        self.ff = a # [name=123]

class F3:

    def __init__(self, b):
        self.dd = b

f1 = F1()  # [name=123]
f2 = F2(f1)# [ff=[name=123]]
f3 = F3(f2) # [dd=[ff=[name=123]]]
# 找到123并输出
print(f3.dd.ff.name)






