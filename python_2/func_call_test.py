# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 1000
print(hex(n1)) # 0xff
print(hex(n2)) # 0x3e8

# print(int(hex(n1))) # 报错
'''
Traceback (most recent call last):
  File "func_call_test.py", line 7, in <module>
    print(int(hex(n1)))
ValueError: invalid literal for int() with base 10: '0xff'
'''
# int() for converting a hexadecimal string to an integer using a base of 16.
print(int(hex(n1), base = 16)) # 255
print(int(hex(n2), base = 16)) # 1000