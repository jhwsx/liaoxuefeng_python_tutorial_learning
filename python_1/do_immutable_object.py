# list 是可变对象
a = ['c', 'b', 'a']
a.sort()
print(a) # ['a', 'b', 'c']
# 可以看到 a 的内容是可以变化的


# str 是不可变对象
a = 'abc'
b = a.replace('a', 'A')
print(b) # Abc
print(a) # abc
