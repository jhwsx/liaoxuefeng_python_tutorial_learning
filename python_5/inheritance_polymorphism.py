class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog = Dog()
dog.run() # 打印：Animal is running...

cat = Cat()
cat.run() # 打印： Animal is running...