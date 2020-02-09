# 请定义一个函数 quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。
import math

def quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

# x^2+6x+5=0的解
print(quadratic(1, 6, 5)) # (-1.0, -5.0)