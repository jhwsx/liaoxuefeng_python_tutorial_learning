# 可接收一个或多个数并计算乘积
def product(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(product(1, 2, 3))
print(product(1, 3, 5))