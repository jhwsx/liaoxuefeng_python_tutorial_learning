classmates = ('Michael', 'Bob', 'Tracy')

# 获取 tuple 中的元素
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 倒着取
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# 获取元素个数
print(len(classmates)) # 3

# 没有追加，插入，删除，替换的方法

# 定义一个空的 tuple
t = ()
print(t) # ()

# 定义一个一个元素的 tuple
# 不正确的写法
t = (1)
print(t) # 1, 从打印结果看，这并不是一个 tuple，而是数值 1。
# 正确的写法
t = (1,) # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
print(t) # (1,)

# "可变"的 tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t) # ('a', 'b', ['X', 'Y'])