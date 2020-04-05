#  使用 type()来判断基本类型
print(type(123)) # <class 'int'>
print(type('hello')) # <class 'str'>
print(type(None))  # <class 'NoneType'>
print(type(3.1415926)) # <class 'float'>
print(type(True)) # <class 'bool'>

# 使用 type() 来判断指向函数或类的变量
print(type(abs)) # <class 'builtin_function_or_method'>
class Animal(object):
    pass
a = Animal()
print(type(a)) # <class '__main__.Animal'>
b = Animal
print(type(b)) # <class 'type'>

# 比较返回的类型是否相同
print(type(123) == type(456)) # True
print(type(123) == int) # True
print(type('abc') == type('123')) # True
print(type('abc') == str) # True
print(type(6.18) == type(3.14)) # True
print(type(6.18) == float) # True
print(type(1 > 0) == type(2 > 1)) # True
print(type(1 > 0) == bool) # True

# 判断一个对象是否是函数
import types
def fn():
    pass

print(type(fn) == types.FunctionType) # True
print(type(abs) == types.BuiltinMethodType) # True
print(type(lambda x:  x + 1) == types.LambdaType) # True
print(type((x for x in range(10))) == types.GeneratorType) # 这种是生成器列型 打印 ：True 

print('*' * 20, 'I am a divider', '*' * 20)

'''
isinstance() 与 type() 区别：

type() 不会认为子类是一种父类类型，不考虑继承关系。

isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
'''
class Fruit(object):
    pass

class Apple(Fruit):
    pass

class Hongfushi(Apple):
    pass

f = Fruit()
a = Apple()
h = Hongfushi()

print(isinstance(f, Fruit)) # True
print(isinstance(a, Fruit)) # True
print(isinstance(h, Fruit)) # True
print(isinstance(a, Hongfushi)) # False

# isinstance 用于基本数据类型
print(isinstance(123, int)) # True
print(isinstance(True, bool)) # True
print(isinstance(3.14, float)) # True
print(isinstance('hello', str)) # True

# isinstance 判断一个变量是否某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple))) # True

print('=' * 20, 'I am a divider', '=' * 20)


