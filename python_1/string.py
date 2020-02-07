print('包含中文的str')

# ord() 函数获取字符的整数表示
print(ord('A')) # 打印：65
print(ord('王')) # 打印：29579, 16进制是0x738b
print(ord('志')) # 打印：24535, 16进制是0x5fd7
print(ord('超')) # 打印：36229, 16进制是0x8d85


# chr() 函数把编码转换成对应的字符
print(chr(66)) # 打印：B
print(chr(36229)) # 打印：超

print('\u738b\u5fd7\u8d85') # 打印：王志超

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii')) # 打印：b'ABC'
print('王志超'.encode('utf-8')) # 打印：b'\xe7\x8e\x8b\xe5\xbf\x97\xe8\xb6\x85'
'''
下面这行代码报错：
Traceback (most recent call last):
  File "string.py", line 18, in <module>
    print('王志超'.encode('ascii'))
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)
'''
# print('王志超'.encode('ascii'))

# 要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii')) # ABC
print(b'\xe7\x8e\x8b\xe5\xbf\x97\xe8\xb6\x85'.decode("utf-8")) # 王志超

# 无法解码的情形
# print(b'\xe17\x8e\x8b\xe5\xbf\x97\xe8\xb6\x85'.decode("utf-8"))
'''
Traceback (most recent call last):
  File "string.py", line 33, in <module>
    print(b'\xe17\x8e\x8b\xe5\xbf\x97\xe8\xb6\x85'.decode("utf-8"))
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe1 in position 0: invalid continuation byte
'''
# 忽略错误的字节
print(b'\xe17\x8e\x8b\xe5\xbf\x97\xe8\xb6\x85'.decode("utf-8", errors='ignore'))

# 计算 str 包含多少个字符, len() 函数
print(len('ABC')) # 3
print(len('王志超')) # 3

# 计算 bytes 包含多少个字节，len() 函数
print(len(b'ABC')) # 3
print(len(b'\xe7\x8e\x8b\xe5\xbf\x97\xe8\xb6\x85')) # 9

# 格式化
# 使用 C 语言的方式
print('Hello, %s' % 'world') # Hello, world
print('Hi %s, your score is %d' %('Bart', 59)) # Hi Bart, your score is 59
print('亲爱的%s你好！你%d月的话费是%.2f元，余额是%.2f元。' %('王志超', 1, 30.22, 6.18))
print('%2d-%02d' %(3, 1)) # 3-01
# 使用字符串的 format() 方法
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)) # Hello, 小明, 成绩提升了 17.1%



