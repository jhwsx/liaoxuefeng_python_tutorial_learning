# 迭代 list
L = [1, 3, 5, 7, 9]
for num in L:
    print(num)

# 迭代 tuple
T = ('a', 'b', 'c', 'd')
for ch in T:
    print(ch)

# 迭代 dict
D = {'name' : 'wangzhichao', 'age' : 18}
# 迭代 dict 中的 key, 这也是默认情况
for key in D:
    print(key)
# 迭代 dict 中的 value
for value in D.values():
    print(value)
# 同时迭代 dict 中的 key 和 value
for k, v in D.items():
    print(k, '->', v)

# 迭代字符串
for ch in 'ABC':
    print(ch)

# 判断一个对象是否是可迭代对象
from collections import Iterable

print(isinstance('abcde', Iterable)) # True
print(isinstance([1, 2, 3], Iterable)) # True
print(isinstance(1234, Iterable)) # False

# 对 list 实现下标迭代
for index, value in enumerate(['A', 'B', 'C']):
    print(index, value)
# enumerate函数可以把一个list变成索引-元素对