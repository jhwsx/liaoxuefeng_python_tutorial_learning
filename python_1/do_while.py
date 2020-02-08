# 计算 100 以内的所有奇数之和
sum = 0
n = 99
while n > 0:
    sum += n
    n = n - 2
print(sum)