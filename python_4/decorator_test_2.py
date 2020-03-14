# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        f = func(*args, **kw)
        print('end call')
        return f
    return wrapper

@log
def greetings():
    print('Hello, World!')

greetings()