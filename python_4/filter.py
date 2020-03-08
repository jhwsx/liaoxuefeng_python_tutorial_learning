# filter 函数

# 在一个list中，删掉偶数，只保留奇数
# 判断是不是奇数的方法
def is_odd(n):
    return n & 1 != 0
print(list(filter(is_odd, [1, 2, 3, 5, 8, 9, 12]))) # [1, 3, 5, 9]

# 在一个list中，删除负数，只保留整数
print(list(filter(lambda x : x > 0, [-1, -2, 3, 4, 5]))) # [3, 4, 5]

# 利用 filter 求素数
# 首先，构造从 3 开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 其次，定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
# 最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列中的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 生成新的序列
# 打印 1000 以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break