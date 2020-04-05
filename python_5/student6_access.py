# 增加对属性的访问限制, 暴露出访问属性的方法
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # getter/setter 方法
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if score >= 0 and score <= 100:
            self.__score = score
        else:
            raise ValueError('illegal score')

wang = Student('zhichao', 100)
# print(wang.__name) # 此行报错
'''
Traceback (most recent call last):
  File "student6_access.py", line 12, in <module>
    print(wang.__name)
AttributeError: 'Student' object has no attribute '__name'
'''
print('%s: %s' % (wang.get_name(), wang.get_score())) # 打印：zhichao: 100
wang.set_name('zhijie')
# wang.set_score(150) # 不合法的分数，抛异常
wang.set_score(99)
print('%s: %d' % (wang.get_name(), wang.get_score())) # 打印：zhijie: 99

