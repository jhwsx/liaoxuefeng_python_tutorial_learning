'''
思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass

'''
import functools
def log(text):
    if isinstance(text, str):
        def decorator(func): # 这是一个返回函数的高阶函数
            @functools.wraps(func)
            def wrapper(*args, **kw): # 这是一个局部函数
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        def wrapper(*args, **kw):
            print('Call %s():' % text.__name__)
            return text(*args, **kw)
        return wrapper



@log
def show():
    print('It is a good day.')

show()

@log("Execute")
def display():
    print('Study hard')

display()

