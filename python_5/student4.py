class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
# 对不同的实例变量绑定不同的数据
wang = Student('zhichao', 100)
li = Student('xiaolong', 100)
wang.age = 18
li.height = 176
print(wang.age) # 打印：18
# print(li.age) # 此行报错
'''
Traceback (most recent call last):
  File "student4.py", line 12, in <module>
    print(li.age)
AttributeError: 'Student' object has no attribute 'age'
'''
print(li.height) # 打印：176
# print(wang.height) # 此行报错
'''
Traceback (most recent call last):
  File "student4.py", line 20, in <module>
    print(wang.height)
AttributeError: 'Student' object has no attribute 'height'
'''