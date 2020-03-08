# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
from functools import reduce


def normalize(s):
    return s.capitalize()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
# 可以接受一个list并利用reduce()求积


def prod(lt):
    def multiply(x, y):
        return x * y
    return reduce(multiply, lt)


# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    splitlist = s.split('.')

    def char2num(ch):
        return DIGITS[ch]

    def intPart(x, y):
        return 10 * x + y

    def decimalPart(x, y):
        return 0.1 * x + y
    if len(splitlist) == 1:
        return reduce(intPart, map(char2num, splitlist[0]))
    else:
        return reduce(intPart, map(char2num, splitlist[0])) + reduce(decimalPart, list(map(char2num, splitlist[1]))[::-1]) / 10

print('str2float(\'0.456\') =', str2float('0.456'))
print('str2float(\'123\') =', str2float('123'))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
