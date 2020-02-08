# break 跳出所在的循环
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

# continue 跳过本次循环
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
