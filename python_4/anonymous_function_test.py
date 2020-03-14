'''
请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
'''
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]