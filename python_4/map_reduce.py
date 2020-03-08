from functools import reduce
from collections.abc import Iterator, Iterable
#  map() 函数
# 把 f(x) = x ^ 2, 作用在一个 list [1,2,3,4,5,6,7,8,9] 上


def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(isinstance(r, Iterator))  # True，说明 r 是 Iterator。
print(isinstance(r, Iterable))  # True，说明 r 是 Iterable。
# Iterator 是一个惰性序列
# 迭代方式一：
print(list(r))
# 迭代方式二：
for y in r:
    print(y)

# 利用 map 函数，把 list 中所有的数字转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 打印结果：['1', '2', '3', '4', '5', '6', '7', '8', '9']

# 利用 map 函数，将字符串转为 list
print(list(map(int, '1234')))  # [1, 2, 3, 4]

# 利用 map 函数，将元组转为 list
print(list(map(int, (1, 2, 3))))  # [1, 2, 3]

# 利用 map 函数，对两个列表相同位置的元素进行相加
# [3, 7, 11, 15, 19]
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))


# reduce 函数
# 计算列表的和
def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))  # 15
# 把序列[1,3,5,7,9]变为整数13579


def trans(x, y):
    return 10 * x + y


print(reduce(trans, [1, 3, 5, 7, 9]))  # 13579
# 把 str 转 int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def char2num(ch):
        return DIGITS[ch]
    def fn(x, y):
        return 10 * x + y
    return reduce(fn, map(char2num, s))
print('1378') # 1378

