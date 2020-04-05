# dir() 函数：获得一个对象的所有属性和方法, 返回的是一个 list
print(dir('ABC'))

# 获取一个对象的长度, 使用 len() 函数，内部就是调用对象的 __len__ 函数
print(len('ABC'))
print('ABC'.__len__())

# 自己编写一个类，定义一个 __len__ 方法，也可以使用 len() 函数获取长度
class MyObject(object):
    def __len__(self):
        return 100

print(MyObject().__len__()) # 100
print(len(MyObject())) # 100

# 配合 getattr(), setattr() 和 hasattr(), 直接操作一个对象的状态
# 这三个都是内置函数
class MyClass(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyClass()
# 判断有无属性 x？
print(hasattr(obj, 'x')) # True
print(obj.x) # 9
# 判断有无属性 y？ 
print(hasattr(obj, 'y')) # False
# 设置一个属性 y？
setattr(obj, 'y', 19)
# 再判断有无属性 y？ 
print(hasattr(obj, 'y')) # True
# 获取属性 y
print(getattr(obj, 'y')) # 19
# 获取一个不存在的属性，抛出异常
# getattr(obj, 'z') # 此行抛出异常，如下所示
'''
  File "attrs.py", line 36, in <module>
    getattr(obj, 'z')
AttributeError: 'MyClass' object has no attribute 'z'
'''
# 获取属性，如果不存在，返回默认值
print(getattr(obj, 'z', -1)) # -1

# 获取对象的方法
print(hasattr(obj, 'power')) # True
print(getattr(obj, 'power')) # <bound method MyClass.power of <__main__.MyClass object at 0x7f5d8dd5cf98>>
fn = getattr(obj, 'power')
print(fn) # <bound method MyClass.power of <__main__.MyClass object at 0x7f5d8dd5cf98>>
print(fn()) # 81
