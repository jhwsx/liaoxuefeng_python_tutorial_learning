class Student():
    pass

bart = Student()
print(bart) # <__main__.Student object at 0x7f64b90fc898>
print(Student) # <class '__main__.Student'>

# 可以自由地给一个实例绑定属性
bart.name = 'Bart Smith'
print(bart.name) # Bart Smith
bart.age = 32
print(bart.age) # 32
bart.salary = 20000.0
print(bart.salary) # 20000.0