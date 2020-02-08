d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}

# 根据 key，获取 value
print(d['Michael'])

# 通过 key，存放 value
d['Adam'] = 67
print(d['Adam'])

# 一个 key 只对应一个 value，后面的 value 会覆盖前面的 value
d['Jack'] = 66
d['Jack'] = 77
print(d['Jack'])

# 如果 key不存在，dict 就会报错
# d['Thomas']
'''
错误信息：
Traceback (most recent call last):
  File "do_dict.py", line 16, in <module>
    d['Thomas']
KeyError: 'Thomas'
'''

# 判断 dict 是否包含某个 key
if 'Thomas' in d:
    print(d['Thomas'])
else:
    print('d doesn\'t contain \'Thomas\'')

# dict 的 get() 方法
print(d.get('Thomas')) # 如果不存在 key，就返回 None。
print(d.get('Thomas', -1)) # 如果不存在 key，就返回指定的值。

# dict 的删除方法 pop(key)，如果 key 存在，则该方法返回对应的 value。
print(d.pop('Bob')) # 打印：75
# print(d.pop('Thomas')) # 报错
'''
Traceback (most recent call last):
  File "do_dict.py", line 37, in <module>
    print(d.pop('Thomas'))
KeyError: 'Thomas'
'''

# dict 的 key 必须是不可变对象
d[1] = 2
print(d) # {'Michael': 95, 'Tracy': 85, 'Adam': 67, 'Jack': 77, 1: 2}
key = [1, 2, 3]
# d[key] = 4 # 此行报错
'''
报错信息：
Traceback (most recent call last):
  File "do_dict.py", line 49, in <module>
    d[key] = 4 # 此行报错
TypeError: unhashable type: 'list'
'''
d[True] = 3 # True 会被认为是 1
print(d) # {'Michael': 95, 'Tracy': 85, 'Adam': 67, 'Jack': 77, 1: 3}
d[False] = 'false'
print(d) # {'Michael': 95, 'Tracy': 85, 'Adam': 67, 'Jack': 77, 1: 3, False: 'false'}
d[0] = 0
print(d) # {'Michael': 95, 'Tracy': 85, 'Adam': 67, 'Jack': 77, 1: 3, False: 0}
