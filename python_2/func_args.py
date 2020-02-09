# 写一个计算 x^2 的函数
# def power(x):
#     return x * x

# print(power(5))
# print(power(15))

# 写一个计算 x^n 的函数
# x 是位置参数，n 设置了默认参数
def power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print(power(5))
print(power(15))
print(power(2, 10))

# 写一个小学生入学注册的函数
def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name: ', name)
    print('gender: ', gender)
    print('age: ', age)
    print('city: ', city)

enroll('Sarah', 'F')
enroll('John', 'M', 7, 'Henan')
# enroll('Peter', 'M', 'Shanghai') # 这种情况下，需要把默认参数名写上。
enroll('Peter', 'M', city = 'Shanghai')

# 默认参数的大坑
def add_end(L = []):
    L.append('END')
    return L

print(add_end([1, 2, 3])) # [1, 2, 3, 'END']
print(add_end(['x', 'y', 'z'])) # ['x', 'y', 'z', 'END']
print(add_end()) # ['END']
print(add_end()) # ['END', 'END']
print(add_end()) # ['END', 'END', 'END']

# 描述一下，出现的大坑：第一次调用 add_end() 的输出是 ok 的，但是第二次，第三次的输出却是不对的。
# 原因是：Python 函数在定义的时候，默认参数 L 的值就被计算出来了，即 [], 因为默认参数 L 也是一个变量，
# 它指向对象 []，每次调用该函数，如果改变了 L 的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的 [] 了。

# 解决办法：默认参数必须指向不变对象！
def add_end2(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2()) # ['END']
print(add_end2()) # ['END']
print(add_end2()) # ['END']

# 可变参数
# 给定一组数字a，b，c……，请计算a^2 + b^2 + c^2 + ……
# 这种写法需要传入一个 list 或者 tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n ** 2
    return sum

print(calc([1, 2, 3])) # 14

# 使用可变参数
def calc2(*numbers):
    # print(isinstance(numbers, tuple)) # True
    sum = 0
    for n in numbers:
        sum = sum + n ** 2
    return sum

print(calc2(1, 2, 3)) # 14
t = (1, 3, 5, 7)
print(calc2(*t)) # 84

# 使用关键字参数
def person(name, age, **kw):
    # print(isinstance(kw, dict)) # True
    print('name:', name, 'age:', age, 'other:', kw)

# 可以不传递关键字参数
person('Michael', 30) # name: Michael age: 30 other: {}
# 传递关键字参数
person('Bob', 35, city='Beijing') # name: Bob age: 35 other: {'city': 'Beijing'}

extra = {'city' : 'Beijing', 'job' : 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job']) # name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#简写
person('Jack', 24, **extra) # name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

# 使用命名关键字参数: 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Engineer') # Jack 24 Beijing Engineer
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

person3('zhichao',32, *[1, 2, 3], city='shanghai', job='Engineer') # zhichao 32 (1, 2, 3) shanghai Engineer

# 命名关键字参数必须传入参数名
# person2('Jack', 24, 'Beijing', 'Engineer') # 报错: 命名关键字参数不传参数名，就被当成了位置参数。
'''
Traceback (most recent call last):
  File "func_args.py", line 110, in <module>
    person2('Jack', 24, 'Beijing', 'Engineer')
TypeError: person2() takes 2 positional arguments but 4 were given
'''

# 命名关键字参数可以有缺省值，从而简化调用
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)

# 由于命名关键字参数有默认值，调用时，可以不传入 city 参数
person4('Bill', 32, job='Driver') # Bill 32 Beijing Driver


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

f1(1, 2) # a= 1 b= 2 c= 0 args= () kw= {}
f1(1, 2, c=3) # a= 1 b= 2 c= 3 args= () kw= {}
f1(1, 2, 3, 'a', 'b') # a= 1 b= 2 c= 3 args= ('a', 'b') kw= {}
f1(1, 2, 3, 'a', 'b', x=99) # a= 1 b= 2 c= 3 args= ('a', 'b') kw= {'x': 99}
f2(1, 2, d=9, ext=None) # a= 1 b= 2 c= 0 d= 9 kw= {'ext': None}
# 通过一个 tuple 和 dict，调用上述函数
args = (1, 2, 3, 4)
kw = {'d' : 99, 'x' : '#'}
f1(*args, **kw) # a= 1 b= 2 c= 3 args= (4,) kw= {'d': 99, 'x': '#'}
args = {1, 2, 3}
kw = {'d' : 88, 'x' : '#'}
f2(*args, **kw) # a= 1 b= 2 c= 3 d= 88 kw= {'x': '#'}
