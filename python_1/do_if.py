# if 语句
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


# if ... else 语句
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


# if ... elif ... else 语句
age = 15
if age >= 18:
    print('adult')
elif age >= 10:
    print('teenager')
else:
    print('kid')

# 简写的判断条件
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 1
if x:
    print(True)
x = ['A']
if x:
    print(True)
x = "a"
if x:
    print(True)
x = 0
if x:
    print(True)
else:
    print(False)
x = []
if x:
    print(True)
else:
    print(False)
x = ''
if x:
    print(True)
else:
    print(False)

# birth = input("birth: ")
# if birth < 2000:
#     print('00前')
# else:
#     print("00后")
'''
上面代码报错信息：
birth: 1988
Traceback (most recent call last):
  File "do_if.py", line 55, in <module>
    if birth < 2000:
TypeError: '<' not supported between instances of 'str' and 'int'
'''

# 正确的处理办法
birth = input("birth: ")
birth = int(birth) # int() 把 str 转换成整数，如果不合法，就抛出异常。
if birth < 2000:
    print('00前')
else:
    print("00后")