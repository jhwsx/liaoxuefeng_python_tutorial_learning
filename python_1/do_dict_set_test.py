# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
d = {'a': 1}
s = set([1,2])
t1 = (1, 2, 3)
d[t1] = 2
print(d) # {'a': 1, (1, 2, 3): 2}
s.add(t1)
print(s) # {1, 2, (1, 2, 3)}

t2 = (1, [2, 3])
# d[t2] = 4 # 报错
'''
报错信息：
Traceback (most recent call last):
  File "do_dict_set_test.py", line 11, in <module>
    d[t2] = 4
TypeError: unhashable type: 'list'
'''
# s.add(t2) # 报错
'''
报错信息：
Traceback (most recent call last):
  File "do_dict_set_test.py", line 19, in <module>
    s.add(t2)
TypeError: unhashable type: 'list'
'''