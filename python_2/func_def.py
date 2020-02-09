# 自定义一个求绝对值的my_abs函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99)) # 99

# 没有返回值的函数
def show1(x):
    print(x)

def show2(x):
    print(x)
    return

def show3(x):
    print(x)
    return None

show1("no return")
show2("no return")
show3("no return")

# 定义一个空函数
def nop():
    pass

# print(my_abs('A')) # 报错
'''
报错信息：
Traceback (most recent call last):
  File "func_def.py", line 14, in <module>
    print(my_abs('A'))
  File "func_def.py", line 3, in my_abs
    if x >= 0:
TypeError: '>=' not supported between instances of 'str' and 'int'
'''
# 而使用内置函数 abs() 
# print(abs('A')) # 报错
'''
报错信息：
Traceback (most recent call last):
  File "func_def.py", line 25, in <module>
    print(abs('A'))
TypeError: bad operand type for abs(): 'str'
'''
# 可以看到，我们自定义的 my_abs() 函数，和内置函数 abs() 报错信息不一样：
# 自定义的不能检查出参数错误，内置的可以检查出参数错误。
# 优化自定义的 my_abs() 函数，对参数类型做检查，只允许整数和浮点数的参数
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type for my_abs2(): %s' % type(x).__name__)
    if x >= 0:
        return x
    else:
        return -x

print(my_abs2(-1)) # 1
# print(my_abs2('a'))

# 返回多个值
import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y) # 151.96152422706632 130.0

# 但实际上，Python 函数返回的仍然是单一值
r = move(100, 100, 60, math.pi / 6)
print(r) # (151.96152422706632, 130.0)
# 可以看到，返回值实际上是一个 tuple