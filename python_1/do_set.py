# 创建 set，需要提供一个 list 作为输入集合
s = set([1, 2, 3])
print(s) # {1, 2, 3}

# 如果提供的集合里包含重复元素，在 set 中会被自动过滤
s = set([1, 1, 2, 2, 3, 3])
print(s) # {1, 2, 3}

# 添加元素方法：add()
print(s.add(4)) # None
print(s.add(4)) # None

# 删除元素方法：remove()
print(s.remove(4)) # None
# print(s.remove(5)) # 报错
'''
报错信息：
Traceback (most recent call last):
  File "do_set.py", line 15, in <module>
    print(s.remove(5))
KeyError: 5
'''

# set 可以做数学意义上的交集，并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) # {2, 3}
print(s1 | s2) # {1, 2, 3, 4}