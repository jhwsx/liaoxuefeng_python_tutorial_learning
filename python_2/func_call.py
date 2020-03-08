# 调用 abs() 函数, 返回一个指定值：整数或浮点数的绝对值
print(abs(100))
print(abs(-20))
print(abs(12.34))
print(abs(-56.789))

# 错误演示一：
# print(abs(1, 2)) # 报错：参数个数不对
'''
Traceback (most recent call last):
  File "func_call.py", line 8, in <module>
    print(abs(1, 2))
TypeError: abs() takes exactly one argument (2 given)
'''

# 错误演示二：
# print(abs('hello')) # 报错：错误的参数类型
'''
Traceback (most recent call last):
  File "func_call.py", line 17, in <module>
    print(abs('hello'))
TypeError: bad operand type for abs(): 'str'
'''

# 调用 max() 函数，它可以接收任意多个参数，返回最大的那个
print(max(1, 2, 3)) # 3
print(max(1, 0, -3, 7, 9, 12)) # 12
grades = [100, 0, 9, -10]
# 接收一个 Iterable
print(max(grades))
# 数据类型转换函数

# 把 str 转换成整数
print(int('123')) # 123
# 把浮点数转换成整数
print(int(12.34)) # 12
# 把 str 转换成浮点数
print(float('12.34')) # 12.34
# 把浮点数转换成 str
print(str(12.3)) # 12.3
# 把整数转换成 str
print(str(1234)) # 1234
# 把 str 转成布尔
print(bool('')) # False
print(bool('a')) # True

# ord(c) 函数：Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
print(ord('A')) # 65

# chr(i) 函数：Return the string representing a character whose Unicode code point is the integer i.
print(chr(97)) # a

# len(s) 函数：Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list,
#  or range) or a collection (such as a dictionary, set, or frozen set).
print(len('abc')) # 3
print(len(b'1234')) # 4
print(len((1, 2, 3, 4, 5))) # 5
print(len(['a', 'b', 1, 4, True])) # 5
print(len(range(10))) # 10

# 函数名
a = abs # 变量 a 指向 abs 函数
print(a(-1)) # 1，这里是通过 a 调用 abs 函数




