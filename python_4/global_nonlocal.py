# https://www.cnblogs.com/itech/archive/2011/12/31/2308640.html

# python引用变量的顺序： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量


# global

# global关键字用来在函数或其他局部作用域中使用全局变量。但是如果不修改全局变量也可以不使用global关键字。
gcount = 0

def global_test():
    return gcount # 没有修改只是读取，不使用 global 关键字是可以的

# 下面的函数不使用 global gcount, 就会报出：UnboundLocalError: local variable 'gcount' referenced before assignment
def global_counter():
    global gcount
    gcount += 1
    return gcount

def global_counter_test():
    print(global_test())
    print(global_counter())
    print(global_counter())
    print(global_test())

global_counter_test()

'''
打印结果：
0
1
2
2
'''
print('**********nonlocal**********')
# nonlocal
# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())

make_counter_test()
'''
打印结果：
1
2
3
'''