#__author:  Administrator
#date:  2016/9/23
"""
class Foo:

    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self.__age = age # 私有，外部无法直接访问

    def show(self):
        return self.__age


obj = Foo('alex', 19)
print(obj.name)
# obj.age
# print(obj.__age)
ret = obj.show()
print(ret)
"""

"""
class Foo:
    __v = '123'

    def __init__(self):
        pass
    def show(self):
        return Foo.__v
    @staticmethod
    def stat():
        return Foo.__v
# print(Foo.__v)
# ret = Foo().show()
# print(ret)

ret = Foo.stat()
print(ret)
"""
"""
class Foo:
    def __f1(self):
        return 123

    def f2(self):
        r = self.__f1()
        return r

obj = Foo()
ret = obj.f2()
print(ret)
"""

"""
class F:
    def __init__(self):
        self.ge = 123
        self.__gene = 123

class S(F):
    def __init__(self,name):
        self.name = name
        self.__age = 18
        super(S, self).__init__()

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.ge)
        print(self.__gene)

s = S('alex')
s.show()
"""

"""
class Foo:
    def __init__(self):
        print('init')

    def __call__(self, *args, **kwargs):
        print('call')

# obj = Foo()
# obj()
Foo()()
"""
# s = "123"
# # s = str('123')
#
# i = int(s)
# print(i,type(i))

"""
class Foo:

    def __init__(self):
        pass

    def __int__(self):
        return 1111

    def __str__(self):
        return 'alex'

obj = Foo()
print(obj, type(obj))

# int,对象，自动执行对象的 __int__方法，并将返回值赋值给int对象
r = int(obj)
print(r)
i = str(obj)
print(i)

"""
"""
class Foo:

    def __init__(self,n,a):
        self.name =n
        self.age =a

    def __str__(self):
        return '%s-%s' %(self.name,self.age,)

obj = Foo('alex', 18)
print(obj) #print(str(obj)) str(obj)   obj中__str__，并获取其返回值
"""
"""
class Foo:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __add__(self, other):
        # self = obj1 (alex,19)
        # other = obj2(eric,66)
        # return self.age + other.age
        #return Foo('tt',99)
        return Foo(obj1.name, other.age)

    def __del__(self):
        print('析构方法') # 对象被销毁（）时，自动执行

obj1 = Foo('alex', 19)
obj2 = Foo('eirc', 66)

r = obj1 + obj2
# 两个对象相加时，自动执行第一个对象的的 __add__方法，并且将第二个对象当作参数传递进入
print(r,type(r))
"""


"""
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.n = 123

# obj = Foo('alex', 18)
#
# d = obj.__dict__
# print(d)

# ret = Foo.__dict__
# print(ret)
"""

# li = [11,22,33,44]
# li = list([11,22,33,44])
#
# li[3]
# #
#
# li[3] = 666
#
# del li[2]

"""
class Foo:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        return item+10

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)
li = Foo('alex', 18)
r= li[8] # 自动执行li对象的类中的 __getitem__方法，8当作参数传递给item
print(r)

li[100] = "asdf"

del li[999]
"""
"""
class Foo:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        # return item+10
        # 如果item是基本类型：int，str，索引获取
        # slice对象的话，切片
        if type(item) == slice:
            print('调用这希望内部做切片处理')
        else:
            print(item.start)
            print(item.stop)
            print(item.step)
            print('调用这希望内部做索引处理')

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)

li = Foo('alex', 18)
li[123]
li[1:4:2]

li[1:3] = [11,22]

del li[1:3]

# class Slice:
#     def __init__(self,a,b,c):
#         self.start = a
#         self.end = b
#         self.step = c
# obj = Slice(1,4,2)
# li[999] = "alex"
#
# del li[234]
"""
"""
class Foo:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([11,22,33])
li = Foo('alex', 18)
# 如果类中有 __iter__ 方法，对象=》可迭代对象
# 对象.__iter__() 的返回值： 迭代器
# for 循环，迭代器，next
# for 循环，可迭代对象，对象.__iter__()，迭代器，next
# 1、执行li对象的类F类中的 __iter__方法，并获取其返回值
# 2、循环上一步中返回的对象
for i in li:
    print(i)
"""
# li = [11,22,33,44]
# li= list([11,22,33,44])
# for item in li:
#     print(item)

"""
class MyType(type):
    def __init__(self,*args, **kwargs):
        # self=Foo
        print(123)
        pass

    def __call__(self, *args, **kwargs):
        # self=Foo
        r = self.__new__()


#

class Foo(object,metaclass=MyType):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return '对象'

    def func(self):
        print('hello wupeiqi')

obj = Foo()





class Bar:
    def __init__(self):
        print(123)


obj = Bar()
"""

"""
while True:
    try:
        # 代码块，逻辑
        inp = input('请输入序号：')
        i = int(inp)
    except Exception as e:
        # e是Exception对象，对象中封装了错误信息
        # 上述代码块如果出错，自动执行当前块的内容
        print(e)
        i = 1
    print(i)
"""
#li = [11,22]
#li[999] # IndexError
# int('qwe') # ValueError
"""
def fun():
    ret = 0
    try:
        li = [11, 22]
        li[1]
        int('w3r')

    except IndexError as e:
        print('IndexError',e)
    except ValueError as e:
        print('ValueError',e)
    except Exception as e:
        print('Exception',e)
    else:
        ret = 1
        print('elese')
    finally:
        print('....')

    return ret
r = fun()
if r == 0:
    print('500')
else:
    pass

"""
"""
class F:
    def __init__(self):
        self.__a = 132

    def show(self):
        # print(self.__a)
        return self.__a

class S(F):
    def __init__(self):
        self.name = 123
        super(S, self).__init__()

obj = S()
r = obj.show()
print(r)
"""
"""
try:
    # int('asdf')
    # 主动出发异常
    # raise Exception('不过了...')
except Exception as e:
    print(e)

def db():
    # return True
    return False

def index():
    try:
        r = input(">>")
        int(r)


        result = db()
        if not result:
            r = open('log','a')
            r.write('数据库处理错误')
            # 打开文件，写日志
            #raise Exception('数据库处理错误')
    except Exception as e:
        str_error = str(e)
        print(str_error)
        r = open('log', 'a')
        r.write(str_error)
        # 打开文件，写日志

index()
"""


"""
class OldBoyError(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

# obj = OldBoyError('xxx')
# print(obj)
try:
    raise OldBoyError('我错了...')
except OldBoyError as e:
    print(e)# e对象的__str__()方法，获取返回

"""

# assert 条件,断言，用于强制用户服从，不服从就报错，可补货，一般不补货
# print(23)
# assert 1==2
# print(456)


"""
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def show(self):
        return  "%s-%s " %(self.name,self.age)
    def __int__(self):
        return 123
    def __str__(self):
        return 'uuu'
obj = Foo('alex', 18)

r = int(obj) # r = 123
u = str(obj)
b = 'name'
"""


# getattr
# hasattr
# setattr
# delattr
# 通过字符串的形式操作对象中的成员

# func = getattr(obj, 'show')
# print(func)
# r = func()
# print(r)

# print(hasattr(obj, 'name'))
# obj.k1
# setattr(obj, 'k1', 'v1')
# print(obj.k1)
# obj.name
# delattr(obj, 'name')
# obj.name

# 去什么东西里面获取什么内容
# inp = input('>>>')
# v = getattr(obj, inp)
# print(v)



"""
obj.name
b = "name"
obj.b # obj.name
"""
# b = "name"
# obj.__dict__['name']
# obj.__dict__[b]

# if b == 'name':
#     obj.name


"""
class Foo:

    stat = '123'

    def __init__(self, name,age):
        self.name = name
        self.age = age

# 通过字符串的形式操作对象中的成员
r = getattr(Foo, 'stat')
print(r)
"""

"""
import s2


# r1 = s2.NAME
# print(r1)
# r2 = s2.func()
# print(r2)

r1 = getattr(s2, 'NAME')
print(r1)

r2 = getattr(s2, 'func')
result = r2()
print(result)

cls = getattr(s2, 'Foo')
print(cls)
obj = cls()
print(obj)
print(obj.name)
"""
"""
import s2
inp = input('请输入要查看的URL：')
if hasattr(s2, inp):
    func = getattr(s2, inp)
    result = func()
    print(result)
else:
    print('404')
"""

# class Foo:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

# obj = Foo() # obj对象，obj也成为Foo类的 实例，（实例化）
# obj1 = Foo()
# obj2 = Foo()
# obj3 = Foo()

# 单例，用于使用同一份实例（对象）
"""
class Foo:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name,self.age)

v = None

while True:
    if v:
        v.show()
    else:
        v = Foo('alex', 123)
        v.show()
"""
class Foo:

    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v

# 不要在使用 类()
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
obj3 = Foo.get_instance()
print(obj3)






