# 偏函数

# 以 int 函数为例子来作说明，第一个参数可以是 str 也可以是数字，第二个
# 参数是可选参数，默认是 10
print(int('12345')) # 默认 base 参数是 10
print(int('12345', base = 8)) # 5349, 把 12345 按照 8 进制，转为十进制是 5349
print(int('12345', 16)) # 74565，把 12345 按照 16 进制，转为十进制是 74565
print(int('100000', base = 2)) # 32，把 100000 按照二进制，转为十进制是32
print(int('10000', base = 2)) # 16，把 100000 按照二进制，转为十进制是16
print(int('1000', base = 2)) # 8，把 100000 按照二进制，转为十进制是8

def int2(x, base=2):
    return int(x, base)

print(int2('100000')) # 32
print(int2('10000')) # 16
print(int2('1000')) # 8

# 使用偏函数
import functools
int2 = functools.partial(int, base = 2)
print(int2('100000')) # 32
print(int2('10000')) # 16
print(int2('1000')) # 8
print(int2('100000',  base = 10)) # 100000
