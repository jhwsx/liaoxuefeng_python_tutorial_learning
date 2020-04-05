# 多态
class Animal(object):

    def run(self):
        print('Animal is running...')
    
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

'''
Animal is running...
Animal is running...
Dog is running...
Dog is running...
Cat is running...
Cat is running...
'''

class Train(object):

    def run(self):
        print('Train is running...')

run_twice(Train())
'''
Train is running...
Train is running...
'''