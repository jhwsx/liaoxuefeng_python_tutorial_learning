# 计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(1))
print(fact(5))
print(fact(100))
# print(fact(1000)) # 报错
'''
Traceback (most recent call last):
  File "func_recur.py", line 10, in <module>
    print(fact(1000))
  File "func_recur.py", line 5, in fact
    return n * fact(n - 1)
  File "func_recur.py", line 5, in fact
    return n * fact(n - 1)
  File "func_recur.py", line 5, in fact
    return n * fact(n - 1)
  [Previous line repeated 995 more times]
  File "func_recur.py", line 3, in fact
    if n == 1:
RecursionError: maximum recursion depth exceeded in comparison
'''
# 使用尾递归
def fact2(n):
  return fact_iter(n, 1)

def fact_iter(num, product):
  if num == 1:
    return product
  return fact_iter(num - 1, num * product) # 这里仅返回递归函数本身

# fact2(1000) # 报错
'''
Traceback (most recent call last):
  File "func_recur.py", line 35, in <module>
    fact2(1000)
  File "func_recur.py", line 28, in fact2
    return fact_iter(n, 1)
  File "func_recur.py", line 33, in fact_iter
    return fact_iter(num - 1, num * product) # 这里仅返回递归函数本身
  File "func_recur.py", line 33, in fact_iter
    return fact_iter(num - 1, num * product) # 这里仅返回递归函数本身
  File "func_recur.py", line 33, in fact_iter
    return fact_iter(num - 1, num * product) # 这里仅返回递归函数本身
  [Previous line repeated 994 more times]
  File "func_recur.py", line 31, in fact_iter
    if num == 1:
RecursionError: maximum recursion depth exceeded in comparison
'''

# 尾调用的代码：
def foo(data):
  return b(data)

def b(data):
  pass
