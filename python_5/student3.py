class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 定义一个类的方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# 使用 Student 类
bart = Student('Peter Wang', 59)
bart.print_score() # 打印结果：Peter Wang: 59
print(bart.get_grade()) # C