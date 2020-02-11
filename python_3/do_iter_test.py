# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(l):
    if not isinstance(l, list):
        raise TypeError('args is not a list.')
    if len(l) == 0:
        return None, None
    min = l[0]
    max = l[0]
    for num in l:
        if num < min:
            min = num
        if num > max:
            max = num
    return min, max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')