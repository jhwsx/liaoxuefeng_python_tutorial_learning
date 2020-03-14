# 函数作为返回值
# 普通的求和函数, 会立即求和
def cal_sum(*args):
    result = 0
    for n in args:
        result += n
    return result

print(cal_sum(1, 2, 3, 4)) # 10

# 函数作为返回值，不会立即求和
def lazy_sum(*args):
    def sum():
        result = 0
        for n in args:
            result += n
        return result
    return sum

# 上面的例子中，内部函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，当 lazy_sum 
# 返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种成为“闭包”。
f = lazy_sum(1, 2, 3, 4)
print(f) # <function lazy_sum.<locals>.sum at 0x7f51b0fd28c8>
print(f()) # 10

# 每次调用 lazy_sum ，都会返回一个新的函数变量
f1 = lazy_sum(1, 2, 3, 4) 
f2 = lazy_sum(1, 2, 3, 4)
print(f1) # <function lazy_sum.<locals>.sum at 0x7f8c919ea950>
print(f2) # <function lazy_sum.<locals>.sum at 0x7f8c919ea9d8>
print(f1()) # 10
print(f2()) # 10

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1()) # 9
print(f2()) # 9
print(f3()) # 9

#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for n in range(1, 4):
        fs.append(f(n))
    return fs

f1, f2, f3 = count2()

print(f1()) # 1
print(f2()) # 4
print(f3()) # 9