#__author:  Administrator
#date:  2016/9/21
"""
class Bar:

    def foo(self,arg):
        print(self,arg)

z1 = Bar()
print(z1)
z1.foo(111)
print('================')
z2 = Bar()
print(z2)
z2.foo(666)
"""

"""
class Bar:

    def foo(self,arg):
        print(self,self.name,self.age,self.gender, arg)

z = Bar()
z.name = 'alex'
z.age = 84
z.gender = 'zhong'
z.foo(666)

z1 = Bar()
z1.name = 'eric'
z1.age = 73
z1.gender = 'nv'
z1.foo(666)
"""

"""
class Bar:

    def foo(self):
        print(self.name)

z = Bar()

z.foo()
"""

# class Bar:
#     def __init__(self,n1,n2,n3):
#         self.nam1=n1
#         self.nam2=n2
#         self.nam3=n3
#         self.nam4=n3
#         self.nam5=n3
#         self.nam6=n3
#
#     def foo(self):
#         print(self.nam1,self.nam2,self.nam3,self.nam4,self.nam5,self.nam6)
#
# z = Bar(1,2,3)
# print(z.nam1)
# z.foo()

"""
class Person:

    def __init__(self, name,age):

        #构造方法，构造方法的特性， 类名() 自动执行构造方法

        self.n = name
        self.a = age
        self.x = '0'
    def show(self):
        print('%s-%s' %(self.n, self.a))
lihuan = Person('李欢', 18)
lihuan.show()

hu = Person('互相林', 73)
hu.show()
"""
"""
class F:

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')

class S(F):
    def s1(self):
        print('S.s1')

    def f2(self):
        # obj
        print('S.f2')
        # super(S, self).f2() # 执行父类（基类）中的f2方法
        # F.f2(self)          # 执行父类（基类）中的f2方法
"""

"""
obj = S()
obj.s1()
obj.f2()
"""
"""
obj = S()
obj.s1() # s1中的self是形参，此时代指 obj
obj.f1() # self用于指调用方法的调用者
"""

# obj = S()
# obj.f2()

"""
class Base:
    def a(self):
        print('Base.a')


class F0(Base):
    def a1(self):
        print('F0.a')

class F1(F0):
    def a1(self):
        print('F1.a')

class F2(Base):
    def a1(self):
        print('F2.a')

class S(F1,F2):
    pass

obj = S()
obj.a()
"""

"""

class BaseReuqest:

    def __init__(self):
        print('BaseReuqest.init')


class RequestHandler(BaseReuqest):
    def __init__(self):
        print('RequestHandler.init')
        BaseReuqest.__init__(self)

    def serve_forever(self):
        # self,是obj
        print('RequestHandler.serve_forever')
        self.process_request()

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:

    def process_request(self):
        print('minx.process_request')


class Son(Minx, RequestHandler):
    pass


obj = Son() # init
obj.serve_forever()
"""
# import socketserver
#
#
# obj = socketserver.ThreadingTCPServer(1,2) # 创建对象，init
# obj.serve_forever()
"""
class BaseReuqest:

    def __init__(self):
        print('BaseReuqest.init')


class RequestHandler(BaseReuqest):
    def __init__(self):
        print('RequestHandler.init')
        BaseReuqest.__init__(self)

    def serve_forever(self):
        # self,是obj
        print('RequestHandler.serve_forever')
        self.process_request()

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:

    def process_request(self):
        print('minx.process_request')


class Son(Minx, RequestHandler):
    pass
"""
# obj = Son() # init
# obj.process_request()
# obj = RequestHandler()
# obj.serve_forever()



# class Province:
#     # 静态字段，属于类
#     country = '中国'
#
#     def __init__(self, name):
#         # 普通字段，属于对象
#         self.name = name


# henan = Province('河南')
# hebei = Province('河北')

# print(Province.country)
# print(Province.name)

# hebei = Province('河北')
# hebei.name
# print(hebei.country)
# print(hebei.name)
# print(hebei)

"""
class Foo:
    def __init__(self):
        self.name ='a'

    def bar(self):
        # self是对象
        print('bar')

    @staticmethod
    def sta():
        print('123')

    @staticmethod
    def stat(a1,a2):
        print(a1,a2)

    @classmethod
    def classmd(cls):
        # cls 是类名
        print(cls)
        print('classmd')


# Foo.sta()
# Foo.stat(1,2)

Foo.classmd()


# obj = Foo()
# obj.bar()

# obj = Foo()
# Foo.bar(obj)

"""

"""
class Foo:
    def __init__(self):
        self.name = 'a'
        # obj.name
        self.name_list = ['alex']

    # obj.bar()
    def bar(self):
        # self是对象
        print('bar')
    # 用于执行 obj.per
    @property
    def perr(self):

        return 123

    # obj.per = 123
    @perr.setter
    def perr(self, val):
        print(val)

    @perr.deleter
    def perr(self):

        print(666)

obj = Foo()
# r = obj.perr
# print(r)

# obj.perr = 123
#
# del obj.perr

class Pergination:

    def __init__(self, current_page):
        try:
            # qwer
            p = int(current_page)
        except Exception as e:
            p = 1

        self.page = p
    @property
    def start(self):
        val = (self.page-1) * 10
        return val

    @property
    def end(self):
        val = self.page * 10
        return val

li = []
for i in range(1000):
    li.append(i)

while True:
    p = input('请输入要查看的页码：') # 1,每页显示10条
    obj = Pergination(p)
    print(li[obj.start:obj.end])

"""

class Foo:

    def f1(self):
        return 123

    def f2(self,v):
        print(v)
    def f3(self):
        print('del')

    per = property(fget=f1,fset=f2,fdel=f3,doc='adfasdfasdfasdf')

    # @property
    # def per(self):
    #     return 123


obj = Foo()
# ret = obj.per
# print(ret)

# obj.per = 123456

del obj.per












