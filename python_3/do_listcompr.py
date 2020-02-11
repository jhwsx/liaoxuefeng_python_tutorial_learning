# 生成 [1x1, 2x2, 3x3, ..., 10x10]
print([x * x for x in range(1, 11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 生成 1 到 10 偶数的平方的 list
print([x * x for x in range(1, 11) if x % 2 == 0]) # [4, 16, 36, 64, 100]

# 使用两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ']) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下的所有文件和目录名
import os # 导入 os 模块
print([d for d in os.listdir('.')]) # ['do_iter.py', 'do_iter_test.py', 'do_listcompr.py', 'do_slice.py', 'do_slice_test.py']

# 使用两个变量来生成list
print([k + '=' + v for k, v in {'x' : 'A', 'y' : 'B', 'z' : 'C'}.items()]) # ['x=A', 'y=B', 'z=C']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'Adups', 'Abup']
print([s.lower() for s in L]) # ['hello', 'world', 'adups', 'abup']