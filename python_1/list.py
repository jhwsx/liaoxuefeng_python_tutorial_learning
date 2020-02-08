classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# len() 函数获取 list 中元素的个数
print(len(classmates))

# 访问集合中的元素
print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3]) # 此行报错：IndexError

# 倒着取
print(classmates[-1]) # Tracy
print(classmates[-2]) # Bob
print(classmates[-3]) # Michael
# print(classmates[-4]) # 此行报错：IndexError

# 追加元素
classmates.append('Adam')
print(classmates)

# 在指定位置插入元素
classmates.insert(1, 'Jack')
print(classmates)

# 删除集合末尾的元素
classmates.pop()
print(classmates)

# 删除指定位置的元素
classmates.pop(1)
print(classmates)

# 替换某个位置的元素
classmates[1] = 'Sarah'
print(classmates)


# list 里面的元素数据类型可以不同
L = ['Apple', 123, True]
print(L)

# list 里面的元素也可以是另一个 list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s) # ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s)) # 4

# 空 list
L = []
print(L) # []
