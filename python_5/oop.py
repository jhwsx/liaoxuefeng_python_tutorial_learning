# 面向过程编程
std1 = {'name' : 'wzc', 'score' : 100}
std2 = {'name' : 'wzj', 'score' : 100}

def print_score(std):
    print('%s, %s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)

print('*' * 20)
# 面向对象编程
class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s %s' % (self.name, self.score))

wzc = Student('wzc', 100)
wzj = Student('wzj', 100)
wzc.print_score()
wzj.print_score()
