# 取 list 或者 tuple 的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L)
# 取出前 3 个元素
print([L[0], L[1], L[2]]) # ['Michael', 'Sarah', 'Tracy']

# 取出前 N 个元素
n = 4
r = []
for i in range(n):
    r.append(L[i])
print(r)

# 使用 slice 操作符

# L[0:3] 表示从 L 的索引 0 开始取，到索引 3 结束，但是不包括索引 3，也就是说取索引 0，1，2 这 3 个元素。
print(L[0:3]) # ['Michael', 'Sarah', 'Tracy']
# 如果是从索引 0 开始，可以省略开始索引
print(L[:3]) # ['Michael', 'Sarah', 'Tracy']
# 如果是取到尾部，可以省略尾部索引
print(L[1:]) # ['Sarah', 'Tracy', 'Bob', 'Jack']
# 支持倒数切片
# 从倒数第 2 个开始，取完。
print(L[-2:]) # ['Bob', 'Jack']
# 从倒数第 2 个开始，取到倒数第 1 个
print(L[-2:-1]) # ['Bob']

print(L[3:0]) # []
print(L[-1:-2]) #[]

# 切片操作进一步学习
L = list(range(100))
print(L)
# 取出前 10 个数
print(L[:10]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 取出后 10 个数
print(L[-10:]) # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# 前 11 到 20 个数
print(L[11:20]) # [11, 12, 13, 14, 15, 16, 17, 18, 19]
# 前 10 个数，每两个取一个
print(L[:10:2]) # [0, 2, 4, 6, 8]
# 所有数，每五个取一个
print(L[::5]) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# 复制一个 list
print(L[:])

# tuple 使用切片操作后，结果仍是 tuple
print((0, 1, 2, 3, 4, 5)[:3]) # (0, 1, 2)

# 字符串使用切片操作，结果仍是字符串
print('ABCDEF'[:3]) # ABC
print('ABCDEF'[::2]) # ACE
