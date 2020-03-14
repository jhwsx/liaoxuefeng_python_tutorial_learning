# 把容器中的数字，经过 f(x) = x^2，变换每一个元素，得到新的容器

def f(x):
    return x ** 2
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 打印结果：[1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 打印结果：[1, 4, 9, 16, 25, 36, 49, 64, 81]

g = lambda x, y: x + y
print(g(1, 1)) # 2

def add(x, y):
    return lambda: x + y

print(add(2, 3)()) # 5

TODO: 这段代码为什么报错？
# def subtract(x, y):
#     nonlocal x
#     def f():
#         x += 1
#         return x - y
#     return f

# print(subtract(1, 2)())
