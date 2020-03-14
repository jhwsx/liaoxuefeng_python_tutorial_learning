def now():
    print('2020-3-14')

f = now
f()

# 通过函数对象的 属性，获取函数的名字
print(now.__name__) # now
print(f.__name__) # now

# 增强 now 函数的功能，在函数调用前后自动打印日志，但不修改 now 函数的定义，这就是装饰器（decorator）的应用
def log(func):
    def wrapper(*args, **kw): # wrapper 是一个局部函数
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# log 就是一个 decorator，decorator 是一个返回函数的高阶函数，它接收一个函数(func)，并且返回一个函数(wrapper)。
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它

@log # 这里使用了 Python 的 @ 语法，把 decorator 置于函数的定义处
def nowday():
    print('2020-3-14')

nowday()
# 等价于
log(now)()

# decorator 本身要传入参数的写法
def log2(text): # log2 是一个返回 decorator 的高阶函数
    def decorator(func): # decorator 是一个返回函数的高阶函数
        def wrapper(*args, **kw): # wrapper 是一个局部函数
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2("execute")
def today():
    print('2020-03-14')

today()

# 等价于
log2('execute')(now)()

now = log2('execute')(now)
print(now.__name__) # wrapper


import functools
def log3(func):
    @functools.wraps(func) # 需要把原始函数的__name__等属性复制到wrapper()函数中
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log3
def tommorrow():
    print('2020-3-15' ) 

tommorrow()

def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
        return wrapper
    return decorator

@log4('execute')
def yesterday():
    print('2020-03-13')

yesterday()

def longlongago():
    print('1970-01-01')

longlongago = log4('execute')(longlongago)

print(longlongago.__name__) # longlongago
