# 判断对象是否是 Iterable 对象
from collections.abc import Iterable, Iterator
print(isinstance([], Iterable)) # True, 说明 list 是 Iterable 对象
print(isinstance((), Iterable)) # True，说明 tuple 是 Iterable 对象
print(isinstance({}, Iterable)) # True，说明 dict 是 Iterable 对象
print(isinstance({1, 2, 3}, Iterable)) # True，说明 set 是 Iterable 对象
print(isinstance('hello', Iterable)) # True，说明 str 是 Iterable 对象
print(isinstance(b'hello', Iterable)) # True, 说明 bytes 是 Iterable 对象
print(isinstance(range(10), Iterable)) # True, 说明 range 是 Iterable 对象

g = (x * x for x in range(10))
print(isinstance(g, Iterable)) # True，说明生成器是 Iterable 对象
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
print(isinstance(f, Iterable)) # True，说明生成器是 Iterable 对象

print('*' * 20)

# 判断对象是否是 Iterator 对象
print(isinstance([], Iterator)) # False, 说明 list 不是 Iterator 对象
print(isinstance((), Iterator)) # False，说明 tuple 不是 Iterator 对象
print(isinstance({}, Iterator)) # False，说明 dict 不是 Iterator 对象
print(isinstance({1, 2, 3}, Iterator)) # False，说明 set 不是 Iterator 对象
print(isinstance('hello', Iterator)) # False，说明 str 不是 Iterator 对象
print(isinstance(b'hello', Iterator)) # False, 说明 bytes 不是 Iterator 对象
print(isinstance(range(10), Iterator)) # False, 说明 range 不是 Iterator 对象

g = (x * x for x in range(10))
print(isinstance(g, Iterator)) # True，说明生成器是 Iterator 对象
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib2(6)
print(isinstance(f, Iterator)) # True，说明生成器是 Iterator 对象

print('*' * 20)

# 把集合类数据类型转为 Iterator
print(isinstance(iter([]), Iterator)) # True
print(isinstance(iter(()), Iterator)) # True
print(isinstance(iter({}), Iterator)) # True
print(isinstance(iter({1, 2, 3}), Iterator)) # True
print(isinstance(iter('hello'), Iterator)) # True
print(isinstance(iter(b'hello'), Iterator)) # True
print(isinstance(iter(range(10)), Iterator)) # True
