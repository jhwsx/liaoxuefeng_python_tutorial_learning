# -----变量可以指向函数------

print(abs(-10)) # 10
# 直接打印 abs 呢？
print(abs) # <built-in function abs>
# 把函数本身赋值给变量
f = abs
print(f) # <built-in function abs>
# 使用变量 f 来调用 abs() 函数
print(f(-100)) # 100

# 函数名也是变量
# abs = 10
# print(abs(-10)) # 报错
'''
Traceback (most recent call last):
  File "higher_order_function_intro.py", line 13, in <module>
    print(abs(-10))
TypeError: 'int' object is not callable
'''

# -----传入函数------
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs)) # 11



