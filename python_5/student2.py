# 把必须绑定的属性强制写进去

class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score

# 通过一个特殊的 __init__ 方法，在创建实例的时候把 name，score等属性绑定上去。
# __init__ 是一个特殊的方法，它的第一个参数永远是 self，表示创建的实例本身。

# 创建实例
# bart = Student() # 报错：TypeError: __init__() missing 2 required positional arguments: 'name' and 'score'
bart = Student('Bart Smith', 0)
print(bart) # <__main__.Student object at 0x7fad2fbf2b00>
print('name = %s, score = %s' % (bart.name, bart.score)) # name = Bart Smith, score = 0

