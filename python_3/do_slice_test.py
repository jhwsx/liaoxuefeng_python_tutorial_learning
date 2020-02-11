# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if not isinstance(s, str):
        raise TypeError('args is not a str.')
    length = len(s)
    st = 0
    while st < length and s[st] <= ' ':
        st += 1
    while st < length and s[length - 1] <= ' ':
        length -= 1
    if st > 0 or length < len(s):
        return s[st:length]
    else:
        return s

# trim(1)
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
