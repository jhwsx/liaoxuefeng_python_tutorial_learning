# 实例属性和类属性
class Student(object):
    # name 是类属性，归 Student 类所有
    name = 'Student'

wang = Student()
print(wang.name) # Student

li = Student()
print(li.name) # Student
