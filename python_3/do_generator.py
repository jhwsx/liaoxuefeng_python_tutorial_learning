from collections.abc import Iterable
# 创建一个 generator
L = [x * x for x in range(10)]
print(L) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
print(g) # <generator object <genexpr> at 0x00000000024E3510>
# 打印 generator 中的元素
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9 
print(next(g)) # 16
print(next(g)) # 25
print(next(g)) # 36
print(next(g)) # 49
print(next(g)) # 64
print(next(g)) # 81
# print(next(g)) # 报错
'''
Traceback (most recent call last):
  File "do_generator.py", line 17, in <module>
    print(next(g))
StopIteration
'''
# generator 也是可迭代对象，使用 for 循环来打印元素
g = (x * x for x in range(10)) # 这里如果不重新赋值，直接循环 g，是没有输出的。
print(isinstance(g, Iterable)) # True
for n in g:
    print(n)

# 用函数来实现 generator
# 先用函数实现斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 把 fib 函数变成 generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib2(6)
print(f) # <generator object fib2 at 0x00000000026682E0>
for x in f:
    print(x)
'''
打印：
1
1
2
3
5
8
'''

# 定义一个 generator，依次返回数字1，3，5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step3')
    yield 5

o = odd()
print(next(o))
print('--------------')
print(next(o))
print('--------------')
print(next(o))
print('--------------')
# print(next(o)) # 这样先注释掉，否则后面代码跑不出来
# 打印
'''
step 1
1
--------------
step 2
3
--------------
step3
5
--------------
Traceback (most recent call last):
  File "do_generator.py", line 72, in <module>
    print(next(o))
StopIteration
'''
# 获取 generator 的 return 语句的返回值
g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

'''
打印结果：
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done
'''

# 理解 yield
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:", res)

g = foo()
print(next(g))
print("*" * 20)
print(next(g))
'''
打印结果：
starting...
4
********************
res: None
4
'''